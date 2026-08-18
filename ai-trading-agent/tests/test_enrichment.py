from datetime import date
from ai_trading_agent.signals.enrichment import earnings_risk, news_confirmation

def test_news_confirmation_is_bounded():
    assert news_confirmation([{"headline": "Upgrade and strong growth"}]) > 50
    assert news_confirmation([{"headline": "Downgrade and lawsuit"}]) < 50

def test_upcoming_earnings_reduce_risk_score():
    calendar = {"earningsCalendar": [{"symbol": "ABC", "date": "2026-08-20"}]}
    assert earnings_risk(calendar, "ABC", today=date(2026, 8, 16)) == 25
    assert earnings_risk(calendar, "XYZ", today=date(2026, 8, 16)) == 100

