from pathlib import Path
from fastapi import FastAPI
from ..cli import run_scan
from ..journal.database import connect
from ..execution.paper_trader import PaperTrader
from ..data.market_data import CsvMarketData
from ..signals.setup import generate_long_setup
from ..sector.live_rotation import rank_sectors
from ..theme.manager import active_theme

def create_app(root: str | Path = ".") -> FastAPI:
    app = FastAPI(title="AI Trading Agent", version="0.1.0")
    root_path = Path(root)

    @app.get("/health")
    def health() -> dict:
        return {"status": "ok", "execution_mode": "signal_only"}

    @app.get("/scan")
    def scan() -> dict:
        results = run_scan(root_path)
        return {"theme": active_theme(root_path), "signals": [{"symbol": item.symbol, "direction": item.direction,
                             "score": item.final_score, "components": item.components}
                            for item in results]}

    @app.get("/paper/orders")
    def paper_orders() -> dict:
        db = connect(root_path / "trading.db")
        return {"orders": [order.__dict__ for order in PaperTrader(db).open_orders()]}

    @app.get("/analyze/{symbol}")
    def analyze(symbol: str) -> dict:
        results = {item.symbol: item for item in run_scan(root_path)}
        item = results.get(symbol.upper())
        if item is None:
            from ..config.env import load_env
            from ..config.settings import load_strategy
            from ..data.market_data import AlpacaMarketData
            from ..market.regime import detect_regime
            from ..screening.scanner import Candidate, score_candidate
            from ..signals.enrichment import news_confirmation
            env = load_env(root_path / "local.env")
            if not env.get("ALPACA_API_KEY") or not env.get("ALPACA_SECRET_KEY"):
                return {"error": f"{symbol.upper()} is unavailable in offline data"}
            provider = AlpacaMarketData(env["ALPACA_API_KEY"], env["ALPACA_SECRET_KEY"])
            try:
                bars = provider.get_bars(symbol.upper())
                benchmark = provider.get_bars("SPY")
                config = load_strategy(root_path / "config" / "strategy.yaml")
                item = score_candidate(Candidate(symbol.upper(), "Unknown", bars, 50.0), benchmark["close"],
                                       config["weights"], detect_regime(benchmark).score)
            except Exception as exc:
                return {"error": f"Unable to analyze {symbol.upper()}: {type(exc).__name__}"}
        if hasattr(item, "final_score"):
            return {"symbol": item.symbol, "direction": item.direction,
                    "score": item.final_score, "components": item.components}
        return {"symbol": item.symbol, "direction": item.direction,
                "score": item.final_score, "components": item.components}

    @app.get("/setup/{symbol}")
    def setup(symbol: str) -> dict:
        from ..config.env import load_env
        from ..data.market_data import AlpacaMarketData
        env = load_env(root_path / "local.env")
        data = (AlpacaMarketData(env["ALPACA_API_KEY"], env["ALPACA_SECRET_KEY"])
                if env.get("ALPACA_API_KEY") and env.get("ALPACA_SECRET_KEY")
                else CsvMarketData(root_path / "data" / "sample"))
        bars = data.get_bars(symbol.upper())
        price = float(bars["close"].iloc[-1])
        tr = (bars["high"] - bars["low"]).rolling(5).mean().iloc[-1]
        generated = generate_long_setup(symbol, price, float(tr), 0.0, "Unknown", 100_000)
        return {"symbol": generated.trade.symbol, "entry": generated.trade.entry,
                "stop": generated.trade.stop, "target": generated.trade.target,
                "shares": generated.risk.shares, "approved": generated.risk.approved,
                "reasons": generated.risk.reasons}

    @app.get("/sectors")
    def sectors() -> dict:
        from ..config.env import load_env
        from ..data.market_data import AlpacaMarketData, CsvMarketData
        env = load_env(root_path / "local.env")
        provider = CsvMarketData(root_path / "data" / "sample")
        source = "offline"
        if env.get("ALPACA_API_KEY") and env.get("ALPACA_SECRET_KEY"):
            provider = AlpacaMarketData(env["ALPACA_API_KEY"], env["ALPACA_SECRET_KEY"])
            source = "alpaca"
        try:
            ranked = rank_sectors(provider)
        except Exception:
            provider = CsvMarketData(root_path / "data" / "sample")
            source = "offline-fallback"
            ranked = rank_sectors(provider)
        return {"source": source, "sectors": [item.__dict__ for item in ranked]}
    return app
