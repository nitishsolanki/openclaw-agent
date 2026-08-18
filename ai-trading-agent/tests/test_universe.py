from types import SimpleNamespace
import sqlite3
from ai_trading_agent.data.universe import refresh_assets, cached_symbols
from ai_trading_agent.data.bars_batch import fetch_liquid_bars

def test_asset_cache():
    db = sqlite3.connect(":memory:")
    provider = SimpleNamespace(get_assets=lambda: [SimpleNamespace(symbol="ABC", name="A", exchange="NYSE", tradable=True)])
    assert refresh_assets(provider, db) == 1
    assert cached_symbols(db) == ["ABC"]

