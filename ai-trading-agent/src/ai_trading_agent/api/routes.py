from pathlib import Path
from fastapi import FastAPI
from ..cli import run_scan
from ..journal.database import connect
from ..execution.paper_trader import PaperTrader

def create_app(root: str | Path = ".") -> FastAPI:
    app = FastAPI(title="AI Trading Agent", version="0.1.0")
    root_path = Path(root)

    @app.get("/health")
    def health() -> dict:
        return {"status": "ok", "execution_mode": "signal_only"}

    @app.get("/scan")
    def scan() -> dict:
        results = run_scan(root_path)
        return {"signals": [{"symbol": item.symbol, "direction": item.direction,
                             "score": item.final_score, "components": item.components}
                            for item in results]}

    @app.get("/paper/orders")
    def paper_orders() -> dict:
        db = connect(root_path / "trading.db")
        return {"orders": [order.__dict__ for order in PaperTrader(db).open_orders()]}
    return app
