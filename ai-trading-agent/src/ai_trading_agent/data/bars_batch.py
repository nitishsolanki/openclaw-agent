import pandas as pd

def fetch_liquid_bars(provider, symbols: list[str], minimum_price: float = 5.0,
                      minimum_average_volume: int = 1_000_000, limit: int = 100) -> dict[str, pd.DataFrame]:
    result = {}
    for symbol in symbols[:limit]:
        try:
            bars = provider.get_bars(symbol)
            if bars.empty or float(bars["close"].iloc[-1]) <= minimum_price:
                continue
            avg_volume = bars["volume"].tail(20).mean()
            if avg_volume >= minimum_average_volume:
                result[symbol] = bars
        except Exception:
            continue
    return result

