import argparse
from pathlib import Path
from ai_trading_agent.config.env import load_env
from ai_trading_agent.data.external import FinnhubProvider
from ai_trading_agent.data.universe import refresh_metadata, symbols_missing_metadata
from ai_trading_agent.journal.database import connect

parser = argparse.ArgumentParser()
parser.add_argument("--limit", type=int, default=100)
args = parser.parse_args()
root = Path(__file__).parents[1]
env = load_env(root / "local.env")
if not env.get("FINNHUB_API_KEY"):
    raise SystemExit("FINNHUB_API_KEY is required")
db = connect(root / "trading.db")
symbols = symbols_missing_metadata(db, args.limit)
count = refresh_metadata(FinnhubProvider(env["FINNHUB_API_KEY"]), db, symbols)
print(f"metadata_updated={count} requested={len(symbols)}")

