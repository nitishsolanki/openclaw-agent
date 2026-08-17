from dataclasses import dataclass
import pandas as pd

from ..indicators.relative_strength import relative_strength
from ..indicators.vwap import vwap_features
from ..signals.scoring import TradeSignal, score_signal

@dataclass(frozen=True)
class Candidate:
    symbol: str
    sector: str
    bars: pd.DataFrame
    sector_score: float

def _bounded(value: float) -> float:
    return max(0.0, min(100.0, value))

def score_candidate(candidate: Candidate, benchmark_close: pd.Series,
                    weights: dict[str, float], market_score: float = 50.0) -> TradeSignal:
    bars = candidate.bars
    close = bars["close"]
    ema20 = close.ewm(span=20, adjust=False).mean().iloc[-1]
    ema50 = close.ewm(span=50, adjust=False).mean().iloc[-1]
    trend = 100.0 if close.iloc[-1] > ema20 > ema50 else 50.0 if close.iloc[-1] > ema20 else 0.0
    vwap = vwap_features(bars)
    vwap_score = _bounded(50 + vwap["distance_pct"] * 10 + (10 if vwap["above"] else 0))
    rs = relative_strength(close, benchmark_close, periods=(5, 20))
    rs_score = _bounded(50 + rs[5] * 500 + rs[20] * 250)
    volume_score = _bounded(vwap["volume_ratio"] * 50)
    momentum = _bounded(50 + (close.iloc[-1] / close.iloc[-6] - 1) * 500) if len(close) > 6 else 50.0
    components = {
        "market": market_score, "sector": candidate.sector_score,
        "relative_strength": rs_score, "vwap": vwap_score, "trend": trend,
        "volume": volume_score, "momentum": momentum, "volatility": 50.0, "options": 50.0,
    }
    return score_signal(candidate.symbol, components, weights)

def scan(candidates: list[Candidate], benchmark_close: pd.Series,
         weights: dict[str, float], limit: int = 10, market_score: float = 50.0) -> list[TradeSignal]:
    return sorted((score_candidate(candidate, benchmark_close, weights, market_score) for candidate in candidates),
                  key=lambda signal: signal.final_score, reverse=True)[:limit]
