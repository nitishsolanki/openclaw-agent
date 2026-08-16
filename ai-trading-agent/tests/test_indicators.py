import pandas as pd
from ai_trading_agent.indicators.vwap import vwap
from ai_trading_agent.indicators.relative_strength import relative_strength

def test_vwap_is_volume_weighted():
    bars = pd.DataFrame({"high": [11, 12], "low": [9, 10], "close": [10, 11], "volume": [1, 3]})
    assert list(vwap(bars).round(6)) == [10.0, 10.75]

def test_relative_strength_beats_flat_benchmark():
    stock = pd.Series([10, 11, 12, 13, 14, 15])
    benchmark = pd.Series([10, 10, 10, 10, 10, 10])
    assert relative_strength(stock, benchmark, periods=(1,))[1] > 0

