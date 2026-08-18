from dataclasses import dataclass
from .policy import ExecutionMode

@dataclass
class AlpacaPaperBroker:
    api_key: str
    secret_key: str
    mode: ExecutionMode = ExecutionMode.PAPER

    def __post_init__(self):
        if self.mode != ExecutionMode.PAPER:
            raise ValueError("AlpacaPaperBroker only permits PAPER mode")
        self._client = None

    def _get_client(self):
        if self._client is None:
            try:
                from alpaca.trading.client import TradingClient
            except ImportError as exc:
                raise RuntimeError("Install alpaca-py to use Alpaca paper trading") from exc
            self._client = TradingClient(self.api_key, self.secret_key, paper=True)
        return self._client

    def account(self):
        return self._get_client().get_account()

    def positions(self):
        return self._get_client().get_all_positions()

