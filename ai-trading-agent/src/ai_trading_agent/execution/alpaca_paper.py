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
                import truststore
                truststore.inject_into_ssl()
            except ImportError:
                pass
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

    def option_snapshots(self, underlying: str, feed: str = "indicative"):
        try:
            import truststore
            truststore.inject_into_ssl()
        except ImportError:
            pass
        try:
            from alpaca.data.historical.option import OptionHistoricalDataClient
            from alpaca.data.requests import OptionChainRequest
        except ImportError as exc:
            raise RuntimeError("Install alpaca-py for options data") from exc
        client = OptionHistoricalDataClient(self.api_key, self.secret_key)
        return client.get_option_chain(OptionChainRequest(underlying_symbol=underlying.upper(), feed=feed))

    def submit_buy(self, symbol: str, quantity: int, limit_price: float):
        if quantity < 1 or limit_price <= 0:
            raise ValueError("invalid paper order parameters")
        try:
            from alpaca.trading.enums import OrderSide, TimeInForce, OrderType
            from alpaca.trading.requests import LimitOrderRequest
        except ImportError as exc:
            raise RuntimeError("Install alpaca-py to submit paper orders") from exc
        request = LimitOrderRequest(symbol=symbol.upper(), qty=quantity, side=OrderSide.BUY,
                                    type=OrderType.LIMIT, time_in_force=TimeInForce.DAY,
                                    limit_price=limit_price)
        return self._get_client().submit_order(request)

    def submit_sell(self, symbol: str, quantity: int, limit_price: float):
        if quantity < 1 or limit_price <= 0:
            raise ValueError("invalid paper sell parameters")
        try:
            from alpaca.trading.enums import OrderSide, TimeInForce, OrderType
            from alpaca.trading.requests import LimitOrderRequest
        except ImportError as exc:
            raise RuntimeError("Install alpaca-py to submit paper orders") from exc
        request = LimitOrderRequest(symbol=symbol.upper(), qty=quantity, side=OrderSide.SELL,
                                    type=OrderType.LIMIT, time_in_force=TimeInForce.DAY,
                                    limit_price=limit_price)
        return self._get_client().submit_order(request)

    def cancel_all(self):
        return self._get_client().cancel_orders()

    def cancel(self, order_id: str):
        return self._get_client().cancel_order_by_id(order_id)
