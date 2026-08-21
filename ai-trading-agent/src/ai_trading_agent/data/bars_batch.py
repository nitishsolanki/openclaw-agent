import pandas as pd

def fetch_liquid_bars(provider, symbols: list[str], minimum_price: float = 10.0,
                      minimum_average_volume: int = 1_000_000, minimum_average_dollar_volume: float = 25_000_000,
                      minimum_median_dollar_volume: float = 15_000_000, maximum_spread_pct: float = 0.50,
                      minimum_history: int = 60, limit: int | None = None) -> dict[str, pd.DataFrame]:
    result = {}
    for symbol in symbols if limit is None else symbols[:limit]:
        try:
            bars = provider.get_bars(symbol)
            if bars.empty or len(bars) < minimum_history or float(bars["close"].iloc[-1]) < minimum_price:
                continue
            recent = bars.tail(20).copy()
            dollar_volume = recent["close"] * recent["volume"]
            if recent["volume"].mean() < minimum_average_volume:
                continue
            if dollar_volume.mean() < minimum_average_dollar_volume or dollar_volume.median() < minimum_median_dollar_volume:
                continue
            spread = provider.get_spread(symbol) if hasattr(provider, "get_spread") else None
            if spread is not None and spread > maximum_spread_pct:
                continue
            result[symbol] = bars
        except Exception:
            continue
    return result
