from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Protocol
import pandas as pd

class MarketDataProvider(Protocol):
    """Normalized, broker-independent market-data boundary."""
    def get_bars(self, symbol: str, timeframe: str = "1D", start: datetime | None = None,
                 end: datetime | None = None) -> pd.DataFrame: ...
    def get_quote(self, symbol: str) -> float: ...

@dataclass(frozen=True)
class InMemoryMarketData:
    bars: dict[str, pd.DataFrame]

    def get_bars(self, symbol: str, timeframe: str = "1D", start: datetime | None = None,
                 end: datetime | None = None) -> pd.DataFrame:
        frame = self.bars[symbol.upper()].copy()
        if start is not None:
            frame = frame[frame.index >= start]
        if end is not None:
            frame = frame[frame.index <= end]
        return frame

    def get_quote(self, symbol: str) -> float:
        return float(self.bars[symbol.upper()]["close"].iloc[-1])

@dataclass(frozen=True)
class CsvMarketData:
    directory: Path

    def get_bars(self, symbol: str, timeframe: str = "1D", start: datetime | None = None,
                 end: datetime | None = None) -> pd.DataFrame:
        frame = pd.read_csv(self.directory / f"{symbol.upper()}.csv", parse_dates=["timestamp"])
        frame = frame.set_index("timestamp").sort_index()
        return InMemoryMarketData({symbol.upper(): frame}).get_bars(symbol, timeframe, start, end)

    def get_quote(self, symbol: str) -> float:
        return float(self.get_bars(symbol)["close"].iloc[-1])

class AlpacaMarketData:
    """Read-only adapter; import and network client creation happen on first request."""
    def __init__(self, api_key: str, secret_key: str, feed: str = "iex"):
        self.api_key, self.secret_key, self.feed = api_key, secret_key, feed
        self._client = None

    def _get_client(self):
        if self._client is None:
            try:
                from alpaca.data.historical import StockHistoricalDataClient
            except ImportError as exc:
                raise RuntimeError("Install alpaca-py to use AlpacaMarketData") from exc
            self._client = StockHistoricalDataClient(self.api_key, self.secret_key)
        return self._client

    def get_bars(self, symbol: str, timeframe: str = "1D", start: datetime | None = None,
                 end: datetime | None = None) -> pd.DataFrame:
        try:
            import truststore
            truststore.inject_into_ssl()
        except ImportError:
            pass
        from alpaca.data.requests import StockBarsRequest
        from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
        unit = TimeFrameUnit.Day if timeframe.upper().endswith("D") else TimeFrameUnit.Minute
        amount = int(timeframe[:-1]) if timeframe[:-1].isdigit() else 1
        if start is None:
            from datetime import timedelta, timezone
            end = end or datetime.now(timezone.utc)
            start = end - timedelta(days=365)
        request = StockBarsRequest(symbol_or_symbols=symbol.upper(), timeframe=TimeFrame(amount, unit),
                                   start=start, end=end, feed=self.feed)
        result = self._get_client().get_stock_bars(request).df
        if isinstance(result.index, pd.MultiIndex):
            result = result.xs(symbol.upper(), level="symbol")
        return result.rename(columns={"open": "open", "high": "high", "low": "low", "close": "close", "volume": "volume"})

    def get_quote(self, symbol: str) -> float:
        bars = self.get_bars(symbol, "1D")
        return float(bars["close"].iloc[-1])

    def get_spread(self, symbol: str) -> float | None:
        try:
            import truststore
            truststore.inject_into_ssl()
            from alpaca.data.requests import StockLatestQuoteRequest
            quote = self._get_client().get_stock_latest_quote(StockLatestQuoteRequest(symbol_or_symbols=symbol.upper(), feed=self.feed))[symbol.upper()]
            midpoint = (float(quote.bid_price) + float(quote.ask_price)) / 2
            return round((float(quote.ask_price) - float(quote.bid_price)) / midpoint * 100, 4) if midpoint else None
        except Exception:
            return None

    def get_assets(self):
        try:
            import truststore
            truststore.inject_into_ssl()
        except ImportError:
            pass
        try:
            from alpaca.trading.client import TradingClient
            from alpaca.trading.requests import GetAssetsRequest
            from alpaca.trading.enums import AssetClass, AssetStatus
        except ImportError as exc:
            raise RuntimeError("Install alpaca-py to load assets") from exc
        client = TradingClient(self.api_key, self.secret_key, paper=True)
        return client.get_all_assets(GetAssetsRequest(asset_class=AssetClass.US_EQUITY, status=AssetStatus.ACTIVE))
