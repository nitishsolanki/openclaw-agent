import pandas as pd
from ai_trading_agent.data.market_data import InMemoryMarketData
from ai_trading_agent.sector.live_rotation import rank_sectors

def test_sector_ranker_skips_missing_etfs():
    index = pd.date_range("2026-01-01", periods=25)
    frame = pd.DataFrame({"high": range(101, 126), "low": range(99, 124),
                          "close": range(100, 125), "volume": [1000] * 25}, index=index)
    result = rank_sectors(InMemoryMarketData({"SPY": frame, "XLK": frame}))
    assert len(result) == 1
    assert result[0].sector == "Technology"
    assert result[0].rank == 1

