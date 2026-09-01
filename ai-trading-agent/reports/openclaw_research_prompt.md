# OpenClaw Top-5 Research Handoff

Review each candidate using the supplied trading data and existing research. Do not place orders. Return only JSON in this format:

```json
{"research":[{"symbol":"MSFT","research_score":0,"conviction":"Low","catalysts":[],"risks":[],"summary":""}]}
```

Use a 0-100 research score. Do not invent facts. Treat missing data as uncertainty. Keep Python's technical score authoritative; this research score is a 30% adjustment.

## WBD
Trading candidate:
```json
{
  "symbol": "WBD",
  "score": 75.71,
  "direction": "LONG",
  "sector": "Communication Services",
  "components": {
    "market": 100.0,
    "sector": 54.49,
    "relative_strength": 64.33852218439041,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 52.119360711926646,
    "momentum": 48.28175640355463,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 96.97189778858117
  }
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## NFLX
Trading candidate:
```json
{
  "symbol": "NFLX",
  "score": 61.09,
  "direction": "LONG",
  "sector": "Communication Services",
  "components": {
    "market": 100.0,
    "sector": 54.49,
    "relative_strength": 77.73836445221534,
    "vwap": 0.0,
    "trend": 100.0,
    "volume": 29.43957451235533,
    "momentum": 55.24934383202096,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 82.5444551219421
  }
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## BAC
Trading candidate:
```json
{
  "symbol": "BAC",
  "score": 58.53,
  "direction": "LONG",
  "sector": "Financials",
  "components": {
    "market": 100.0,
    "sector": 88.06,
    "relative_strength": 39.379104394258555,
    "vwap": 100.0,
    "trend": 0.0,
    "volume": 44.03392630344886,
    "momentum": 49.4653084142135,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 100.0
  }
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## WMT
Trading candidate:
```json
{
  "symbol": "WMT",
  "score": 37.46,
  "direction": "WATCH",
  "sector": "Consumer Discretionary",
  "components": {
    "market": 100.0,
    "sector": 55.78,
    "relative_strength": 23.547796588114167,
    "vwap": 0.0,
    "trend": 0.0,
    "volume": 48.11284464498413,
    "momentum": 48.65377393916634,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 100.0
  }
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## PCG
Trading candidate:
```json
{
  "symbol": "PCG",
  "score": 33.67,
  "direction": "WATCH",
  "sector": "Utilities",
  "components": {
    "market": 100.0,
    "sector": 57.67,
    "relative_strength": 0.0,
    "vwap": 0.0,
    "trend": 0.0,
    "volume": 100.0,
    "momentum": 4.0,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 100.0
  }
}
```
Existing research:
No local stock research file exists. Use available provider data only.