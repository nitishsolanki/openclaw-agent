from ai_trading_agent.data.external import FinnhubProvider, PolygonProvider

def test_provider_endpoints_are_configured():
    assert FinnhubProvider("x").base_url.startswith("https://")
    assert PolygonProvider("x").base_url.startswith("https://")

def test_finnhub_research_endpoints_are_available():
    provider = FinnhubProvider("x")
    assert provider.fundamentals.__name__ == "fundamentals"
    assert provider.filings.__name__ == "filings"

