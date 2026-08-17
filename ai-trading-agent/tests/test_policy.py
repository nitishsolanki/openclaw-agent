from ai_trading_agent.execution.policy import ExecutionMode, authorize_order

def test_signal_only_never_authorizes_orders():
    assert not authorize_order(ExecutionMode.SIGNAL_ONLY, True)
    assert not authorize_order(ExecutionMode.DISABLED, True)

def test_paper_requires_risk_approval():
    assert authorize_order(ExecutionMode.PAPER, True)
    assert not authorize_order(ExecutionMode.PAPER, False)

