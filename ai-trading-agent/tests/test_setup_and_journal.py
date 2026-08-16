import sqlite3
from ai_trading_agent.journal.database import connect, record_signal
from ai_trading_agent.signals.setup import generate_long_setup

def test_setup_uses_atr_and_risk_engine():
    setup = generate_long_setup("abc", 100, 5, 88, "Technology", 100_000)
    assert setup.trade.stop == 95
    assert setup.trade.target == 110
    assert setup.risk.approved
    assert setup.confidence == "high"

def test_signal_is_journaled():
    connection = connect(":memory:")
    signal_id = record_signal(connection, "abc", "LONG", 88, 100, 95, 110, "VWAP reclaim")
    row = connection.execute("SELECT symbol, final_score FROM signals WHERE id=?", (signal_id,)).fetchone()
    assert row == ("ABC", 88.0)

