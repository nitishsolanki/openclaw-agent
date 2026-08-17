import pandas as pd
from ai_trading_agent.market.regime import detect_regime

def test_rising_benchmark_is_bullish():
    close = list(range(100, 130))
    frame = pd.DataFrame({"close": close})
    regime = detect_regime(frame)
    assert regime.score == 100
    assert regime.label == "Strong Bull"

