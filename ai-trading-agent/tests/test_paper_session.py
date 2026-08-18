from ai_trading_agent.execution.paper_session import PaperSession
from ai_trading_agent.risk.risk_engine import TradeSetup

def test_session_enforces_cap_and_tracks_exit():
    session = PaperSession()
    approved, shares, _ = session.approve_entry(TradeSetup("ABC", 5, 4.5, 6, "Technology"), 88)
    assert approved and shares == 1
    decision = session.evaluate("ABC", 4, 70, True, True, True)
    assert decision.action == "SELL_ALL"
    assert not session.open_positions

