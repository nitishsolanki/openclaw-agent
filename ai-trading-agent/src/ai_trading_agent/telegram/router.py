COMMANDS = {"scan": "GET /scan", "sectors": "GET /sectors", "positions": "GET /paper/orders", "status": "GET /health",
            "orders": "GET /paper/orders", "pnl": "GET /paper/orders", "journal": "GET /paper/orders"}

def route_command(text: str) -> str:
    parts = text.strip().lstrip("/").split() if text.strip() else ["status"]
    command = parts[0].lower()
    if command in {"analyze", "setup"} and len(parts) > 1:
        return f"GET /{command}/{parts[1].upper()}"
    return COMMANDS.get(command, "Unsupported command. Use /scan, /positions, /pnl, /journal, or /status.")
