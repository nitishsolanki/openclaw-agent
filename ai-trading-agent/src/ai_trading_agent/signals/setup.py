from dataclasses import dataclass
from ..risk.risk_engine import RiskDecision, RiskLimits, TradeSetup, validate_trade

@dataclass(frozen=True)
class GeneratedSetup:
    trade: TradeSetup
    risk: RiskDecision
    signal_score: float
    confidence: str

def generate_long_setup(symbol: str, price: float, atr: float, signal_score: float,
                        sector: str, account_value: float, limits: RiskLimits | None = None) -> GeneratedSetup:
    if price <= 0 or atr <= 0:
        raise ValueError("price and ATR must be positive")
    # ATR-derived levels are deterministic; risk_engine remains the authority on approval and size.
    stop = price - 1.0 * atr
    target = price + 2.0 * atr
    trade = TradeSetup(symbol.upper(), price, stop, target, sector)
    risk = validate_trade(trade, account_value, limits=limits)
    confidence = "high" if signal_score >= 85 else "medium" if signal_score >= 75 else "low"
    return GeneratedSetup(trade, risk, signal_score, confidence)

