from pathlib import Path
from ai_trading_agent.config.env import load_env
from ai_trading_agent.telegram.bot import create_bot

config = load_env(Path(__file__).parents[1] / "local.env")
token = config.get("TELEGRAM_BOT_TOKEN")
if not token:
    raise SystemExit("TELEGRAM_BOT_TOKEN is missing")
create_bot(token).run_polling()

