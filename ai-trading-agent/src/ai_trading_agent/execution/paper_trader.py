from dataclasses import dataclass
import sqlite3

from ..risk.risk_engine import RiskDecision, TradeSetup

@dataclass(frozen=True)
class PaperOrder:
    id: int
    symbol: str
    quantity: int
    entry_price: float
    stop_price: float
    target_price: float
    status: str

class PaperTrader:
    """Deterministic local paper broker. Orders fill at the requested entry price."""
    def __init__(self, connection: sqlite3.Connection, account_value: float = 100_000.0):
        self.connection = connection
        self.account_value = float(account_value)

    def submit_long(self, setup: TradeSetup, risk: RiskDecision, signal_id: int | None = None) -> PaperOrder:
        if not risk.approved:
            raise ValueError("paper order rejected: " + "; ".join(risk.reasons))
        cursor = self.connection.execute(
            "INSERT INTO trades(signal_id,symbol,side,quantity,entry_price,stop_price,target_price,status) "
            "VALUES (?,?,?,?,?,?,?,?)",
            (signal_id, setup.symbol.upper(), "BUY", risk.shares, setup.entry, setup.stop, setup.target, "open"))
        self.connection.commit()
        return PaperOrder(cursor.lastrowid, setup.symbol.upper(), risk.shares, setup.entry,
                          setup.stop, setup.target, "open")

    def close(self, order_id: int, exit_price: float) -> float:
        row = self.connection.execute(
            "SELECT quantity,entry_price,status FROM trades WHERE id=?", (order_id,)).fetchone()
        if row is None:
            raise KeyError(f"unknown paper order {order_id}")
        quantity, entry, status = row
        if status != "open":
            raise ValueError("paper order is not open")
        pnl = round((exit_price - entry) * quantity, 2)
        self.connection.execute(
            "UPDATE trades SET exit_price=?,status='closed',realized_pnl=?,closed_at=CURRENT_TIMESTAMP WHERE id=?",
            (exit_price, pnl, order_id))
        self.connection.commit()
        return pnl

    def open_orders(self) -> list[PaperOrder]:
        rows = self.connection.execute(
            "SELECT id,symbol,quantity,entry_price,stop_price,target_price,status FROM trades WHERE status='open'"
        ).fetchall()
        return [PaperOrder(*row) for row in rows]

