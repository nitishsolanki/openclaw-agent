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

    def get_premarket_snapshot(self, symbol: str) -> dict[str, float]:
        """Return today's extended-hours movement relative to the prior daily close."""
        from datetime import datetime, timedelta, timezone
        from zoneinfo import ZoneInfo
        central = datetime.now(ZoneInfo("America/Chicago"))
        session_start = central.replace(hour=4, minute=0, second=0, microsecond=0).astimezone(timezone.utc)
        market_open = central.replace(hour=8, minute=30, second=0, microsecond=0).astimezone(timezone.utc)
        end = min(datetime.now(timezone.utc), market_open)
        if end < session_start:
            return {"gap_pct": 0.0, "volume_ratio": 0.0, "score": 50.0}
        bars = self.get_bars(symbol, "1Min", start=session_start, end=end)
        if bars.empty:
            return {"gap_pct": 0.0, "volume_ratio": 0.0, "score": 50.0}
        daily = self.get_bars(symbol, "1D", start=end - timedelta(days=10), end=end)
        previous_close = float(daily["close"].iloc[-2]) if len(daily) > 1 else float(bars["close"].iloc[0])
        latest = float(bars["close"].iloc[-1])
        gap_pct = (latest / previous_close - 1) * 100 if previous_close else 0.0
        volume_ratio = float(bars["volume"].sum()) / max(float(daily["volume"].tail(5).mean()) / 390 * max(len(bars), 1), 1)
        score = max(0.0, min(100.0, 50.0 + gap_pct * 12.0))
        return {"gap_pct": round(gap_pct, 3), "volume_ratio": round(volume_ratio, 2), "score": round(score, 2)}

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
