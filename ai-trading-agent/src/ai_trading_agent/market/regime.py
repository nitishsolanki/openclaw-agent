from dataclasses import dataclass
import pandas as pd

@dataclass(frozen=True)
class MarketRegime:
    score: float
    label: str

def detect_regime(benchmark: pd.DataFrame) -> MarketRegime:
    close = benchmark["close"]
    ema20 = close.ewm(span=20, adjust=False).mean().iloc[-1]
    ema50 = close.ewm(span=50, adjust=False).mean().iloc[-1]
    price = close.iloc[-1]
    score = 50.0
    score += 25.0 if price > ema20 else -25.0
    score += 25.0 if ema20 > ema50 else -25.0
    score = max(0.0, min(100.0, score))
    label = "Strong Bull" if score >= 80 else "Bull" if score >= 65 else "Neutral" if score >= 45 else "Bear" if score >= 30 else "Strong Bear"
    return MarketRegime(score, label)

