from ..portfolio.analytics import performance_report

def walk_forward(pnls: list[float], train_size: int = 50, test_size: int = 20) -> list[dict]:
    reports = []
    cursor = train_size
    while cursor < len(pnls):
        test = pnls[cursor:cursor + test_size]
        if test:
            reports.append({"start": cursor, "end": cursor + len(test),
                            "performance": performance_report(test)})
        cursor += test_size
    return reports

def apply_execution_costs(pnl: float, slippage_bps: float = 5.0, latency_bps: float = 1.0) -> float:
    return round(pnl * (1 - (slippage_bps + latency_bps) / 10_000), 2)

