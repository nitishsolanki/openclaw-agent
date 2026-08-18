from pathlib import Path
from ai_trading_agent.config.env import load_env
from ai_trading_agent.execution.alpaca_paper import AlpacaPaperBroker
from ai_trading_agent.execution.policy import ExecutionMode
from ai_trading_agent.telegram.router import route_command

def test_local_env_loader_does_not_require_environment_mutation(tmp_path):
    path = tmp_path / "local.env"
    path.write_text("ALPACA_API_KEY=secret\nTELEGRAM_BOT_TOKEN=token\n")
    assert load_env(path)["ALPACA_API_KEY"] == "secret"

def test_alpaca_adapter_rejects_non_paper_mode():
    try:
        AlpacaPaperBroker("x", "y", ExecutionMode.LIVE)
    except ValueError:
        assert True
    else:
        assert False

def test_telegram_routes_are_signal_only():
    assert route_command("/scan") == "GET /scan"
    assert "Unsupported" in route_command("/trade ABC")

