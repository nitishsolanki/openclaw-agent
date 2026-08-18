from dataclasses import dataclass

@dataclass(frozen=True)
class RiskLimits:
    risk_per_trade: float = 0.005
    max_position_percent: float = 0.10
    max_sector_percent: float = 0.25
    max_daily_loss_percent: float = 0.02
    max_open_positions: int = 8
    minimum_rr: float = 2.0
    paper_allocation_cap: float | None = None

@dataclass(frozen=True)
class TradeSetup:
    symbol: str
    entry: float
    stop: float
    target: float
    sector: str

@dataclass(frozen=True)
class RiskDecision:
    approved: bool
    shares: int
    dollar_risk: float
    risk_reward: float
    reasons: tuple[str, ...]

def validate_trade(setup: TradeSetup, account_value: float, current_sector_exposure: float = 0.0,
                   open_positions: int = 0, daily_loss: float = 0.0,
                   limits: RiskLimits | None = None) -> RiskDecision:
    limits = limits or RiskLimits()
    reasons: list[str] = []
    if setup.entry <= 0 or setup.stop <= 0 or setup.target <= 0:
        reasons.append("prices must be positive")
    if not setup.stop < setup.entry < setup.target:
        reasons.append("long setup requires stop < entry < target")
    per_share = abs(setup.entry - setup.stop)
    rr = (setup.target - setup.entry) / per_share if per_share else 0.0
    if rr < limits.minimum_rr:
        reasons.append(f"risk/reward {rr:.2f} is below minimum {limits.minimum_rr:.2f}")
    if open_positions >= limits.max_open_positions:
        reasons.append("maximum open positions reached")
    effective_account = min(account_value, limits.paper_allocation_cap) if limits.paper_allocation_cap else account_value
    if daily_loss >= effective_account * limits.max_daily_loss_percent:
        reasons.append("maximum daily loss reached")
    risk_budget = effective_account * limits.risk_per_trade
    position_cap = effective_account * limits.max_position_percent
    sector_room = max(0.0, effective_account * limits.max_sector_percent - current_sector_exposure)
    shares = int(min(risk_budget / per_share if per_share else 0, position_cap / setup.entry,
                     sector_room / setup.entry if setup.entry else 0))
    dollar_risk = round(shares * per_share, 2)
    if shares < 1:
        reasons.append("calculated position size is less than one share")
    return RiskDecision(not reasons, shares, dollar_risk, round(rr, 2), tuple(reasons))
