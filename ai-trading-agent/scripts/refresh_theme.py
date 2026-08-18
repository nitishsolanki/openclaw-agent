from pathlib import Path
from ai_trading_agent.config.env import load_env
from ai_trading_agent.data.market_data import AlpacaMarketData
from ai_trading_agent.sector.live_rotation import rank_sectors
from ai_trading_agent.theme.manager import refresh_theme

root = Path(__file__).parents[1]
env = load_env(root / "local.env")
if not env.get("ALPACA_API_KEY") or not env.get("ALPACA_SECRET_KEY"):
    raise SystemExit("Alpaca credentials are required for weekly theme refresh")
theme = refresh_theme(root, rank_sectors(AlpacaMarketData(env["ALPACA_API_KEY"], env["ALPACA_SECRET_KEY"])))
print(theme)

