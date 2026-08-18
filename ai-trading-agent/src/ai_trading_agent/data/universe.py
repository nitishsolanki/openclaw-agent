import json
import sqlite3
from datetime import datetime, timezone

def refresh_assets(provider, connection: sqlite3.Connection) -> int:
    connection.execute("CREATE TABLE IF NOT EXISTS assets(symbol TEXT PRIMARY KEY, name TEXT, exchange TEXT, tradable INTEGER, updated_at TEXT)")
    count = 0
    for asset in provider.get_assets():
        connection.execute("INSERT OR REPLACE INTO assets VALUES (?,?,?,?,?)",
                           (asset.symbol, getattr(asset, "name", ""), getattr(asset, "exchange", ""),
                            int(bool(getattr(asset, "tradable", False))), datetime.now(timezone.utc).isoformat()))
        count += 1
    connection.commit()
    return count

def cached_symbols(connection: sqlite3.Connection, limit: int | None = None) -> list[str]:
    query = "SELECT symbol FROM assets WHERE tradable=1 ORDER BY symbol"
    if limit: query += f" LIMIT {int(limit)}"
    return [row[0] for row in connection.execute(query)]

def next_batch(connection: sqlite3.Connection, batch_size: int = 100) -> list[str]:
    symbols = cached_symbols(connection)
    if not symbols:
        return []
    connection.execute("CREATE TABLE IF NOT EXISTS scan_state(key TEXT PRIMARY KEY, value INTEGER NOT NULL)")
    row = connection.execute("SELECT value FROM scan_state WHERE key='cursor'").fetchone()
    cursor = int(row[0]) if row else 0
    batch = [symbols[(cursor + offset) % len(symbols)] for offset in range(min(batch_size, len(symbols)))]
    connection.execute("INSERT OR REPLACE INTO scan_state(key,value) VALUES ('cursor',?)", ((cursor + len(batch)) % len(symbols),))
    connection.commit()
    return batch
