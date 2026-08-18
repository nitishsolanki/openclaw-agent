from ai_trading_agent.signals.options import options_confirmation

def test_options_score_is_neutral_without_data():
    assert options_confirmation([]) == 50

