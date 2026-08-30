# OpenClaw Top-5 Research Handoff

Review each candidate using the supplied trading data and existing research. Do not place orders. Return only JSON in this format:

```json
{"research":[{"symbol":"MSFT","research_score":0,"conviction":"Low","catalysts":[],"risks":[],"summary":""}]}
```

Use a 0-100 research score. Do not invent facts. Treat missing data as uncertainty. Keep Python's technical score authoritative; this research score is a 30% adjustment.

## SMCI
Trading candidate:
```json
{
  "symbol": "SMCI",
  "score": 82.9,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 100.0,
    "sector": 86.5,
    "relative_strength": 100.0,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 26.85061947974159,
    "momentum": 58.38839645447219,
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


## HPQ
Trading candidate:
```json
{
  "symbol": "HPQ",
  "score": 82.56,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 100.0,
    "sector": 86.5,
    "relative_strength": 83.1304793349444,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 51.007553323922735,
    "momentum": 70.70346684617977,
    "volatility": 50.0,
    "options": 50.0
  }
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## T
Trading candidate:
```json
{
  "symbol": "T",
  "score": 80.55,
  "direction": "LONG",
  "sector": "Communication Services",
  "components": {
    "market": 100.0,
    "sector": 89.1,
    "relative_strength": 83.11463038793799,
    "vwap": 97.29177704314735,
    "trend": 100.0,
    "volume": 30.13706412019465,
    "momentum": 69.90478071908336,
    "volatility": 50.0,
    "options": 50.0
  }
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## AAPL
Trading candidate:
```json
{
  "symbol": "AAPL",
  "score": 77.95,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 100.0,
    "sector": 86.5,
    "relative_strength": 65.55248221441619,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 39.18987108465256,
    "momentum": 72.33462670158765,
    "volatility": 50.0,
    "options": 50.0
  }
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## PFE
Trading candidate:
```json
{
  "symbol": "PFE",
  "score": 76.3,
  "direction": "LONG",
  "sector": "Healthcare",
  "components": {
    "market": 100.0,
    "sector": 83.5,
    "relative_strength": 67.21020014460612,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 36.370305605819695,
    "momentum": 50.360947799750555,
    "volatility": 50.0,
    "options": 50.0
  }
}
```
Existing research:
No local stock research file exists. Use available provider data only.