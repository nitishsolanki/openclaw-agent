from types import SimpleNamespace
import sqlite3
from ai_trading_agent.data.universe import refresh_assets, cached_symbols, next_batch
from ai_trading_agent.data.bars_batch import fetch_liquid_bars

def test_asset_cache():
    db = sqlite3.connect(":memory:")
    provider = SimpleNamespace(get_assets=lambda: [SimpleNamespace(symbol="ABC", name="A", exchange="NYSE", tradable=True)])
    assert refresh_assets(provider, db) == 1
    assert cached_symbols(db) == ["ABC"]

def test_batches_rotate_without_repeating_until_wrap():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE assets(symbol TEXT PRIMARY KEY, name TEXT, exchange TEXT, tradable INTEGER, updated_at TEXT)")
    db.executemany("INSERT INTO assets VALUES (?,?,?,?,?)", [(s, "", "", 1, "") for s in ["A", "B", "C", "D"]])
    assert next_batch(db, 2) == ["A", "B"]
    assert next_batch(db, 2) == ["C", "D"]
    assert next_batch(db, 2) == ["A", "B"]
