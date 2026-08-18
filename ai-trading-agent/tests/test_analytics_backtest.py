import pandas as pd
from ai_trading_agent.portfolio.analytics import performance_report
from ai_trading_agent.backtest.simple import moving_average_backtest

def test_performance_report():
    report = performance_report([10, -5, 15])
    assert report["trades"] == 3 and report["win_rate"] == 0.6667 and report["net_pnl"] == 20

def test_backtest_returns_performance():
    result = moving_average_backtest(pd.DataFrame({"close": list(range(1, 30))}))
    assert result["performance"]["trades"] >= 1

