COMMANDS = {"scan": "GET /scan", "positions": "GET /paper/orders", "status": "GET /health",
            "orders": "GET /paper/orders", "pnl": "GET /paper/orders", "journal": "GET /paper/orders"}

def route_command(text: str) -> str:
    command = text.strip().lstrip("/").split()[0].lower() if text.strip() else "status"
    return COMMANDS.get(command, "Unsupported command. Use /scan, /positions, /pnl, /journal, or /status.")

