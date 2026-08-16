import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS signals (
 id INTEGER PRIMARY KEY, timestamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
 symbol TEXT NOT NULL, direction TEXT NOT NULL, final_score REAL NOT NULL,
 entry REAL, stop REAL, target REAL, reasoning TEXT
);
CREATE TABLE IF NOT EXISTS trades (
 id INTEGER PRIMARY KEY, signal_id INTEGER, symbol TEXT NOT NULL, side TEXT NOT NULL,
 quantity INTEGER NOT NULL, entry_price REAL NOT NULL, exit_price REAL,
 stop_price REAL NOT NULL, target_price REAL NOT NULL, status TEXT NOT NULL DEFAULT 'pending',
 realized_pnl REAL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, closed_at TEXT
);
"""

def connect(path: str | Path) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.executescript(SCHEMA)
    return connection

def record_signal(connection: sqlite3.Connection, symbol: str, direction: str, score: float,
                  entry: float | None = None, stop: float | None = None,
                  target: float | None = None, reasoning: str = "") -> int:
    cursor = connection.execute(
        "INSERT INTO signals(symbol,direction,final_score,entry,stop,target,reasoning) VALUES (?,?,?,?,?,?,?)",
        (symbol.upper(), direction, score, entry, stop, target, reasoning))
    connection.commit()
    return int(cursor.lastrowid)

