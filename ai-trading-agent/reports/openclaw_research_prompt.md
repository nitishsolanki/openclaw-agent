# OpenClaw Full Candidate Research Handoff

Review every candidate below using the supplied trading data and existing research. Do not place orders. Return only JSON in this exact format:

{"research":[{"symbol":"MSFT","research_score":0,"conviction":"Low","catalysts":[],"risks":[],"summary":""}]}

Return exactly one research row for every symbol. Use a 0-100 research score. Do not invent facts; treat missing data as uncertainty. The technical score remains authoritative. Research is used only as a 30% score adjustment.

## AAPL
Trading candidate:
```json
{
  "symbol": "AAPL",
  "direction": "LONG",
  "score": 76.17,
  "boosted_score": 68.32,
  "research": {
    "symbol": "AAPL",
    "research_score": 50.0,
    "conviction": "Low",
    "catalysts": [],
    "risks": [
      "Insufficient company-specific research data"
    ],
    "summary": "No local research or provider-specific fundamental information was supplied; conviction is limited to the technical setup."
  },
  "sector": "Technology",
  "reasons": [
    "market: 100.0",
    "sector: 82.8",
    "vwap: 100.0",
    "trend: 100.0",
    "extension: 100.0"
  ]
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## AMZN
Trading candidate:
```json
{
  "symbol": "AMZN",
  "direction": "LONG",
  "score": 51.78,
  "boosted_score": 57.85,
  "research": {
    "symbol": "AMZN",
    "research_score": 72.0,
    "conviction": "High",
    "catalysts": [
      "AWS acceleration",
      "AI monetization",
      "Advertising growth",
      "Retail operating-margin expansion",
      "Stronger free cash flow"
    ],
    "risks": [
      "AI and cloud capex pressure",
      "AWS competition",
      "Consumer slowdown",
      "Regulatory and antitrust actions",
      "Execution risk"
    ],
    "summary": "Existing research describes a diversified growth platform led by AWS, advertising, and retail efficiency, but capex intensity, competition, regulation, and the weak technical trend warrant discipline."
  },
  "sector": "Consumer Discretionary",
  "reasons": [
    "market: 100.0",
    "vwap: 100.0",
    "extension: 100.0"
  ]
}
```
Existing research:
# AMZN — Amazon.com, Inc.

## Overview
Amazon is a global technology and commerce platform spanning online marketplace, first-party retail, logistics, advertising, subscriptions, devices/media, and Amazon Web Services (AWS). The investment case is increasingly driven by AWS, high-margin advertising, fulfillment efficiency, and AI infrastructure/software adoption.

## Sector / Industry
- Sector: Consumer Discretionary / Communication Services / Information Technology exposure
- Industry: Internet & Direct Marketing Retail; Cloud Infrastructure; Digital Advertising

## Recent Developments / News / Earnings / Analyst / SEC / Product Notes
- SEC EDGAR shows recent Amazon filings in July 2026, including 8-K current reports and prospectus/free-writing-prospectus filings tied to securities activity.
- Public news flow continues to focus on AI/cloud capex, AWS competitive positioning, retail margin expansion, advertising growth, and the balance between investment spending and free cash flow.
- Product/business themes: AWS generative-AI services, custom silicon, marketplace/Prime ecosystem, retail logistics automation, and expanding ad inventory across commerce and video.
- Source blocker: Amazon IR earnings page was blocked by Cloudflare/403 via web_fetch, so this summary relies on SEC availability plus accessible public-news context rather than direct IR release text.

## Bull Thesis
- AWS remains a scaled, high-margin cloud platform with a long runway from AI workloads, enterprise migration, and proprietary chips/services.
- Advertising is a structurally attractive, high-margin growth business embedded at the point of purchase.
- Retail margins can keep improving as regionalized fulfillment, automation, and delivery density reduce cost-to-serve.
- Prime, marketplace sellers, logistics, and media create a reinforcing ecosystem that is difficult to replicate.

## Bear Thesis
- AI and cloud infrastructure spending may pressure near-term free cash flow if returns lag expectations.
- AWS faces intense competition from Microsoft Azure, Google Cloud, and specialized AI infrastructure providers.
- Retail remains operationally complex and exposed to consumer demand, wage inflation, and regulatory scrutiny.
- Valuation can compress if revenue growth decelerates or investors question the payback on capex.

## Risks
Regulatory/antitrust actions, cloud price competition, execution risk in AI infrastructure, margin pressure from logistics and wages, cybersecurity incidents, labor disputes, and macro-driven consumer slowdown.

## Catalysts
AWS acceleration, evidence of AI monetization, advertising growth, retail operating-margin expansion, stronger free cash flow, shareholder returns, and favorable outcomes in regulatory matters.

## Long-Term Outlook
Amazon remains a high-quality compounder if AWS and advertising continue to scale while retail efficiency improves. The key long-term debate is whether AI capex becomes a durable moat and profit pool or a lower-return arms race.

## Conviction Rating
High — strong multi-engine growth platform, though capex intensity and regulatory risk keep position sizing discipline important.


## BAC
Trading candidate:
```json
{
  "symbol": "BAC",
  "direction": "LONG",
  "score": 78.57,
  "boosted_score": 70.0,
  "research": {
    "symbol": "BAC",
    "research_score": 50.0,
    "conviction": "Low",
    "catalysts": [],
    "risks": [
      "Insufficient company-specific research data"
    ],
    "summary": "No local research or provider-specific fundamental information was supplied; conviction is limited to the technical setup."
  },
  "sector": "Financials",
  "reasons": [
    "market: 100.0",
    "sector: 88.8",
    "vwap: 100.0",
    "trend: 100.0",
    "extension: 100.0"
  ]
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## BSX
Trading candidate:
```json
{
  "symbol": "BSX",
  "direction": "WATCH",
  "score": 46.91,
  "boosted_score": 46.91,
  "research": {},
  "sector": "Healthcare",
  "reasons": [
    "market: 100.0",
    "sector: 86.3",
    "extension: 100.0"
  ]
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## CCL
Trading candidate:
```json
{
  "symbol": "CCL",
  "direction": "WATCH",
  "score": 31.5,
  "boosted_score": 31.5,
  "research": {},
  "sector": "Consumer Discretionary",
  "reasons": [
    "market: 100.0",
    "extension: 100.0"
  ]
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## CMG
Trading candidate:
```json
{
  "symbol": "CMG",
  "direction": "LONG",
  "score": 72.44,
  "boosted_score": 72.44,
  "research": {},
  "sector": "Consumer Discretionary",
  "reasons": [
    "market: 100.0",
    "vwap: 100.0",
    "trend: 100.0",
    "extension: 90.5"
  ]
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## HPQ
Trading candidate:
```json
{
  "symbol": "HPQ",
  "direction": "LONG",
  "score": 80.19,
  "boosted_score": 80.19,
  "research": {},
  "sector": "Technology",
  "reasons": [
    "market: 100.0",
    "sector: 82.8",
    "relative_strength: 85.9",
    "vwap: 100.0",
    "trend: 100.0"
  ]
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## INTC
Trading candidate:
```json
{
  "symbol": "INTC",
  "direction": "LONG",
  "score": 70.04,
  "boosted_score": 70.04,
  "research": {},
  "sector": "Technology",
  "reasons": [
    "market: 100.0",
    "sector: 82.8",
    "vwap: 100.0",
    "momentum: 85.7",
    "extension: 100.0"
  ]
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## NFLX
Trading candidate:
```json
{
  "symbol": "NFLX",
  "direction": "LONG",
  "score": 71.46,
  "boosted_score": 71.46,
  "research": {},
  "sector": "Communication Services",
  "reasons": [
    "market: 100.0",
    "sector: 82.0",
    "trend: 100.0",
    "extension: 95.8"
  ]
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## NKE
Trading candidate:
```json
{
  "symbol": "NKE",
  "direction": "WATCH",
  "score": 34.21,
  "boosted_score": 34.21,
  "research": {},
  "sector": "Unknown",
  "reasons": [
    "market: 100.0",
    "extension: 100.0"
  ]
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## NVDA
Trading candidate:
```json
{
  "symbol": "NVDA",
  "direction": "LONG",
  "score": 84.32,
  "boosted_score": 75.52,
  "research": {
    "symbol": "NVDA",
    "research_score": 55.0,
    "conviction": "Medium",
    "catalysts": [
      "Next earnings and guidance",
      "AI/data-center spending",
      "Customer wins and backlog"
    ],
    "risks": [
      "Crowded AI positioning",
      "Execution risk",
      "Valuation compression",
      "No ticker-specific filing independently verified"
    ],
    "summary": "Existing research supports the AI and infrastructure thesis but remains conditional on fresh company-level verification, valuation, margins, backlog, and filings."
  },
  "sector": "Technology",
  "reasons": [
    "market: 100.0",
    "sector: 82.8",
    "relative_strength: 93.9",
    "vwap: 100.0",
    "trend: 100.0",
    "momentum: 86.9"
  ]
}
```
Existing research:
# NVDA — 2026-08-12

**View:** Watchlist coverage; conviction is conditional on valuation and company-specific verification. **Theme:** AI/infrastructure, software, fintech, mobility or space depending on issuer.

**Bull case:** Continued AI/data-center spending, easing inflation, and resilient equity demand can support growth names and infrastructure suppliers.

**Bear case:** 4.68% long yields, Brent near $89, geopolitical disruption, crowded AI positioning, execution risk and any financing/dilution could compress multiples.

**Catalysts / checks:** next earnings, guidance, customer wins, backlog, margins, cash burn and SEC filings. No ticker-specific filing was independently verified in today’s collection window.

**Rating:** Medium conviction only after fresh company-level verification; not investment advice.


## PCG
Trading candidate:
```json
{
  "symbol": "PCG",
  "direction": "WATCH",
  "score": 33.46,
  "boosted_score": 33.46,
  "research": {},
  "sector": "Utilities",
  "reasons": [
    "market: 100.0",
    "volume: 100.0",
    "extension: 100.0"
  ]
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## PFE
Trading candidate:
```json
{
  "symbol": "PFE",
  "direction": "LONG",
  "score": 79.61,
  "boosted_score": 70.73,
  "research": {
    "symbol": "PFE",
    "research_score": 50.0,
    "conviction": "Low",
    "catalysts": [],
    "risks": [
      "Insufficient company-specific research data"
    ],
    "summary": "No local research or provider-specific fundamental information was supplied; conviction is limited to the strong technical setup."
  },
  "sector": "Healthcare",
  "reasons": [
    "market: 100.0",
    "sector: 81.6",
    "vwap: 100.0",
    "trend: 100.0"
  ]
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## SMCI
Trading candidate:
```json
{
  "symbol": "SMCI",
  "direction": "LONG",
  "score": 81.77,
  "boosted_score": 81.77,
  "research": {},
  "sector": "Technology",
  "reasons": [
    "market: 100.0",
    "sector: 82.8",
    "relative_strength: 100.0",
    "vwap: 100.0",
    "trend: 100.0",
    "momentum: 84.8"
  ]
}
```
Existing research:
# SMCI — 2026-08-12

**View:** Watchlist coverage; conviction is conditional on valuation and company-specific verification. **Theme:** AI/infrastructure, software, fintech, mobility or space depending on issuer.

**Bull case:** Continued AI/data-center spending, easing inflation, and resilient equity demand can support growth names and infrastructure suppliers.

**Bear case:** 4.68% long yields, Brent near $89, geopolitical disruption, crowded AI positioning, execution risk and any financing/dilution could compress multiples.

**Catalysts / checks:** next earnings, guidance, customer wins, backlog, margins, cash burn and SEC filings. No ticker-specific filing was independently verified in today’s collection window.

**Rating:** Medium conviction only after fresh company-level verification; not investment advice.


## T
Trading candidate:
```json
{
  "symbol": "T",
  "direction": "LONG",
  "score": 78.91,
  "boosted_score": 78.91,
  "research": {},
  "sector": "Communication Services",
  "reasons": [
    "market: 100.0",
    "sector: 82.0",
    "vwap: 100.0",
    "trend: 100.0"
  ]
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## WBD
Trading candidate:
```json
{
  "symbol": "WBD",
  "direction": "LONG",
  "score": 75.26,
  "boosted_score": 75.26,
  "research": {},
  "sector": "Communication Services",
  "reasons": [
    "market: 100.0",
    "sector: 82.0",
    "vwap: 100.0",
    "trend: 100.0",
    "extension: 100.0"
  ]
}
```
Existing research:
No local stock research file exists. Use available provider data only.

## WMT
Trading candidate:
```json
{
  "symbol": "WMT",
  "direction": "WATCH",
  "score": 41.81,
  "boosted_score": 41.81,
  "research": {},
  "sector": "Consumer Discretionary",
  "reasons": [
    "market: 100.0",
    "extension: 100.0"
  ]
}
```
Existing research:
No local stock research file exists. Use available provider data only.