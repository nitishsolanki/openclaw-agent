import pandas as pd

def relative_strength(stock: pd.Series, benchmark: pd.Series, periods=(1, 5, 20, 60)) -> dict[int, float]:
    aligned = pd.concat([stock, benchmark], axis=1).dropna()
    result = {}
    for period in periods:
        if len(aligned) <= period:
            result[period] = 0.0
            continue
        result[period] = float((aligned.iloc[-1, 0] / aligned.iloc[-period-1, 0] - 1) -
                               (aligned.iloc[-1, 1] / aligned.iloc[-period-1, 1] - 1))
    return result

