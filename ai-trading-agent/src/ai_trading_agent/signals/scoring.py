from dataclasses import dataclass

@dataclass(frozen=True)
class TradeSignal:
    symbol: str
    direction: str
    final_score: float
    components: dict[str, float]

    def __post_init__(self) -> None:
        if self.direction.upper() == "SHORT":
            raise ValueError("short signals are disabled; only long trades are allowed")

def score_signal(symbol: str, components: dict[str, float], weights: dict[str, float]) -> TradeSignal:
    missing = set(weights) - set(components)
    if missing:
        raise ValueError(f"Missing score components: {sorted(missing)}")
    if abs(sum(weights.values()) - 1.0) > 1e-6:
        raise ValueError("Signal weights must sum to 1.0")
    score = max(0.0, min(100.0, sum(components[k] * weights[k] for k in weights)))
    return TradeSignal(symbol=symbol.upper(), direction="LONG" if score >= 50 else "WATCH",
                       final_score=round(score, 2), components=dict(components))

