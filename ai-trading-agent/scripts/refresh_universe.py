from pathlib import Path
from ai_trading_agent.config.env import load_env
from ai_trading_agent.data.market_data import AlpacaMarketData
from ai_trading_agent.data.universe import refresh_assets
from ai_trading_agent.journal.database import connect

root = Path(__file__).parents[1]
env = load_env(root / "local.env")
if not env.get("ALPACA_API_KEY") or not env.get("ALPACA_SECRET_KEY"):
    raise SystemExit("Alpaca credentials are required")
count = refresh_assets(AlpacaMarketData(env["ALPACA_API_KEY"], env["ALPACA_SECRET_KEY"]), connect(root / "trading.db"))
print(f"cached_assets={count}")

