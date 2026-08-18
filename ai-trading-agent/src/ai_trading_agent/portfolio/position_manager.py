from dataclasses import dataclass

@dataclass(frozen=True)
class PositionState:
    symbol: str
    quantity: int
    entry_price: float
    stop_price: float
    target_price: float
    signal_score: float
    sector: str

@dataclass(frozen=True)
class ExitDecision:
    action: str
    reason: str
    quantity: int

def evaluate_exit(position: PositionState, current_price: float, current_score: float,
                  above_vwap: bool, trend_intact: bool, sector_active: bool,
                  rotation_buffer: float = 10.0) -> ExitDecision:
    if current_price <= position.stop_price:
        return ExitDecision("SELL_ALL", "stop_loss", position.quantity)
    if current_price >= position.target_price:
        return ExitDecision("TAKE_PARTIAL", "target_reached", max(1, position.quantity // 2))
    if not above_vwap and not trend_intact:
        return ExitDecision("SELL_ALL", "technical_invalidation", position.quantity)
    if not sector_active and current_score < 75:
        return ExitDecision("SELL_ALL", "sector_theme_lost", position.quantity)
    if current_score < 75:
        return ExitDecision("SELL_ALL", "score_below_exit_threshold", position.quantity)
    if current_score >= position.signal_score + rotation_buffer:
        return ExitDecision("ROTATE", "stronger_candidate", position.quantity)
    return ExitDecision("HOLD", "conditions_intact", 0)

def trailing_stop(entry: float, current_price: float, atr: float, multiple: float = 1.0) -> float:
    if atr <= 0:
        raise ValueError("ATR must be positive")
    return max(entry, current_price - multiple * atr)

