import pandas as pd

def sector_score(sector: pd.DataFrame, benchmark_close: pd.Series) -> float:
    close = sector["close"]
    rs5 = relative_return(close, benchmark_close, 5)
    rs10 = relative_return(close, benchmark_close, 10)
    rs20 = relative_return(close, benchmark_close, 20)
    trend = 1.0 if close.iloc[-1] > close.ewm(span=20, adjust=False).mean().iloc[-1] else 0.0
    vol = sector["volume"].iloc[-1] / sector["volume"].rolling(20).mean().iloc[-1]
    raw = 0.20 * rs5 + 0.20 * rs10 + 0.15 * rs20 + 0.15 * trend + 0.15 * min(vol, 2) / 2 + 0.15 * trend
    return max(0.0, min(100.0, 50.0 + raw * 100.0))

def relative_return(series: pd.Series, benchmark: pd.Series, period: int) -> float:
    if len(series) <= period or len(benchmark) <= period:
        return 0.0
    return (series.iloc[-1] / series.iloc[-period-1] - 1) - (benchmark.iloc[-1] / benchmark.iloc[-period-1] - 1)

