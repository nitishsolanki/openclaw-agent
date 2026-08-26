# OpenClaw Top-5 Research Handoff

Review each candidate using the supplied trading data and existing research. Do not place orders. Return only JSON in this format:

```json
{"research":[{"symbol":"MSFT","research_score":0,"conviction":"Low","catalysts":[],"risks":[],"summary":""}]}
```

Use a 0-100 research score. Do not invent facts. Treat missing data as uncertainty. Keep Python's technical score authoritative; this research score is a 30% adjustment.

## PFE
Trading candidate:
```json
{
  "symbol": "PFE",
  "score": 76.0,
  "direction": "LONG",
  "sector": "Healthcare",
  "components": {
    "market": 100.0,
    "sector": 81.52,
    "relative_strength": 71.9225464232531,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 22.678817160278182,
    "momentum": 60.77862325252172,
    "volatility": 50.0,
    "options": 50.0
  }
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## WBD
Trading candidate:
```json
{
  "symbol": "WBD",
  "score": 75.8,
  "direction": "LONG",
  "sector": "Communication Services",
  "components": {
    "market": 100.0,
    "sector": 83.91,
    "relative_strength": 77.11636223585595,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 8.561765680900118,
    "momentum": 54.76858345021034,
    "volatility": 50.0,
    "options": 50.0
  }
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## VZ
Trading candidate:
```json
{
  "symbol": "VZ",
  "score": 75.62,
  "direction": "LONG",
  "sector": "Communication Services",
  "components": {
    "market": 100.0,
    "sector": 83.91,
    "relative_strength": 67.90996337764783,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 20.096817703587256,
    "momentum": 64.95461912479743,
    "volatility": 50.0,
    "options": 50.0
  }
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## CMG
Trading candidate:
```json
{
  "symbol": "CMG",
  "score": 75.43,
  "direction": "LONG",
  "sector": "Consumer Discretionary",
  "components": {
    "market": 100.0,
    "sector": 52.0,
    "relative_strength": 100.0,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 7.384949986276271,
    "momentum": 85.75591459896145,
    "volatility": 50.0,
    "options": 50.0
  }
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## SMCI
Trading candidate:
```json
{
  "symbol": "SMCI",
  "score": 75.02,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 100.0,
    "sector": 51.27,
    "relative_strength": 100.0,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 8.938738991708908,
    "momentum": 77.44122471295793,
    "volatility": 50.0,
    "options": 50.0
  }
}
```
Existing research:
# SMCI — 2026-08-12

**View:** Watchlist coverage; conviction is conditional on valuation and company-specific verification. **Theme:** AI/infrastructure, software, fintech, mobility or space depending on issuer.

**Bull case:** Continued AI/data-center spending, easing inflation, and resilient equity demand can support growth names and infrastructure suppliers.

**Bear case:** 4.68% long yields, Brent near $89, geopolitical disruption, crowded AI positioning, execution risk and any financing/dilution could compress multiples.

**Catalysts / checks:** next earnings, guidance, customer wins, backlog, margins, cash burn and SEC filings. No ticker-specific filing was independently verified in today’s collection window.

**Rating:** Medium conviction only after fresh company-level verification; not investment advice.
