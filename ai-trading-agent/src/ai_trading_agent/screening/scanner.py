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

def extension_score(close: pd.Series, lookback: int = 50) -> float:
    """Score distance from the 50-bar simple moving average."""
    if len(close) < lookback:
        return 50.0
    sma50 = float(close.rolling(lookback).mean().iloc[-1])
    distance_pct = (float(close.iloc[-1]) / sma50 - 1.0) * 100.0
    if distance_pct <= 5.0:
        return 100.0
    if distance_pct >= 25.0:
        return 0.0
    return _bounded(100.0 - (distance_pct - 5.0) * 5.0)

def score_candidate(candidate: Candidate, benchmark_close: pd.Series,
                    weights: dict[str, float], market_score: float = 50.0,
                    news_score: float = 50.0, options_score: float = 50.0) -> TradeSignal:
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
    momentum = 0.8 * momentum + 0.2 * news_score
    components = {
        "market": market_score, "sector": candidate.sector_score,
        "sector_name": candidate.sector,
        "relative_strength": rs_score, "vwap": vwap_score, "trend": trend,
        "volume": volume_score, "momentum": momentum, "volatility": 50.0, "options": options_score,
    }
    if "extension" in weights:
        components["extension"] = extension_score(close)
    return score_signal(candidate.symbol, components, weights)

def scan(candidates: list[Candidate], benchmark_close: pd.Series,
         weights: dict[str, float], limit: int = 10, market_score: float = 50.0,
         enrichments: dict[str, dict[str, float]] | None = None,
         minimum_filters: dict[str, float] | None = None,
         minimum_score: float | None = None) -> list[TradeSignal]:
    enrichments = enrichments or {}
    signals = (score_candidate(candidate, benchmark_close, weights, market_score,
                               enrichments.get(candidate.symbol, {}).get("news", 50.0),
                               enrichments.get(candidate.symbol, {}).get("options", 50.0))
               for candidate in candidates)
    def passes_filters(signal: TradeSignal) -> bool:
        if signal.direction == "SHORT":
            return False
        if minimum_score is not None and signal.final_score < minimum_score:
            return False
        return all(signal.components.get(name, 0.0) >= threshold
                   for name, threshold in (minimum_filters or {}).items())

    return sorted((signal for signal in signals if passes_filters(signal)),
                  key=lambda signal: signal.final_score, reverse=True)[:limit]
