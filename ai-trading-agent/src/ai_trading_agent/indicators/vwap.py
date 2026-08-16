import pandas as pd

def vwap(bars: pd.DataFrame) -> pd.Series:
    typical = (bars["high"] + bars["low"] + bars["close"]) / 3
    return (typical * bars["volume"]).cumsum() / bars["volume"].cumsum()

def vwap_features(bars: pd.DataFrame, average_window: int = 20) -> dict[str, float | bool]:
    values = vwap(bars)
    close = float(bars["close"].iloc[-1])
    avg_volume = bars["volume"].rolling(average_window).mean().iloc[-1]
    volume_ratio = float(bars["volume"].iloc[-1] / avg_volume) if avg_volume else 0.0
    slope = float(values.iloc[-1] - values.iloc[-2]) if len(values) > 1 else 0.0
    return {"vwap": float(values.iloc[-1]), "distance_pct": (close / values.iloc[-1] - 1) * 100,
            "above": close > values.iloc[-1], "slope": slope, "volume_ratio": volume_ratio}

