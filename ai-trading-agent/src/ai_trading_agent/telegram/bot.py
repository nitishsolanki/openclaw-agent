from pathlib import Path
from .router import route_command

def create_bot(token: str, api_base: str = "http://127.0.0.1:8000"):
    """Build a Telegram bot; starting polling is deliberately caller-controlled."""
    try:
        import truststore
        truststore.inject_into_ssl()
    except ImportError:
        pass
    try:
        from telegram import Update
        from telegram.ext import Application, CommandHandler, ContextTypes
    except ImportError as exc:
        raise RuntimeError("Install the optional telegram dependency") from exc
    import urllib.request

    async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
        command = update.message.text if update.message else "/status"
        endpoint = route_command(command)
        if not endpoint.startswith("GET "):
            await update.message.reply_text(endpoint)
            return
        url = api_base + endpoint[4:]
        with urllib.request.urlopen(url, timeout=10) as response:
            await update.message.reply_text(response.read().decode("utf-8")[:4000])

    application = Application.builder().token(token).build()
    for command in ("scan", "positions", "orders", "pnl", "journal", "status", "analyze", "setup"):
        application.add_handler(CommandHandler(command, handle))
    return application
