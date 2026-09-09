import json
import os
from datetime import datetime, timezone
from pathlib import Path

from ai_trading_agent.cli import run_scan, run_profiles
from ai_trading_agent.config.env import load_env
from ai_trading_agent.config.settings import load_strategy
from ai_trading_agent.data.market_data import AlpacaMarketData
from ai_trading_agent.sector.live_rotation import rank_sectors, sector_score_history
from ai_trading_agent.signals.llm import analyze_top_candidates
from ai_trading_agent.research.bridge import load_research, boosted_score
from ai_trading_agent.theme.manager import active_theme
from generate_site import build

def generate_report(root: Path, signals=None, research=None) -> Path:
    env = load_env(root / "local.env")
    if not env.get("ALPACA_API_KEY") or not env.get("ALPACA_SECRET_KEY"):
        raise SystemExit("Alpaca credentials are required")
    provider = AlpacaMarketData(env["ALPACA_API_KEY"], env["ALPACA_SECRET_KEY"])
    sectors = [item.__dict__ for item in rank_sectors(provider)]
    history_path = root / "reports" / "sector_history.json"
    try:
        history = json.loads(history_path.read_text(encoding="utf-8"))
        if not isinstance(history, list): history = []
    except (FileNotFoundError, json.JSONDecodeError):
        history = []
    # Long history is refreshed by the dedicated 7 AM job. Report builds only
    # use the stored history and avoid repeating the expensive backfill.
    if not history:
        history = sector_score_history(provider, days=5)
    current_prices = {}
    for item in sectors:
        try:
            current_prices[item["sector"]] = round(float(provider.get_bars(item["symbol"])["close"].iloc[-1]), 2)
        except (KeyError, ValueError, IndexError, FileNotFoundError):
            pass
    today = datetime.now(timezone.utc).date().isoformat()
    history = [item for item in history if item.get("date") != today]
    history.append({"date": today, "scores": {item["sector"]: item["score"] for item in sectors}, "prices": current_prices})
    history = sorted(history, key=lambda item: str(item.get("date", "")))
    history_path.write_text(json.dumps(history, indent=2) + "\n", encoding="utf-8")
    if signals is None:
        profile_results = run_profiles(root, require_live=True,
                                       profiles=("day", "swing", "growth"), limit=1000)
        signals = profile_results["swing"][:10]
    else:
        profile_results = run_profiles(root, require_live=True,
                                       profiles=("day", "swing", "growth"), limit=1000)
    sector_tickers = {}
    seen_tickers = set()
    for profile_items in profile_results.values():
        for signal in profile_items:
            sector = signal.components.get("sector_name", "Unknown")
            if sector == "Unknown" or signal.symbol in seen_tickers:
                continue
            try:
                bars = provider.get_bars(signal.symbol)
                prices = bars["close"].dropna()
                change = ((float(prices.iloc[-1]) / float(prices.iloc[-2])) - 1) * 100 if len(prices) >= 2 else 0.0
                sector_tickers.setdefault(sector, []).append({"symbol": signal.symbol, "change": round(change, 2)})
                seen_tickers.add(signal.symbol)
            except (KeyError, ValueError, IndexError, FileNotFoundError):
                continue
    for sector in sector_tickers:
        sector_tickers[sector] = sector_tickers[sector][:10]
    if os.getenv("GITHUB_ACTIONS") == "true" and any(item.symbol in {"AAA", "BBB", "CCC"} for item in signals):
        raise RuntimeError("Refusing to publish sample candidates in GitHub Actions")
    research = research or load_research(root)
    def serialize(items, profile):
        strategy_path = root / "config" / f"strategy_{profile}.yaml"
        weights = load_strategy(strategy_path).get("weights", {})
        return [{"symbol": item.symbol, "profile": profile, "direction": item.direction, "score": item.final_score,
                 "profile_status": item.profile_status,
                 "early_setup_score": item.components.get("early_setup_score", 0),
                 "entry_timing_score": item.components.get("entry_timing_score", 0),
                 "setup_maturity": item.components.get("setup_maturity", "BUILDING"),
                 "opportunity_score": item.components.get("opportunity_score", item.final_score),
                 "recommendation": item.components.get("recommendation", "WATCH"),
                 "boosted_score": boosted_score(item.final_score, research.get(item.symbol)),
                 "research": research.get(item.symbol, {}),
                 "components": {key: value for key, value in item.components.items() if isinstance(value, (int, float))},
                 "weights": weights,
                 "sector": item.components.get("sector_name", "Unknown"),
                 "reasons": [f"{key}: {value:.1f}" for key, value in item.components.items() if isinstance(value, (int, float)) and value >= 80]}
                for item in items]

    theme = active_theme(root)
    if not theme and sectors:
        leaders = sorted(sectors, key=lambda item: float(item.get("score", 0)), reverse=True)[:3]
        leader_sectors = [item["sector"] for item in leaders]
        theme = {
            "name": "+".join(f"{sector.lower().replace(' ', '_')}_leadership" for sector in leader_sectors),
            "sectors": leader_sectors,
            "industries": [],
            "score": round(sum(float(item.get("score", 0)) for item in leaders) / max(len(leaders), 1), 2),
            "source": "sector_rotation_fallback",
        }
    market_indices = []
    for label, symbol in (("S&P 500", "SPY"), ("Dow", "DIA"), ("Nasdaq", "QQQ")):
        try:
            bars = provider.get_bars(symbol)
            closes = bars["close"].dropna()
            latest = float(closes.iloc[-1])
            previous = float(closes.iloc[-2]) if len(closes) > 1 else latest
            market_indices.append({"label": label, "symbol": symbol, "price": round(latest, 2), "change_pct": round((latest / previous - 1) * 100, 2) if previous else 0.0})
        except (KeyError, ValueError, IndexError, FileNotFoundError):
            market_indices.append({"label": label, "symbol": symbol, "price": None, "change_pct": None})
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(), "data_source": "alpaca_live",
        "market": {"label": "Latest index movement", "score": signals[0].components.get("market", 0) if signals else 0, "indices": market_indices},
        "theme": theme or {"name": "market_leadership", "sectors": []}, "sectors": sectors,
        "sector_history": history, "sector_current_prices": current_prices, "sector_tickers": sector_tickers,
        "signals": serialize(signals, "swing"),
        "profiles": {profile: serialize(items, profile) for profile, items in profile_results.items()},
        "disclaimer": "Paper-trading research only. Not investment advice. Live trading is disabled."
    }
    if env.get("OPENAI_API_KEY") and not research:
        analyses = analyze_top_candidates(env["OPENAI_API_KEY"], report["signals"][:5], env.get("OPENAI_MODEL", "gpt-5-mini"))
        for signal in report["signals"][:5]:
            signal["llm_analysis"] = analyses.get(signal["symbol"], {"status": "unavailable"})
    json_path = root / "reports" / "latest.json"
    json_path.write_text(json.dumps(report, indent=2, default=float), encoding="utf-8")
    output = root / "reports" / "site"
    build(json_path, output)
    return output

if __name__ == "__main__":
    output = generate_report(Path(__file__).parents[1])
    print(f"report_generated={output}")
