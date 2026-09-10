import argparse
from pathlib import Path
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

from .config.settings import load_strategy
from .data.market_data import CsvMarketData, AlpacaMarketData
from .data.universe import refresh_assets, cached_symbols, next_batch
from .data.bars_batch import fetch_liquid_bars
from .journal.database import connect, record_signal
from .market.regime import detect_regime
from .config.env import load_env
from .data.external import FinnhubProvider
from .execution.alpaca_paper import AlpacaPaperBroker
from .signals.options import options_confirmation
from .screening.scanner import score_candidate
from .signals.enrichment import news_confirmation, earnings_risk
from .theme.manager import active_theme
from .sector.live_rotation import rank_sectors
from .data.external import FinnhubProvider
from .screening.scanner import Candidate, scan

def _normalize_sector(profile: dict) -> str:
    sector = str(profile.get("sector") or "").strip()
    industry = str(profile.get("finnhubIndustry") or "").strip()
    if sector in {"Consumer Defensive", "Consumer Staples", "Consumer Defensive Goods"}:
        return "Consumer Staples"
    known = {"Technology", "Financials", "Energy", "Healthcare", "Industrials",
             "Consumer Discretionary", "Consumer Staples", "Utilities", "Materials",
             "Real Estate", "Communication Services"}
    if sector in known:
        return sector
    text = f"{sector} {industry}".lower()
    groups = {
        "Technology": ("technology", "software", "semiconductor", "computer", "electronic"),
        "Financials": ("bank", "financial", "insurance", "capital market", "credit"),
        "Energy": ("oil", "gas", "energy", "coal"),
        "Healthcare": ("health", "biotech", "pharma", "medical"),
        "Industrials": ("rail", "industrial", "machinery", "aerospace", "defense", "transport"),
        "Consumer Discretionary": ("restaurant", "hotel", "automobile", "auto", "leisure", "travel", "luxury", "apparel"),
        "Consumer Staples": ("beverage", "food", "household", "tobacco", "grocery", "supermarket", "discount store", "consumer defensive", "personal care"),
        "Utilities": ("utility", "utilities", "electric", "water"),
        "Materials": ("chemical", "materials", "steel", "metal", "mining"),
        "Real Estate": ("real estate", "reit", "property"),
        "Communication Services": ("telecommunication", "telecom", "media", "entertainment", "internet content"),
    }
    return next((name for name, terms in groups.items() if any(term in text for term in terms)), "Unknown")

def _prepare_scan(root: Path, require_live: bool = False):
    env = load_env(root / "local.env")
    db = connect(root / "trading.db")
    provider = CsvMarketData(root / "data" / "sample")
    symbols = ["AAA", "BBB", "CCC"]
    live = bool(env.get("ALPACA_API_KEY") and env.get("ALPACA_SECRET_KEY"))
    if require_live and not live:
        raise RuntimeError("Live scan requires ALPACA_API_KEY and ALPACA_SECRET_KEY")
    if live:
        provider = AlpacaMarketData(env["ALPACA_API_KEY"], env["ALPACA_SECRET_KEY"])
        try:
            if not cached_symbols(db, 1):
                refresh_assets(provider, db)
            symbols = cached_symbols(db)
            bars = fetch_liquid_bars(provider, symbols)
            symbols = list(bars)
        except Exception:
            if require_live:
                raise
            provider = CsvMarketData(root / "data" / "sample")
            symbols = ["AAA", "BBB", "CCC"]
    benchmark = provider.get_bars("SPY")["close"]
    regime = detect_regime(provider.get_bars("SPY"))
    sector_map = {"AAA": "Technology", "BBB": "Energy", "CCC": "Industrials"}
    candidates = [Candidate(symbol, sector_map.get(symbol, "Unknown"), provider.get_bars(symbol), 50.0)
                  for symbol in symbols]
    if live:
        sector_ranks = {item.sector: item.score for item in rank_sectors(provider)}
        finnhub = FinnhubProvider(env["FINNHUB_API_KEY"]) if env.get("FINNHUB_API_KEY") else None
        enriched = []
        for candidate in candidates:
            sector = candidate.sector
            if finnhub and sector == "Unknown":
                try:
                    sector = _normalize_sector(finnhub.profile(candidate.symbol))
                except Exception:
                    pass
            matched_score = max((score for name, score in sector_ranks.items() if name.lower() in sector.lower() or sector.lower() in name.lower()), default=50.0)
            enriched.append(Candidate(candidate.symbol, sector, candidate.bars, matched_score))
        candidates = enriched
    theme = active_theme(root)
    if theme and not live:
        candidates = [candidate for candidate in candidates if candidate.sector in theme["sectors"]]
    enrichments = {}
    env = load_env(root / "local.env")
    if live and hasattr(provider, "get_premarket_snapshot"):
        def premarket_symbol(symbol):
            try:
                snapshot = provider.get_premarket_snapshot(symbol)
                # Ignore thin/insignificant moves; the daily model remains primary.
                meaningful = abs(float(snapshot.get("gap_pct", 0))) >= 0.50 and float(snapshot.get("volume_ratio", 0)) >= 0.25
                return symbol, {"premarket": float(snapshot.get("score", 50.0)) if meaningful else 50.0}
            except Exception:
                return symbol, {"premarket": 50.0}
        with ThreadPoolExecutor(max_workers=8) as executor:
            for future in as_completed([executor.submit(premarket_symbol, symbol) for symbol in symbols]):
                symbol, values = future.result()
                enrichments[symbol] = values
    if env.get("FINNHUB_API_KEY"):
        provider = FinnhubProvider(env["FINNHUB_API_KEY"])
        def enrich_symbol(symbol):
            try:
                news = provider.company_news(symbol)
                calendar = provider.earnings_calendar()
                news_score = news_confirmation(news)
                earnings_score = earnings_risk(calendar, symbol)
                return symbol, {**enrichments.get(symbol, {}), "news": news_score * earnings_score / 100.0, "options": 50.0}
            except Exception:
                return symbol, {**enrichments.get(symbol, {}), "news": 50.0, "options": 50.0}
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(enrich_symbol, symbol) for symbol in symbols]
            for future in as_completed(futures):
                symbol, values = future.result()
                enrichments[symbol] = values
    return db, env, candidates, benchmark, regime, enrichments

def _score_prepared(root: Path, prepared, profile: str, limit: int = 10) -> list:
    if profile not in {"day", "swing", "growth"}:
        raise ValueError("profile must be one of: day, swing, growth")
    db, env, candidates, benchmark, regime, enrichments = prepared
    live = bool(env.get("ALPACA_API_KEY") and env.get("ALPACA_SECRET_KEY"))
    config_path = root / "config" / f"strategy_{profile}.yaml"
    if not config_path.exists():
        config_path = root / "config" / "strategy.yaml"
    config = load_strategy(config_path)
    results = scan(candidates, benchmark, config["weights"], limit=limit, market_score=regime.score,
                   enrichments=enrichments, minimum_filters=config.get("filters"), setup_config=config.get("early_setup"))
    if live:
        try:
            broker = AlpacaPaperBroker(env["ALPACA_API_KEY"], env["ALPACA_SECRET_KEY"])
            options = dict(enrichments)
            for result in results[:10]:
                snapshots = broker.option_snapshots(result.symbol)
                options[result.symbol] = {**options.get(result.symbol, {}),
                                          "options": options_confirmation(snapshots)}
            results = scan(candidates, benchmark, config["weights"], limit=limit, market_score=regime.score,
                           enrichments=options, minimum_filters=config.get("filters"), setup_config=config.get("early_setup"))
        except Exception:
            pass
    return results

def run_profiles(root: Path, require_live: bool = False,
                 profiles=("day", "swing", "growth"), limit: int = 10) -> dict:
    """Prepare the market universe once, then apply each profile's scoring rules."""
    prepared = _prepare_scan(root, require_live=require_live)
    results = {profile: _score_prepared(root, prepared, profile, limit=limit)
               for profile in profiles}
    db = prepared[0]
    for items in results.values():
        for result in items:
            record_signal(db, result.symbol, result.direction, result.final_score,
                          reasoning=str(result.components))
    return results

def run_scan(root: Path, require_live: bool = False, profile: str = "swing", limit: int = 10) -> list:
    return run_profiles(root, require_live=require_live, profiles=(profile,), limit=limit)[profile]

def main() -> None:
    parser = argparse.ArgumentParser(description="AI Trading Agent (signal-only scanner)")
    parser.add_argument("command", choices=["scan"])
    parser.add_argument("--profile", choices=["day", "swing", "growth"], default="swing",
                        help="Scoring profile: day, swing, or growth (default: swing)")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    for rank, result in enumerate(run_scan(args.root, profile=args.profile), 1):
        print(f"{rank}. {result.symbol} {result.final_score:.2f}/100 {result.direction}")
        print(f"   {result.components}")

if __name__ == "__main__":
    main()
