import pandas as pd
from ai_trading_agent.data.market_data import InMemoryMarketData

def test_in_memory_provider_normalizes_symbol_and_filters_dates():
    index = pd.date_range("2026-01-01", periods=3, freq="D")
    bars = pd.DataFrame({"open": [1, 2, 3], "high": [2, 3, 4], "low": [0, 1, 2],
                         "close": [1.5, 2.5, 3.5], "volume": [10, 20, 30]}, index=index)
    provider = InMemoryMarketData({"SPY": bars})
    result = provider.get_bars("spy", start=index[1])
    assert len(result) == 2
    assert provider.get_quote("spy") == 3.5
