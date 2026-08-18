from ai_trading_agent.risk.risk_engine import RiskLimits, TradeSetup, validate_trade

def test_valid_trade_is_sized_with_hard_caps():
    result = validate_trade(TradeSetup("ABC", 100, 95, 115, "Technology"), 100_000)
    assert result.approved
    assert result.shares == 100
    assert result.dollar_risk == 500

def test_bad_rr_is_rejected():
    result = validate_trade(TradeSetup("ABC", 100, 95, 105, "Technology"), 100_000)
    assert not result.approved
    assert any("risk/reward" in reason for reason in result.reasons)

def test_portfolio_limits_are_rejected():
    result = validate_trade(TradeSetup("ABC", 100, 95, 115, "Technology"), 100_000,
                            open_positions=8, limits=RiskLimits())
    assert not result.approved

def test_paper_allocation_cap_limits_position_size():
    limits = RiskLimits(paper_allocation_cap=100)
    result = validate_trade(TradeSetup("ABC", 5, 4.5, 6, "Technology"), 100_000, limits=limits)
    assert result.shares == 1
    assert result.dollar_risk == 0.5
