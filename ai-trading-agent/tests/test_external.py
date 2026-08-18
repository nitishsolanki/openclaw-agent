from ai_trading_agent.data.external import FinnhubProvider, PolygonProvider

def test_provider_endpoints_are_configured():
    assert FinnhubProvider("x").base_url.startswith("https://")
    assert PolygonProvider("x").base_url.startswith("https://")

