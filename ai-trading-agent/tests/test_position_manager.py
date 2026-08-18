from ai_trading_agent.portfolio.position_manager import PositionState, evaluate_exit, trailing_stop

def position():
    return PositionState("ABC", 10, 100, 95, 110, 82, "Technology")

def test_stop_and_target_rules():
    assert evaluate_exit(position(), 94, 82, True, True, True).action == "SELL_ALL"
    assert evaluate_exit(position(), 110, 90, True, True, True).action == "TAKE_PARTIAL"

def test_invalidation_and_rotation():
    assert evaluate_exit(position(), 101, 70, True, True, True).reason == "score_below_exit_threshold"
    assert evaluate_exit(position(), 101, 93, True, True, True).action == "ROTATE"

def test_trailing_stop_never_below_entry():
    assert trailing_stop(100, 110, 4) == 106
    assert trailing_stop(100, 102, 4) == 100

