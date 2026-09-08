from dataclasses import dataclass, replace
import pandas as pd

from ..indicators.relative_strength import relative_strength
from ..indicators.vwap import vwap_features
from ..signals.scoring import TradeSignal, score_signal
from .early_setup import evaluate_setup

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
                    news_score: float = 50.0, options_score: float = 50.0,
                    setup_config: dict[str, float] | None = None) -> TradeSignal:
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
    default_setup = {"relative_strength_acceleration": .15, "trend_acceleration": .15, "compression": .15, "volatility_contraction": .10, "volume_accumulation": .10, "breakout_distance": .15, "support_quality": .10, "momentum_improvement": .10, "profile_score_weight": .70, "early_setup_weight": .30, "breakout_ready_distance_pct": 3.0, "confirmed_breakout_buffer_pct": 1.0, "extended_atr_multiple": 3.0, "extended_return_20d_pct": 15.0}
    setup = evaluate_setup(bars, benchmark_close, setup_config or default_setup)
    components.update(setup)
    signal = score_signal(candidate.symbol, components, weights)
    components["opportunity_score"] = round(float(signal.final_score) * (setup_config or default_setup)["profile_score_weight"] + float(setup["entry_timing_score"]) * (setup_config or default_setup)["early_setup_weight"], 2)
    direction = "WATCH" if setup["setup_maturity"] == "EXTENDED" else signal.direction
    return replace(signal, direction=direction, components=components)

def scan(candidates: list[Candidate], benchmark_close: pd.Series,
         weights: dict[str, float], limit: int = 10, market_score: float = 50.0,
         enrichments: dict[str, dict[str, float]] | None = None,
         minimum_filters: dict[str, float] | None = None,
         minimum_score: float | None = None,
         setup_config: dict[str, float] | None = None) -> list[TradeSignal]:
    enrichments = enrichments or {}
    signals = (score_candidate(candidate, benchmark_close, weights, market_score,
                               enrichments.get(candidate.symbol, {}).get("news", 50.0),
                   enrichments.get(candidate.symbol, {}).get("options", 50.0), setup_config)
               for candidate in candidates)
    def passes_filters(signal: TradeSignal) -> bool:
        if signal.direction == "SHORT":
            return False
        if minimum_score is not None and signal.final_score < minimum_score:
            return False
        return all(signal.components.get(name, 0.0) >= threshold
                   for name, threshold in (minimum_filters or {}).items())

    ranked = sorted((signal for signal in signals if signal.direction != "SHORT"),
                    key=lambda signal: (float(signal.final_score) * .70 + float(signal.components.get("entry_timing_score", 0)) * .30), reverse=True)
    qualified = [replace(signal, profile_status="QUALIFIED")
                 for signal in ranked if passes_filters(signal)]
    qualified_symbols = {signal.symbol for signal in qualified}
    fallback = [replace(signal, profile_status="FILTER_FALLBACK")
                for signal in ranked if signal.symbol not in qualified_symbols]
    return (qualified + fallback)[:limit]
