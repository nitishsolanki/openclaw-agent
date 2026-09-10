from __future__ import annotations

import pandas as pd


def _bounded(value: float) -> float:
    return max(0.0, min(100.0, float(value)))


def _return(close: pd.Series, periods: int) -> float:
    return (float(close.iloc[-1]) / float(close.iloc[-periods - 1]) - 1) * 100 if len(close) > periods else 0.0


def evaluate_setup(bars: pd.DataFrame, benchmark: pd.Series, config: dict[str, float]) -> dict[str, float | str]:
    close = bars["close"].astype(float)
    high, low = bars["high"].astype(float), bars["low"].astype(float)
    volume = bars.get("volume", pd.Series(1.0, index=bars.index)).astype(float)
    price = float(close.iloc[-1])
    dma20 = float(close.rolling(20).mean().iloc[-1]) if len(close) >= 20 else price
    dma50 = float(close.rolling(50).mean().iloc[-1]) if len(close) >= 50 else price
    atr = float((high - low).rolling(14).mean().iloc[-1]) if len(close) >= 14 else price * .02
    breakout = float(close.iloc[:-1].rolling(20).max().iloc[-1]) if len(close) >= 21 else price
    dist_breakout = max(0.0, (breakout - price) / price * 100)
    range_now = float((close.tail(10).max() - close.tail(10).min()) / price * 100) if len(close) >= 10 else 10
    range_prior = float((close.iloc[-20:-10].max() - close.iloc[-20:-10].min()) / price * 100) if len(close) >= 20 else range_now
    compression = _bounded(100 - range_now * 12)
    atr_pct = atr / max(price, .01) * 100
    volatility = _bounded(100 - atr_pct * 12)
    volume_ratio = float(volume.tail(10).mean() / max(volume.tail(30).mean(), 1)) if len(volume) >= 30 else 1
    accumulation = _bounded(50 + (volume_ratio - 1) * 100 + (float(volume[close.diff() > 0].tail(10).mean() or 0) / max(float(volume.tail(10).mean()), 1) - float(volume[close.diff() < 0].tail(10).mean() or 0) / max(float(volume.tail(10).mean()), 1)) * 25)
    aligned = pd.concat([close, benchmark], axis=1).dropna()
    rs5 = ((aligned.iloc[-1, 0] / aligned.iloc[-6, 0]) - (aligned.iloc[-1, 1] / aligned.iloc[-6, 1])) if len(aligned) > 6 else 0
    rs20 = ((aligned.iloc[-1, 0] / aligned.iloc[-21, 0]) - (aligned.iloc[-1, 1] / aligned.iloc[-21, 1])) if len(aligned) > 21 else 0
    rs_accel = _bounded(50 + (rs5 - rs20 / 4) * 350)
    trend_accel = 85 if price > dma20 > dma50 else 55 if price > dma20 else 25
    ret5, ret10, ret20 = _return(close, 5), _return(close, 10), _return(close, 20)
    momentum = _bounded(50 + (ret5 - ret20 / 4) * 4)
    support = _bounded(100 - abs(price - min(float(close.tail(20).min()), dma20)) / max(price, .01) * 1000)
    breakout_score = _bounded(100 - dist_breakout * 20)
    metrics = {"relative_strength_acceleration": _bounded(rs_accel), "trend_acceleration": trend_accel, "compression": compression, "volatility_contraction": volatility, "volume_accumulation": accumulation, "breakout_distance": breakout_score, "support_quality": support, "momentum_improvement": momentum}
    early = round(sum(metrics[key] * config[key] for key in metrics), 2)
    atr_extension = (price - dma20) / max(atr, .01)
    extended = ret20 >= config["extended_return_20d_pct"] or atr_extension >= config["extended_atr_multiple"]
    confirmed = price > breakout + atr * config.get("confirmed_breakout_atr_multiple", .5) and volume_ratio >= config.get("confirmed_volume_ratio", 1.5)
    failed = price < dma50 and ret20 < float(config.get("failed_return_20d_pct", -8)) and early < float(config.get("failed_early_score", 45))
    if failed: maturity = "FAILED"
    elif confirmed and accumulation >= 55: maturity = "CONFIRMED"
    elif dist_breakout <= config["breakout_ready_distance_pct"] and early >= 60: maturity = "BREAKOUT"
    elif ret20 > 5 and compression >= 60 and early >= 55: maturity = "PULLBACK"
    else: maturity = "BUILDING"
    timing = round(_bounded(early - max(0, ret20 - 10) * 2 - max(0, atr_extension - 1.5) * 8), 2)
    recommendation = "WAIT" if extended else "AVOID" if maturity == "FAILED" else "WATCH" if maturity == "PULLBACK" else "PRIORITIZE"
    return {**metrics, "early_setup_score": early, "entry_timing_score": timing, "opportunity_score": round(config["profile_score_weight"] * 50 + config["early_setup_weight"] * timing, 2), "setup_maturity": maturity, "extended": extended, "return_5d": round(ret5, 2), "return_10d": round(ret10, 2), "return_20d": round(ret20, 2), "distance_to_breakout": round(dist_breakout, 2), "atr_extension": round(atr_extension, 2), "recommendation": recommendation}
