import json
import sqlite3
from datetime import datetime, timezone

def refresh_assets(provider, connection: sqlite3.Connection) -> int:
    connection.execute("CREATE TABLE IF NOT EXISTS assets(symbol TEXT PRIMARY KEY, name TEXT, exchange TEXT, tradable INTEGER, updated_at TEXT)")
    for column in ("industry", "sector"):
        try:
            connection.execute(f"ALTER TABLE assets ADD COLUMN {column} TEXT")
        except sqlite3.OperationalError:
            pass
    count = 0
    for asset in provider.get_assets():
        connection.execute("INSERT OR REPLACE INTO assets(symbol,name,exchange,tradable,updated_at) VALUES (?,?,?,?,?)",
                           (asset.symbol, getattr(asset, "name", ""), getattr(asset, "exchange", ""),
                            int(bool(getattr(asset, "tradable", False))), datetime.now(timezone.utc).isoformat()))
        count += 1
    connection.commit()
    return count

def replace_symbol_universe(connection: sqlite3.Connection, symbols: list[str],
                            name: str = "") -> int:
    """Replace the cached tradable universe with a controlled symbol list."""
    connection.execute("CREATE TABLE IF NOT EXISTS assets(symbol TEXT PRIMARY KEY, name TEXT, exchange TEXT, tradable INTEGER, updated_at TEXT, industry TEXT, sector TEXT)")
    connection.execute("DELETE FROM assets")
    now = datetime.now(timezone.utc).isoformat()
    for symbol in sorted({item.upper().strip() for item in symbols if item.strip()}):
        connection.execute("INSERT INTO assets(symbol,name,exchange,tradable,updated_at,industry,sector) VALUES (?,?,?,?,?,?,?)",
                           (symbol, name, "S&P 500", 1, now, "Unknown", "Unknown"))
    connection.execute("DELETE FROM scan_state WHERE key='cursor'")
    connection.commit()
    return len(symbols)

def refresh_metadata(provider, connection: sqlite3.Connection, symbols: list[str]) -> int:
    for column in ("industry", "sector"):
        try:
            connection.execute(f"ALTER TABLE assets ADD COLUMN {column} TEXT")
        except sqlite3.OperationalError:
            pass
    updated = 0
    for symbol in symbols:
        try:
            profile = provider.profile(symbol)
            connection.execute("UPDATE assets SET industry=?,sector=? WHERE symbol=?",
                               (profile.get("finnhubIndustry") or "Unknown", profile.get("sector") or "Unknown", symbol))
            updated += 1
        except Exception:
            continue
    connection.commit()
    return updated

def symbols_missing_metadata(connection: sqlite3.Connection, limit: int = 100) -> list[str]:
    columns = [row[1] for row in connection.execute("PRAGMA table_info(assets)")]
    if "industry" not in columns:
        return cached_symbols(connection, limit)
    return [row[0] for row in connection.execute("SELECT symbol FROM assets WHERE industry IS NULL OR industry='' LIMIT ?", (limit,))]

def cached_symbols(connection: sqlite3.Connection, limit: int | None = None) -> list[str]:
    connection.execute("CREATE TABLE IF NOT EXISTS assets(symbol TEXT PRIMARY KEY, name TEXT, exchange TEXT, tradable INTEGER, updated_at TEXT, industry TEXT, sector TEXT)")
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
