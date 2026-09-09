"""Refresh the long sector history once per trading day."""
import json
from pathlib import Path
import sys

root = Path(__file__).parents[1]
sys.path.insert(0, str(root / "src"))
from ai_trading_agent.config.env import load_env
from ai_trading_agent.data.market_data import AlpacaMarketData
from ai_trading_agent.sector.live_rotation import sector_score_history

env = load_env(root / "local.env")
provider = AlpacaMarketData(env["ALPACA_API_KEY"], env["ALPACA_SECRET_KEY"])
path = root / "reports" / "sector_history.json"
history = sector_score_history(provider, days=60)
path.write_text(json.dumps(history, indent=2) + "\n", encoding="utf-8")
print(f"sector_history_refreshed={len(history)}")
