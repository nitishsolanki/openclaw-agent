import pytest
from ai_trading_agent.journal.database import connect
from ai_trading_agent.execution.paper_trader import PaperTrader
from ai_trading_agent.risk.risk_engine import TradeSetup, validate_trade

def test_paper_order_open_and_close():
    db = connect(":memory:")
    trader = PaperTrader(db)
    setup = TradeSetup("ABC", 100, 95, 110, "Technology")
    risk = validate_trade(setup, 100_000)
    order = trader.submit_long(setup, risk)
    assert order.status == "open"
    assert trader.close(order.id, 105) == 500
    assert trader.open_orders() == []

def test_rejected_risk_cannot_be_submitted():
    db = connect(":memory:")
    trader = PaperTrader(db)
    setup = TradeSetup("ABC", 100, 95, 105, "Technology")
    risk = validate_trade(setup, 100_000)
    with pytest.raises(ValueError, match="rejected"):
        trader.submit_long(setup, risk)

