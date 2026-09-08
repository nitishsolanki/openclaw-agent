from pathlib import Path
import yaml

DEFAULT_WEIGHTS = {
    "market": .10, "sector": .20, "relative_strength": .20, "vwap": .15,
    "trend": .10, "volume": .10, "momentum": .05, "volatility": .05, "options": .05,
}
DEFAULT_EARLY_SETUP = {
    "relative_strength_acceleration": .15, "trend_acceleration": .15,
    "compression": .15, "volatility_contraction": .10,
    "volume_accumulation": .10, "breakout_distance": .15,
    "support_quality": .10, "momentum_improvement": .10,
    "profile_score_weight": .70, "early_setup_weight": .30,
    "breakout_ready_distance_pct": 3.0, "confirmed_breakout_buffer_pct": 1.0,
    "extended_atr_multiple": 3.0, "extended_return_20d_pct": 15.0,
}

def load_strategy(path: str | Path) -> dict:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    configured = raw.get("signals", {})
    weights = {key: float(configured.get(f"{key}_weight", value)) for key, value in DEFAULT_WEIGHTS.items()}
    if "extension_weight" in configured:
        weights["extension"] = float(configured["extension_weight"])
    total = sum(weights.values())
    if abs(total - 1.0) > 1e-6:
        raise ValueError(f"Signal weights must sum to 1.0: {path} totals {total:.6f}; weights={weights}")
    filters = {str(key): float(value) for key, value in (raw.get("filters", {}) or {}).items()}
    early = {key: float((raw.get("early_setup", {}) or {}).get(key, value)) for key, value in DEFAULT_EARLY_SETUP.items()}
    early_total = sum(early[key] for key in ("relative_strength_acceleration", "trend_acceleration", "compression", "volatility_contraction", "volume_accumulation", "breakout_distance", "support_quality", "momentum_improvement"))
    if abs(early_total - 1.0) > 1e-6:
        raise ValueError(f"Early setup weights must sum to 1.0: {path} totals {early_total:.6f}")
    return {**raw, "weights": weights, "filters": filters, "early_setup": early}
