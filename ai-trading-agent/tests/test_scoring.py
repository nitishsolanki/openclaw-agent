import pytest
from ai_trading_agent.signals.scoring import score_signal

def test_score_is_bounded_and_directional():
    weights = {"market": .5, "sector": .5}
    signal = score_signal("spy", {"market": 90, "sector": 80}, weights)
    assert signal.final_score == 85
    assert signal.direction == "LONG"

def test_weights_must_sum_to_one():
    with pytest.raises(ValueError):
        score_signal("SPY", {"market": 90}, {"market": .5})

