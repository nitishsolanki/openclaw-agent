from pathlib import Path
import yaml

DEFAULT_WEIGHTS = {
    "market": .10, "sector": .20, "relative_strength": .20, "vwap": .15,
    "trend": .10, "volume": .10, "momentum": .05, "volatility": .05, "options": .05,
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
    return {**raw, "weights": weights, "filters": filters}
