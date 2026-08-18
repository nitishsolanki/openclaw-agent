import argparse
import time
from pathlib import Path
from ai_trading_agent.cli import run_scan
from ai_trading_agent.journal.database import connect
from ai_trading_agent.execution.paper_trader import PaperTrader
from ai_trading_agent.portfolio.analytics import performance_report

def run(root: Path, cycles: int, interval: int) -> None:
    db = connect(root / "trading.db")
    trader = PaperTrader(db)
    for cycle in range(cycles):
        signals = run_scan(root)
        print(f"cycle={cycle + 1} signals={len(signals)} open_orders={len(trader.open_orders())}")
        if cycle + 1 < cycles:
            time.sleep(interval)
    rows = db.execute("SELECT realized_pnl FROM trades WHERE status='closed' AND realized_pnl IS NOT NULL").fetchall()
    print({"closed_trades": len(rows), "performance": performance_report([row[0] for row in rows])})

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--cycles", type=int, default=1)
    parser.add_argument("--interval", type=int, default=900)
    args = parser.parse_args()
    run(args.root, args.cycles, args.interval)

