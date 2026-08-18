import argparse
from pathlib import Path
import pandas as pd

from .config.settings import load_strategy
from .data.market_data import CsvMarketData, AlpacaMarketData
from .data.universe import refresh_assets, cached_symbols
from .data.bars_batch import fetch_liquid_bars
from .journal.database import connect, record_signal
from .market.regime import detect_regime
from .config.env import load_env
from .data.external import FinnhubProvider
from .signals.enrichment import news_confirmation, earnings_risk
from .theme.manager import active_theme
from .screening.scanner import Candidate, scan

def run_scan(root: Path) -> list:
    config = load_strategy(root / "config" / "strategy.yaml")
    env = load_env(root / "local.env")
    db = connect(root / "trading.db")
    provider = CsvMarketData(root / "data" / "sample")
    symbols = ["AAA", "BBB", "CCC"]
    live = bool(env.get("ALPACA_API_KEY") and env.get("ALPACA_SECRET_KEY"))
    if live:
        provider = AlpacaMarketData(env["ALPACA_API_KEY"], env["ALPACA_SECRET_KEY"])
        try:
            if not cached_symbols(db, 1):
                refresh_assets(provider, db)
            symbols = cached_symbols(db, 100)
            bars = fetch_liquid_bars(provider, symbols, limit=100)
            symbols = list(bars)
        except Exception:
            provider = CsvMarketData(root / "data" / "sample")
            symbols = ["AAA", "BBB", "CCC"]
    benchmark = provider.get_bars("SPY")["close"]
    regime = detect_regime(provider.get_bars("SPY"))
    sector_map = {"AAA": "Technology", "BBB": "Energy", "CCC": "Industrials"}
    candidates = [Candidate(symbol, sector_map.get(symbol, "Unknown"), provider.get_bars(symbol), 50.0)
                  for symbol in symbols]
    theme = active_theme(root)
    if theme and not live:
        candidates = [candidate for candidate in candidates if candidate.sector in theme["sectors"]]
    enrichments = {}
    env = load_env(root / "local.env")
    if env.get("FINNHUB_API_KEY"):
        provider = FinnhubProvider(env["FINNHUB_API_KEY"])
        for symbol in symbols:
            try:
                news = provider.company_news(symbol)
                calendar = provider.earnings_calendar()
                news_score = news_confirmation(news)
                earnings_score = earnings_risk(calendar, symbol)
                enrichments[symbol] = {"news": news_score * earnings_score / 100.0,
                                       "options": 50.0}
            except Exception:
                enrichments[symbol] = {"news": 50.0, "options": 50.0}
    results = scan(candidates, benchmark, config["weights"], market_score=regime.score,
                   enrichments=enrichments)
    journal = db
    for result in results:
        record_signal(journal, result.symbol, result.direction, result.final_score,
                      reasoning=str(result.components))
    return results

def main() -> None:
    parser = argparse.ArgumentParser(description="AI Trading Agent (signal-only scanner)")
    parser.add_argument("command", choices=["scan"])
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    for rank, result in enumerate(run_scan(args.root), 1):
        print(f"{rank}. {result.symbol} {result.final_score:.2f}/100 {result.direction}")
        print(f"   {result.components}")

if __name__ == "__main__":
    main()
