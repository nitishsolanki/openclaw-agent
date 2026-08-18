import math

def performance_report(pnls: list[float]) -> dict[str, float]:
    if not pnls:
        return {"trades": 0, "win_rate": 0.0, "profit_factor": 0.0, "net_pnl": 0.0, "max_drawdown": 0.0}
    wins = [x for x in pnls if x > 0]
    losses = [x for x in pnls if x < 0]
    equity = peak = drawdown = 0.0
    for pnl in pnls:
        equity += pnl; peak = max(peak, equity); drawdown = max(drawdown, peak - equity)
    gross_loss = abs(sum(losses))
    return {"trades": len(pnls), "win_rate": round(len(wins) / len(pnls), 4),
            "profit_factor": round(sum(wins) / gross_loss, 4) if gross_loss else math.inf,
            "net_pnl": round(sum(pnls), 2), "max_drawdown": round(drawdown, 2)}

