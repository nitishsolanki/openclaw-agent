from enum import Enum

class ExecutionMode(str, Enum):
    DISABLED = "disabled"
    SIGNAL_ONLY = "signal_only"
    PAPER = "paper"
    LIVE = "live"

def authorize_order(mode: ExecutionMode, risk_approved: bool) -> bool:
    """Final policy gate. Live execution is never implicitly authorized."""
    return mode in {ExecutionMode.PAPER, ExecutionMode.LIVE} and risk_approved

