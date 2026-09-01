from pathlib import Path
from .router import route_command

def format_response(endpoint: str, payload: dict) -> str:
    if endpoint == "/scan":
        lines = [f"MARKET SCAN\nTheme: {payload.get('theme', {}).get('name', 'none')}\n"]
        for index, signal in enumerate(payload.get("signals", []), 1):
            lines.append(f"{index}. {signal['symbol']} — {signal['score']:.2f}/100 {signal['direction']}")
            components = signal.get("components", {})
            lines.append(f"   RS {components.get('relative_strength', 0):.1f} | VWAP {components.get('vwap', 0):.1f} | Volume {components.get('volume', 0):.1f}")
        return "\n".join(lines)[:4000]
    if endpoint.startswith("/analyze/"):
        if "error" in payload:
            return f"ANALYSIS ERROR\n{payload['error']}"
        symbol = payload.get("symbol", endpoint.rsplit("/", 1)[-1])
        components = payload.get("components", {})
        ranked = sorted(components.items(), key=lambda item: float(item[1]), reverse=True)
        strengths = ", ".join(f"{key.replace('_', ' ')} {float(value):.0f}" for key, value in ranked[:3]) or "No signal details"
        return (f"📊 {symbol} — {payload.get('direction', 'UNKNOWN')}\n"
                f"Score: {payload.get('score', 0):.0f}/100\n\n"
                f"Signal strengths: {strengths}\n\n"
                "Action: Use /setup for entry, stop, target, and position size.")
    if endpoint.startswith("/setup/"):
        return (f"TRADE SETUP — {payload.get('symbol')}\nEntry: ${payload.get('entry', 0):.2f}\nStop: ${payload.get('stop', 0):.2f}\nTarget: ${payload.get('target', 0):.2f}\nShares: {payload.get('shares', 0)}\nApproved: {payload.get('approved')}\nReasons: {', '.join(payload.get('reasons', [])) or 'none'}")
    if endpoint == "/sectors":
        return "SECTOR ROTATION\n" + "\n".join(f"{item['rank']}. {item['sector']} ({item['symbol']}) — {item['score']:.1f}" for item in payload.get("sectors", []))
    if "orders" in payload:
        return "PAPER ORDERS\n" + ("\n".join(f"{o['symbol']} — {o['quantity']} shares @ ${o['entry_price']:.2f} — {o['status']}" for o in payload["orders"]) or "No open orders.")
    return str(payload)[:4000]

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
        import json
        with urllib.request.urlopen(url, timeout=20) as response:
            payload = json.loads(response.read().decode("utf-8"))
        await update.message.reply_text(format_response(url.split(api_base)[-1], payload))

    application = Application.builder().token(token).build()
    for command in ("scan", "sectors", "positions", "orders", "pnl", "journal", "status", "analyze", "setup"):
        application.add_handler(CommandHandler(command, handle))
    return application
