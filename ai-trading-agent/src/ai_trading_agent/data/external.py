from dataclasses import dataclass
from datetime import date, timedelta
import requests

def _session() -> requests.Session:
    try:
        import truststore
        truststore.inject_into_ssl()
    except ImportError:
        pass
    return requests.Session()

@dataclass(frozen=True)
class FinnhubProvider:
    api_key: str
    base_url: str = "https://finnhub.io/api/v1"

    def _get(self, endpoint: str, **params):
        params["token"] = self.api_key
        response = _session().get(self.base_url + endpoint, params=params, timeout=20)
        response.raise_for_status()
        return response.json()

    def company_news(self, symbol: str, start: date | None = None, end: date | None = None):
        end = end or date.today(); start = start or (end - timedelta(days=7))
        return self._get("/company-news", symbol=symbol.upper(), **{"from": start.isoformat(), "to": end.isoformat()})

    def earnings_calendar(self, start: date | None = None, end: date | None = None):
        end = end or date.today(); start = start or end
        return self._get("/calendar/earnings", **{"from": start.isoformat(), "to": end.isoformat()})

    def profile(self, symbol: str) -> dict:
        return self._get("/stock/profile2", symbol=symbol.upper())

@dataclass(frozen=True)
class PolygonProvider:
    api_key: str
    base_url: str = "https://api.polygon.io"

    def ticker_news(self, symbol: str, limit: int = 10):
        response = _session().get(self.base_url + "/v2/reference/news",
                                  params={"ticker": symbol.upper(), "limit": limit, "apiKey": self.api_key}, timeout=20)
        response.raise_for_status()
        return response.json()
