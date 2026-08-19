import sqlite3
from types import SimpleNamespace
from ai_trading_agent.data.universe import refresh_metadata, symbols_missing_metadata

def test_metadata_refresh_updates_sector_and_industry():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE assets(symbol TEXT PRIMARY KEY, name TEXT, exchange TEXT, tradable INTEGER, updated_at TEXT, industry TEXT, sector TEXT)")
    db.execute("INSERT INTO assets VALUES ('ABC','','',1,'',NULL,NULL)")
    provider = SimpleNamespace(profile=lambda symbol: {"finnhubIndustry": "Semiconductors", "sector": "Technology"})
    assert refresh_metadata(provider, db, symbols_missing_metadata(db)) == 1
    assert db.execute("SELECT industry,sector FROM assets WHERE symbol='ABC'").fetchone() == ('Semiconductors', 'Technology')

