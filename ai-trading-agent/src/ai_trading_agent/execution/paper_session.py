from dataclasses import dataclass
from ..risk.risk_engine import RiskLimits, TradeSetup, validate_trade
from ..portfolio.position_manager import PositionState, evaluate_exit

@dataclass
class PaperSession:
    account_value: float = 100.0
    allocated: float = 0.0
    open_positions: dict[str, PositionState] | None = None

    def __post_init__(self):
        if self.open_positions is None:
            self.open_positions = {}

    @property
    def limits(self) -> RiskLimits:
        return RiskLimits(paper_allocation_cap=self.account_value, max_open_positions=2)

    def approve_entry(self, setup: TradeSetup, signal_score: float) -> tuple[bool, int, str]:
        if setup.symbol in self.open_positions:
            return False, 0, "position already open"
        risk = validate_trade(setup, self.account_value, open_positions=len(self.open_positions),
                              limits=self.limits)
        notional = risk.shares * setup.entry
        if risk.approved and self.allocated + notional <= self.account_value:
            self.allocated += notional
            self.open_positions[setup.symbol] = PositionState(setup.symbol, risk.shares, setup.entry,
                                                               setup.stop, setup.target, signal_score, setup.sector)
            return True, risk.shares, "approved"
        return False, risk.shares, "; ".join(risk.reasons) or "allocation cap exceeded"

    def evaluate(self, symbol: str, current_price: float, current_score: float,
                 above_vwap: bool, trend_intact: bool, sector_active: bool):
        position = self.open_positions.get(symbol)
        if not position:
            raise KeyError(symbol)
        decision = evaluate_exit(position, current_price, current_score, above_vwap, trend_intact, sector_active)
        if decision.action in {"SELL_ALL", "ROTATE"}:
            self.allocated = max(0.0, self.allocated - position.entry_price * decision.quantity)
            del self.open_positions[symbol]
        elif decision.action == "TAKE_PARTIAL":
            self.allocated = max(0.0, self.allocated - position.entry_price * decision.quantity)
            self.open_positions[symbol] = PositionState(position.symbol, position.quantity - decision.quantity,
                                                        position.entry_price, position.stop_price, position.target_price,
                                                        position.signal_score, position.sector)
        return decision

