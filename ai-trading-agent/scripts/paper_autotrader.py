from pathlib import Path
from ai_trading_agent.cli import run_scan
from ai_trading_agent.config.env import load_env
from ai_trading_agent.data.market_data import AlpacaMarketData
from ai_trading_agent.execution.paper_trader import PaperTrader
from ai_trading_agent.execution.alpaca_paper import AlpacaPaperBroker
from ai_trading_agent.journal.database import connect
from ai_trading_agent.risk.risk_engine import RiskLimits
from ai_trading_agent.signals.setup import generate_long_setup
from ai_trading_agent.execution.policy import ExecutionMode
from ai_trading_agent.portfolio.position_manager import PositionState, evaluate_exit
from ai_trading_agent.indicators.vwap import vwap_features

root = Path(__file__).parents[1]
env = load_env(root / "local.env")
db = connect(root / "trading.db")
trader = PaperTrader(db, account_value=100.0)
mode = ExecutionMode(env.get("EXECUTION_MODE", "signal_only"))
if mode == ExecutionMode.LIVE:
    raise SystemExit("Refusing to run: live execution is permanently disabled")
alpaca = None
if mode == ExecutionMode.PAPER and env.get("ALPACA_API_KEY") and env.get("ALPACA_SECRET_KEY"):
    alpaca = AlpacaPaperBroker(env["ALPACA_API_KEY"], env["ALPACA_SECRET_KEY"])
for order in trader.open_orders():
    try:
        bars = (AlpacaMarketData(env["ALPACA_API_KEY"], env["ALPACA_SECRET_KEY"])
                .get_bars(order.symbol))
        price = float(bars["close"].iloc[-1])
        ema20 = bars["close"].ewm(span=20, adjust=False).mean().iloc[-1]
        ema50 = bars["close"].ewm(span=50, adjust=False).mean().iloc[-1]
        features = vwap_features(bars)
        decision = evaluate_exit(PositionState(order.symbol, order.quantity, order.entry_price,
                                               order.stop_price, order.target_price, 50.0, "Unknown"),
                                  price, 50.0, bool(features["above"]), price > ema20 > ema50, True)
        if decision.action in {"SELL_ALL", "TAKE_PARTIAL"}:
            if alpaca:
                alpaca.submit_sell(order.symbol, decision.quantity, price)
            pnl = trader.close_quantity(order.id, price, decision.quantity)
            print(f"paper_exit={order.symbol} action={decision.action} pnl={pnl} reason={decision.reason}")
    except Exception as exc:
        print(f"monitor_skip={order.symbol} reason={type(exc).__name__}")

signals = run_scan(root)

if env.get("ALPACA_API_KEY") and env.get("ALPACA_SECRET_KEY"):
    provider = AlpacaMarketData(env["ALPACA_API_KEY"], env["ALPACA_SECRET_KEY"])
    limits = RiskLimits(paper_allocation_cap=100.0, max_open_positions=2)
    for signal in signals:
        if signal.final_score < 63 or signal.symbol in {order.symbol for order in trader.open_orders()}:
            continue
        try:
            bars = provider.get_bars(signal.symbol)
            price = float(bars["close"].iloc[-1])
            atr = float((bars["high"] - bars["low"]).rolling(14).mean().iloc[-1])
            setup = generate_long_setup(signal.symbol, price, atr, signal.final_score, "Unknown", 100.0, limits)
            if setup.risk.approved:
                local_order = trader.submit_long(setup.trade, setup.risk)
                if alpaca:
                    broker_order = alpaca.submit_buy(signal.symbol, setup.risk.shares, price)
                    print(f"alpaca_paper_order={getattr(broker_order, 'id', 'submitted')}")
                print(f"paper_entry={signal.symbol} shares={setup.risk.shares} score={signal.final_score}")
        except Exception as exc:
            print(f"skip={signal.symbol} reason={type(exc).__name__}")

print(f"open_paper_orders={len(trader.open_orders())}")
