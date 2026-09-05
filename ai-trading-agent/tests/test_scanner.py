import pandas as pd
from ai_trading_agent.screening.scanner import Candidate, scan

def bars(closes):
    index = pd.date_range("2026-01-01", periods=len(closes), freq="D")
    return pd.DataFrame({"high": [x + 1 for x in closes], "low": [x - 1 for x in closes],
                         "close": closes, "volume": [100] * len(closes)}, index=index)

def test_scanner_returns_ranked_signals():
    benchmark = pd.Series([100] * 30)
    weights = {"market": .10, "sector": .20, "relative_strength": .20, "vwap": .15,
               "trend": .10, "volume": .10, "momentum": .05, "volatility": .05, "options": .05}
    candidates = [Candidate("AAA", "Technology", bars(range(10, 40)), 90),
                  Candidate("BBB", "Energy", bars(range(10, 25)), 60)]
    results = scan(candidates, benchmark, weights)
    assert [result.symbol for result in results] == ["AAA", "BBB"]
    assert results[0].final_score > results[1].final_score

def test_scanner_applies_profile_filters():
    benchmark = pd.Series([100] * 30)
    weights = {"market": .5, "sector": .5}
    candidates = [Candidate("AAA", "Technology", bars(range(10, 40)), 90),
                  Candidate("BBB", "Energy", bars(range(10, 25)), 60)]
    results = scan(candidates, benchmark, weights, market_score=50,
                   minimum_filters={"sector": 70})
    assert [result.symbol for result in results] == ["AAA"]

