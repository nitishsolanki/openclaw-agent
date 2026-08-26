import json
import os
from datetime import datetime, timezone
from pathlib import Path

from ai_trading_agent.cli import run_scan
from ai_trading_agent.config.env import load_env
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
    if len(history) < 5 or any("prices" not in item for item in history):
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
    history = history[-5:]
    history_path.write_text(json.dumps(history, indent=2) + "\n", encoding="utf-8")
    signals = run_scan(root, require_live=True) if signals is None else signals
    if os.getenv("GITHUB_ACTIONS") == "true" and any(item.symbol in {"AAA", "BBB", "CCC"} for item in signals):
        raise RuntimeError("Refusing to publish sample candidates in GitHub Actions")
    research = research or load_research(root)
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(), "data_source": "alpaca_live",
        "market": {"label": "See signal components", "score": signals[0].components.get("market", 0) if signals else 0},
        "theme": active_theme(root) or {"name": "none", "sectors": []}, "sectors": sectors,
        "sector_history": history, "sector_current_prices": current_prices,
        "signals": [{"symbol": item.symbol, "direction": item.direction, "score": item.final_score,
                     "boosted_score": boosted_score(item.final_score, research.get(item.symbol)),
                     "research": research.get(item.symbol, {}),
                     "sector": item.components.get("sector_name", "Unknown"),
                     "reasons": [f"{key}: {value:.1f}" for key, value in item.components.items() if isinstance(value, (int, float)) and value >= 80]}
                    for item in signals],
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
