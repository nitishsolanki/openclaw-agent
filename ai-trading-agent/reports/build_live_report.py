import json
import os
from pathlib import Path
from datetime import datetime, timezone
from ai_trading_agent.cli import run_scan
from ai_trading_agent.config.env import load_env
from ai_trading_agent.data.market_data import AlpacaMarketData
from ai_trading_agent.sector.live_rotation import rank_sectors
from ai_trading_agent.theme.manager import active_theme
from generate_site import build

root = Path(__file__).parents[1]
env = load_env(root / "local.env")
if not env.get("ALPACA_API_KEY") or not env.get("ALPACA_SECRET_KEY"):
    raise SystemExit("Alpaca credentials are required")
provider = AlpacaMarketData(env["ALPACA_API_KEY"], env["ALPACA_SECRET_KEY"])
sectors = [item.__dict__ for item in rank_sectors(provider)]
signals = run_scan(root, require_live=True)
if os.getenv("GITHUB_ACTIONS") == "true" and any(item.symbol in {"AAA", "BBB", "CCC"} for item in signals):
    raise RuntimeError("Refusing to publish sample candidates in GitHub Actions")
report = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "data_source": "alpaca_live",
    "market": {"label": "See signal components", "score": signals[0].components.get("market", 0) if signals else 0},
    "theme": active_theme(root) or {"name": "none", "sectors": []},
    "sectors": sectors,
    "signals": [{"symbol": item.symbol, "direction": item.direction, "score": item.final_score,
                 "sector": item.components.get("sector", "Unknown"),
                 "reasons": [f"{key}: {value:.1f}" for key, value in item.components.items() if value >= 80]}
                for item in signals],
    "disclaimer": "Paper-trading research only. Not investment advice. Live trading is disabled."
}
output = root / "reports" / "site"
json_path = root / "reports" / "latest.json"
json_path.write_text(json.dumps(report, indent=2, default=float), encoding="utf-8")
build(json_path, output)
print(f"report_generated={output}")
