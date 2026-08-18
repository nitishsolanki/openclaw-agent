from ai_trading_agent.screening.universe import liquid_candidates
from ai_trading_agent.validation.walk_forward import apply_execution_costs, walk_forward
from ai_trading_agent.execution.reconciliation import reconcile
import pandas as pd

def test_liquidity_filter():
    result = liquid_candidates(pd.DataFrame({"symbol": ["A", "B"], "price": [10, 3], "average_volume": [2_000_000, 2_000_000]}))
    assert result["symbol"].tolist() == ["A"]

def test_walk_forward_and_costs():
    assert len(walk_forward([10] * 75, 50, 20)) == 2
    assert apply_execution_costs(100) < 100

def test_reconciliation():
    result = reconcile([{"id": 1, "status": "open"}], [{"id": 1, "status": "closed"}, {"id": 2, "status": "open"}])
    assert result["unknown_at_broker"] == ["2"]
    assert result["status_mismatches"] == ["1"]

