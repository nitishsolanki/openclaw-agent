from pathlib import Path
from fastapi import FastAPI
from ..cli import run_scan

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
    return app

