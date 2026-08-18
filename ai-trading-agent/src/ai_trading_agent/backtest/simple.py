import pandas as pd
from ..portfolio.analytics import performance_report

def moving_average_backtest(bars: pd.DataFrame, fast: int = 5, slow: int = 10) -> dict:
    close = bars["close"]; fast_ma = close.rolling(fast).mean(); slow_ma = close.rolling(slow).mean()
    position = False; entry = 0.0; pnls = []
    for index in range(slow, len(close)):
        if not position and fast_ma.iloc[index] > slow_ma.iloc[index]:
            position, entry = True, float(close.iloc[index])
        elif position and fast_ma.iloc[index] < slow_ma.iloc[index]:
            pnls.append(float(close.iloc[index]) - entry); position = False
    if position: pnls.append(float(close.iloc[-1]) - entry)
    return {"strategy": "moving_average_crossover", "fast": fast, "slow": slow,
            "performance": performance_report(pnls)}

