# OpenClaw Candidate Research Handoff

Review each candidate using the supplied trading data and evidence packet. Do not place orders. Return only JSON in this format:

```json
{"research":[{"symbol":"MSFT","research_score":0,"conviction":"Low","catalysts":[],"risks":[],"summary":""}]}
```

Use a 0-100 research score. Do not invent facts or infer fundamentals from technical data. Treat missing data as uncertainty, name the missing source in risks, and use only dated/source-labelled news, earnings, filings, or fundamentals. Keep Python's technical score authoritative; this research score is a 30% adjustment.

## NVDA
Trading candidate:
```json
{
  "symbol": "NVDA",
  "score": 86.27,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 100.0,
    "sector": 55.47,
    "relative_strength": 93.01440576434432,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 63.81216217295071,
    "momentum": 87.96396052819752,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 88.78612129827623
  }
}
```
Evidence packet (source-labelled; missing sources must remain uncertain):
```json
{
  "local_research": [
    "[NVDA.md]\n# NVDA \u2014 2026-08-12\n\n**View:** Watchlist coverage; conviction is conditional on valuation and company-specific verification. **Theme:** AI/infrastructure, software, fintech, mobility or space depending on issuer.\n\n**Bull case:** Continued AI/data-center spending, easing inflation, and resilient equity demand can support growth names and infrastructure suppliers.\n\n**Bear case:** 4.68% long yields, Brent near $89, geopolitical disruption, crowded AI positioning, execution risk and any financing/dilution could compress multiples.\n\n**Catalysts / checks:** next earnings, guidance, customer wins, backlog, margins, cash burn and SEC filings. No ticker-specific filing was independently verified in today\u2019s collection window.\n\n**Rating:** Medium conviction only after fresh company-level verification; not investment advice.\n"
  ],
  "local_news": [
    "[2026-08-14.md]\n# Market News \u2014 2026-08-14\n\n- U.S. index futures were mixed before the open: S&P 500 futures +0.1%, Nasdaq futures +0.1%, Dow futures -0.1% (AP, 05:58 UTC).\n- Thursday closed at records after softer July PPI and falling oil supported growth shares.\n- Oil rebounded into Friday after reports that two UAE tankers were attacked while crossing the Strait of Hormuz; geopolitical energy risk remains active.\n- Applied Materials' record quarter and stronger outlook remain a positive read-through for AI infrastructure, semiconductors, servers, and storage, although the stock's weak reaction highlights elevated expectations.\n- Watchlist market snapshots around 11:45 UTC: NVDA $225.30 (+0.5%), ORCL $156.22 (+1.9%), SMCI $39.16 (+4.0%), WDC $487.29 (+7.3%), VST $146.40 (-0.2%). Quotes are time-stamped snapshots, not end-of-day closes.\n\nSources: https://apnews.com/article/5d9870d6c5ae735f9b74bf4ceefaa3ec ; https://ir.appliedmaterials.com/\n",
    "[2026-08-13.md]\n# Market News \u2014 2026-08-13\n\n## Executive read\n\nU.S. stocks closed at records as benign July PPI and lower oil supported growth shares. AI and semiconductor leadership remained dominant, while Applied Materials\u2019 post-close results reinforced the equipment and AI-capex thesis. The tape is constructive but expectations and geopolitical risks are elevated.\n\n## Market-moving developments\n\n1. The S&P 500 rose 0.7% to 7,798.99 and the Nasdaq rose 0.8% to 26,803.03; both set record closes. The Dow gained 0.1% and Russell 2000 gained 0.2%. [AP](https://apnews.com/article/892c5409d8ed26bfd5965eb2a89d9005)\n2. July PPI was flat month over month and core PPI rose 0.2%, slightly below forecasts, supporting hopes that rate pressure can ease. [Axios](https://www.axios.com/2026/08/13/inflation-july-ppi)\n3. Brent fell 2.1%, helping duration-sensitive equities, but the Iran/Hormuz disruption remains a material inflation and supply-chain risk.\n4. Applied Materials reported record Q3 revenue of about $9.12B and adjusted EPS of about $3.50, above consensus, with above-estimate forward guidance reported in market coverage. The read-through is positive for semiconductor equipment and AI infrastructure, though after-hours weakness highlights valuation risk.\n\n## Watchlist implications\n\n- Favor profitable AI infrastructure, cloud, storage, and power names.\n- Treat speculative space, EV, leveraged crypto, and fintech as satellite exposures.\n- No additions or removals; raise priority on NVDA, AMD, AVGO, SMCI, WDC, and ORCL.\n"
  ],
  "local_sec_filings": [
    "[2026-08-31.md]\n# SEC Filing Review \u2014 2026-08-31\n\n- AMD: SEC EDGAR filing index shows an August 13, 2026 filing with associated XBRL exhibits; this is the only fresh ticker-specific filing independently verified in the current collection window.\n- NVDA: an August 26, 2026 8-K is listed by a secondary filing index; verify the primary EDGAR document before relying on details.\n- For the remaining watchlist names, no new material filing was independently verified in this run. Treat filing status as unavailable rather than clean.\n- Source: https://www.sec.gov/Archives/edgar/data/2488/000119312526354029/0001193125-26-354029-index.htm\n",
    "[2026-08-13.md]\n# SEC Filings \u2014 2026-08-13\n\nNo fresh ticker-specific SEC filing was independently verified for the watchlist in this collection window. This is a data-quality limitation, not evidence that no filing exists. Priority checks remain SMCI, NVDA, ORCL, AMD, AVGO, and financing/dilution disclosures for MSTR, ASTS, RKLB, RIVN, UPST, and POET.\n"
  ],
  "finnhub_news": [
    {
      "category": "company",
      "datetime": 1788799140,
      "headline": "1 Stat That Makes Costco Hard to Ignore this September",
      "id": 141765108,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NVDA",
      "source": "Yahoo",
      "summary": "The warehouse chain's latest sales update gave investors another reason to watch September closely.",
      "url": "https://finnhub.io/api/news?id=cb18f714fda83bd60a692cbfddf9735cdf2cc14fe004910f1889b74157a4f418"
    },
    {
      "category": "company",
      "datetime": 1788799020,
      "headline": "Up 26% in 2026, Is Coca-Cola a Buy Near an All-Time High?",
      "id": 141765109,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NVDA",
      "source": "Yahoo",
      "summary": "The beverage bellwether is beating the market this year. Is the fizz about to go flat?",
      "url": "https://finnhub.io/api/news?id=cc58735c2e268622cdb2b60372b4b56194f0e75eaea492afd4473dc018f3cd58"
    },
    {
      "category": "company",
      "datetime": 1788798300,
      "headline": "What If the Clarity Act Doesn't Pass This Year? Here Are 3 Ways to Bulletproof Your Crypto Portfolio.",
      "id": 141765112,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NVDA",
      "source": "Yahoo",
      "summary": "Plan for the contingency now so that you won't be chasing the market later.",
      "url": "https://finnhub.io/api/news?id=04cf90d6658bb59287c971a7ecbdea09a06259ea4b3739333c02f24ba9cf0d35"
    },
    {
      "category": "company",
      "datetime": 1788798001,
      "headline": "What's Wrong With PepsiCo Stock?",
      "id": 141765110,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NVDA",
      "source": "Yahoo",
      "summary": "The stock has drastically underperformed the market over the past five years.",
      "url": "https://finnhub.io/api/news?id=f5605ef5323b02d2ef76dfd77a0ea86515c9486606a9079d3b9e296b5237daec"
    },
    {
      "category": "company",
      "datetime": 1788797100,
      "headline": "Caterpillar's Power Generation Backlog Just Hit $72 Billion. The Construction Cycle Barely Matters Anymore.",
      "id": 141765113,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NVDA",
      "source": "Yahoo",
      "summary": "The construction industry giant has become a compelling AI-driven winning stock.",
      "url": "https://finnhub.io/api/news?id=4a729d7e3a6e8ca0e894aec5b980f5438d95f79edfd86290591b737842e5ffd0"
    }
  ],
  "polygon_news": [],
  "earnings": [
    {
      "symbol": "NVDA",
      "date": "2026-11-17",
      "hour": "amc",
      "quarter": 3,
      "year": 2027,
      "epsEstimate": 2.4659,
      "epsActual": null,
      "revenueEstimate": 108129157692,
      "revenueActual": null
    }
  ],
  "fundamentals": {
    "10DayAverageTradingVolume": 159.30202,
    "13WeekPriceReturnDaily": 5.3508,
    "26WeekPriceReturnDaily": 27.9422,
    "3MonthADReturnStd": 42.17823,
    "3MonthAverageTradingVolume": 146.35042,
    "52WeekHigh": 236.54,
    "52WeekHighDate": "2026-05-14",
    "52WeekLow": 164.07,
    "52WeekLowDate": "2025-09-05",
    "52WeekPriceReturnDaily": 37.9236,
    "5DayPriceReturnDaily": 4.3392,
    "assetTurnoverAnnual": 1.0442,
    "assetTurnoverTTM": 1.2788,
    "beta": 2.2200592,
    "bookValuePerShareAnnual": 6.4719,
    "bookValuePerShareQuarterly": 9.4829,
    "bookValueShareGrowth5Y": 56.87,
    "capexCagr5Y": 39.89,
    "cashFlowPerShareAnnual": 3.9778,
    "cashFlowPerShareQuarterly": 5.2597,
    "cashFlowPerShareTTM": 8.20683,
    "cashPerSharePerShareAnnual": 2.5739,
    "cashPerSharePerShareQuarterly": 4.1152,
    "currentDividendYieldTTM": 0.1221,
    "currentEv/freeCashFlowAnnual": 57.5386,
    "currentEv/freeCashFlowTTM": 43.7979,
    "currentRatioAnnual": 3.9053,
    "currentRatioQuarterly": 4.5889,
    "dividendGrowthRate5Y": 20.05,
    "dividendIndicatedAnnual": 1,
    "dividendPerShareAnnual": 0.0399,
    "dividendPerShareTTM": 0.2795,
    "dividendYieldIndicatedAnnual": 0.03349,
    "ebitdPerShareAnnual": 5.4349,
    "ebitdPerShareTTM": 8.2446,
    "ebitdaCagr5Y": 88.29,
    "ebitdaInterimCagr5Y": 88.37,
    "enterpriseValue": 5562599,
    "epsAnnual": 4.8979,
    "epsBasicExclExtraItemsAnnual": 4.8979,
    "epsBasicExclExtraItemsTTM": 7.9108,
    "epsExclExtraItemsAnnual": 4.8979,
    "epsExclExtraItemsTTM": 7.9108,
    "epsGrowth3Y": 204.08,
    "epsGrowth5Y": 95.27,
    "epsGrowthQuarterlyYoy": 128.21,
    "epsGrowthTTMYoy": 125.15,
    "epsInclExtraItemsAnnual": 4.8979,
    "epsInclExtraItemsTTM": 7.9108,
    "epsNormalizedAnnual": 4.8979,
    "epsTTM": 7.9108,
    "evEbitdaTTM": 27.6547,
    "evRevenueTTM": 18.3603,
    "focfCagr5Y": 83.13,
    "forwardPE": 18.10034,
    "forwardPEG": 0.34983,
    "grossMargin5Y": 68.54,
    "grossMarginAnnual": 73.15,
    "grossMarginTTM": 74.67,
    "inventoryTurnoverAnnual": 3.6829,
    "inventoryTurnoverTTM": 3.2975,
    "longTermDebt/equityAnnual": 0.0475,
    "longTermDebt/equityQuarterly": 0.1413,
    "marketCapitalization": 5551676,
    "monthToDatePriceReturnDaily": 4.3392,
    "netIncomeEmployeeAnnual": 2.8587,
    "netIncomeEmployeeTTM": 4.5924,
    "netInterestCoverageAnnual": 29.0975,
    "netInterestCoverageTTM": 75.6607,
    "netMarginGrowth5Y": 16.44,
    "netProfitMargin5Y": 42.54,
    "netProfitMarginAnnual": 55.6,
    "netProfitMarginTTM": 63.66,
    "operatingMargin5Y": 45.98,
    "operatingMarginAnnual": 60.38,
    "operatingMarginTTM": 65.17,
    "payoutRatioAnnual": 0.81,
    "payoutRatioTTM": 3.51,
    "pb": 24.2448,
    "pbAnnual": 28.8075,
    "pbQuarterly": 20.768,
    "pcfShareAnnual": 54.0477,
    "pcfShareTTM": 41.3194,
    "peAnnual": 46.2382,
    "peBasicExclExtraTTM": 28.7832,
    "peExclExtraAnnual": 274.2091,
    "peExclExtraTTM": 28.7832,
    "peInclExtraTTM": 28.7832,
    "peNormalizedAnnual": 46.2382,
    "peTTM": 28.7832,
    "pegTTM": 0.57728,
    "pfcfShareAnnual": 57.4256,
    "pfcfShareTTM": 43.7119,
    "pretaxMargin5Y": 47.57,
    "pretaxMarginAnnual": 65.5,
    "pretaxMarginTTM": 75.83,
    "priceRelativeToS&P50013Week": 3.6205,
    "priceRelativeToS&P50026Week": 14.7339,
    "priceRelativeToS&P5004Week": 6.2557,
    "priceRelativeToS&P50052Week": 18.9276,
    "priceRelativeToS&P500Ytd": 10.5731,
    "psAnnual": 25.7096,
    "psTTM": 18.3242,
    "ptbvAnnual": 29.426,
    "ptbvQuarterly": 21.0435,
    "quickRatioAnnual": 3.1409,
    "quickRatioQuarterly": 3.7757,
    "receivablesTurnoverAnnual": 7.0188,
    "receivablesTurnoverTTM": 6.6684,
    "revenueEmployeeAnnual": 5.1414,
    "revenueEmployeeTTM": 7.2135,
    "revenueGrowth3Y": 100.05,
    "revenueGrowth5Y": 66.9,
    "revenueGrowthQuarterlyYoy": 105.85,
    "revenueGrowthTTMYoy": 83.38,
    "revenuePerShareAnnual": 8.8088,
    "revenuePerShareTTM": 12.4756,
    "revenueShareGrowth5Y": 67.72,
    "roa5Y": 40.26,
    "roaRfy": 58.06,
    "roaTTM": 81.41000000000001,
    "roe5Y": 58.77,
    "roeRfy": 76.33,
    "roeTTM": 110.11,
    "roi5Y": 50.22,
    "roiAnnual": 72.43,
    "roiTTM": 101.59,
    "tangibleBookValuePerShareAnnual": 6.3359,
    "tangibleBookValuePerShareQuarterly": 9.3588,
    "tbvCagr5Y": 61.18,
    "totalDebt/totalEquityAnnual": 0.0538,
    "totalDebt/totalEquityQuarterly": 0.1457,
    "yearToDatePriceReturnDaily": 23.5174
  },
  "source_status": {
    "local_research": true,
    "local_news": true,
    "local_sec_filings": true,
    "finnhub_news": true,
    "polygon_news": false,
    "earnings": true,
    "fundamentals": true
  }
}
```

## PFE
Trading candidate:
```json
{
  "symbol": "PFE",
  "score": 84.84,
  "direction": "LONG",
  "sector": "Healthcare",
  "components": {
    "market": 100.0,
    "sector": 86.35,
    "relative_strength": 95.84824959756426,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 44.22160887745767,
    "momentum": 69.95762711864404,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 62.332071974969374
  }
}
```
Evidence packet (source-labelled; missing sources must remain uncertain):
```json
{
  "local_research": [],
  "local_news": [],
  "local_sec_filings": [],
  "finnhub_news": [
    {
      "category": "company",
      "datetime": 1788784860,
      "headline": "AstraZeneca Secures FDA Nod for New Breast Cancer Therapy Etcamah",
      "id": 141762863,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "AZN's Etcamah wins accelerated FDA approval for certain advanced breast cancer patients, backed by a 56% risk reduction in progression or death.",
      "url": "https://finnhub.io/api/news?id=41ffd461059d01b83af5f6b005e0cd9ed487a6bbd0d0ecd81a797819bfe6cdb1"
    },
    {
      "category": "company",
      "datetime": 1788778920,
      "headline": "Vaccines Global Market Intelligence Report 2026-2035 Featuring Bio Farma, Emergent BioSolutions, GC Pharma, GlaxoSmithKline, Janssen, Merck, Novavax, Moderna, Pfizer, Sanofi Pasteur, and Valneva",
      "id": 141760935,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "Dublin, Sept. 07, 2026 (GLOBE NEWSWIRE) -- The \"Vaccines Market Distribution by Type of Vaccine API, Targeted Patient Population, Type of Vaccines, Route of Administration, and Key Geographical Region - Trends and Forecasts Till 2035\" has been added to ResearchAndMarkets.com's offering. The global vaccines market is projected to increase from approximately USD 48 billion to USD 94 billion by 2030, representing a compound annual growth rate of about 11.9% during the forecast period. Market expans",
      "url": "https://finnhub.io/api/news?id=9f51313c5b3c77384d06c621b598127ced700b1ca8ebed5cb5ba133ec949c83a"
    },
    {
      "category": "company",
      "datetime": 1788547801,
      "headline": "AbbVie vs. Pfizer: Which Healthcare Stock Is a Better Buy in 2026?",
      "id": 141455037,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "AbbVie's immunology pivot is offsetting Humira's decline, while Pfizer trades at half the valuation despite patent risks ahead.",
      "url": "https://finnhub.io/api/news?id=882e78db4092ee8e4a4f8c9153c570608198427b13f54f3413147816ac706bb2"
    },
    {
      "category": "company",
      "datetime": 1788541047,
      "headline": "Was JNJ Stock Rally Actually Its Own?",
      "id": 141444058,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "Johnson & Johnson (JNJ) stock returned 59.9% over the past year, against 21.1% for the S&P 500. The company has a clean story for it. The biosimilar hit it had been bracing for arrived and was absorbed, and its talc litigation now has a proposed ending. Both are real. The first does not explain a move that size, and the second is not finished.",
      "url": "https://finnhub.io/api/news?id=905919b186b2cb70f624aa1750860bd8a239d54c5d4daa0db9581cc8254fae21"
    },
    {
      "category": "company",
      "datetime": 1788532931,
      "headline": "Pfizer\u2019s Stock Has Been Crushed\u2014Is Its 6% Dividend Finally Worth Buying?",
      "id": 141431642,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "Pfizer shareholders are collecting a 6% yield while the stock bleeds value, and the CEO just made a bold promise about keeping that payout alive through what could be the company's toughest stretch in years.",
      "url": "https://finnhub.io/api/news?id=30c88d515f9a37e92b3066e6f44c71beb646245c32bfe22b3b84e95acef516c2"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 32.73994,
    "13WeekPriceReturnDaily": 10.7435,
    "26WeekPriceReturnDaily": 7.0354,
    "3MonthADReturnStd": 22.492231,
    "3MonthAverageTradingVolume": 40.13358,
    "52WeekHigh": 29.21,
    "52WeekHighDate": "2026-09-03",
    "52WeekLow": 23.58,
    "52WeekLowDate": "2025-09-25",
    "52WeekPriceReturnDaily": 14.3489,
    "5DayPriceReturnDaily": -0.0351,
    "assetTurnoverAnnual": 0.3006,
    "assetTurnoverTTM": 0.3086,
    "beta": 0.27623326,
    "bookValuePerShareAnnual": 15.2086,
    "bookValuePerShareQuarterly": 14.9482,
    "bookValueShareGrowth5Y": 6.01,
    "capexCagr5Y": -1.19,
    "cashFlowPerShareAnnual": 1.5962,
    "cashFlowPerShareQuarterly": 1.9277,
    "cashFlowPerShareTTM": 2.91656,
    "cashPerSharePerShareAnnual": 2.3911,
    "cashPerSharePerShareQuarterly": 2.0528,
    "currentDividendYieldTTM": 6.0343,
    "currentEv/freeCashFlowAnnual": 24.7217,
    "currentEv/freeCashFlowTTM": 20.4236,
    "currentRatioAnnual": 1.1599,
    "currentRatioQuarterly": 1.2669,
    "dividendGrowthRate5Y": 2.51,
    "dividendIndicatedAnnual": 1.72,
    "dividendPerShareAnnual": 1.7213,
    "dividendPerShareTTM": 1.7191,
    "dividendYieldIndicatedAnnual": 5.37705,
    "ebitdPerShareAnnual": 2.4968,
    "ebitdPerShareTTM": 1.6023,
    "ebitdaCagr5Y": 5.56,
    "ebitdaInterimCagr5Y": null,
    "enterpriseValue": 224373.7,
    "epsAnnual": 1.3601,
    "epsBasicExclExtraItemsAnnual": 1.3601,
    "epsBasicExclExtraItemsTTM": 0.7554000000000001,
    "epsExclExtraItemsAnnual": 1.3601,
    "epsExclExtraItemsTTM": 0.7554000000000001,
    "epsGrowth3Y": -37.13,
    "epsGrowth5Y": -3.51,
    "epsGrowthQuarterlyYoy": null,
    "epsGrowthTTMYoy": -59.91,
    "epsInclExtraItemsAnnual": 1.3601,
    "epsInclExtraItemsTTM": 0.7554000000000001,
    "epsNormalizedAnnual": 1.3601,
    "epsTTM": 0.7554000000000001,
    "evEbitdaTTM": 24.5351,
    "evRevenueTTM": 3.5226,
    "focfCagr5Y": -4.81,
    "forwardPE": 8.64266,
    "grossMargin5Y": 69.76,
    "grossMarginAnnual": 75.81,
    "grossMarginTTM": 74.71,
    "inventoryTurnoverAnnual": 1.408,
    "inventoryTurnoverTTM": 1.4903,
    "longTermDebt/equityAnnual": 0.7128,
    "longTermDebt/equityQuarterly": 0.7101,
    "marketCapitalization": 162155.7,
    "monthToDatePriceReturnDaily": -0.0351,
    "netIncomeEmployeeAnnual": 0.1036,
    "netIncomeEmployeeTTM": 0.0578,
    "netInterestCoverageAnnual": 5.3511,
    "netInterestCoverageTTM": 5.0214,
    "netMarginGrowth5Y": -10.8,
    "netProfitMargin5Y": 17.33,
    "netProfitMarginAnnual": 12.42,
    "netProfitMarginTTM": 6.8,
    "operatingMargin5Y": 18.78,
    "operatingMarginAnnual": 15.01,
    "operatingMarginTTM": 6.79,
    "payoutRatioAnnual": 125.75,
    "payoutRatioTTM": 80.25,
    "pb": 1.9035,
    "pbAnnual": 1.6371,
    "pbQuarterly": 1.6304,
    "pcfShareAnnual": 13.8535,
    "pcfShareTTM": 12.0994,
    "peAnnual": 20.8695,
    "peBasicExclExtraTTM": 37.4234,
    "peExclExtraAnnual": 5.57472,
    "peExclExtraTTM": 37.4234,
    "peInclExtraTTM": 37.4234,
    "peNormalizedAnnual": 20.8695,
    "peTTM": 37.4234,
    "pegTTM": -2.72351,
    "pfcfShareAnnual": 17.8664,
    "pfcfShareTTM": 14.7602,
    "pretaxMargin5Y": 18.13,
    "pretaxMarginAnnual": 12.02,
    "pretaxMarginTTM": 6.61,
    "priceRelativeToS&P50013Week": 9.0132,
    "priceRelativeToS&P50026Week": -6.1729,
    "priceRelativeToS&P5004Week": 5.543,
    "priceRelativeToS&P50052Week": -4.6471,
    "priceRelativeToS&P500Ytd": 1.3127,
    "psAnnual": 2.5912,
    "psTTM": 2.5458,
    "ptbvAnnual": 4.3235,
    "ptbvQuarterly": 3.642,
    "quickRatioAnnual": 0.8718,
    "quickRatioQuarterly": 0.9622,
    "receivablesTurnoverAnnual": 5.3631,
    "receivablesTurnoverTTM": 5.1852,
    "revenueEmployeeAnnual": 0.8344,
    "revenueEmployeeTTM": 0.8493,
    "revenueGrowth3Y": -14.8,
    "revenueGrowth5Y": 8.48,
    "revenueGrowthQuarterlyYoy": 2.6,
    "revenueGrowthTTMYoy": -0.22,
    "revenuePerShareAnnual": 10.9538,
    "revenuePerShareTTM": 11.1765,
    "revenueShareGrowth5Y": 8.17,
    "roa5Y": 7.29,
    "roaRfy": 3.73,
    "roaTTM": 2.1,
    "roe5Y": 16.35,
    "roeRfy": 8.99,
    "roeTTM": 4.89,
    "roi5Y": 10.92,
    "roiAnnual": 5.140000000000001,
    "roiTTM": 2.85,
    "tangibleBookValuePerShareAnnual": 5.7589,
    "tangibleBookValuePerShareQuarterly": 6.6919,
    "tbvCagr5Y": -1.19,
    "totalDebt/totalEquityAnnual": 0.7493,
    "totalDebt/totalEquityQuarterly": 0.7418,
    "yearToDatePriceReturnDaily": 14.257
  },
  "source_status": {
    "local_research": false,
    "local_news": false,
    "local_sec_filings": false,
    "finnhub_news": true,
    "polygon_news": false,
    "earnings": false,
    "fundamentals": true
  }
}
```

## AAPL
Trading candidate:
```json
{
  "symbol": "AAPL",
  "score": 81.45,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 100.0,
    "sector": 55.47,
    "relative_strength": 81.8012107844726,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 47.71724543948731,
    "momentum": 72.74439747986276,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 100.0
  }
}
```
Evidence packet (source-labelled; missing sources must remain uncertain):
```json
{
  "local_research": [],
  "local_news": [],
  "local_sec_filings": [],
  "finnhub_news": [
    {
      "category": "company",
      "datetime": 1788793500,
      "headline": "There Are Only a Handful of Nasdaq-100 Stocks That Yield Over 3%. Here's My Top Pick to Buy Now.",
      "id": 141763725,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "For my money, Mondelez is the best bet of the Nasdaq-100's high-yield names.",
      "url": "https://finnhub.io/api/news?id=2174d70a766081bdd8a73346df33a60a96c42372d1e9faef2a5fadd7bbf61936"
    },
    {
      "category": "company",
      "datetime": 1788793200,
      "headline": "Is Apple Stock a Buy Now Ahead of its Product Launch Event?",
      "id": 141763751,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "Ahead of Wednesday's launch, AAPL faces a tricky mix: strong demand, rising costs, tight supply, and a premium stock valuation.",
      "url": "https://finnhub.io/api/news?id=3ee56adc580aeb1cfdce31ba37534e7d5f9b8531f9126d2dfb8877003cf73321"
    },
    {
      "category": "company",
      "datetime": 1788792776,
      "headline": "The S&P 100 ETF Just Dumped Nike and Colgate for 4 AI Stocks. Here\u2019s What That Means for Your Portfolio",
      "id": 141763616,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "The iShares S&P 100 ETF just swapped out a toothpaste giant and a mall REIT for four AI infrastructure plays, and the move reveals something uncomfortable about what this so-called blue-chip fund has quietly become.",
      "url": "https://finnhub.io/api/news?id=42fbcd571f4e0ff319ea17c0fe94bd2d9085859a6a211459ff345ebc0a878b0d"
    },
    {
      "category": "company",
      "datetime": 1788792695,
      "headline": "Apple Just Made a Move Most Investors Overlooked. This Is Why I Keep Buying The Stock",
      "id": 141763434,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "Apple quietly broke its own product release playbook, and most investors scrolled right past the announcement without realizing what it signals for the decade ahead.",
      "url": "https://finnhub.io/api/news?id=159511197735622223a1ac598a177a9d78adfa4368e7ee238e0652b15dcff7aa"
    },
    {
      "category": "company",
      "datetime": 1788789628,
      "headline": "Why Apple May Be the Safest AI Stock Nobody Calls an AI Stock",
      "id": 141762760,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "Wall Street obsesses over the hyperscalers burning billions on AI infrastructure, but one mega-cap with 2.5 billion active devices keeps getting left out of the conversation, and that oversight may be exactly where the opportunity hides.",
      "url": "https://finnhub.io/api/news?id=e4892590c0acf4caf6687e6804e32ca4e16379ef5abc4560a18eb47e8d755755"
    }
  ],
  "polygon_news": [
    {
      "id": "6b8b11836a92751e7364a010dce3a2c1c55a4cfa025d86636006a6823b9f3bd4",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Is Adobe's Stock Heading for $300?",
      "author": "David Jagielski, Cpa",
      "published_utc": "2026-09-07T16:02:29Z",
      "article_url": "https://www.fool.com/investing/2026/09/07/is-adobe-s-stock-heading-for-300/?source=iedfolrf0000001",
      "tickers": [
        "ADBE",
        "AAPL",
        "NVDA"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F6acb60eadf30fcaa13192897bd2c1c41552f7973-2000x1125.jpg%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "Adobe's stock has fallen 24% year-to-date due to AI-related concerns, as AI chatbots threaten its core image creation software business. However, the stock has been rallying recently and trades at a discount (15x trailing earnings vs. S&P 500 average of 24x). Despite valid risks from potential demand erosion, the author believes Adobe's continued solid growth (11% revenue increase) and attractive valuation provide sufficient margin of safety for the stock to potentially finish the year above $300.",
      "keywords": [
        "artificial intelligence threat",
        "software stocks",
        "valuation discount",
        "AI chatbots",
        "subscription services",
        "tech stock rally",
        "margin of safety"
      ],
      "insights": [
        {
          "ticker": "ADBE",
          "sentiment": "positive",
          "sentiment_reasoning": "Despite significant AI-related headwinds and a 24% year-to-date decline, Adobe trades at an attractive valuation discount (15x trailing earnings) compared to the broader market. The company continues to show solid revenue growth (11%) and is incorporating AI into its products. The author believes the stock has more upside than downside at current levels and could reach $300 by year-end."
        },
        {
          "ticker": "AAPL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Apple is mentioned as a high-flying tech stock that has hit record levels and is receiving significant investor focus, but it is not the subject of analysis in this article and no specific sentiment is expressed about its investment merits."
        },
        {
          "ticker": "NVDA",
          "sentiment": "neutral",
          "sentiment_reasoning": "Nvidia is mentioned as a high-flying tech stock that has hit record levels, but it is not the subject of analysis in this article and no specific sentiment is expressed about its investment merits."
        }
      ]
    },
    {
      "id": "3b34584ade763b81c1916f106859262eee211985f16bdac318e22b762efb84bb",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Bill Gates Says He Still Won't Invest in Crypto, Calls It a \"Pure Mania-Driven Asset.\" Here's Why He's Right.",
      "author": "Jeff Siegel",
      "published_utc": "2026-09-05T23:30:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/05/bill-gates-says-he-still-wont-invest-in-crypto-cal/?source=iedfolrf0000001",
      "tickers": [
        "AAPL",
        "CAT",
        "MSFT",
        "TSLA"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F886100%2Fgettyimages-1318918012.jpg&w=1200&op=resize",
      "description": "Bill Gates reiterates his stance against cryptocurrency investment, describing Bitcoin as a 'mania-driven asset' lacking fundamental value. Unlike stocks in productive companies that generate revenue and earnings, Bitcoin's value depends solely on future buyer demand. While Bitcoin could continue appreciating, Gates argues that diversified stock portfolios offer a more tangible foundation for long-term wealth building.",
      "keywords": [
        "Bitcoin",
        "cryptocurrency",
        "investment fundamentals",
        "Bill Gates",
        "stock vs crypto",
        "long-term investing",
        "asset valuation"
      ],
      "insights": [
        {
          "ticker": "AAPL",
          "sentiment": "positive",
          "sentiment_reasoning": "Used as an example of a productive company with tangible business fundamentals, generating revenue through product sales (iPhones), supporting the argument for stocks over crypto as long-term investments."
        },
        {
          "ticker": "CAT",
          "sentiment": "positive",
          "sentiment_reasoning": "Referenced as a productive business generating revenue through tangible products (heavy equipment), exemplifying the type of company-based investment preferred over cryptocurrency."
        },
        {
          "ticker": "MSFT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as Bill Gates' company affiliation; no specific investment sentiment expressed in the article content."
        },
        {
          "ticker": "TSLA",
          "sentiment": "neutral",
          "sentiment_reasoning": "Referenced only in context of Gates' past investment mistake shorting the company; used as an example of Gates' occasional lack of foresight, not as commentary on current investment merit."
        }
      ]
    },
    {
      "id": "4d7feb52c8dcfa23ecb725209894d4377063885b7b280dfe84fe8a4d341ce859",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Prediction: Amazon Will Join Nvidia, Apple, and Alphabet in the $4 Trillion Club Before 2029",
      "author": "Keith Noonan",
      "published_utc": "2026-09-05T19:20:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/05/prediction-amazon-will-join-nvidia-apple-and-alpha/?source=iedfolrf0000001",
      "tickers": [
        "AMZN",
        "NVDA",
        "AAPL",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "TSLA"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F885421%2Fgettyimages-1200037244.jpg&w=1200&op=resize",
      "description": "Amazon, currently valued at $2.75 trillion, is predicted to reach a $4 trillion market cap by 2029, requiring approximately 45.5% stock growth. Despite underperforming the S&P 500 over the past five years, Amazon's strong AWS cloud infrastructure growth (37% YoY), AI-driven demand, and e-commerce dominance position it well for future gains. The company's potential margin improvements through automation and robotics, combined with digital advertising growth, provide multiple growth engines.",
      "keywords": [
        "Amazon",
        "market capitalization",
        "artificial intelligence",
        "cloud infrastructure",
        "AWS",
        "e-commerce",
        "stock valuation",
        "Magnificent Seven"
      ],
      "insights": [
        {
          "ticker": "AMZN",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong AWS growth at 37% YoY exceeding analyst expectations, accelerating overall revenue growth at 20%, leadership in AI infrastructure, and multiple optimization opportunities in e-commerce and digital ads support bullish outlook for reaching $4 trillion valuation."
        },
        {
          "ticker": "NVDA",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as already part of the $4 trillion club; no specific analysis or commentary provided in the article."
        },
        {
          "ticker": "AAPL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as already part of the $4 trillion club; no specific analysis or commentary provided in the article."
        },
        {
          "ticker": "GOOG",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as already part of the $4 trillion club; no specific analysis or commentary provided in the article."
        },
        {
          "ticker": "GOOGL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as already part of the $4 trillion club; no specific analysis or commentary provided in the article."
        },
        {
          "ticker": "GOOGM",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as already part of the $4 trillion club; no specific analysis or commentary provided in the article."
        },
        {
          "ticker": "GOOGN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as already part of the $4 trillion club; no specific analysis or commentary provided in the article."
        },
        {
          "ticker": "TSLA",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as the lowest-performing Magnificent Seven stock with 46% five-year return; included for context but not analyzed."
        }
      ]
    },
    {
      "id": "c47d2607f5cb0220701504e1f01b61610e6b6ec78d2bc32426950d8d437bfc5f",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Schwab U.S. Dividend Equity vs. Vanguard Dividend Appreciation: Which ETF Looks Better for Your Portfolio?",
      "author": "Erin Kennedy",
      "published_utc": "2026-09-05T12:15:01Z",
      "article_url": "https://www.fool.com/coverage/etfs/2026/09/05/schwab-u-s-dividend-equity-vs-vanguard-dividend-appreciation-which-etf-looks-better-for-your-portfolio/?source=iedfolrf0000001",
      "tickers": [
        "SCHD",
        "VIG",
        "MRK",
        "ABT",
        "AMGN",
        "AVGO",
        "AAPL",
        "MSFT"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F3f28864d917b18e124dc110dee6614eac0a6339c-1401x1251.png%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "Schwab U.S. Dividend Equity ETF (SCHD) offers nearly double the dividend yield of Vanguard Dividend Appreciation ETF (VIG) at 3% versus 1.5%, with a value-focused portfolio in healthcare and consumer defensives. VIG emphasizes technology stocks and requires 10-year dividend growth streaks. SCHD showed stronger one-year returns (29.5% vs 17.1%) and lower volatility, making it the analyst's preferred choice for income investors seeking higher yields.",
      "keywords": [
        "dividend ETF",
        "income investing",
        "SCHD vs VIG",
        "dividend yield",
        "portfolio comparison",
        "value investing",
        "technology stocks"
      ],
      "insights": [
        {
          "ticker": "SCHD",
          "sentiment": "positive",
          "sentiment_reasoning": "SCHD is recommended as the better buy due to significantly higher dividend yield (3% vs 1.5%), stronger one-year returns (29.5%), lower beta (0.68), and better liquidity. The value-focused portfolio with healthcare and consumer defensive concentration is viewed favorably for income investors."
        },
        {
          "ticker": "VIG",
          "sentiment": "neutral",
          "sentiment_reasoning": "VIG is presented as a solid alternative with attractive features including lower expense ratio, larger AUM, and stricter dividend growth criteria (10-year track record). However, it underperforms SCHD on yield and one-year returns, and its tech-heavy concentration (26%) presents concentration risk despite broader holdings (333 stocks)."
        },
        {
          "ticker": "MRK",
          "sentiment": "neutral",
          "sentiment_reasoning": "Merck is mentioned as a top holding in SCHD (4.92% weighting), representing the healthcare sector concentration in the fund."
        },
        {
          "ticker": "ABT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Abbott is listed as a top holding in SCHD (4.83% weighting), contributing to the healthcare sector focus."
        },
        {
          "ticker": "AMGN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Amgen is a top holding in SCHD (4.8% weighting), part of the healthcare concentration."
        },
        {
          "ticker": "AVGO",
          "sentiment": "neutral",
          "sentiment_reasoning": "Broadcom is a top holding in VIG (4.63% weighting), representing the technology sector concentration."
        },
        {
          "ticker": "AAPL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Apple is a top holding in VIG (4.45% weighting), contributing to the tech-heavy portfolio that presents concentration risk."
        },
        {
          "ticker": "MSFT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Microsoft is a top holding in VIG (4.34% weighting), part of the technology sector concentration that raises concentration concerns."
        }
      ]
    },
    {
      "id": "bdeb98af43a76c8d672bf0eb7296afdf7f7ddd76febe17c7db0b7713e0b0de83",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Here's How Many Shares of Apple (AAPL) Stock You'd Need for $12,000 in Yearly Dividends",
      "author": "Selena Maranjian",
      "published_utc": "2026-09-05T09:05:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/05/heres-how-many-shares-of-apple-aapl-stock-youd-nee/?source=iedfolrf0000001",
      "tickers": [
        "AAPL",
        "SCHD"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F885117%2Ffool-apple-aapl.jpg&w=1200&op=resize",
      "description": "To generate $12,000 in annual dividend income from Apple stock, an investor would need to purchase approximately 11,111 shares at a cost of $3.6 million, given Apple's current quarterly dividend of $0.27 per share ($1.08 annually) and stock price around $325. The article cautions that Apple's dividend yield is low at 0.33% and suggests investors may be better served by focusing on Apple's price appreciation potential or seeking dividend income through dividend-focused ETFs instead.",
      "keywords": [
        "dividend income",
        "Apple stock",
        "dividend yield",
        "valuation",
        "passive income",
        "dividend-focused ETF"
      ],
      "insights": [
        {
          "ticker": "AAPL",
          "sentiment": "neutral",
          "sentiment_reasoning": "While Apple is acknowledged as a solid investment with strong historical returns (24% annually over 15 years) and growing dividends (4.2-6.7% annually), the article cautions that current valuations appear stretched with a P/E ratio of 32 versus a 5-year average of 28. The low dividend yield of 0.33% makes it unsuitable for income-focused investors seeking $12,000 annually."
        },
        {
          "ticker": "SCHD",
          "sentiment": "positive",
          "sentiment_reasoning": "The article recommends this ETF as an excellent alternative for investors seeking dividend income, positioning it as a better option than Apple for those prioritizing dividend yields over capital appreciation."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 37.06557,
    "13WeekPriceReturnDaily": 2.8082,
    "26WeekPriceReturnDaily": 21.3156,
    "3MonthADReturnStd": 31.72754,
    "3MonthAverageTradingVolume": 52.997,
    "52WeekHigh": 344.5699,
    "52WeekHighDate": "2026-07-29",
    "52WeekLow": 225.95,
    "52WeekLowDate": "2025-09-10",
    "52WeekPriceReturnDaily": 33.4933,
    "5DayPriceReturnDaily": 0.9847,
    "assetTurnoverAnnual": 1.1584,
    "assetTurnoverTTM": 1.2508,
    "beta": 1.0966319,
    "bookValuePerShareAnnual": 4.991,
    "bookValuePerShareQuarterly": 7.3599,
    "bookValueShareGrowth5Y": 5.34,
    "capexCagr5Y": 11.71,
    "cashFlowPerShareAnnual": 6.6855,
    "cashFlowPerShareQuarterly": 9.3561,
    "cashFlowPerShareTTM": 6.86253,
    "cashPerSharePerShareAnnual": 3.7024,
    "cashPerSharePerShareQuarterly": 4.2713,
    "currentDividendYieldTTM": 0.3349,
    "currentEv/freeCashFlowAnnual": 47.7335,
    "currentEv/freeCashFlowTTM": 34.4922,
    "currentRatioAnnual": 0.8933,
    "currentRatioQuarterly": 1.0033,
    "dividendGrowthRate5Y": 4.95,
    "dividendIndicatedAnnual": 1.08,
    "dividendPerShareAnnual": 1.0318,
    "dividendPerShareTTM": 1.0616,
    "dividendYieldIndicatedAnnual": 0.50534,
    "ebitdPerShareAnnual": 9.6468,
    "ebitdPerShareTTM": 11.365,
    "ebitdaCagr5Y": 13.35,
    "ebitdaInterimCagr5Y": 7.67,
    "enterpriseValue": 4714499.5,
    "epsAnnual": 7.465,
    "epsBasicExclExtraItemsAnnual": 7.465,
    "epsBasicExclExtraItemsTTM": 8.723299999999998,
    "epsExclExtraItemsAnnual": 7.465,
    "epsExclExtraItemsTTM": 8.723299999999998,
    "epsGrowth3Y": 6.89,
    "epsGrowth5Y": 17.91,
    "epsGrowthQuarterlyYoy": 29.13,
    "epsGrowthTTMYoy": 32.61,
    "epsInclExtraItemsAnnual": 7.465,
    "epsInclExtraItemsTTM": 8.723299999999998,
    "epsNormalizedAnnual": 7.465,
    "epsTTM": 8.723299999999998,
    "evEbitdaTTM": 28.0693,
    "evRevenueTTM": 10.0991,
    "focfCagr5Y": 6.13,
    "forwardPE": 34.85022,
    "forwardPEG": 2.52538,
    "grossMargin5Y": 44.47,
    "grossMarginAnnual": 46.91,
    "grossMarginTTM": 48.65,
    "inventoryTurnoverAnnual": 33.9834,
    "inventoryTurnoverTTM": 28.1718,
    "longTermDebt/equityAnnual": 1.0623,
    "longTermDebt/equityQuarterly": 0.6635,
    "marketCapitalization": 4669699.5,
    "monthToDatePriceReturnDaily": 0.9847,
    "netIncomeEmployeeAnnual": 0.6748,
    "netIncomeEmployeeTTM": 0.7767,
    "netInterestCoverageAnnual": 622.5082,
    "netInterestCoverageTTM": 622.5082,
    "netMarginGrowth5Y": 5.18,
    "netProfitMargin5Y": 25.48,
    "netProfitMarginAnnual": 26.92,
    "netProfitMarginTTM": 27.62,
    "operatingMargin5Y": 30.67,
    "operatingMarginAnnual": 31.97,
    "operatingMarginTTM": 33.17,
    "payoutRatioAnnual": 13.77,
    "payoutRatioTTM": 12.13,
    "pb": 43.431,
    "pbAnnual": 50.978,
    "pbQuarterly": 38.486,
    "pcfShareAnnual": 41.8875,
    "pcfShareTTM": 31.8264,
    "peAnnual": 41.69,
    "peBasicExclExtraTTM": 36.2189,
    "peExclExtraAnnual": 30.96975,
    "peExclExtraTTM": 36.2189,
    "peInclExtraTTM": 36.2189,
    "peNormalizedAnnual": 41.69,
    "peTTM": 36.2189,
    "pegTTM": 2.93443,
    "pfcfShareAnnual": 47.28,
    "pfcfShareTTM": 34.1644,
    "pretaxMargin5Y": 30.64,
    "pretaxMarginAnnual": 31.89,
    "pretaxMarginTTM": 33.4,
    "priceRelativeToS&P50013Week": 1.0779,
    "priceRelativeToS&P50026Week": 8.1073,
    "priceRelativeToS&P5004Week": 4.1661,
    "priceRelativeToS&P50052Week": 14.4973,
    "priceRelativeToS&P500Ytd": 4.7523,
    "psAnnual": 11.2209,
    "psTTM": 10.0031,
    "ptbvAnnual": 4.8643,
    "ptbvQuarterly": 47.4663,
    "quickRatioAnnual": 0.8588,
    "quickRatioQuarterly": 0.929,
    "receivablesTurnoverAnnual": 11.3725,
    "receivablesTurnoverTTM": 15.8366,
    "revenueEmployeeAnnual": 2.507,
    "revenueEmployeeTTM": 2.8122,
    "revenueGrowth3Y": 1.81,
    "revenueGrowth5Y": 8.68,
    "revenueGrowthQuarterlyYoy": 16.36,
    "revenueGrowthTTMYoy": 14.24,
    "revenuePerShareAnnual": 27.7354,
    "revenuePerShareTTM": 31.725,
    "revenueShareGrowth5Y": 12.11,
    "roa5Y": 27.93,
    "roaRfy": 31.180000000000003,
    "roaTTM": 34.55,
    "roe5Y": 163.92,
    "roeRfy": 151.91,
    "roeTTM": 137.17999999999998,
    "roi5Y": 57.1,
    "roiAnnual": 64.51,
    "roiTTM": 70.25,
    "tangibleBookValuePerShareAnnual": 5.8583,
    "tangibleBookValuePerShareQuarterly": 5.9674,
    "tbvCagr5Y": 11.34,
    "totalDebt/totalEquityAnnual": 1.3547,
    "totalDebt/totalEquityQuarterly": 0.7844,
    "yearToDatePriceReturnDaily": 17.6966
  },
  "source_status": {
    "local_research": false,
    "local_news": false,
    "local_sec_filings": false,
    "finnhub_news": true,
    "polygon_news": true,
    "earnings": false,
    "fundamentals": true
  }
}
```

## BAC
Trading candidate:
```json
{
  "symbol": "BAC",
  "score": 78.57,
  "direction": "LONG",
  "sector": "Financials",
  "components": {
    "market": 100.0,
    "sector": 88.76,
    "relative_strength": 52.62699670745095,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 54.161419497273734,
    "momentum": 62.507232401157204,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 100.0
  }
}
```
Evidence packet (source-labelled; missing sources must remain uncertain):
```json
{
  "local_research": [
    "[WDC.md]\n# WDC \u2014 Western Digital Corporation\n\n**As of:** 2026-08-31  \n**Sector / industry:** Technology / Computer hardware and data storage  \n**Conviction:** Medium \u2014 strong AI-driven HDD cycle and improving economics, but highly cyclical and customer-concentrated\n\n## Snapshot\n\nWestern Digital is now primarily a hard-disk-drive company following the 2025 separation of its Flash business into SanDisk. It supplies high-capacity HDDs to hyperscale cloud providers, neoclouds, enterprises, OEMs, distributors, and consumers. The central thesis is that AI creates enormous volumes of data that must be stored economically, while HDDs remain attractive for high-capacity, lower-cost archival and nearline storage.\n\nWDC closed around **$450.55** on August 31, 2026. With approximately 360.5 million shares, implied market capitalization is about **$162.5 billion**. FY26 non-GAAP EPS was $10.22, but the current valuation is better judged against forward earnings because the business is in a sharp upcycle. The company ended FY26 with $1.58B of cash and $1.06B of debt, including $350M drawn on its revolver.\n\n## Latest operating results\n\nQ4 FY26 revenue was **$3.747B, up 44% year over year** and 12% sequentially. GAAP gross margin was 54.1%, GAAP operating margin was 41.7%, and non-GAAP operating margin was 44.2%. Non-GAAP diluted EPS was **$3.56**, up 109% year over year. Operating cash flow was $1.39B and free cash flow was $1.28B.\n\nFor full FY26, revenue rose 36% to **$12.919B**, non-GAAP operating income rose 107% to $4.817B, and non-GAAP EPS rose 104% to $10.22. The company declared a quarterly dividend of $0.15 per share.\n\nQ1 FY27 guidance is particularly strong: revenue is expected to be about **$4.1B at the midpoint**, up 42%\u201349% year over year, with non-GAAP gross margin of 55.5% and non-GAAP EPS of $4.00. Management expects FY27 capital expenditures to rise from FY26 as it invests in heads, media, and automation; long-term capex is expected to average 4%\u20136% of revenue.\n\n## Bull thesis\n\n- AI and cloud workloads are creating a secular need for cheap, dense, reliable storage. HDDs remain difficult to replace economically for hyperscale nearline and archival capacity.\n- The HDD market is structurally concentrated, giving Western Digital and Seagate scale, customer relationships, and engineering advantages.\n- Higher-capacity ePMR and future HAMR-related products can improve areal density, reduce customers\u2019 total storage cost, and support better pricing and margins.\n- The company has moved from a low-margin, leveraged storage cycle into a high-cash-flow period: Q4 free-cash-flow margin was about 34%, and debt has been substantially reduced since the Flash separation.\n- Cloud represented 89% of FY26 revenue, making WDC a direct beneficiary of hyperscaler infrastructure spending rather than a broad consumer-electronics bet.\n\n## Bear thesis\n\n- This is still a cyclical hardware manufacturer. Cloud customers can pause purchases, digest inventory, or reduce AI infrastructure spending, causing abrupt revenue and margin declines.\n- Customer concentration is very high: the top 10 customers represented **73%** of FY26 revenue, and three individual customers each represented at least 10%.\n- The current stock price appears to discount sustained peak-to-near-peak profitability. A return toward historical HDD margins could make headline trailing earnings look far less attractive.\n- NAND/flash is no longer consolidated inside WDC, so the company has less diversification; the remaining business is more dependent on HDD technology and cloud demand.\n- Seagate is a powerful competitor, while SSDs continue to improve in density, performance, power efficiency, and total-cost economics for some workloads.\n- Supply-chain disruptions, component shortages, manufacturing transitions, export controls, foreign exchange, and large fixed costs can amplify both upside and downside.\n\n## Catalysts\n\n1. Q1 FY27 revenue and EPS meeting or exceeding the $4.1B / $4.00 midpoint guidance.\n2. Additional cloud capacity commitments and evidence that AI data growth is increasing HDD demand rather than merely accelerating SSD adoption.\n3. Successful high-capacity product ramps with sustained gross margin above 50%.\n4. Debt reduction, share repurchases, and dividend growth funded by free cash flow.\n5. Industry supply discipline and continued favorable pricing in nearline HDDs.\n\n## What would change the view\n\n**Upgrade:** cloud growth remains strong, revenue stays above $4B quarterly, gross margins hold near the mid-50s, customer concentration does not translate into pricing pressure, and free cash flow compounds after higher capex.  \n**Downgrade:** hyperscaler orders or capex plans weaken, inventory corrections emerge, gross margin falls sharply, SSD substitution accelerates, or the stock continues to rerate upward faster than forward EPS.\n\n## Bottom line\n\nWDC is a compelling way to own the storage side of the AI infrastructure buildout. The latest quarter showed operating l",
    "[VST.md]\n# VST \u2014 Vistra Corp.\n\n**As of:** 2026-08-27  \n**Sector / industry:** Utilities / Independent power producer and electricity generation  \n**Conviction:** Medium \u2014 attractive power-demand exposure and cash flow, but cyclical prices, regulation, and valuation matter\n\n## Snapshot\n\nVistra is a competitive power producer and electricity retailer with a large U.S. generation portfolio, including nuclear, natural gas, and renewable assets. It is not a regulated utility in the traditional sense: earnings depend substantially on wholesale power prices, capacity markets, hedging, fuel economics, and retail demand.\n\nVST was about **$139.81** on August 27, 2026, with a market capitalization of approximately **$47.4 billion** and a trailing P/E near **23.6x**. The stock is a premium-priced way to access the U.S. power shortage and data-center load-growth theme, but the valuation already reflects a meaningful part of that opportunity.\n\n## Latest operating results\n\nQ2 2026 net income was **$305 million**. Ongoing Operations Adjusted EBITDA was **$1.767 billion**, up more than 30% year over year, driven by higher realized energy and capacity prices plus the contribution from the Lotus generation acquisition. Net income was reduced by a $472 million unrealized hedge loss expected to settle in future years.\n\nVistra reaffirmed 2026 guidance for Ongoing Operations Adjusted EBITDA of **$6.8\u2013$7.6 billion** and Ongoing Operations Adjusted Free Cash Flow before Growth of **$3.925\u2013$4.725 billion**. The company had hedged approximately 100% of expected 2026 generation, 94% for 2027, and 72% for 2028 as of August 3. Management's 2027 EBITDA midpoint opportunity range is $7.4\u2013$7.8 billion, excluding potential benefits from the pending Cogentrix acquisition and Meta PPAs.\n\nVistra had approximately **$6.3 billion of available liquidity** at June 30, including $435 million of cash, $4.4 billion under its corporate revolver, and $1.45 billion under its commodity-linked facility. It has repurchased approximately $6.5 billion of stock since November 2021, reducing shares outstanding by about 30%; roughly $1.2 billion remained under the authorization as of August 3.\n\n## Bull thesis\n\n- AI data centers, industrial reshoring, EV adoption, and electrification are increasing the value of reliable, dispatchable power. Existing nuclear plants are particularly scarce and difficult to replace.\n- Vistra has long-duration nuclear PPAs with hyperscalers: a 20-year agreement with AWS for 1,200 MW from Comanche Peak and agreements with Meta covering more than 2,600 MW from PJM nuclear plants.\n- Higher capacity prices and constrained regional supply can support earnings even before new generation is built.\n- The Lotus acquisition adds approximately 2,600 MW of natural-gas generation and expands Vistra's ability to serve load growth and benefit from Texas/ERCOT demand.\n- Hedging provides substantial near-term earnings visibility, while disciplined repurchases can drive per-share growth.\n- Helix Digital Infrastructure, established with KKR, KIA, and NVIDIA, could create an additional platform for power and data-center infrastructure investment; Vistra's initial commitment is up to $1 billion.\n\n## Bear thesis\n\n- Wholesale power prices and capacity revenues are cyclical. A mild summer, weaker load, lower gas prices, transmission improvements, or new generation could reduce realized prices.\n- Nuclear operations carry outage, regulatory, maintenance, fuel, and decommissioning risks. A major forced outage can materially affect quarterly cash flow.\n- The data-center theme is powerful but not guaranteed to translate into Vistra earnings quickly; PPAs, grid interconnection, permitting, and data-center construction can take years.\n- Hedging reduces upside as well as downside. If power prices rise sharply, much of the near-term generation may already be sold forward.\n- Vistra carries meaningful debt and commodity-linked collateral requirements. Liquidity can be pressured when prices rise and margin-posting needs increase.\n- Competition for nuclear assets and AI-power exposure has pushed the valuation higher. If the market rotates away from utilities, nuclear, or AI infrastructure, multiple compression is possible even with stable earnings.\n- Environmental, nuclear-safety, market-design, and political decisions can materially change economics across ERCOT, PJM, and other markets.\n\n## Catalysts\n\n1. Higher PJM capacity prices and continued ERCOT load growth from data centers and industrial demand.\n2. Closing and integration of the Cogentrix acquisition.\n3. Initial earnings contribution from the Meta nuclear PPAs and continued execution of the AWS agreement.\n4. Helix fund investments that connect Vistra's generation assets with hyperscale data-center development.\n5. Continued share repurchases, rising free cash flow, and positive 2027 guidance revisions.\n\n## What would change the view\n\n**Upgrade:** sustained power-price and capacity-market strength, Cogentrix accretion, vi"
  ],
  "local_news": [
    "[2026-07-26.md]\n# Daily Market-Moving News \u2014 2026-07-26\n\n## Overall Market\n- U.S. stock futures rose into the new week as oil fell sharply on reports of a U.S.-Iran pause, easing immediate energy/inflation fears.\n- Major index direction is likely to be driven by the Fed decision, U.S. macro data, and mega-cap technology earnings.\n\n## AI / Semiconductors\n- NVIDIA reportedly discussed a $250B financing guarantee/backstop for OpenAI data-center capacity, reinforcing the scale of AI infrastructure demand while raising financing-quality questions.\n- NVIDIA's planned $1B investment in South Korea's Naver pushed Naver shares higher and highlights NVIDIA's strategic role in AI data-center ecosystems.\n- Chinese memory chipmaker CXMT surged in its Shanghai debut after a major IPO, keeping China semiconductor funding and memory competition in focus.\n\n## Cloud / Software\n- Oracle remained in focus around Pentagon/cloud contract commentary and AI infrastructure demand.\n- Cloud and neocloud demand remains tied to AI capacity shortages and hyperscaler capex.\n\n## Commodities / Geopolitics\n- Oil tumbled after signs of a pause in U.S.-Iran hostilities, reducing risk premium and supporting bonds/equities.\n- Gold remained bid in some market feeds ahead of Fed/GDP/PCE risk, showing residual macro hedging demand.\n\n## Earnings\n- Apple, Microsoft, Meta, Amazon and other large-cap tech names are key earnings catalysts for the week.\n- Exxon and energy-linked earnings are more sensitive after the oil move.\n\n## M&A / IPOs\n- EQT returned with a higher $1.8B offer for Australia\u2019s Perpetual.\n- Brown-Forman rejected Sazerac\u2019s unsolicited proposal as not actionable.\n- Shein flagged tariff pressure and quarterly losses ahead of a Hong Kong IPO.\n\n## Sources Checked\n- Google News RSS market queries\n- Investing.com / Reuters market RSS\n- Prior daily news artifact from this workflow\n"
  ],
  "local_sec_filings": [
    "[2026-07-26.md]\n# SEC Filings \u2014 2026-07-26\n\n## Overview\n\nRecent filings for watchlisted tickers are concentrated in FY2026 10-K and FY2027 Q1 10-Q disclosures. Sector focus is centered on tech/semiconductors, defense, and nuclear energy names.\n\n## Key Disclosures\n\n- **NVIDIA Corporation (NVDA):** Filed Form 10-Q on 2026-05-20 (accession `0001045810-26-000052`). Shares outstanding reported at 24.2 billion shares. Public float rose to $4.0T as of 2025-07-25.\n- **Oracle Corporation (ORCL):** Pentagon/defense cloud contract discussions are material for its cloud services backlog and infrastructure segments.\n- **Shein:** (Pre-IPO) Disclosed a quarterly loss and warned of tariff risks in preliminary filings ahead of its planned Hong Kong IPO.\n- **Nuclear/Uranium names:** Micro-reactor and fuel names (OKLO, SMR, CCJ) are highlighting capacity additions and fuel contracts in recent SEC disclosures.\n"
  ],
  "finnhub_news": [
    {
      "category": "company",
      "datetime": 1788797280,
      "headline": "What's Powering Bank of America's Strong Capital Return Strategy?",
      "id": 141765137,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "BAC",
      "source": "Yahoo",
      "summary": "Strong earnings momentum, a solid capital cushion and ample buyback capacity are underpinning BAC's shareholder-return strategy.",
      "url": "https://finnhub.io/api/news?id=2ec7c71a0b634eb0cd0f102a57713f436e063a6e527e3acd994cc7c8f9e92b7d"
    },
    {
      "category": "company",
      "datetime": 1788783611,
      "headline": "BofA Sees Clear Winner Between Adobe and Oracle",
      "id": 141761949,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "BAC",
      "source": "Yahoo",
      "summary": "Wall Street sees opportunity in one and trouble in another",
      "url": "https://finnhub.io/api/news?id=e77059e178d026f47db3771bc007a9a4633fac553c174e4ad8d07282dd79d7f7"
    },
    {
      "category": "company",
      "datetime": 1788764400,
      "headline": "Gen Z and Millennials Had a Big Summer of Sports Betting",
      "id": 141761950,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "BAC",
      "source": "Yahoo",
      "summary": "In 1967, Baby Boomers had the Summer of Love.  This year, Gen Z had a Summer of Sports Betting.  Researchers from Bank of America found that 88% of online bettors in July were Gen Zers and Millennials, a group that covers adults born after 1978.",
      "url": "https://finnhub.io/api/news?id=6684d87edffb4ba805b96a96a244cb98d4c1b350a93010d6fa15ffa21e94f224"
    },
    {
      "category": "company",
      "datetime": 1788642384,
      "headline": "Blue Owl Capital (OWL) Stock Fair Value Edges Higher After Q2 Analyst Revisions",
      "id": 141546905,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "BAC",
      "source": "Yahoo",
      "summary": "Price targets for Blue Owl Capital now cluster in a wide band between about US$10 and US$17, as updated models adjust fair value estimates such as the move from roughly US$12.38 to about US$12.74. Recent analyst research links these shifts to Q2 results, revised fundraising expectations, and changing sentiment toward private credit and alternative asset managers. As you read on, you will see how to track this evolving narrative and what to watch as new information comes through. Analyst Price...",
      "url": "https://finnhub.io/api/news?id=230863c367a7a1af5e7dc1309a91f12bd413ce1e7d623d06ec58fea74b9afa11"
    },
    {
      "category": "company",
      "datetime": 1788605524,
      "headline": "Bitcoin Drops Below $80K After Strong Jobs Data, ETF Inflows Collapse 76% In A Day",
      "id": 141514109,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "BAC",
      "source": "Yahoo",
      "summary": "Bank of America flagged September 11 CPI as the more decisive signal for the Fed rate path, Bitunix analysts said.",
      "url": "https://finnhub.io/api/news?id=c9e5ac009d9dd26f419e797f2399aea12083dec033c48b59f1923ee28cd90040"
    }
  ],
  "polygon_news": [
    {
      "id": "ac40caf97706a635e74a3e60c7e8fa3f9a0210944e11f55e57cfbd9d144e861f",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "What's Powering Bank of America's Strong Capital Return Strategy?",
      "author": "Na",
      "published_utc": "2026-09-07T15:08:00Z",
      "article_url": "https://www.zacks.com/stock/news/2985984/what-s-powering-bank-of-america-s-strong-capital-return-strategy?cid=CS-ZC-FT-analyst_blog|quick_take-2985984",
      "tickers": [
        "BAC",
        "BACpB",
        "BACpE",
        "BACpK",
        "BACpL",
        "BACpM",
        "BACpN",
        "BACpO",
        "BACpP",
        "BACpQ",
        "BACpS",
        "BMLpG",
        "BMLpH",
        "BMLpJ",
        "BMLpL",
        "MERpK",
        "AMJB",
        "JPM",
        "JPMpC",
        "JPMpD",
        "JPMpJ",
        "JPMpK",
        "JPMpL",
        "JPMpM",
        "VYLD",
        "MS",
        "MSpA",
        "MSpE",
        "MSpF",
        "MSpI",
        "MSpK",
        "MSpL",
        "MSpO",
        "MSpP",
        "MSpQ"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/0b/57.jpg",
      "description": "Bank of America demonstrates strong capacity for shareholder returns through robust earnings generation, healthy CET1 capital ratios, and disciplined balance-sheet management. The bank raised its quarterly dividend 14.3% to 32 cents per share and maintains $17 billion in remaining buyback authorization. Strong Q2 2026 results with $9.1 billion net income and 15% revenue growth support continued capital distributions, though a higher G-SIB surcharge from January 2027 may modestly increase capital requirements.",
      "keywords": [
        "capital returns",
        "dividend increase",
        "share buybacks",
        "earnings growth",
        "CET1 ratio",
        "banking sector",
        "shareholder returns"
      ],
      "insights": [
        {
          "ticker": "BAC",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "BACpB",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "BACpE",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "BACpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "BACpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "BACpM",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "BACpN",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "BACpO",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "BACpP",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "BACpQ",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "BACpS",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "BMLpG",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "BMLpH",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "BMLpJ",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "BMLpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "MERpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings generation ($30.5B in 2025, $9.1B in Q2 2026), healthy CET1 capital ratio at 11.2% well above regulatory minimums, 14.3% dividend increase marking sixth consecutive annual hike, and $17B remaining in $40B buyback authorization demonstrate robust financial health and commitment to shareholder returns."
        },
        {
          "ticker": "AMJB",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings and regulatory capital position support 10% dividend increase to $1.65 per share, six dividend hikes over five years with 11.3% annualized growth rate, and $50B share repurchase program authorization effective July 2026."
        },
        {
          "ticker": "JPM",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings and regulatory capital position support 10% dividend increase to $1.65 per share, six dividend hikes over five years with 11.3% annualized growth rate, and $50B share repurchase program authorization effective July 2026."
        },
        {
          "ticker": "JPMpC",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings and regulatory capital position support 10% dividend increase to $1.65 per share, six dividend hikes over five years with 11.3% annualized growth rate, and $50B share repurchase program authorization effective July 2026."
        },
        {
          "ticker": "JPMpD",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings and regulatory capital position support 10% dividend increase to $1.65 per share, six dividend hikes over five years with 11.3% annualized growth rate, and $50B share repurchase program authorization effective July 2026."
        },
        {
          "ticker": "JPMpJ",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings and regulatory capital position support 10% dividend increase to $1.65 per share, six dividend hikes over five years with 11.3% annualized growth rate, and $50B share repurchase program authorization effective July 2026."
        },
        {
          "ticker": "JPMpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings and regulatory capital position support 10% dividend increase to $1.65 per share, six dividend hikes over five years with 11.3% annualized growth rate, and $50B share repurchase program authorization effective July 2026."
        },
        {
          "ticker": "JPMpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings and regulatory capital position support 10% dividend increase to $1.65 per share, six dividend hikes over five years with 11.3% annualized growth rate, and $50B share repurchase program authorization effective July 2026."
        },
        {
          "ticker": "JPMpM",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings and regulatory capital position support 10% dividend increase to $1.65 per share, six dividend hikes over five years with 11.3% annualized growth rate, and $50B share repurchase program authorization effective July 2026."
        },
        {
          "ticker": "VYLD",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong earnings and regulatory capital position support 10% dividend increase to $1.65 per share, six dividend hikes over five years with 11.3% annualized growth rate, and $50B share repurchase program authorization effective July 2026."
        },
        {
          "ticker": "MS",
          "sentiment": "positive",
          "sentiment_reasoning": "Increased quarterly dividend 15% to $1.15 per share in Q3 2026 following 8% hike in 2025, reauthorized $20B multi-year share repurchase program without expiration date, and emphasis on disciplined capital allocation."
        },
        {
          "ticker": "MSpA",
          "sentiment": "positive",
          "sentiment_reasoning": "Increased quarterly dividend 15% to $1.15 per share in Q3 2026 following 8% hike in 2025, reauthorized $20B multi-year share repurchase program without expiration date, and emphasis on disciplined capital allocation."
        },
        {
          "ticker": "MSpE",
          "sentiment": "positive",
          "sentiment_reasoning": "Increased quarterly dividend 15% to $1.15 per share in Q3 2026 following 8% hike in 2025, reauthorized $20B multi-year share repurchase program without expiration date, and emphasis on disciplined capital allocation."
        },
        {
          "ticker": "MSpF",
          "sentiment": "positive",
          "sentiment_reasoning": "Increased quarterly dividend 15% to $1.15 per share in Q3 2026 following 8% hike in 2025, reauthorized $20B multi-year share repurchase program without expiration date, and emphasis on disciplined capital allocation."
        },
        {
          "ticker": "MSpI",
          "sentiment": "positive",
          "sentiment_reasoning": "Increased quarterly dividend 15% to $1.15 per share in Q3 2026 following 8% hike in 2025, reauthorized $20B multi-year share repurchase program without expiration date, and emphasis on disciplined capital allocation."
        },
        {
          "ticker": "MSpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Increased quarterly dividend 15% to $1.15 per share in Q3 2026 following 8% hike in 2025, reauthorized $20B multi-year share repurchase program without expiration date, and emphasis on disciplined capital allocation."
        },
        {
          "ticker": "MSpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Increased quarterly dividend 15% to $1.15 per share in Q3 2026 following 8% hike in 2025, reauthorized $20B multi-year share repurchase program without expiration date, and emphasis on disciplined capital allocation."
        },
        {
          "ticker": "MSpO",
          "sentiment": "positive",
          "sentiment_reasoning": "Increased quarterly dividend 15% to $1.15 per share in Q3 2026 following 8% hike in 2025, reauthorized $20B multi-year share repurchase program without expiration date, and emphasis on disciplined capital allocation."
        },
        {
          "ticker": "MSpP",
          "sentiment": "positive",
          "sentiment_reasoning": "Increased quarterly dividend 15% to $1.15 per share in Q3 2026 following 8% hike in 2025, reauthorized $20B multi-year share repurchase program without expiration date, and emphasis on disciplined capital allocation."
        },
        {
          "ticker": "MSpQ",
          "sentiment": "positive",
          "sentiment_reasoning": "Increased quarterly dividend 15% to $1.15 per share in Q3 2026 following 8% hike in 2025, reauthorized $20B multi-year share repurchase program without expiration date, and emphasis on disciplined capital allocation."
        }
      ]
    },
    {
      "id": "2f9dbd7991fb08e5f497d0a26b7239b9057e1cfc06158f26f4543eefe8ed1d99",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Capital Markets Momentum Fades: What it Means for Big Banks in Q3",
      "author": "Na",
      "published_utc": "2026-09-07T15:08:00Z",
      "article_url": "https://www.zacks.com/stock/news/2986006/capital-markets-momentum-fades-what-it-means-for-big-banks-in-q3?cid=CS-ZC-FT-analyst_blog|industry_focus-2986006",
      "tickers": [
        "GS",
        "GSpA",
        "GSpC",
        "GSpD",
        "MS",
        "MSpA",
        "MSpE",
        "MSpF",
        "MSpI",
        "MSpK",
        "MSpL",
        "MSpO",
        "MSpP",
        "MSpQ",
        "AMJB",
        "JPM",
        "JPMpC",
        "JPMpD",
        "JPMpJ",
        "JPMpK",
        "JPMpL",
        "JPMpM",
        "VYLD",
        "BAC",
        "BACpB",
        "BACpE",
        "BACpK",
        "BACpL",
        "BACpM",
        "BACpN",
        "BACpO",
        "BACpP",
        "BACpQ",
        "BACpS",
        "BMLpG",
        "BMLpH",
        "BMLpJ",
        "BMLpL",
        "MERpK",
        "C",
        "CpN",
        "CpR"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/2e/65031.jpg",
      "description": "U.S. banks enter Q3 2026 with supportive lending conditions but face mixed capital markets trends. Investment banking volumes declined 6% YoY in July due to weak debt markets, though M&A and equity underwriting showed strength. Goldman Sachs and Morgan Stanley face greater sensitivity to capital markets weakness, while diversified banks like JPMorgan, Bank of America, and Citigroup benefit from broader revenue streams including loan and deposit growth.",
      "keywords": [
        "investment banking",
        "capital markets",
        "Q3 2026 earnings",
        "debt capital markets",
        "M&A activity",
        "equity underwriting",
        "trading revenues",
        "loan growth",
        "deposit growth"
      ],
      "insights": [
        {
          "ticker": "GS",
          "sentiment": "negative",
          "sentiment_reasoning": "Most sensitive to weaker capital markets conditions. While benefits from M&A and equity underwriting strength, weakness in debt capital markets could offset gains and moderate investment banking revenue growth."
        },
        {
          "ticker": "GSpA",
          "sentiment": "negative",
          "sentiment_reasoning": "Most sensitive to weaker capital markets conditions. While benefits from M&A and equity underwriting strength, weakness in debt capital markets could offset gains and moderate investment banking revenue growth."
        },
        {
          "ticker": "GSpC",
          "sentiment": "negative",
          "sentiment_reasoning": "Most sensitive to weaker capital markets conditions. While benefits from M&A and equity underwriting strength, weakness in debt capital markets could offset gains and moderate investment banking revenue growth."
        },
        {
          "ticker": "GSpD",
          "sentiment": "negative",
          "sentiment_reasoning": "Most sensitive to weaker capital markets conditions. While benefits from M&A and equity underwriting strength, weakness in debt capital markets could offset gains and moderate investment banking revenue growth."
        },
        {
          "ticker": "MS",
          "sentiment": "neutral",
          "sentiment_reasoning": "Similar capital markets exposure to Goldman Sachs, but Wealth Management franchise provides a more stable revenue base that could cushion softness in investment banking or trading."
        },
        {
          "ticker": "MSpA",
          "sentiment": "neutral",
          "sentiment_reasoning": "Similar capital markets exposure to Goldman Sachs, but Wealth Management franchise provides a more stable revenue base that could cushion softness in investment banking or trading."
        },
        {
          "ticker": "MSpE",
          "sentiment": "neutral",
          "sentiment_reasoning": "Similar capital markets exposure to Goldman Sachs, but Wealth Management franchise provides a more stable revenue base that could cushion softness in investment banking or trading."
        },
        {
          "ticker": "MSpF",
          "sentiment": "neutral",
          "sentiment_reasoning": "Similar capital markets exposure to Goldman Sachs, but Wealth Management franchise provides a more stable revenue base that could cushion softness in investment banking or trading."
        },
        {
          "ticker": "MSpI",
          "sentiment": "neutral",
          "sentiment_reasoning": "Similar capital markets exposure to Goldman Sachs, but Wealth Management franchise provides a more stable revenue base that could cushion softness in investment banking or trading."
        },
        {
          "ticker": "MSpK",
          "sentiment": "neutral",
          "sentiment_reasoning": "Similar capital markets exposure to Goldman Sachs, but Wealth Management franchise provides a more stable revenue base that could cushion softness in investment banking or trading."
        },
        {
          "ticker": "MSpL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Similar capital markets exposure to Goldman Sachs, but Wealth Management franchise provides a more stable revenue base that could cushion softness in investment banking or trading."
        },
        {
          "ticker": "MSpO",
          "sentiment": "neutral",
          "sentiment_reasoning": "Similar capital markets exposure to Goldman Sachs, but Wealth Management franchise provides a more stable revenue base that could cushion softness in investment banking or trading."
        },
        {
          "ticker": "MSpP",
          "sentiment": "neutral",
          "sentiment_reasoning": "Similar capital markets exposure to Goldman Sachs, but Wealth Management franchise provides a more stable revenue base that could cushion softness in investment banking or trading."
        },
        {
          "ticker": "MSpQ",
          "sentiment": "neutral",
          "sentiment_reasoning": "Similar capital markets exposure to Goldman Sachs, but Wealth Management franchise provides a more stable revenue base that could cushion softness in investment banking or trading."
        },
        {
          "ticker": "AMJB",
          "sentiment": "positive",
          "sentiment_reasoning": "Highly diversified business model across consumer/commercial banking, payments, and asset management reduces dependence on capital markets. Strong buffer against underwriting/trading revenue shortfalls with loan and deposit growth support."
        },
        {
          "ticker": "JPM",
          "sentiment": "positive",
          "sentiment_reasoning": "Highly diversified business model across consumer/commercial banking, payments, and asset management reduces dependence on capital markets. Strong buffer against underwriting/trading revenue shortfalls with loan and deposit growth support."
        },
        {
          "ticker": "JPMpC",
          "sentiment": "positive",
          "sentiment_reasoning": "Highly diversified business model across consumer/commercial banking, payments, and asset management reduces dependence on capital markets. Strong buffer against underwriting/trading revenue shortfalls with loan and deposit growth support."
        },
        {
          "ticker": "JPMpD",
          "sentiment": "positive",
          "sentiment_reasoning": "Highly diversified business model across consumer/commercial banking, payments, and asset management reduces dependence on capital markets. Strong buffer against underwriting/trading revenue shortfalls with loan and deposit growth support."
        },
        {
          "ticker": "JPMpJ",
          "sentiment": "positive",
          "sentiment_reasoning": "Highly diversified business model across consumer/commercial banking, payments, and asset management reduces dependence on capital markets. Strong buffer against underwriting/trading revenue shortfalls with loan and deposit growth support."
        },
        {
          "ticker": "JPMpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Highly diversified business model across consumer/commercial banking, payments, and asset management reduces dependence on capital markets. Strong buffer against underwriting/trading revenue shortfalls with loan and deposit growth support."
        },
        {
          "ticker": "JPMpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Highly diversified business model across consumer/commercial banking, payments, and asset management reduces dependence on capital markets. Strong buffer against underwriting/trading revenue shortfalls with loan and deposit growth support."
        },
        {
          "ticker": "JPMpM",
          "sentiment": "positive",
          "sentiment_reasoning": "Highly diversified business model across consumer/commercial banking, payments, and asset management reduces dependence on capital markets. Strong buffer against underwriting/trading revenue shortfalls with loan and deposit growth support."
        },
        {
          "ticker": "VYLD",
          "sentiment": "positive",
          "sentiment_reasoning": "Highly diversified business model across consumer/commercial banking, payments, and asset management reduces dependence on capital markets. Strong buffer against underwriting/trading revenue shortfalls with loan and deposit growth support."
        },
        {
          "ticker": "BAC",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "BACpB",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "BACpE",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "BACpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "BACpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "BACpM",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "BACpN",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "BACpO",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "BACpP",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "BACpQ",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "BACpS",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "BMLpG",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "BMLpH",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "BMLpJ",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "BMLpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "MERpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Large consumer banking and wealth-management franchises provide cushion against weaker capital markets fees. Balanced impact from both investment banking and traditional banking with loan/deposit growth support."
        },
        {
          "ticker": "C",
          "sentiment": "positive",
          "sentiment_reasoning": "Broader earnings mix including Services, Wealth, and U.S. Personal Banking provides balance. Loan and deposit growth momentum could support net interest income and offset capital markets softness."
        },
        {
          "ticker": "CpN",
          "sentiment": "positive",
          "sentiment_reasoning": "Broader earnings mix including Services, Wealth, and U.S. Personal Banking provides balance. Loan and deposit growth momentum could support net interest income and offset capital markets softness."
        },
        {
          "ticker": "CpR",
          "sentiment": "positive",
          "sentiment_reasoning": "Broader earnings mix including Services, Wealth, and U.S. Personal Banking provides balance. Loan and deposit growth momentum could support net interest income and offset capital markets softness."
        }
      ]
    },
    {
      "id": "c56e737222de0b590e6f7589e0aafd603f51254a79f569b6e2a578d90b27b3de",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Warren Buffett's Successor, Greg Abel, Has 63% of Berkshire's $360 Billion Portfolio Concentrated in 5 Superstar Stocks",
      "author": "Sean Williams",
      "published_utc": "2026-09-04T09:06:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/04/warren-buffett-abel-has-63-brka-invest-in-5-stocks/?source=iedfolrf0000001",
      "tickers": [
        "BRK.A",
        "BRK.B",
        "AAPL",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "KO",
        "AXP",
        "BAC",
        "BACpB",
        "BACpE",
        "BACpK",
        "BACpL",
        "BACpM",
        "BACpN",
        "BACpO",
        "BACpP",
        "BACpQ",
        "BACpS",
        "BMLpG",
        "BMLpH",
        "BMLpJ",
        "BMLpL",
        "MERpK"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F885721%2Fbuffett8-tmf.jpg&w=1200&op=resize",
      "description": "Greg Abel, who took over as Berkshire Hathaway's CEO on December 31, maintains Warren Buffett's investment philosophy of concentrating assets in best ideas. As of August 28, 63% ($226 billion) of Berkshire's $360 billion portfolio is concentrated in five stocks. Tech stocks now comprise over 30% of the portfolio, driven by significant positions in Apple and Alphabet. Abel has tripled Berkshire's Alphabet position and added $17 billion in Q2. Meanwhile, Berkshire has been reducing its Bank of America stake for eight consecutive quarters due to valuation concerns.",
      "keywords": [
        "Berkshire Hathaway",
        "Greg Abel",
        "portfolio concentration",
        "technology stocks",
        "investment strategy"
      ],
      "insights": [
        {
          "ticker": "BRK.A",
          "sentiment": "positive",
          "sentiment_reasoning": "Continuation of successful investment philosophy under new leadership with strategic focus on high-conviction positions and tech sector growth opportunities"
        },
        {
          "ticker": "BRK.B",
          "sentiment": "positive",
          "sentiment_reasoning": "Continuation of successful investment philosophy under new leadership with strategic focus on high-conviction positions and tech sector growth opportunities"
        },
        {
          "ticker": "AAPL",
          "sentiment": "positive",
          "sentiment_reasoning": "iPhone sales picking up after multiyear lull, with Apple Intelligence launch signaling renewed growth momentum"
        },
        {
          "ticker": "GOOG",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as splash addition under Abel's leadership with position tripled in Q1 and additional $17 billion added in Q2; Google Cloud showing parabolic growth with AI integration"
        },
        {
          "ticker": "GOOGL",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as splash addition under Abel's leadership with position tripled in Q1 and additional $17 billion added in Q2; Google Cloud showing parabolic growth with AI integration"
        },
        {
          "ticker": "GOOGM",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as splash addition under Abel's leadership with position tripled in Q1 and additional $17 billion added in Q2; Google Cloud showing parabolic growth with AI integration"
        },
        {
          "ticker": "GOOGN",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as splash addition under Abel's leadership with position tripled in Q1 and additional $17 billion added in Q2; Google Cloud showing parabolic growth with AI integration"
        },
        {
          "ticker": "KO",
          "sentiment": "positive",
          "sentiment_reasoning": "Long-term indefinite holding with ultra-low cost basis ($3.25/share) and exceptional 65% yield on cost; global presence benefits from economic growth"
        },
        {
          "ticker": "AXP",
          "sentiment": "positive",
          "sentiment_reasoning": "Long-term indefinite holding with ultra-low cost basis ($8.49/share) and strong 45% yield on cost; benefits from economic expansion as payment facilitator and lender"
        },
        {
          "ticker": "BAC",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "BACpB",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "BACpE",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "BACpK",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "BACpL",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "BACpM",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "BACpN",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "BACpO",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "BACpP",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "BACpQ",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "BACpS",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "BMLpG",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "BMLpH",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "BMLpJ",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "BMLpL",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        },
        {
          "ticker": "MERpK",
          "sentiment": "negative",
          "sentiment_reasoning": "Position reduced for eighth consecutive quarter with 53% stake reduction over two years; valuation concern cited as stock trades at 58% premium to book value versus 62% discount when initially purchased"
        }
      ]
    },
    {
      "id": "49ed898004a9c09905430294ad47c8d89a8b16e9fb1cd561242a9e9ad926334c",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Greg Abel Bought $39.4 Billion of Stocks in 6 Months, Up From the $7.1 Billion Berkshire Purchased a Year Earlier Under Warren Buffett",
      "author": "Neil Patel",
      "published_utc": "2026-09-03T18:15:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/03/greg-abel-stocks-2026-berkshire-warren-buffett/?source=iedfolrf0000001",
      "tickers": [
        "BRK.A",
        "BRK.B",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "BAC",
        "BACpB",
        "BACpE",
        "BACpK",
        "BACpL",
        "BACpM",
        "BACpN",
        "BACpO",
        "BACpP",
        "BACpQ",
        "BACpS",
        "BMLpG",
        "BMLpH",
        "BMLpJ",
        "BMLpL",
        "MERpK",
        "COF",
        "COFpI",
        "COFpJ",
        "COFpK",
        "COFpL",
        "COFpN",
        "KR"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F883054%2Fperson-trading-berkshire-hathaway-stock-on-mobile-app_-getty.jpg&w=1200&op=resize",
      "description": "Berkshire Hathaway shifted to net stock buying in Q2 2026 under CEO Greg Abel, purchasing $39.4 billion in equities during the first half of the year compared to $7.1 billion a year earlier. The company's most notable addition was Alphabet, making it the third-largest portfolio position. Despite a frothy market with elevated valuations, Abel is playing offense while managing $365.5 billion in cash and Treasuries awaiting deployment.",
      "keywords": [
        "Berkshire Hathaway",
        "stock buying",
        "Greg Abel",
        "portfolio allocation",
        "Alphabet investment",
        "net buyer",
        "cash reserves"
      ],
      "insights": [
        {
          "ticker": "BRK.A",
          "sentiment": "positive",
          "sentiment_reasoning": "Shifted from net seller to aggressive net buyer of stocks, purchasing $39.4B in H1 2026 vs $7.1B year-over-year, indicating renewed confidence in equity markets and active capital deployment under new CEO leadership."
        },
        {
          "ticker": "BRK.B",
          "sentiment": "positive",
          "sentiment_reasoning": "Shifted from net seller to aggressive net buyer of stocks, purchasing $39.4B in H1 2026 vs $7.1B year-over-year, indicating renewed confidence in equity markets and active capital deployment under new CEO leadership."
        },
        {
          "ticker": "GOOG",
          "sentiment": "positive",
          "sentiment_reasoning": "Became Berkshire's third-largest portfolio position through significant purchases in H1 2026, demonstrating CEO Abel's bullishness on the company's AI positioning and competitive advantages."
        },
        {
          "ticker": "GOOGL",
          "sentiment": "positive",
          "sentiment_reasoning": "Became Berkshire's third-largest portfolio position through significant purchases in H1 2026, demonstrating CEO Abel's bullishness on the company's AI positioning and competitive advantages."
        },
        {
          "ticker": "GOOGM",
          "sentiment": "positive",
          "sentiment_reasoning": "Became Berkshire's third-largest portfolio position through significant purchases in H1 2026, demonstrating CEO Abel's bullishness on the company's AI positioning and competitive advantages."
        },
        {
          "ticker": "GOOGN",
          "sentiment": "positive",
          "sentiment_reasoning": "Became Berkshire's third-largest portfolio position through significant purchases in H1 2026, demonstrating CEO Abel's bullishness on the company's AI positioning and competitive advantages."
        },
        {
          "ticker": "BAC",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "BACpB",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "BACpE",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "BACpK",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "BACpL",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "BACpM",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "BACpN",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "BACpO",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "BACpP",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "BACpQ",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "BACpS",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "BMLpG",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "BMLpH",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "BMLpJ",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "BMLpL",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "MERpK",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire trimmed its position in the bank during H1 2026, indicating reduced conviction or reallocation of capital away from the financial sector."
        },
        {
          "ticker": "COF",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire reduced share ownership in the company during H1 2026, suggesting decreased confidence in the financial services firm."
        },
        {
          "ticker": "COFpI",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire reduced share ownership in the company during H1 2026, suggesting decreased confidence in the financial services firm."
        },
        {
          "ticker": "COFpJ",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire reduced share ownership in the company during H1 2026, suggesting decreased confidence in the financial services firm."
        },
        {
          "ticker": "COFpK",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire reduced share ownership in the company during H1 2026, suggesting decreased confidence in the financial services firm."
        },
        {
          "ticker": "COFpL",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire reduced share ownership in the company during H1 2026, suggesting decreased confidence in the financial services firm."
        },
        {
          "ticker": "COFpN",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire reduced share ownership in the company during H1 2026, suggesting decreased confidence in the financial services firm."
        },
        {
          "ticker": "KR",
          "sentiment": "negative",
          "sentiment_reasoning": "Berkshire reduced its stake in the grocery retailer during H1 2026, indicating a shift away from this consumer staples position."
        }
      ]
    },
    {
      "id": "bc9c286791bc4017d720fc865c8f3b23a46d6441a0367687f61713449b3fd6e4",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Major Banks Make a Move Into Stablecoins: What Should Investors Watch?",
      "author": "Zacks.Com",
      "published_utc": "2026-09-02T14:14:00Z",
      "article_url": "https://www.zacks.com/stock/news/2983832/major-banks-make-a-move-into-stablecoins-what-should-investors-watch?cid=CS-ZC-FT-analyst_blog|industry_focus-2983832",
      "tickers": [
        "C",
        "CpN",
        "CpR",
        "BAC",
        "BACpB",
        "BACpE",
        "BACpK",
        "BACpL",
        "BACpM",
        "BACpN",
        "BACpO",
        "BACpP",
        "BACpQ",
        "BACpS",
        "BMLpG",
        "BMLpH",
        "BMLpJ",
        "BMLpL",
        "MERpK",
        "GS",
        "GSpA",
        "GSpC",
        "GSpD",
        "WFC",
        "WFCpA",
        "WFCpC",
        "WFCpD",
        "WFCpL",
        "WFCpY",
        "WFCpZ",
        "CRCL"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/a7/148399.webp",
      "description": "A consortium of 21 major global banks including Citigroup, Bank of America, Goldman Sachs, and Wells Fargo plans to launch a U.S. dollar-denominated stablecoin in the first half of 2027, enabled by the new GENIUS Act regulatory framework. While this represents a long-term strategic opportunity for the participating banks, it poses a competitive threat to Circle Internet Group's USDC stablecoin, which currently dominates the market with $73.3B in circulation.",
      "keywords": [
        "stablecoins",
        "digital payments",
        "blockchain",
        "GENIUS Act",
        "regulatory framework",
        "USDC",
        "cryptocurrency",
        "financial institutions"
      ],
      "insights": [
        {
          "ticker": "C",
          "sentiment": "positive",
          "sentiment_reasoning": "Long-term strategic opportunity to leverage global transaction-banking and cross-border payment capabilities as blockchain-based settlement expands among corporations and financial institutions."
        },
        {
          "ticker": "CpN",
          "sentiment": "positive",
          "sentiment_reasoning": "Long-term strategic opportunity to leverage global transaction-banking and cross-border payment capabilities as blockchain-based settlement expands among corporations and financial institutions."
        },
        {
          "ticker": "CpR",
          "sentiment": "positive",
          "sentiment_reasoning": "Long-term strategic opportunity to leverage global transaction-banking and cross-border payment capabilities as blockchain-based settlement expands among corporations and financial institutions."
        },
        {
          "ticker": "BAC",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "BACpB",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "BACpE",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "BACpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "BACpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "BACpM",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "BACpN",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "BACpO",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "BACpP",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "BACpQ",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "BACpS",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "BMLpG",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "BMLpH",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "BMLpJ",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "BMLpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "MERpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Can deepen payment and treasury relationships with commercial and corporate clients as they adopt tokenized forms of money through the stablecoin initiative."
        },
        {
          "ticker": "GS",
          "sentiment": "positive",
          "sentiment_reasoning": "Positioned to benefit from greater institutional adoption of tokenized assets and blockchain-based settlement, particularly in capital markets integration."
        },
        {
          "ticker": "GSpA",
          "sentiment": "positive",
          "sentiment_reasoning": "Positioned to benefit from greater institutional adoption of tokenized assets and blockchain-based settlement, particularly in capital markets integration."
        },
        {
          "ticker": "GSpC",
          "sentiment": "positive",
          "sentiment_reasoning": "Positioned to benefit from greater institutional adoption of tokenized assets and blockchain-based settlement, particularly in capital markets integration."
        },
        {
          "ticker": "GSpD",
          "sentiment": "positive",
          "sentiment_reasoning": "Positioned to benefit from greater institutional adoption of tokenized assets and blockchain-based settlement, particularly in capital markets integration."
        },
        {
          "ticker": "WFC",
          "sentiment": "positive",
          "sentiment_reasoning": "Can enhance treasury management and payment offerings for corporate customers through stablecoin infrastructure."
        },
        {
          "ticker": "WFCpA",
          "sentiment": "positive",
          "sentiment_reasoning": "Can enhance treasury management and payment offerings for corporate customers through stablecoin infrastructure."
        },
        {
          "ticker": "WFCpC",
          "sentiment": "positive",
          "sentiment_reasoning": "Can enhance treasury management and payment offerings for corporate customers through stablecoin infrastructure."
        },
        {
          "ticker": "WFCpD",
          "sentiment": "positive",
          "sentiment_reasoning": "Can enhance treasury management and payment offerings for corporate customers through stablecoin infrastructure."
        },
        {
          "ticker": "WFCpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Can enhance treasury management and payment offerings for corporate customers through stablecoin infrastructure."
        },
        {
          "ticker": "WFCpY",
          "sentiment": "positive",
          "sentiment_reasoning": "Can enhance treasury management and payment offerings for corporate customers through stablecoin infrastructure."
        },
        {
          "ticker": "WFCpZ",
          "sentiment": "positive",
          "sentiment_reasoning": "Can enhance treasury management and payment offerings for corporate customers through stablecoin infrastructure."
        },
        {
          "ticker": "CRCL",
          "sentiment": "negative",
          "sentiment_reasoning": "Faces credible competitive risk to its USDC stablecoin from a bank-backed alternative with strong regulatory standing and distribution networks, potentially pressuring market share and reserve income which comprises 95% of revenues."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 30.97334,
    "13WeekPriceReturnDaily": 15.7098,
    "26WeekPriceReturnDaily": 25.4353,
    "3MonthADReturnStd": 18.81254,
    "3MonthAverageTradingVolume": 33.80886,
    "52WeekHigh": 65.225,
    "52WeekHighDate": "2026-08-17",
    "52WeekLow": 46.12,
    "52WeekLowDate": "2026-03-19",
    "52WeekPriceReturnDaily": 25.9393,
    "5DayPriceReturnDaily": 1.1947,
    "beta": 1.1966906,
    "bookValuePerShareAnnual": 42.0443,
    "bookValuePerShareQuarterly": 42.9033,
    "bookValueShareGrowth5Y": 5.91,
    "capexCagr5Y": null,
    "cashFlowPerShareAnnual": 1.7488,
    "cashFlowPerShareQuarterly": 13.4999,
    "cashFlowPerShareTTM": 3.81224,
    "cashPerSharePerShareAnnual": 28.78697,
    "cashPerSharePerShareQuarterly": 44.39103,
    "currentDividendYieldTTM": 2.2284,
    "currentEv/freeCashFlowAnnual": 92.7904,
    "currentEv/freeCashFlowTTM": 12.3532,
    "dividendGrowthRate5Y": 7.86,
    "dividendIndicatedAnnual": 1.28,
    "dividendPerShareAnnual": 1.2903,
    "dividendPerShareTTM": 1.3514,
    "dividendYieldIndicatedAnnual": 3.22906,
    "ebitdPerShareTTM": 9.51473,
    "ebitdaCagr5Y": 3.48988,
    "ebitdaInterimCagr5Y": 10.41612,
    "enterpriseValue": 1170365.5,
    "epsAnnual": 3.9721,
    "epsBasicExclExtraItemsAnnual": 3.9721,
    "epsBasicExclExtraItemsTTM": 4.5089,
    "epsExclExtraItemsAnnual": 3.9721,
    "epsExclExtraItemsTTM": 4.5089,
    "epsGrowth3Y": 5.63,
    "epsGrowth5Y": 14.32,
    "epsGrowthQuarterlyYoy": 33.76,
    "epsGrowthTTMYoy": 25.82,
    "epsInclExtraItemsAnnual": 3.9721,
    "epsInclExtraItemsTTM": 4.5089,
    "epsNormalizedAnnual": 3.9721,
    "epsTTM": 4.5089,
    "focfCagr5Y": -19.79,
    "forwardPE": 13.5005698110631,
    "longTermDebt/equityAnnual": 0.9103,
    "longTermDebt/equityQuarterly": 1.1288,
    "marketCapitalization": 438305.5,
    "monthToDatePriceReturnDaily": 1.1947,
    "netIncomeEmployeeAnnual": 0.1439,
    "netIncomeEmployeeTTM": 0.1588,
    "netMarginGrowth5Y": 4.58749,
    "netProfitMargin5Y": 29.42913,
    "netProfitMarginAnnual": 28.9921,
    "netProfitMarginTTM": 30.15501,
    "operatingMargin5Y": 33.47932,
    "operatingMarginAnnual": 32.61611,
    "operatingMarginTTM": 32.73721,
    "payoutRatioAnnual": 31.34,
    "payoutRatioTTM": 29.02,
    "pb": 1.4557,
    "pbAnnual": 1.3245,
    "pbQuarterly": 1.3281,
    "pcfShareAnnual": 34.7503,
    "pcfShareTTM": 4.6263,
    "peAnnual": 14.3664,
    "peBasicExclExtraTTM": 13.0235,
    "peExclExtraAnnual": 9.33382,
    "peExclExtraTTM": 13.0235,
    "peInclExtraTTM": 13.0235,
    "peNormalizedAnnual": 14.3664,
    "peTTM": 13.0235,
    "pegTTM": 0.9209,
    "pfcfShareAnnual": 34.7503,
    "pfcfShareTTM": 3.7243,
    "pretaxMargin5Y": 33.47932,
    "pretaxMarginAnnual": 32.61611,
    "pretaxMarginTTM": 32.73721,
    "priceRelativeToS&P50013Week": 13.9795,
    "priceRelativeToS&P50026Week": 12.227,
    "priceRelativeToS&P5004Week": -1.4804,
    "priceRelativeToS&P50052Week": 6.9433,
    "priceRelativeToS&P500Ytd": 1.0193,
    "psAnnual": 2.48091,
    "psTTM": 2.32875,
    "ptbvAnnual": 1.3324,
    "ptbvQuarterly": 1.163,
    "revenueEmployeeAnnual": 446823.5,
    "revenueGrowth3Y": 0.61805,
    "revenueGrowth5Y": 4.73519,
    "revenueGrowthQuarterlyYoy": 71.36741,
    "revenueGrowthTTMYoy": 99.36713,
    "revenuePerShareAnnual": 11.62534,
    "revenuePerShareTTM": 12.45394,
    "revenueShareGrowth5Y": 7.53813,
    "roa5Y": 0.89,
    "roaRfy": 0.89,
    "roaTTM": 0.97,
    "roe5Y": 10.04,
    "roeRfy": 10.059999999999999,
    "roeTTM": 11.129999999999999,
    "roi5Y": 3.3,
    "roiAnnual": 3.02,
    "roiTTM": 3.3000000000000003,
    "tangibleBookValuePerShareAnnual": 41.7947,
    "tangibleBookValuePerShareQuarterly": 41.9175,
    "tbvCagr5Y": 2.13,
    "totalDebt/totalEquityAnnual": 2.3296,
    "totalDebt/totalEquityQuarterly": 2.4313,
    "yearToDatePriceReturnDaily": 13.9636
  },
  "source_status": {
    "local_research": true,
    "local_news": true,
    "local_sec_filings": true,
    "finnhub_news": true,
    "polygon_news": true,
    "earnings": false,
    "fundamentals": true
  }
}
```

## AMZN
Trading candidate:
```json
{
  "symbol": "AMZN",
  "score": 51.78,
  "direction": "LONG",
  "sector": "Consumer Discretionary",
  "components": {
    "market": 100.0,
    "sector": 53.67,
    "relative_strength": 25.56105999703835,
    "vwap": 100.0,
    "trend": 0.0,
    "volume": 36.23578589946771,
    "momentum": 51.807562250230525,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 100.0
  }
}
```
Evidence packet (source-labelled; missing sources must remain uncertain):
```json
{
  "local_research": [
    "[AMZN.md]\n# AMZN \u2014 Amazon.com, Inc.\n\n## Overview\nAmazon is a global technology and commerce platform spanning online marketplace, first-party retail, logistics, advertising, subscriptions, devices/media, and Amazon Web Services (AWS). The investment case is increasingly driven by AWS, high-margin advertising, fulfillment efficiency, and AI infrastructure/software adoption.\n\n## Sector / Industry\n- Sector: Consumer Discretionary / Communication Services / Information Technology exposure\n- Industry: Internet & Direct Marketing Retail; Cloud Infrastructure; Digital Advertising\n\n## Recent Developments / News / Earnings / Analyst / SEC / Product Notes\n- SEC EDGAR shows recent Amazon filings in July 2026, including 8-K current reports and prospectus/free-writing-prospectus filings tied to securities activity.\n- Public news flow continues to focus on AI/cloud capex, AWS competitive positioning, retail margin expansion, advertising growth, and the balance between investment spending and free cash flow.\n- Product/business themes: AWS generative-AI services, custom silicon, marketplace/Prime ecosystem, retail logistics automation, and expanding ad inventory across commerce and video.\n- Source blocker: Amazon IR earnings page was blocked by Cloudflare/403 via web_fetch, so this summary relies on SEC availability plus accessible public-news context rather than direct IR release text.\n\n## Bull Thesis\n- AWS remains a scaled, high-margin cloud platform with a long runway from AI workloads, enterprise migration, and proprietary chips/services.\n- Advertising is a structurally attractive, high-margin growth business embedded at the point of purchase.\n- Retail margins can keep improving as regionalized fulfillment, automation, and delivery density reduce cost-to-serve.\n- Prime, marketplace sellers, logistics, and media create a reinforcing ecosystem that is difficult to replicate.\n\n## Bear Thesis\n- AI and cloud infrastructure spending may pressure near-term free cash flow if returns lag expectations.\n- AWS faces intense competition from Microsoft Azure, Google Cloud, and specialized AI infrastructure providers.\n- Retail remains operationally complex and exposed to consumer demand, wage inflation, and regulatory scrutiny.\n- Valuation can compress if revenue growth decelerates or investors question the payback on capex.\n\n## Risks\nRegulatory/antitrust actions, cloud price competition, execution risk in AI infrastructure, margin pressure from logistics and wages, cybersecurity incidents, labor disputes, and macro-driven consumer slowdown.\n\n## Catalysts\nAWS acceleration, evidence of AI monetization, advertising growth, retail operating-margin expansion, stronger free cash flow, shareholder returns, and favorable outcomes in regulatory matters.\n\n## Long-Term Outlook\nAmazon remains a high-quality compounder if AWS and advertising continue to scale while retail efficiency improves. The key long-term debate is whether AI capex becomes a durable moat and profit pool or a lower-return arms race.\n\n## Conviction Rating\nHigh \u2014 strong multi-engine growth platform, though capex intensity and regulatory risk keep position sizing discipline important.\n"
  ],
  "local_news": [],
  "local_sec_filings": [],
  "finnhub_news": [
    {
      "category": "company",
      "datetime": 1788798000,
      "headline": "Jabil Rises 36.2% Year to Date: Should You Buy the Stock?",
      "id": 141765020,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AMZN",
      "source": "Yahoo",
      "summary": "JBL's AI infrastructure growth and diversified portfolio are fueling gains, but supply chain risks and customer concentration remain key concerns.",
      "url": "https://finnhub.io/api/news?id=44dddb55bb0d7ed25552d7253c8bf8e890e65c33b8405b205c6779707d7fd853"
    },
    {
      "category": "company",
      "datetime": 1788796653,
      "headline": "Bernie Sanders Wants to Ban Superintelligence. What It Means for Microsoft and Amazon",
      "id": 141765118,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AMZN",
      "source": "Yahoo",
      "summary": "Senator Bernie Sanders and Representative Greg Casar announced forthcoming legislation on September 3 that would permanently ban artificial superintelligence and temporarily pause advanced AI development until a federal regulator sets safety rules. The proposal would also direct the United States to pursue international agreements and establish penalties for violations. Microsoft Corporation (NASDAQ:MSFT) and Amazon.com, Inc. [\u2026]",
      "url": "https://finnhub.io/api/news?id=0c382cbcde9ba4178268a50dcc2b63d7dbc8013a1e3fd61d2e9e43c49ce4ea8e"
    },
    {
      "category": "company",
      "datetime": 1788794119,
      "headline": "Microsoft Stock Is Building a Trillion-Dollar AI Opportunity. Is $600 Next?",
      "id": 141765119,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AMZN",
      "source": "Yahoo",
      "summary": "Azure just crossed a revenue milestone that caught Wall Street off guard, and Microsoft's backlog tells a story the headline numbers barely hint at. Whether the stock can push toward $600 depends on one number that most investors are not watching closely enough.",
      "url": "https://finnhub.io/api/news?id=cb0691a9cce468da03f653426f3bea8ca9143c1dd284f0365fe1f7bfe52756fc"
    },
    {
      "category": "company",
      "datetime": 1788792776,
      "headline": "The S&P 100 ETF Just Dumped Nike and Colgate for 4 AI Stocks. Here\u2019s What That Means for Your Portfolio",
      "id": 141763616,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AMZN",
      "source": "Yahoo",
      "summary": "The iShares S&P 100 ETF just swapped out a toothpaste giant and a mall REIT for four AI infrastructure plays, and the move reveals something uncomfortable about what this so-called blue-chip fund has quietly become.",
      "url": "https://finnhub.io/api/news?id=42fbcd571f4e0ff319ea17c0fe94bd2d9085859a6a211459ff345ebc0a878b0d"
    },
    {
      "category": "company",
      "datetime": 1788792005,
      "headline": "Are Retail-Wholesale Stocks Lagging  Amazon.com (AMZN) This Year?",
      "id": 141763773,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AMZN",
      "source": "Yahoo",
      "summary": "Here is how Amazon (AMZN) and BJ's Restaurants (BJRI) have performed compared to their sector so far this year.",
      "url": "https://finnhub.io/api/news?id=645bc31ee7bf59b926ae27a3fab502e63dfbde1d7da2e2829960510937f98c2a"
    }
  ],
  "polygon_news": [
    {
      "id": "78850692ca8aa44969c6a542b1a6e7efabb5f9073aee93c04bce9863318d7784",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Chewy vs. Uber Technologies: Which Consumer Stock Is a Better Buy in 2026?",
      "author": "Brendan Coffey",
      "published_utc": "2026-09-07T16:25:01Z",
      "article_url": "https://www.fool.com/coverage/better-buy/2026/09/07/chewy-vs-uber-technologies-which-consumer-stock-is-a-better-buy-in-2026/?source=iedfolrf0000001",
      "tickers": [
        "CHWY",
        "UBER",
        "AMZN",
        "LYFT",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F0c505d84cb72f436b60eccbf9455c368770fd2e7-1200x800.png%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "The article compares Chewy and Uber Technologies as investment options for 2026. Chewy, a pet e-commerce leader with 21.3 million customers, shows steady 6% revenue growth and expanding veterinary services but faces intense competition and narrow margins. Uber, with $52 billion in revenue and strong profitability, dominates global mobility and delivery but faces regulatory risks regarding driver classification. The author recommends Uber for long-term investors due to its stronger competitive moat and profitability, despite Chewy's promising growth trajectory in pet health services.",
      "keywords": [
        "pet e-commerce",
        "ride-sharing",
        "delivery services",
        "subscription revenue",
        "veterinary services",
        "platform business model",
        "profitability",
        "competitive moat",
        "regulatory risk",
        "free cash flow"
      ],
      "insights": [
        {
          "ticker": "CHWY",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong market position with 21.3 million active customers, predictable recurring revenue from Autoship subscriptions, expanding high-margin veterinary services, and expected 50% net income growth in 2026. However, faces competitive pressures and narrow margins."
        },
        {
          "ticker": "UBER",
          "sentiment": "positive",
          "sentiment_reasoning": "Demonstrates robust profitability with 19% net margin, strong free cash flow of $9.8 billion, 18% revenue growth, and a dominant global platform across mobility and delivery. Author's recommended pick due to stronger competitive moat, though faces regulatory risks regarding driver classification."
        },
        {
          "ticker": "AMZN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive threat to Chewy in online retail and pet supplies, but not analyzed as an investment option in this article."
        },
        {
          "ticker": "LYFT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Identified as a competitor to Uber in ride-sharing, engaging in aggressive pricing strategies, but not evaluated as an investment option."
        },
        {
          "ticker": "GOOG",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a strategic dependency for Uber's mapping services, representing a potential risk, but not analyzed as an investment option."
        },
        {
          "ticker": "GOOGL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a strategic dependency for Uber's mapping services, representing a potential risk, but not analyzed as an investment option."
        },
        {
          "ticker": "GOOGM",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a strategic dependency for Uber's mapping services, representing a potential risk, but not analyzed as an investment option."
        },
        {
          "ticker": "GOOGN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a strategic dependency for Uber's mapping services, representing a potential risk, but not analyzed as an investment option."
        }
      ]
    },
    {
      "id": "7d6bed2e75bdf028ec921b762c205aaaabd63ea4d50a226a5a6fdcc2c1e8df59",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Why Does Amazon Trade at a Discount to Walmart and Costco? Here's the Only Answer That Makes Sense.",
      "author": "James Brumley",
      "published_utc": "2026-09-07T16:22:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/07/why-does-amazon-trade-at-a-discount-to-walmart-and/?source=iedfolrf0000001",
      "tickers": [
        "AMZN",
        "WMT",
        "COST"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F885115%2Ffinancial-analysis-company-filing-business-papers.jpg&w=1200&op=resize",
      "description": "Amazon trades at a P/E multiple of ~20x compared to Walmart (37x) and Costco (44x) due to investor concerns over its massive $220 billion AI infrastructure spending. While the reasoning is sound, Walmart and Costco valuations may have become excessive as defensive plays. The author suggests investors may be overreacting to AI risks and recommends looking elsewhere.",
      "keywords": [
        "valuation",
        "price-to-earnings ratio",
        "artificial intelligence",
        "capital expenditures",
        "defensive stocks",
        "cloud computing"
      ],
      "insights": [
        {
          "ticker": "AMZN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Amazon's lower valuation is justified by significant AI infrastructure spending ($220B), but the author suggests this concern may be overblown and the discount could present opportunity. The company's long-term AI investments should eventually generate returns."
        },
        {
          "ticker": "WMT",
          "sentiment": "negative",
          "sentiment_reasoning": "Trading at 37x earnings as a defensive play against AI risks, but the author argues this valuation has become excessive and unjustified. High P/E multiples offer no guarantee of protection in a market correction."
        },
        {
          "ticker": "COST",
          "sentiment": "negative",
          "sentiment_reasoning": "Trading at 44x earnings as a defensive holding, but the author contends this valuation far exceeds its worth as a defensive stock. The premium pricing leaves it vulnerable if the broader market faces headwinds."
        }
      ]
    },
    {
      "id": "e7a5a37b215fd8be0adb914a2d708db0ce4434c6a393ed2e9ed2649d7ac65798",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Is MercadoLibre Becoming Latin America's Leading Fintech?",
      "author": "Na",
      "published_utc": "2026-09-07T12:41:00Z",
      "article_url": "https://www.zacks.com/stock/news/2985620/is-mercadolibre-becoming-latin-america-s-leading-fintech?cid=CS-ZC-FT-analyst_blog|quick_take-2985620",
      "tickers": [
        "MELI",
        "AMZN",
        "SE"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/ea/308.jpg",
      "description": "MercadoLibre's fintech segment Mercado Pago demonstrated strong growth in Q2 2026, with monthly active users surging 30% to 88 million, AUM jumping 68% to $23.2 billion, and total payment volume reaching $101 billion. The credit portfolio expanded 75% to $16.4 billion with stable asset quality. However, MELI stock trades at a premium valuation (P/E of 39.01) compared to industry peers, and recent earnings estimates have declined.",
      "keywords": [
        "fintech",
        "Latin America",
        "payment volume",
        "credit expansion",
        "user growth",
        "valuation premium",
        "earnings decline"
      ],
      "insights": [
        {
          "ticker": "MELI",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong operational metrics including 30% user growth, 68% AUM growth, 56% payment volume increase, and stable asset quality demonstrate robust business expansion and market leadership in Latin America's fintech sector."
        },
        {
          "ticker": "AMZN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitor with modest share gains (5.4% over three months) and lower valuation multiples (P/E 22.76) compared to MELI, indicating stable but less dynamic performance."
        },
        {
          "ticker": "SE",
          "sentiment": "neutral",
          "sentiment_reasoning": "Cited as a competitor with stronger recent share performance (32.6% gain) but similar valuation metrics (P/E 22.82) to Amazon, suggesting competitive positioning without clear advantage over MELI operationally."
        }
      ]
    },
    {
      "id": "7579d3032a6c7f0c199feeadbd34b818058dbf11185716c63a99ef5bfc82c7f6",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "The Stock Market Has Not Been This Expensive Since the Dot-com Bubble's Peak. History Says to Prepare for What Might Come Next.",
      "author": "Brett Schafer",
      "published_utc": "2026-09-07T11:30:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/07/the-stock-market-has-not-been-this-expensive-since/?source=iedfolrf0000001",
      "tickers": [
        "AMZN",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "MSFT"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F885711%2Fai-6.jpg&w=1200&op=resize",
      "description": "The S&P 500's Shiller CAPE ratio has reached its highest level since the dot-com bubble peak, driven by unsustainable AI-related earnings gains and massive capital expenditures. While super-intelligent AI could justify current valuations, the market faces significant downside risk. Investors should maintain diversified portfolios rather than betting heavily on either scenario.",
      "keywords": [
        "Shiller CAPE ratio",
        "stock market valuation",
        "AI bubble",
        "dot-com bubble comparison",
        "earnings growth",
        "free cash flow",
        "market risk",
        "diversification"
      ],
      "insights": [
        {
          "ticker": "AMZN",
          "sentiment": "negative",
          "sentiment_reasoning": "Company is spending at torrid rates on capital expenditures and is close to generating zero free cash flow, indicating unsustainable spending patterns that could pressure future profitability."
        },
        {
          "ticker": "GOOG",
          "sentiment": "negative",
          "sentiment_reasoning": "Similar to Amazon, Alphabet is approaching zero free cash flow generation due to high capital expenditure rates, raising concerns about long-term value creation."
        },
        {
          "ticker": "GOOGL",
          "sentiment": "negative",
          "sentiment_reasoning": "Similar to Amazon, Alphabet is approaching zero free cash flow generation due to high capital expenditure rates, raising concerns about long-term value creation."
        },
        {
          "ticker": "GOOGM",
          "sentiment": "negative",
          "sentiment_reasoning": "Similar to Amazon, Alphabet is approaching zero free cash flow generation due to high capital expenditure rates, raising concerns about long-term value creation."
        },
        {
          "ticker": "GOOGN",
          "sentiment": "negative",
          "sentiment_reasoning": "Similar to Amazon, Alphabet is approaching zero free cash flow generation due to high capital expenditure rates, raising concerns about long-term value creation."
        },
        {
          "ticker": "MSFT",
          "sentiment": "negative",
          "sentiment_reasoning": "Microsoft faces the same issue as Amazon and Alphabet, with capital expenditures threatening free cash flow generation and creating precariousness in the current bull market."
        }
      ]
    },
    {
      "id": "380f93feb7ad8ce6421db30a235183a44317930c1a52449f45eb322da4e26dd2",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Nuclear Stock Face-Off: Is Constellation Energy or Vistra the Better Buy Right Now?",
      "author": "Manali Pradhan, Cfa",
      "published_utc": "2026-09-07T02:02:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/06/nuclear-stock-face-off-is-stock-or-stock-the-bette/?source=iedfolrf0000001",
      "tickers": [
        "CEG",
        "VST",
        "MSFT",
        "META",
        "AMZN"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F885440%2Fprofessionals_discussing_in_a_meeting.jpg&w=1200&op=resize",
      "description": "Constellation Energy operates the largest U.S. nuclear portfolio with over 22 GW capacity and has signed major 20-year power agreements with Microsoft and Meta. Vistra has a smaller 6.4 GW nuclear portfolio but has secured substantial long-term contracts with Meta and AWS. While Constellation deserves a premium valuation, Vistra offers a stronger risk-reward proposition at 14.4x forward earnings compared to Constellation's 22.4x, combined with aggressive share buybacks and additional growth catalysts.",
      "keywords": [
        "nuclear energy",
        "power generation",
        "data center demand",
        "long-term contracts",
        "valuation comparison",
        "earnings growth",
        "technology partnerships"
      ],
      "insights": [
        {
          "ticker": "CEG",
          "sentiment": "positive",
          "sentiment_reasoning": "Largest U.S. nuclear portfolio with 22+ GW capacity, secured major 20-year agreements with Microsoft (835 MW) and Meta (1,121 MW), and expects base EPS to grow 20%+ annually through 2029. However, premium valuation at 22.4x forward earnings limits upside."
        },
        {
          "ticker": "VST",
          "sentiment": "positive",
          "sentiment_reasoning": "Secured substantial long-term contracts with Meta (2,609 MW) and AWS (1,200 MW), expects 2027 adjusted EBITDA of $7.4-7.8 billion, reduced share count by 30% since 2021 to boost EPS, and trades at attractive 14.4x forward earnings. Offers stronger risk-reward proposition despite smaller nuclear portfolio."
        },
        {
          "ticker": "MSFT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a major customer signing 20-year power agreement with Constellation Energy for data center operations, but article focuses on nuclear energy companies rather than Microsoft's business implications."
        },
        {
          "ticker": "META",
          "sentiment": "neutral",
          "sentiment_reasoning": "Signed significant long-term power agreements with both Constellation Energy (1,121 MW) and Vistra (2,609 MW) for data center needs, but article focuses on nuclear energy companies' perspectives rather than Meta's operations."
        },
        {
          "ticker": "AMZN",
          "sentiment": "neutral",
          "sentiment_reasoning": "AWS signed 20-year agreement with Vistra for up to 1,200 MW of power, but article focuses on nuclear energy companies rather than Amazon's business implications."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 32.00686,
    "13WeekPriceReturnDaily": 1.8598,
    "26WeekPriceReturnDaily": 23.849,
    "3MonthADReturnStd": 43.733322,
    "3MonthAverageTradingVolume": 46.83426,
    "52WeekHigh": 287.2,
    "52WeekHighDate": "2026-08-03",
    "52WeekLow": 196,
    "52WeekLowDate": "2026-02-17",
    "52WeekPriceReturnDaily": 11.2685,
    "5DayPriceReturnDaily": -0.485,
    "assetTurnoverAnnual": 0.8764,
    "assetTurnoverTTM": 0.872,
    "beta": 1.5024469,
    "bookValuePerShareAnnual": 38.3063,
    "bookValuePerShareQuarterly": 51.1564,
    "bookValueShareGrowth5Y": 32.77,
    "capexCagr5Y": 26.85,
    "cashFlowPerShareAnnual": 0.7171,
    "cashFlowPerShareQuarterly": -1.0781,
    "cashFlowPerShareTTM": 6.54859,
    "cashPerSharePerShareAnnual": 11.4648,
    "cashPerSharePerShareQuarterly": 11.4057,
    "currentDividendYieldTTM": null,
    "currentEv/freeCashFlowAnnual": 372.381,
    "currentEv/freeCashFlowTTM": 115.2247,
    "currentRatioAnnual": 1.0508,
    "currentRatioQuarterly": 1.0331,
    "dividendIndicatedAnnual": 0,
    "dividendPerShareTTM": null,
    "ebitdPerShareAnnual": 7.4621,
    "ebitdPerShareTTM": 15.5375,
    "ebitdaCagr5Y": 28.12,
    "ebitdaInterimCagr5Y": 24.69,
    "enterpriseValue": 2865472,
    "epsAnnual": 7.1737,
    "epsBasicExclExtraItemsAnnual": 7.1737,
    "epsBasicExclExtraItemsTTM": 12.4325,
    "epsExclExtraItemsAnnual": 7.1737,
    "epsExclExtraItemsTTM": 12.4325,
    "epsGrowth3Y": null,
    "epsGrowth5Y": 27.96,
    "epsGrowthQuarterlyYoy": 241.83,
    "epsGrowthTTMYoy": 89.71,
    "epsInclExtraItemsAnnual": 7.1737,
    "epsInclExtraItemsTTM": 12.4325,
    "epsNormalizedAnnual": 7.1737,
    "epsTTM": 12.4325,
    "evEbitdaTTM": 16.9643,
    "evRevenueTTM": 3.6941,
    "focfCagr5Y": -21.57,
    "forwardPE": 24.69711,
    "forwardPEG": 1.20181,
    "grossMargin5Y": 46.39,
    "grossMarginAnnual": 50.29,
    "grossMarginTTM": 50.77,
    "inventoryTurnoverAnnual": 9.8268,
    "inventoryTurnoverTTM": 9.6665,
    "longTermDebt/equityAnnual": 0.1597,
    "longTermDebt/equityQuarterly": 0.2337,
    "marketCapitalization": 2788370,
    "monthToDatePriceReturnDaily": -0.485,
    "netIncomeEmployeeAnnual": 0.0493,
    "netIncomeEmployeeTTM": 0.0859,
    "netInterestCoverageAnnual": 8.033,
    "netInterestCoverageTTM": 0.6192,
    "netMarginGrowth5Y": 14.39,
    "netProfitMargin5Y": 6.4,
    "netProfitMarginAnnual": 10.83,
    "netProfitMarginTTM": 17.44,
    "operatingMargin5Y": 7.2,
    "operatingMarginAnnual": 11.16,
    "operatingMarginTTM": 12.08,
    "payoutRatioTTM": null,
    "pb": 5.0549,
    "pbAnnual": 6.0027,
    "pbQuarterly": 4.6479,
    "pcfShareAnnual": 19.9863,
    "pcfShareTTM": 17.2758,
    "peAnnual": 35.9002,
    "peBasicExclExtraTTM": 20.6117,
    "peExclExtraTTM": 20.6117,
    "peInclExtraTTM": 20.6117,
    "peNormalizedAnnual": 35.9002,
    "peTTM": 20.6117,
    "pegTTM": 1.36953,
    "pfcfShareAnnual": 362.3613,
    "pfcfShareTTM": 177.6145,
    "pretaxMargin5Y": 7.57,
    "pretaxMarginAnnual": 13.57,
    "pretaxMarginTTM": 22.62,
    "priceRelativeToS&P50013Week": 0.1295,
    "priceRelativeToS&P50026Week": 10.6407,
    "priceRelativeToS&P5004Week": -6.6735,
    "priceRelativeToS&P50052Week": -7.7275,
    "priceRelativeToS&P500Ytd": -0.9479,
    "psAnnual": 3.8894,
    "psTTM": 3.5947,
    "ptbvAnnual": 6.1401,
    "ptbvQuarterly": 8.0857,
    "quickRatioAnnual": 0.8434,
    "quickRatioQuarterly": 0.8442,
    "receivablesTurnoverAnnual": 13.1025,
    "receivablesTurnoverTTM": 11.8635,
    "revenueEmployeeAnnual": 0.4552,
    "revenueEmployeeTTM": 0.4925,
    "revenueGrowth3Y": 11.73,
    "revenueGrowth5Y": 13.18,
    "revenueGrowthQuarterlyYoy": 19.62,
    "revenueGrowthTTMYoy": 15.77,
    "revenuePerShareAnnual": 66.2163,
    "revenuePerShareTTM": 71.1437,
    "revenueShareGrowth5Y": 11.84,
    "roa5Y": 6.41,
    "roaRfy": 9.49,
    "roaTTM": 15.21,
    "roe5Y": 15.39,
    "roeRfy": 18.89,
    "roeTTM": 30.5,
    "roi5Y": 11.31,
    "roiAnnual": 15.52,
    "roiTTM": 24.19,
    "tangibleBookValuePerShareAnnual": 37.4493,
    "tangibleBookValuePerShareQuarterly": 18.7025,
    "tbvCagr5Y": 35.36,
    "totalDebt/totalEquityAnnual": 0.2172,
    "totalDebt/totalEquityQuarterly": 0.2816,
    "yearToDatePriceReturnDaily": 11.9964
  },
  "source_status": {
    "local_research": true,
    "local_news": false,
    "local_sec_filings": false,
    "finnhub_news": true,
    "polygon_news": true,
    "earnings": false,
    "fundamentals": true
  }
}
```

## BSX
Trading candidate:
```json
{
  "symbol": "BSX",
  "score": 46.91,
  "direction": "WATCH",
  "sector": "Healthcare",
  "components": {
    "market": 100.0,
    "sector": 86.35,
    "relative_strength": 57.46919904561053,
    "vwap": 0.0,
    "trend": 0.0,
    "volume": 32.11504852896883,
    "momentum": 60.66044001660444,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 100.0
  }
}
```
Evidence packet (source-labelled; missing sources must remain uncertain):
```json
{
  "local_research": [],
  "local_news": [],
  "local_sec_filings": [],
  "finnhub_news": [
    {
      "category": "company",
      "datetime": 1788796260,
      "headline": "ISRG's Ion Platform Is Quietly Becoming a Second Growth Engine",
      "id": 141765193,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "BSX",
      "source": "Yahoo",
      "summary": "Intuitive Surgical's Ion platform is gaining momentum, with rising procedures, a larger installed base and global expansion fueling a second growth engine.",
      "url": "https://finnhub.io/api/news?id=30f82c3d71c728c02b8284a8860ea904bbbc22691e7920cba19df99641cdfb6e"
    },
    {
      "category": "company",
      "datetime": 1788546339,
      "headline": "How Much Upside Can BSX Stock's Growth Deliver?",
      "id": 141455029,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "BSX",
      "source": "Yahoo",
      "summary": "While two high-profile segments - WATCHMAN and Electrophysiology - have stumbled, the market is overlooking the company's core stability. Business units representing roughly 75% of revenue are performing consistently with their historical track record, though this durable base's near-term ~6% growth leaves our 10.8% three-year CAGR reliant on a post-2026 pipeline re-acceleration.",
      "url": "https://finnhub.io/api/news?id=9980113490b89d23a66c8ffb6cd96ecfaacbd42b6a644618293f4755fb4708bf"
    },
    {
      "category": "company",
      "datetime": 1788534720,
      "headline": "Should Investors Buy IRTC as Growth Improves but Risks Stay Elevated?",
      "id": 141437831,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "BSX",
      "source": "Yahoo",
      "summary": "iRhythm's Q2 revenue growth, margin expansion and record free cash flow strengthen its case, but reimbursement and regulatory risks remain elevated.",
      "url": "https://finnhub.io/api/news?id=00e92f371d6e988ca4bd8fe94b0fb3a9be741d74f0e36ca5ae35fd44bc8650f2"
    },
    {
      "category": "company",
      "datetime": 1788532020,
      "headline": "Boston Scientific's ICVT Business Gains Momentum: Can Growth Continue?",
      "id": 141437622,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "BSX",
      "source": "Yahoo",
      "summary": "BSX's ICVT sales have jumped 15% as coronary therapies gained traction, while new devices and deals could extend its growth momentum.",
      "url": "https://finnhub.io/api/news?id=b8be0d1796ec27cd587c8ff457009a5f9f1b699de6e93f7019af2c890c63a139"
    },
    {
      "category": "company",
      "datetime": 1788525830,
      "headline": "Boston Scientific Recalls Spinal Cord Stimulator Leads Over Fracture Risk",
      "id": 141470804,
      "image": "https://cdn.benzinga.com/files/images/story/2026/09/04/Sep-16--2019-Fremont--Ca--Usa---Boston.jpg?width=2048&height=1536",
      "related": "BSX",
      "source": "Benzinga",
      "summary": "Boston Scientific recalls Infinion CX SCS leads following 1,081 injury reports. Health authorities urge immediate return of unused inventory.",
      "url": "https://finnhub.io/api/news?id=4595326a6a8093c576238d4fffe33477d69e8468b34008143ded118f32a14fc0"
    }
  ],
  "polygon_news": [
    {
      "id": "035ea264374f70758e22dbdbae34de99e082a779630bd6eedc11cd0372379f73",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Novocure Reports Patient Data Exposure in Cybersecurity Incident",
      "author": "Na",
      "published_utc": "2026-09-07T15:12:00Z",
      "article_url": "https://www.zacks.com/stock/news/2986010/novocure-reports-patient-data-exposure-in-cybersecurity-incident?cid=CS-ZC-FT-analyst_blog|company_news_medical_sector-2986010",
      "tickers": [
        "NVCR",
        "BSX",
        "MCK",
        "ABT",
        "WST",
        "MDT",
        "SYK"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/d6/3739.jpg",
      "description": "Novocure Limited (NVCR) disclosed unauthorized access to internal systems in mid-August 2026, exposing internal patient ID numbers for over 1,400 U.S. patients and contact information for healthcare providers and employees. The company stated that medical devices were not accessed, systems remained functional, and no material financial impact is expected. NVCR shares rose 3.2% since the September 1 disclosure.",
      "keywords": [
        "cybersecurity incident",
        "data breach",
        "patient records",
        "healthcare security",
        "medical technology",
        "unauthorized access"
      ],
      "insights": [
        {
          "ticker": "NVCR",
          "sentiment": "neutral",
          "sentiment_reasoning": "While the cybersecurity incident is concerning, the company's proactive disclosure, containment measures, and assurance that devices were not compromised and no material financial impact is expected mitigate negative sentiment. Stock performance has been positive post-disclosure."
        },
        {
          "ticker": "BSX",
          "sentiment": "negative",
          "sentiment_reasoning": "Experienced a cybersecurity incident in August that disrupted access to systems and business applications, affecting order processing and shipping operations."
        },
        {
          "ticker": "MCK",
          "sentiment": "negative",
          "sentiment_reasoning": "Disclosed a data breach involving unauthorized access to third-party applications with alleged theft of data from Oncology & Multispecialty and Medical-Surgical business units."
        },
        {
          "ticker": "ABT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Reported two separate cyber incidents but stated they did not affect products, manufacturing, or patient services, limiting material impact."
        },
        {
          "ticker": "WST",
          "sentiment": "neutral",
          "sentiment_reasoning": "Faced a cyberattack in May with data exfiltration and encryption, but the article notes it carries a Zacks Rank #2 with strong earnings performance."
        },
        {
          "ticker": "MDT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Reported unauthorized access to corporate IT systems, but products and patient care were not compromised."
        },
        {
          "ticker": "SYK",
          "sentiment": "neutral",
          "sentiment_reasoning": "Experienced a cyberattack affecting Microsoft environment and temporarily disrupting manufacturing and shipping, but products and patient care were not compromised."
        }
      ]
    },
    {
      "id": "6b6dec635c7036735a6a9876900e9c968108bf688c8425a6cd5f09d7a3aafb4a",
      "publisher": {
        "name": "GlobeNewswire Inc.",
        "homepage_url": "https://www.globenewswire.com",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/globenewswire.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/globenewswire.ico"
      },
      "title": "Renal Denervation Market Size, Share & Trends Analysis - Global Opportunity Analysis and Industry Forecast (2026-2036)",
      "author": "Researchandmarkets.Com",
      "published_utc": "2026-09-04T14:54:00Z",
      "article_url": "https://www.globenewswire.com/news-release/2026/09/04/3356656/28124/en/renal-denervation-market-size-share-trends-analysis-global-opportunity-analysis-and-industry-forecast-2026-2036.html",
      "tickers": [
        "MDT",
        "BSX",
        "JNJ",
        "ABT"
      ],
      "image_url": "https://ml.globenewswire.com/Resource/Download/908fb457-7f8e-4a08-9081-5565e3dfb3d7",
      "description": "The global renal denervation market is expected to experience significant growth driven by rising resistant hypertension cases, positive clinical trial results, regulatory approvals, and technological advances in radiofrequency, ultrasound, and micro-infusion technologies. North America currently leads the market while Asia-Pacific is projected to grow fastest. The minimally invasive procedure treats uncontrolled hypertension by disrupting sympathetic nerves surrounding renal arteries.",
      "keywords": [
        "renal denervation",
        "hypertension treatment",
        "minimally invasive procedure",
        "medical devices",
        "interventional cardiology",
        "radiofrequency ablation",
        "ultrasound energy",
        "resistant hypertension",
        "market forecast",
        "cardiovascular disease"
      ],
      "insights": [
        {
          "ticker": "MDT",
          "sentiment": "positive",
          "sentiment_reasoning": "Listed as a key company profiled in the report with FDA approvals for Symplicity systems, positioning it as a market leader in the rapidly growing renal denervation market."
        },
        {
          "ticker": "BSX",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as a leading company in the competitive landscape with significant presence in the renal denervation market, benefiting from the projected 19.6% CAGR growth."
        },
        {
          "ticker": "JNJ",
          "sentiment": "positive",
          "sentiment_reasoning": "Featured as a major competitor through Shockwave Medical and Biosense Webster divisions, positioned to capitalize on expanding renal denervation adoption and technological innovation."
        },
        {
          "ticker": "ABT",
          "sentiment": "positive",
          "sentiment_reasoning": "Included in company profiles, positioned to benefit from market expansion in interventional cardiology and hypertension management solutions."
        }
      ]
    },
    {
      "id": "843e9ad0cb80753299aaf2d63b648f1e00462579f17e2f1291c4d6f34cd13421",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Aging Population Drives Healthcare Growth: Stocks to Watch",
      "author": "Na",
      "published_utc": "2026-08-31T15:29:00Z",
      "article_url": "https://www.zacks.com/stock/news/2982600/aging-population-drives-healthcare-growth-stocks-to-watch?cid=CS-ZC-FT-seniors_&_aging-2982600",
      "tickers": [
        "ABBV",
        "TNDM",
        "AMGN",
        "SYK",
        "BSX"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/c3/648.jpg",
      "description": "The global aging population is reshaping healthcare investment opportunities, with the geriatric care services market projected to grow from $1.24 trillion in 2025 to $2.16 trillion by 2034. Healthcare companies are capitalizing on this demographic shift through innovations in diabetes care, cardiovascular treatments, robotic surgery, and digital health solutions. Key players like AbbVie, Tandem Diabetes Care, Amgen, Stryker, and Boston Scientific are advancing AI-enabled technologies and specialized treatments for age-related conditions.",
      "keywords": [
        "aging population",
        "geriatric care",
        "healthcare investment",
        "chronic disease",
        "digital health",
        "AI-enabled medical devices",
        "diabetes care",
        "cardiovascular disease",
        "robotic surgery"
      ],
      "insights": [
        {
          "ticker": "ABBV",
          "sentiment": "positive",
          "sentiment_reasoning": "Company is strengthening its position in aging-related healthcare through immunology and neuroscience, with recent regulatory submissions and acquisitions to deepen its immunology portfolio."
        },
        {
          "ticker": "TNDM",
          "sentiment": "positive",
          "sentiment_reasoning": "Advancing automated diabetes management with recent FDA clearance and CE Mark approvals for Control-IQ+ insulin delivery system, expanding international market presence."
        },
        {
          "ticker": "AMGN",
          "sentiment": "positive",
          "sentiment_reasoning": "Expanding in cardiovascular and metabolic care with Repatha showing 20% reduction in all-cause mortality, and MariTide obesity therapy in Phase 3 trials for multiple age-related conditions."
        },
        {
          "ticker": "SYK",
          "sentiment": "positive",
          "sentiment_reasoning": "Advancing AI-enabled orthopedics through Mako SmartRobotics platform for joint replacement procedures, positioning itself in the growing elderly care market."
        },
        {
          "ticker": "BSX",
          "sentiment": "positive",
          "sentiment_reasoning": "Incorporating AI into cardiovascular portfolio with AI-powered imaging platforms and minimally invasive treatments for complex coronary lesions, addressing age-related cardiovascular disease."
        }
      ]
    },
    {
      "id": "7bade5af89840b270fabcfab495e9eb9a3964a45c940dd343f17953b01b40bc2",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "New Strong Sell Stocks for August 28th",
      "author": "Na",
      "published_utc": "2026-08-28T07:28:00Z",
      "article_url": "https://www.zacks.com/stock/news/2981496/new-strong-sell-stocks-for-august-28th?cid=CS-ZC-FT-tale_of_the_tape|new_zacks_5_rank_stocks-2981496",
      "tickers": [
        "AU",
        "APTV",
        "BSX"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/83/587.jpg",
      "description": "Zacks has added three stocks to its Strong Sell list today: AngloGold Ashanti (gold mining), Aptiv PLC (industrial technology), and Boston Scientific Corporation (medical devices). All three companies have experienced downward revisions to their current year earnings estimates over the last 60 days, with Aptiv seeing the largest revision at 10.1% downward.",
      "keywords": [
        "Strong Sell",
        "earnings revision",
        "Zacks Rank",
        "stock rating"
      ],
      "insights": [
        {
          "ticker": "AU",
          "sentiment": "negative",
          "sentiment_reasoning": "Added to Zacks Rank #5 (Strong Sell) list with 8.6% downward revision to current year earnings estimate over the last 60 days"
        },
        {
          "ticker": "APTV",
          "sentiment": "negative",
          "sentiment_reasoning": "Added to Zacks Rank #5 (Strong Sell) list with 10.1% downward revision to current year earnings estimate over the last 60 days, representing the largest earnings cut among the three stocks"
        },
        {
          "ticker": "BSX",
          "sentiment": "negative",
          "sentiment_reasoning": "Added to Zacks Rank #5 (Strong Sell) list with 1.8% downward revision to current year earnings estimate over the last 60 days"
        }
      ]
    },
    {
      "id": "13779f16f9066c260f8afa24e26e11960b8c0227b092e404daf18726a909771f",
      "publisher": {
        "name": "GlobeNewswire Inc.",
        "homepage_url": "https://www.globenewswire.com",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/globenewswire.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/globenewswire.ico"
      },
      "title": "Atrial Fibrillation Treatment Devices Market Trends and Forecast, 2035 | Includes Profiles of Abbott, AtriCure, Boston Scientific, Johnson & Johnson, and Medtronic",
      "author": "Researchandmarkets.Com",
      "published_utc": "2026-08-26T11:57:00Z",
      "article_url": "https://www.globenewswire.com/news-release/2026/08/26/3351252/28124/en/atrial-fibrillation-treatment-devices-market-trends-and-forecast-2035-includes-profiles-of-abbott-atricure-boston-scientific-johnson-johnson-and-medtronic.html",
      "tickers": [
        "ABT",
        "BSX",
        "ATRC",
        "MDT",
        "JNJ"
      ],
      "image_url": "https://ml.globenewswire.com/Resource/Download/7881985f-8bdf-40b5-9843-a6ec6aa269bd",
      "description": "The global atrial fibrillation treatment devices market is expected to grow at a 13.1% CAGR from $9.6 billion in 2026 to $29 billion by 2035, driven by aging populations, rising AF prevalence affecting 50-60 million people worldwide, and increasing adoption of advanced ablation and left atrial appendage closure technologies. Pulsed field ablation is forecast to generate over 60% of market revenue by 2035, while North America will retain approximately 50% of global market share. Asia-Pacific is expected to register the fastest regional growth.",
      "keywords": [
        "atrial fibrillation",
        "treatment devices",
        "ablation catheters",
        "left atrial appendage closure",
        "pulsed field ablation",
        "medical devices",
        "cardiac care",
        "aging population",
        "market forecast"
      ],
      "insights": [
        {
          "ticker": "ABT",
          "sentiment": "positive",
          "sentiment_reasoning": "Abbott's Amplatzer Amulet is identified as a leading LAAC product with strong market positioning. The company is benefiting from the fastest-growing device segment (LAAC with 13.4% CAGR) and overall market expansion driven by favorable regulatory approvals and clinical evidence."
        },
        {
          "ticker": "BSX",
          "sentiment": "positive",
          "sentiment_reasoning": "Boston Scientific's WATCHMAN FLX and FLX Pro are highlighted as leading LAAC products. The company benefits from recent FDA approvals, strong market demand for stroke-prevention solutions, and the overall growth trajectory of the atrial fibrillation treatment devices market."
        },
        {
          "ticker": "ATRC",
          "sentiment": "positive",
          "sentiment_reasoning": "AtriCure is listed among the prominent companies in the competitive landscape. The company is positioned to benefit from market growth driven by increasing adoption of advanced ablation technologies and favorable regulatory momentum."
        },
        {
          "ticker": "MDT",
          "sentiment": "positive",
          "sentiment_reasoning": "Medtronic is identified as a key competitor in the atrial fibrillation treatment devices market. The company stands to benefit from the 13.1% CAGR market growth and opportunities in pulsed field ablation and advanced mapping technologies."
        },
        {
          "ticker": "JNJ",
          "sentiment": "positive",
          "sentiment_reasoning": "Johnson & Johnson is listed among the prominent companies operating in the market. The company is positioned to capitalize on market expansion driven by aging populations, rising AF prevalence, and increased demand for minimally invasive treatment options."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 19.25725,
    "13WeekPriceReturnDaily": -2.1494,
    "26WeekPriceReturnDaily": -35.2742,
    "3MonthADReturnStd": 33.320415,
    "3MonthAverageTradingVolume": 20.34585,
    "52WeekHigh": 109.5,
    "52WeekHighDate": "2025-09-09",
    "52WeekLow": 42.2,
    "52WeekLowDate": "2026-07-15",
    "52WeekPriceReturnDaily": -55.4188,
    "5DayPriceReturnDaily": -1.0352,
    "assetTurnoverAnnual": 0.4596,
    "assetTurnoverTTM": 0.4773,
    "beta": 0.5958565,
    "bookValuePerShareAnnual": 16.3405,
    "bookValuePerShareQuarterly": 17.2323,
    "bookValueShareGrowth5Y": 8.6,
    "capexCagr5Y": 10.91,
    "cashFlowPerShareAnnual": 2.4666,
    "cashFlowPerShareQuarterly": 2.5057,
    "cashFlowPerShareTTM": 1.62958,
    "cashPerSharePerShareAnnual": 1.325,
    "cashPerSharePerShareQuarterly": 0.3726,
    "currentDividendYieldTTM": 0,
    "currentEv/freeCashFlowAnnual": 22.2412,
    "currentEv/freeCashFlowTTM": 22.4436,
    "currentRatioAnnual": 1.6168,
    "currentRatioQuarterly": 1.2402,
    "dividendGrowthRate5Y": null,
    "dividendPerShareAnnual": 0,
    "dividendPerShareTTM": 0,
    "ebitdPerShareAnnual": 3.0177,
    "ebitdPerShareTTM": 3.4019,
    "ebitdaCagr5Y": 44.78,
    "ebitdaInterimCagr5Y": 26.13,
    "enterpriseValue": 81358.17,
    "epsAnnual": 1.9391,
    "epsBasicExclExtraItemsAnnual": 1.9391,
    "epsBasicExclExtraItemsTTM": 2.4659999999999997,
    "epsExclExtraItemsAnnual": 1.9391,
    "epsExclExtraItemsTTM": 2.4659999999999997,
    "epsGrowth3Y": 58.74,
    "epsGrowth5Y": null,
    "epsGrowthQuarterlyYoy": 15.25,
    "epsGrowthTTMYoy": 46.78,
    "epsInclExtraItemsAnnual": 1.9391,
    "epsInclExtraItemsTTM": 2.4659999999999997,
    "epsNormalizedAnnual": 1.9391,
    "epsTTM": 2.4659999999999997,
    "evEbitdaTTM": 16.047,
    "evRevenueTTM": 3.8749,
    "focfCagr5Y": 29.98,
    "forwardPE": 14.470132798281504,
    "grossMargin5Y": 69.08,
    "grossMarginAnnual": 69.01,
    "grossMarginTTM": 69.5,
    "inventoryTurnoverAnnual": 2.1627,
    "inventoryTurnoverTTM": 2.1007,
    "longTermDebt/equityAnnual": 0.4596,
    "longTermDebt/equityQuarterly": 0.4378,
    "marketCapitalization": 69273.17,
    "monthToDatePriceReturnDaily": -1.0352,
    "netIncomeEmployeeAnnual": 0.0491,
    "netIncomeEmployeeTTM": 0.0623,
    "netInterestCoverageAnnual": 10.6284,
    "netInterestCoverageTTM": 18.5389,
    "netMarginGrowth5Y": null,
    "netProfitMargin5Y": 10.19,
    "netProfitMarginAnnual": 14.44,
    "netProfitMarginTTM": 17.5,
    "operatingMargin5Y": 14.58,
    "operatingMarginAnnual": 18,
    "operatingMarginTTM": 19.78,
    "payoutRatioAnnual": null,
    "payoutRatioTTM": null,
    "pb": 2.7787,
    "pbAnnual": 5.833,
    "pbQuarterly": 2.5446,
    "pcfShareAnnual": 15.2786,
    "pcfShareTTM": 15.2955,
    "peAnnual": 23.9038,
    "peBasicExclExtraTTM": 18.8498,
    "peExclExtraAnnual": 124.7505,
    "peExclExtraTTM": 18.8498,
    "peInclExtraTTM": 18.8498,
    "peNormalizedAnnual": 23.9038,
    "peTTM": 18.8498,
    "pegTTM": 0.4070226757591562,
    "pfcfShareAnnual": 18.9374,
    "pfcfShareTTM": 19.1098,
    "pretaxMargin5Y": 12.5,
    "pretaxMarginAnnual": 16.86,
    "pretaxMarginTTM": 18.39,
    "priceRelativeToS&P50013Week": -3.8797,
    "priceRelativeToS&P50026Week": -48.4825,
    "priceRelativeToS&P5004Week": -4.9041,
    "priceRelativeToS&P50052Week": -74.4148,
    "priceRelativeToS&P500Ytd": -62.8132,
    "psAnnual": 3.4509,
    "psTTM": 3.2994,
    "ptbvAnnual": 8.2114,
    "ptbvQuarterly": 3.522,
    "quickRatioAnnual": 1.0208,
    "quickRatioQuarterly": 0.6763,
    "receivablesTurnoverAnnual": 7.3209,
    "receivablesTurnoverTTM": 7.161,
    "revenueEmployeeAnnual": 0.3402,
    "revenueEmployeeTTM": 0.3559,
    "revenueGrowth3Y": 16.54,
    "revenueGrowth5Y": 15.16,
    "revenueGrowthQuarterlyYoy": 7.53,
    "revenueGrowthTTMYoy": 13.53,
    "revenuePerShareAnnual": 13.4319,
    "revenuePerShareTTM": 14.2365,
    "revenueShareGrowth5Y": 13.93,
    "roa5Y": 4.25,
    "roaRfy": 6.64,
    "roaTTM": 8.35,
    "roe5Y": 7.79,
    "roeRfy": 11.959999999999999,
    "roeTTM": 14.940000000000001,
    "roi5Y": 5.22,
    "roiAnnual": 8.12,
    "roiTTM": 10.13,
    "tangibleBookValuePerShareAnnual": 11.6075,
    "tangibleBookValuePerShareQuarterly": 12.4504,
    "tbvCagr5Y": 12.84,
    "totalDebt/totalEquityAnnual": 0.4719,
    "totalDebt/totalEquityQuarterly": 0.5064,
    "yearToDatePriceReturnDaily": -49.8689
  },
  "source_status": {
    "local_research": false,
    "local_news": false,
    "local_sec_filings": false,
    "finnhub_news": true,
    "polygon_news": true,
    "earnings": false,
    "fundamentals": true
  }
}
```

## WMT
Trading candidate:
```json
{
  "symbol": "WMT",
  "score": 41.81,
  "direction": "WATCH",
  "sector": "Consumer Discretionary",
  "components": {
    "market": 100.0,
    "sector": 53.67,
    "relative_strength": 46.22500545872455,
    "vwap": 0.0,
    "trend": 0.0,
    "volume": 38.3679403679244,
    "momentum": 58.59382787042358,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 100.0
  }
}
```
Evidence packet (source-labelled; missing sources must remain uncertain):
```json
{
  "local_research": [],
  "local_news": [],
  "local_sec_filings": [],
  "finnhub_news": [
    {
      "category": "company",
      "datetime": 1788791760,
      "headline": "Walmart's Ad Business Expands: Can High-Margin Growth Lift Profits?",
      "id": 141763862,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WMT",
      "source": "Yahoo",
      "summary": "Walmart's fast-growing ad business boosts its higher-margin mix as digital sales scale, though Vibe costs are likely to pressure fiscal 2027 profit growth.",
      "url": "https://finnhub.io/api/news?id=be4e68e76cfc51b72a6c35e93877a63480bf4f2d3bc064a8852d7cbd2fa825b4"
    },
    {
      "category": "company",
      "datetime": 1788775200,
      "headline": "Weight loss is just the beginning of GLP-1's: Novo Nordisk CEO",
      "id": 141761854,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WMT",
      "source": "Yahoo",
      "summary": "Yahoo Finance Executive Editor Brian Sozzi chats with Novo Nordisk CEO Mike Doustdar about the true timeline for how GLP-1s will impact the food and airline industries, and what the future of weight loss and preventative health looks like over the next decade.",
      "url": "https://finnhub.io/api/news?id=b46f69d07e94378e750f3d2f11bd8b2436d620a7118b7c75308ea6ee80253b62"
    },
    {
      "category": "company",
      "datetime": 1788772380,
      "headline": "Agentic Commerce Optimisation: Azoma on Which Platforms Help Brands Get Recommended by AI Shopping Agents",
      "id": 141762273,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WMT",
      "source": "Yahoo",
      "summary": "Harvard Business Review reports that 90% of B2B purchases could flow through AI agent exchanges by 2028. Azoma sets out what agentic commerce optimisation platforms should deliver for enterprise brands and digital shelf teamsLondon, Sept. 07, 2026 (GLOBE NEWSWIRE) -- Azoma, the Agentic Commerce Optimisation platform that helps brands drive revenue through AI shopping agents like ChatGPT, Google Gemini, Amazon Rufus and Walmart Sparky, today set out what enterprise brands and digital shelf teams",
      "url": "https://finnhub.io/api/news?id=6505a24d500a7b597e4eef69527ff58ac5358256f26b2407de3d1d9dd4c7f41d"
    },
    {
      "category": "company",
      "datetime": 1788771600,
      "headline": "Amazon made fast delivery the norm. Now rivals want in",
      "id": 141761915,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WMT",
      "source": "Yahoo",
      "summary": "Retailers are turning stores into local delivery hubs, making waiting for an order feel increasingly outdated",
      "url": "https://finnhub.io/api/news?id=ac8519e585e71157db8c222e0c13c577c1ef624d80747747ad5b3fdcc0cb0a1f"
    },
    {
      "category": "company",
      "datetime": 1788738988,
      "headline": "Retailers are Handling Tariff Refunds in Very Different Ways: Walmart and Home Depot",
      "id": 141593660,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WMT",
      "source": "Yahoo",
      "summary": "Walmart Inc. (NASDAQ:WMT) and The Home Depot, Inc. (NYSE:HD) are both booking real tariff refund windfalls, but reporting and using the money in noticeably different ways, CNBC reported. Walmart CFO John David Rainey said the company is eligible for roughly $2.9 billion in refunds, has yet to receive just under $100 million of that, and [\u2026]",
      "url": "https://finnhub.io/api/news?id=dab219b647819749dd7929fc00e006cccd3252d851db791e2dcf83c7e5a810ed"
    }
  ],
  "polygon_news": [],
  "earnings": [
    {
      "symbol": "WMT",
      "date": "2026-11-19",
      "hour": "",
      "quarter": 3,
      "year": 2027,
      "epsEstimate": 0.6428,
      "epsActual": null,
      "revenueEstimate": 189031752661,
      "revenueActual": null
    }
  ],
  "fundamentals": {
    "10DayAverageTradingVolume": 26.78224,
    "13WeekPriceReturnDaily": -9.0029,
    "26WeekPriceReturnDaily": -16.238,
    "3MonthADReturnStd": 28.070448,
    "3MonthAverageTradingVolume": 23.83652,
    "52WeekHigh": 135.16,
    "52WeekHighDate": "2026-05-19",
    "52WeekLow": 98.88,
    "52WeekLowDate": "2025-11-14",
    "52WeekPriceReturnDaily": 6.5964,
    "5DayPriceReturnDaily": 2.1646,
    "assetTurnoverAnnual": 2.5052,
    "assetTurnoverTTM": 2.5443,
    "beta": 0.5638519,
    "bookValuePerShareAnnual": 12.5006,
    "bookValuePerShareQuarterly": 12.3444,
    "bookValueShareGrowth5Y": 5.51,
    "capexCagr5Y": 21.02,
    "cashFlowPerShareAnnual": 1.8726,
    "cashFlowPerShareQuarterly": 1.6975,
    "cashFlowPerShareTTM": 10.33484,
    "cashPerSharePerShareAnnual": 1.3461,
    "cashPerSharePerShareQuarterly": 1.4487,
    "currentDividendYieldTTM": 0.9027,
    "currentEv/freeCashFlowAnnual": 60.1985,
    "currentEv/freeCashFlowTTM": 66.4996,
    "currentRatioAnnual": 0.7898,
    "currentRatioQuarterly": 0.7671,
    "dividendGrowthRate5Y": 5.41,
    "dividendIndicatedAnnual": 0.99,
    "dividendPerShareAnnual": 0.9388,
    "dividendPerShareTTM": 0.9662,
    "dividendYieldIndicatedAnnual": 0.7596102202102354,
    "ebitdPerShareAnnual": 5.4884,
    "ebitdPerShareTTM": 5.922,
    "ebitdaCagr5Y": 11.72,
    "ebitdaInterimCagr5Y": 5.89,
    "enterpriseValue": 898342.7,
    "epsAnnual": 2.7291,
    "epsBasicExclExtraItemsAnnual": 2.7291,
    "epsBasicExclExtraItemsTTM": 2.76,
    "epsExclExtraItemsAnnual": 2.7291,
    "epsExclExtraItemsTTM": 2.76,
    "epsGrowth3Y": 24.21,
    "epsGrowth5Y": 11.53,
    "epsGrowthQuarterlyYoy": -8.97,
    "epsGrowthTTMYoy": 4.13,
    "epsInclExtraItemsAnnual": 2.7291,
    "epsInclExtraItemsTTM": 2.76,
    "epsNormalizedAnnual": 2.7291,
    "epsTTM": 2.76,
    "evEbitdaTTM": 18.9632,
    "evRevenueTTM": 1.2208,
    "focfCagr5Y": -10.38,
    "forwardPE": 35.98552,
    "forwardPEG": 3.68232,
    "grossMargin5Y": 24.68,
    "grossMarginAnnual": 24.93,
    "grossMarginTTM": 25.23,
    "inventoryTurnoverAnnual": 9.2881,
    "inventoryTurnoverTTM": 9.2213,
    "longTermDebt/equityAnnual": 0.3476,
    "longTermDebt/equityQuarterly": 0.3712,
    "marketCapitalization": 852628.7,
    "monthToDatePriceReturnDaily": 2.1646,
    "netIncomeEmployeeAnnual": 0.0104,
    "netIncomeEmployeeTTM": 0.0105,
    "netInterestCoverageAnnual": 8.7913,
    "netInterestCoverageTTM": 90.0302,
    "netMarginGrowth5Y": 4.87,
    "netProfitMargin5Y": 2.52,
    "netProfitMarginAnnual": 3.07,
    "netProfitMarginTTM": 3,
    "operatingMargin5Y": 3.99,
    "operatingMarginAnnual": 4.18,
    "operatingMarginTTM": 4.39,
    "payoutRatioAnnual": 34.29,
    "payoutRatioTTM": 34.87,
    "pb": 8.6792,
    "pbAnnual": 9.9258,
    "pbQuarterly": 9.0081,
    "pcfShareAnnual": 20.5131,
    "pcfShareTTM": 19.8641,
    "peAnnual": 38.9453,
    "peBasicExclExtraTTM": 38.6224,
    "peExclExtraAnnual": 36.52979,
    "peExclExtraTTM": 38.6224,
    "peInclExtraTTM": 38.6224,
    "peNormalizedAnnual": 38.9453,
    "peTTM": 38.6224,
    "pegTTM": 4.005,
    "pfcfShareAnnual": 57.1352,
    "pfcfShareTTM": 55.1685,
    "pretaxMargin5Y": 3.48,
    "pretaxMarginAnnual": 4.13,
    "pretaxMarginTTM": 3.98,
    "priceRelativeToS&P50013Week": -10.7332,
    "priceRelativeToS&P50026Week": -29.4463,
    "priceRelativeToS&P5004Week": -4.5323,
    "priceRelativeToS&P50052Week": -12.3996,
    "priceRelativeToS&P500Ytd": -16.777,
    "psAnnual": 1.1956,
    "psTTM": 1.1587,
    "ptbvAnnual": 10.3736,
    "ptbvQuarterly": 8.16558,
    "quickRatioAnnual": 0.2038,
    "quickRatioQuarterly": 0.1955,
    "receivablesTurnoverAnnual": 67.4481,
    "receivablesTurnoverTTM": 68.1554,
    "revenueEmployeeAnnual": 0.3396,
    "revenueEmployeeTTM": 0.3504,
    "revenueGrowth3Y": 5.27,
    "revenueGrowth5Y": 4.99,
    "revenueGrowthQuarterlyYoy": 5.94,
    "revenueGrowthTTMYoy": 6.16,
    "revenuePerShareAnnual": 88.9009,
    "revenuePerShareTTM": 92.2336,
    "revenueShareGrowth5Y": 6.31,
    "roa5Y": 6.33,
    "roaRfy": 7.6899999999999995,
    "roaTTM": 7.630000000000001,
    "roe5Y": 18.7,
    "roeRfy": 21.98,
    "roeTTM": 22.74,
    "roi5Y": 12.21,
    "roiAnnual": 14.49,
    "roiTTM": 14.52,
    "tangibleBookValuePerShareAnnual": 11.961,
    "tangibleBookValuePerShareQuarterly": 19.11194,
    "tbvCagr5Y": -4.03922,
    "totalDebt/totalEquityAnnual": 0.5172,
    "totalDebt/totalEquityQuarterly": 0.5827,
    "yearToDatePriceReturnDaily": -3.8327
  },
  "source_status": {
    "local_research": false,
    "local_news": false,
    "local_sec_filings": false,
    "finnhub_news": true,
    "polygon_news": false,
    "earnings": true,
    "fundamentals": true
  }
}
```

## NKE
Trading candidate:
```json
{
  "symbol": "NKE",
  "score": 34.21,
  "direction": "WATCH",
  "sector": "Unknown",
  "components": {
    "market": 100.0,
    "sector": 50.0,
    "relative_strength": 22.370131740700913,
    "vwap": 0.0,
    "trend": 0.0,
    "volume": 36.19827565757765,
    "momentum": 36.16580310880823,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 100.0
  }
}
```
Evidence packet (source-labelled; missing sources must remain uncertain):
```json
{
  "local_research": [
    "[VST.md]\n# VST \u2014 Vistra Corp.\n\n**As of:** 2026-08-27  \n**Sector / industry:** Utilities / Independent power producer and electricity generation  \n**Conviction:** Medium \u2014 attractive power-demand exposure and cash flow, but cyclical prices, regulation, and valuation matter\n\n## Snapshot\n\nVistra is a competitive power producer and electricity retailer with a large U.S. generation portfolio, including nuclear, natural gas, and renewable assets. It is not a regulated utility in the traditional sense: earnings depend substantially on wholesale power prices, capacity markets, hedging, fuel economics, and retail demand.\n\nVST was about **$139.81** on August 27, 2026, with a market capitalization of approximately **$47.4 billion** and a trailing P/E near **23.6x**. The stock is a premium-priced way to access the U.S. power shortage and data-center load-growth theme, but the valuation already reflects a meaningful part of that opportunity.\n\n## Latest operating results\n\nQ2 2026 net income was **$305 million**. Ongoing Operations Adjusted EBITDA was **$1.767 billion**, up more than 30% year over year, driven by higher realized energy and capacity prices plus the contribution from the Lotus generation acquisition. Net income was reduced by a $472 million unrealized hedge loss expected to settle in future years.\n\nVistra reaffirmed 2026 guidance for Ongoing Operations Adjusted EBITDA of **$6.8\u2013$7.6 billion** and Ongoing Operations Adjusted Free Cash Flow before Growth of **$3.925\u2013$4.725 billion**. The company had hedged approximately 100% of expected 2026 generation, 94% for 2027, and 72% for 2028 as of August 3. Management's 2027 EBITDA midpoint opportunity range is $7.4\u2013$7.8 billion, excluding potential benefits from the pending Cogentrix acquisition and Meta PPAs.\n\nVistra had approximately **$6.3 billion of available liquidity** at June 30, including $435 million of cash, $4.4 billion under its corporate revolver, and $1.45 billion under its commodity-linked facility. It has repurchased approximately $6.5 billion of stock since November 2021, reducing shares outstanding by about 30%; roughly $1.2 billion remained under the authorization as of August 3.\n\n## Bull thesis\n\n- AI data centers, industrial reshoring, EV adoption, and electrification are increasing the value of reliable, dispatchable power. Existing nuclear plants are particularly scarce and difficult to replace.\n- Vistra has long-duration nuclear PPAs with hyperscalers: a 20-year agreement with AWS for 1,200 MW from Comanche Peak and agreements with Meta covering more than 2,600 MW from PJM nuclear plants.\n- Higher capacity prices and constrained regional supply can support earnings even before new generation is built.\n- The Lotus acquisition adds approximately 2,600 MW of natural-gas generation and expands Vistra's ability to serve load growth and benefit from Texas/ERCOT demand.\n- Hedging provides substantial near-term earnings visibility, while disciplined repurchases can drive per-share growth.\n- Helix Digital Infrastructure, established with KKR, KIA, and NVIDIA, could create an additional platform for power and data-center infrastructure investment; Vistra's initial commitment is up to $1 billion.\n\n## Bear thesis\n\n- Wholesale power prices and capacity revenues are cyclical. A mild summer, weaker load, lower gas prices, transmission improvements, or new generation could reduce realized prices.\n- Nuclear operations carry outage, regulatory, maintenance, fuel, and decommissioning risks. A major forced outage can materially affect quarterly cash flow.\n- The data-center theme is powerful but not guaranteed to translate into Vistra earnings quickly; PPAs, grid interconnection, permitting, and data-center construction can take years.\n- Hedging reduces upside as well as downside. If power prices rise sharply, much of the near-term generation may already be sold forward.\n- Vistra carries meaningful debt and commodity-linked collateral requirements. Liquidity can be pressured when prices rise and margin-posting needs increase.\n- Competition for nuclear assets and AI-power exposure has pushed the valuation higher. If the market rotates away from utilities, nuclear, or AI infrastructure, multiple compression is possible even with stable earnings.\n- Environmental, nuclear-safety, market-design, and political decisions can materially change economics across ERCOT, PJM, and other markets.\n\n## Catalysts\n\n1. Higher PJM capacity prices and continued ERCOT load growth from data centers and industrial demand.\n2. Closing and integration of the Cogentrix acquisition.\n3. Initial earnings contribution from the Meta nuclear PPAs and continued execution of the AWS agreement.\n4. Helix fund investments that connect Vistra's generation assets with hyperscale data-center development.\n5. Continued share repurchases, rising free cash flow, and positive 2027 guidance revisions.\n\n## What would change the view\n\n**Upgrade:** sustained power-price and capacity-market strength, Cogentrix accretion, vi",
    "[MSFT.md]\n# MSFT \u2014 Microsoft Corporation\n\n## Overview\nMicrosoft is a global software, cloud, gaming, productivity, security, and AI platform company. Core businesses include Azure, Microsoft 365, Windows, LinkedIn, Dynamics, GitHub, Xbox/Activision, and a rapidly expanding Copilot/OpenAI-linked AI ecosystem.\n\n## Sector / Industry\n- Sector: Information Technology\n- Industry: Systems Software; Cloud Infrastructure; Productivity Software; AI Platforms\n\n## Recent Developments / News / Earnings / Analyst / SEC / Product Notes\n- SEC EDGAR shows recent Microsoft filings in July 2026, including exempt-solicitation notices and June 2026 employee-plan annual reports; the latest visible 8-K in the fetched SEC listing was from June 2026.\n- Google News RSS query for the last 30 days returned no MSFT-specific items via web_fetch, so no recent article headlines were available from that source.\n- Business/product focus remains Azure AI infrastructure, Microsoft 365 Copilot adoption, GitHub Copilot, security products, Windows/PC cycle, and gaming integration after Activision Blizzard.\n- A Microsoft FY2026 Q4 earnings URL attempted via web_fetch returned 404, so direct IR earnings release text was not accessible through that path.\n\n## Bull Thesis\n- Azure is one of the two largest global cloud platforms and is well positioned for enterprise AI workloads.\n- Microsoft controls key enterprise distribution channels through Office, Teams, Windows, LinkedIn, Dynamics, GitHub, and security.\n- Copilot creates a potentially large per-seat monetization layer across productivity, development, security, and business apps.\n- High recurring revenue, strong balance sheet, and operating discipline support durable compounding.\n\n## Bear Thesis\n- AI capex may remain extremely high, and Copilot monetization could take longer than investors expect.\n- Azure growth is watched closely; any slowdown or share loss would pressure the premium multiple.\n- Regulatory scrutiny of cloud, AI partnerships, security, and gaming may increase.\n- Security failures or customer-trust issues could damage Microsoft's enterprise moat.\n\n## Risks\nCloud competition, AI return-on-invested-capital risk, OpenAI/partner dependency and governance complexity, cybersecurity incidents, antitrust scrutiny, FX/macro pressure on enterprise IT budgets, and execution risk across a broad product stack.\n\n## Catalysts\nAzure growth acceleration, Copilot attach-rate proof, margin resilience despite AI capex, security share gains, GitHub/AI developer monetization, gaming synergies, and larger capital returns.\n\n## Long-Term Outlook\nMicrosoft remains one of the clearest enterprise AI/platform compounders. If Copilot and Azure AI become standard enterprise infrastructure, long-term earnings power can expand meaningfully; if AI revenue lags capex, returns may be more muted.\n\n## Conviction Rating\nHigh \u2014 exceptional franchise quality and enterprise distribution, with the main debate centered on AI capex payback and valuation.\n"
  ],
  "local_news": [
    "[2026-08-14.md]\n# Market News \u2014 2026-08-14\n\n- U.S. index futures were mixed before the open: S&P 500 futures +0.1%, Nasdaq futures +0.1%, Dow futures -0.1% (AP, 05:58 UTC).\n- Thursday closed at records after softer July PPI and falling oil supported growth shares.\n- Oil rebounded into Friday after reports that two UAE tankers were attacked while crossing the Strait of Hormuz; geopolitical energy risk remains active.\n- Applied Materials' record quarter and stronger outlook remain a positive read-through for AI infrastructure, semiconductors, servers, and storage, although the stock's weak reaction highlights elevated expectations.\n- Watchlist market snapshots around 11:45 UTC: NVDA $225.30 (+0.5%), ORCL $156.22 (+1.9%), SMCI $39.16 (+4.0%), WDC $487.29 (+7.3%), VST $146.40 (-0.2%). Quotes are time-stamped snapshots, not end-of-day closes.\n\nSources: https://apnews.com/article/5d9870d6c5ae735f9b74bf4ceefaa3ec ; https://ir.appliedmaterials.com/\n",
    "[2026-07-26.md]\n# Daily Market-Moving News \u2014 2026-07-26\n\n## Overall Market\n- U.S. stock futures rose into the new week as oil fell sharply on reports of a U.S.-Iran pause, easing immediate energy/inflation fears.\n- Major index direction is likely to be driven by the Fed decision, U.S. macro data, and mega-cap technology earnings.\n\n## AI / Semiconductors\n- NVIDIA reportedly discussed a $250B financing guarantee/backstop for OpenAI data-center capacity, reinforcing the scale of AI infrastructure demand while raising financing-quality questions.\n- NVIDIA's planned $1B investment in South Korea's Naver pushed Naver shares higher and highlights NVIDIA's strategic role in AI data-center ecosystems.\n- Chinese memory chipmaker CXMT surged in its Shanghai debut after a major IPO, keeping China semiconductor funding and memory competition in focus.\n\n## Cloud / Software\n- Oracle remained in focus around Pentagon/cloud contract commentary and AI infrastructure demand.\n- Cloud and neocloud demand remains tied to AI capacity shortages and hyperscaler capex.\n\n## Commodities / Geopolitics\n- Oil tumbled after signs of a pause in U.S.-Iran hostilities, reducing risk premium and supporting bonds/equities.\n- Gold remained bid in some market feeds ahead of Fed/GDP/PCE risk, showing residual macro hedging demand.\n\n## Earnings\n- Apple, Microsoft, Meta, Amazon and other large-cap tech names are key earnings catalysts for the week.\n- Exxon and energy-linked earnings are more sensitive after the oil move.\n\n## M&A / IPOs\n- EQT returned with a higher $1.8B offer for Australia\u2019s Perpetual.\n- Brown-Forman rejected Sazerac\u2019s unsolicited proposal as not actionable.\n- Shein flagged tariff pressure and quarterly losses ahead of a Hong Kong IPO.\n\n## Sources Checked\n- Google News RSS market queries\n- Investing.com / Reuters market RSS\n- Prior daily news artifact from this workflow\n"
  ],
  "local_sec_filings": [
    "[2026-08-26.md]\n# SEC Filing Review \u2014 2026-08-26\n\n- No fresh ticker-specific SEC filing was independently verified in the current collection window.\n- SEC-linked watch item: AI-capex intensity, customer concentration, debt funding, and forward-looking risk disclosures in upcoming company filings.\n\nSource: SEC EDGAR; no new watchlist-specific filing validated for this run.\n"
  ],
  "finnhub_news": [
    {
      "category": "company",
      "datetime": 1788798480,
      "headline": "NIKE's China Business: Recovery Story or Ongoing Challenge?",
      "id": 141765247,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NKE",
      "source": "Yahoo",
      "summary": "NIKE sees early China traction in running, football and premium retail, but steep sales declines and inventory cleanup show the recovery remains at an early stage.",
      "url": "https://finnhub.io/api/news?id=a54cdb665002dabdf22bc898d5239bd6d33f30c783922be8cbec31a98c28d57d"
    },
    {
      "category": "company",
      "datetime": 1788796201,
      "headline": "Has Nike's Stock Bottomed Out?",
      "id": 141765114,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NKE",
      "source": "Yahoo",
      "summary": "The footwear and apparel stock has been in a free fall over the past few years.",
      "url": "https://finnhub.io/api/news?id=e975fd90f7b798480493cc314dccf3ca1f6659db1ed151380c8712c762c87b12"
    },
    {
      "category": "company",
      "datetime": 1788792776,
      "headline": "The S&P 100 ETF Just Dumped Nike and Colgate for 4 AI Stocks. Here\u2019s What That Means for Your Portfolio",
      "id": 141763616,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NKE",
      "source": "Yahoo",
      "summary": "The iShares S&P 100 ETF just swapped out a toothpaste giant and a mall REIT for four AI infrastructure plays, and the move reveals something uncomfortable about what this so-called blue-chip fund has quietly become.",
      "url": "https://finnhub.io/api/news?id=42fbcd571f4e0ff319ea17c0fe94bd2d9085859a6a211459ff345ebc0a878b0d"
    },
    {
      "category": "company",
      "datetime": 1788784565,
      "headline": "Nike Exits S&P 100 After Nearly 18 Years. Dell, SanDisk and 2 Tech Giants Take Its Place",
      "id": 141762235,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NKE",
      "source": "Yahoo",
      "summary": "Nike stock suffers a new setback. Nearly 18 years in the S&P 100 comes to an end",
      "url": "https://finnhub.io/api/news?id=f4ae093e4b51ff35a08d1072df57e96306373b501686e859f5db7ec851178bd0"
    },
    {
      "category": "company",
      "datetime": 1788784268,
      "headline": "62-Year-Old Retail Giant Gets Booted Off S&P 500",
      "id": 141762236,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NKE",
      "source": "Yahoo",
      "summary": "One familiar name is losing its place among market royalty",
      "url": "https://finnhub.io/api/news?id=8a04f350677aae1404810d71248a9eb592ff5688c8e474d884fee14521a675f3"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 28.10822,
    "13WeekPriceReturnDaily": -11.967,
    "26WeekPriceReturnDaily": -35.3427,
    "3MonthADReturnStd": 33.580822,
    "3MonthAverageTradingVolume": 23.9381,
    "52WeekHigh": 76.97,
    "52WeekHighDate": "2025-10-02",
    "52WeekLow": 37.95,
    "52WeekLowDate": "2026-09-03",
    "52WeekPriceReturnDaily": -48.0449,
    "5DayPriceReturnDaily": -1.6897,
    "assetTurnoverAnnual": 1.208,
    "assetTurnoverTTM": 1.2324,
    "beta": 1.0557201,
    "bookValuePerShareAnnual": 10.0379,
    "bookValuePerShareQuarterly": 10.0379,
    "bookValueShareGrowth5Y": 4.41,
    "capexCagr5Y": -0.32,
    "cashFlowPerShareAnnual": 1.4748,
    "cashFlowPerShareQuarterly": 1.4748,
    "cashFlowPerShareTTM": 3.82458,
    "cashPerSharePerShareAnnual": 6.0957,
    "cashPerSharePerShareQuarterly": 6.0957,
    "currentDividendYieldTTM": 4.2253,
    "currentEv/freeCashFlowAnnual": 26.257,
    "currentEv/freeCashFlowTTM": 26.257,
    "currentRatioAnnual": 1.9609,
    "currentRatioQuarterly": 1.9609,
    "dividendGrowthRate5Y": 9.28,
    "dividendIndicatedAnnual": 1.64,
    "dividendPerShareAnnual": 1.6281,
    "dividendPerShareTTM": 1.6281,
    "dividendYieldIndicatedAnnual": 1.37495,
    "ebitdPerShareAnnual": 3.0682,
    "ebitdPerShareTTM": 3.0679,
    "ebitdaCagr5Y": -9.85,
    "ebitdaInterimCagr5Y": -6.61,
    "enterpriseValue": 57345.35,
    "epsAnnual": 2.0986,
    "epsBasicExclExtraItemsAnnual": 2.0986,
    "epsBasicExclExtraItemsTTM": 2.0982,
    "epsExclExtraItemsAnnual": 2.0986,
    "epsExclExtraItemsTTM": 2.0982,
    "epsGrowth3Y": -13.39,
    "epsGrowth5Y": -10.02,
    "epsGrowthQuarterlyYoy": 404.83,
    "epsGrowthTTMYoy": -2.83,
    "epsInclExtraItemsAnnual": 2.0986,
    "epsInclExtraItemsTTM": 2.0982,
    "epsNormalizedAnnual": 2.0986,
    "epsTTM": 2.0982,
    "evEbitdaTTM": 12.62,
    "evRevenueTTM": 1.2359,
    "focfCagr5Y": -18.2,
    "forwardPE": 24.62716,
    "forwardPEG": 2.99146,
    "grossMargin5Y": 43.94,
    "grossMarginAnnual": 42.91,
    "grossMarginTTM": 42.91,
    "inventoryTurnoverAnnual": 3.534,
    "inventoryTurnoverTTM": 3.534,
    "longTermDebt/equityAnnual": 0.3997,
    "longTermDebt/equityQuarterly": 0.3997,
    "marketCapitalization": 56966.35,
    "monthToDatePriceReturnDaily": -1.6897,
    "netIncomeEmployeeAnnual": 0.0399,
    "netIncomeEmployeeTTM": 0.0399,
    "netInterestCoverageAnnual": 11.2832,
    "netInterestCoverageTTM": 48.963,
    "netMarginGrowth5Y": -12.23,
    "netProfitMargin5Y": 9.52,
    "netProfitMarginAnnual": 6.7,
    "netProfitMarginTTM": 6.7,
    "operatingMargin5Y": 10.86,
    "operatingMarginAnnual": 8.18,
    "operatingMarginTTM": 8.18,
    "payoutRatioAnnual": 77.45,
    "payoutRatioTTM": 77.45,
    "pb": 3.8322,
    "pbAnnual": 4.5757,
    "pbQuarterly": 4.5757,
    "pcfShareAnnual": 19.8627,
    "pcfShareTTM": 19.8627,
    "peAnnual": 18.3289,
    "peBasicExclExtraTTM": 18.3289,
    "peExclExtraAnnual": 33.32807,
    "peExclExtraTTM": 18.3289,
    "peInclExtraTTM": 18.3289,
    "peNormalizedAnnual": 18.3289,
    "peTTM": 18.3289,
    "pegTTM": 2.44825,
    "pfcfShareAnnual": 26.0835,
    "pfcfShareTTM": 26.0835,
    "pretaxMargin5Y": 11.24,
    "pretaxMarginAnnual": 8.41,
    "pretaxMarginTTM": 8.41,
    "priceRelativeToS&P50013Week": -13.6973,
    "priceRelativeToS&P50026Week": -48.551,
    "priceRelativeToS&P5004Week": -8.4429,
    "priceRelativeToS&P50052Week": -67.0409,
    "priceRelativeToS&P500Ytd": -52.6712,
    "psAnnual": 1.2278,
    "psTTM": 1.2278,
    "ptbvAnnual": 4.6568,
    "ptbvQuarterly": 4.6568,
    "quickRatioAnnual": 1.1922,
    "quickRatioQuarterly": 1.1922,
    "receivablesTurnoverAnnual": 8.7149,
    "receivablesTurnoverTTM": 8.7149,
    "revenueEmployeeAnnual": 0.5964,
    "revenueEmployeeTTM": 0.5964,
    "revenueGrowth3Y": -3.24,
    "revenueGrowth5Y": 0.82,
    "revenueGrowthQuarterlyYoy": -1.13,
    "revenueGrowthTTMYoy": 0.19,
    "revenuePerShareAnnual": 31.3288,
    "revenuePerShareTTM": 31.2887,
    "revenueShareGrowth5Y": 2.51,
    "roa5Y": 12.07,
    "roaRfy": 8.09,
    "roaTTM": 8.260000000000002,
    "roe5Y": 32.11,
    "roeRfy": 20.91,
    "roeTTM": 22,
    "roi5Y": 19.96,
    "roiAnnual": 13.63,
    "roiTTM": 14.05,
    "tangibleBookValuePerShareAnnual": 9.863,
    "tangibleBookValuePerShareQuarterly": 9.863,
    "tbvCagr5Y": 3.17,
    "totalDebt/totalEquityAnnual": 0.5343,
    "totalDebt/totalEquityQuarterly": 0.5343,
    "yearToDatePriceReturnDaily": -39.7269
  },
  "source_status": {
    "local_research": true,
    "local_news": true,
    "local_sec_filings": true,
    "finnhub_news": true,
    "polygon_news": false,
    "earnings": false,
    "fundamentals": true
  }
}
```

## PCG
Trading candidate:
```json
{
  "symbol": "PCG",
  "score": 33.46,
  "direction": "WATCH",
  "sector": "Utilities",
  "components": {
    "market": 100.0,
    "sector": 59.58,
    "relative_strength": 0.0,
    "vwap": 0.0,
    "trend": 0.0,
    "volume": 100.0,
    "momentum": 0.0,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 100.0
  }
}
```
Evidence packet (source-labelled; missing sources must remain uncertain):
```json
{
  "local_research": [],
  "local_news": [],
  "local_sec_filings": [],
  "finnhub_news": [
    {
      "category": "company",
      "datetime": 1788603969,
      "headline": "Jim Cramer on PG&E (PCG): Wildfire Liability Puts Growth Plans Under Pressure",
      "id": 141515114,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PCG",
      "source": "Yahoo",
      "summary": "On September 2, while discussing how California lawmakers failed to advance wildfire-liability reform, Mad Money host Jim Cramer mentioned PG&E Corporation (NYSE:PCG) and said: Boy, it\u2019s been a tough week if you own any California-based electric utilities. Last weekend, a deal to reform the way wildfire liabilities are treated fell through, sending stocks like PG&E [\u2026]",
      "url": "https://finnhub.io/api/news?id=6b0eed1c9d5527a75d9510ee56da287da29be76d2dda6d8d1db3be3d46c5946b"
    },
    {
      "category": "company",
      "datetime": 1788571442,
      "headline": "Truist Securities Downgrades PG&E (PCG) to Hold from Buy",
      "id": 141480246,
      "image": "",
      "related": "PCG",
      "source": "Fintel",
      "summary": "",
      "url": "https://finnhub.io/api/news?id=5cfd0b53aa2e4e32dbfb444c708efae9cba4c713c635df60b135709b113b0b67"
    },
    {
      "category": "company",
      "datetime": 1788548812,
      "headline": "PG&E Corporation (PCG) Discusses Strategic Review and Response to California Wildfire Liability Framework - Slideshow",
      "id": 141469532,
      "image": "https://static.seekingalpha.com/assets/og_image_1200-29b2bfe1a595477db6826bd2126c63ac2091efb7ec76347a8e7f81ba17e3de6c.png",
      "related": "PCG",
      "source": "SeekingAlpha",
      "summary": "2026-09-04. The following slide deck was published by PG&E Corporation in conjunction with this event.",
      "url": "https://finnhub.io/api/news?id=ab29978b1a9cc3d0347d61ce503068d17868acb3e83bf46c183b7535a1f763da"
    },
    {
      "category": "company",
      "datetime": 1788545102,
      "headline": "These S&P500 stocks are the most active in today's session",
      "id": 141448067,
      "image": "https://www.chartmill.com/images/uploads/CM_Most_Active_Stocks_Small_free_fec0650b7f.webp",
      "related": "PCG",
      "source": "ChartMill",
      "summary": "Stay informed about the most active S&P500 stocks in today's session as we take a closer look at what's happening on the US markets on Friday. Discover the stocks that are generating the highest trading volume and driving market activity.",
      "url": "https://finnhub.io/api/news?id=1139f0a9b5cae48fa39f337dfe60d02ded1241a1ffee1eeb21cb4f8344a9d2ec"
    },
    {
      "category": "company",
      "datetime": 1788535193,
      "headline": "PG&E (PCG) Sub Says California\u2019s Wildfire Bill Leaves Financing Risk Unresolved. What Protection Is Still Missing?",
      "id": 141438173,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PCG",
      "source": "Yahoo",
      "summary": "Pacific Gas and Electric Company, the regulated utility subsidiary of PG&E Corporation (NYSE:PCG), said California Senate Bill 492 would improve wildfire-survivor recovery and strengthen preparedness, but would not resolve the financing risk created by the state\u2019s wildfire-liability framework. The amended bill would establish a fast-pay claims program, would expand statewide preparedness planning, and would adjust [\u2026]",
      "url": "https://finnhub.io/api/news?id=78788fef7ed6205dbe4bc451ba3ad7fde05d26c37f761c68c4db7ad503d23856"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 72.63924,
    "13WeekPriceReturnDaily": -14.9822,
    "26WeekPriceReturnDaily": -24.4186,
    "3MonthADReturnStd": 52.44273,
    "3MonthAverageTradingVolume": 26.34604,
    "52WeekHigh": 19.16,
    "52WeekHighDate": "2026-03-02",
    "52WeekLow": 12.59,
    "52WeekLowDate": "2026-09-02",
    "52WeekPriceReturnDaily": -5.2353,
    "5DayPriceReturnDaily": 7.7619,
    "assetTurnoverAnnual": 0.1761,
    "assetTurnoverTTM": 0.1823,
    "beta": 0.18612945,
    "bookValuePerShareAnnual": 14.8048,
    "bookValuePerShareQuarterly": 15.393,
    "bookValueShareGrowth5Y": 6.95,
    "capexCagr5Y": 8.92,
    "cashFlowPerShareAnnual": -1.3972,
    "cashFlowPerShareQuarterly": -1.9356,
    "cashFlowPerShareTTM": 2.65106,
    "cashPerSharePerShareAnnual": 0.3244,
    "cashPerSharePerShareQuarterly": 0.4413,
    "currentDividendYieldTTM": 1.3558,
    "currentRatioAnnual": 0.9712,
    "currentRatioQuarterly": 1.2161,
    "dividendGrowthRate5Y": -39.41,
    "dividendIndicatedAnnual": 0.2,
    "dividendPerShareAnnual": 0.1444,
    "dividendPerShareTTM": 0.1941,
    "ebitdPerShareAnnual": 4.2611,
    "ebitdPerShareTTM": 4.3576,
    "ebitdaCagr5Y": 23.51,
    "ebitdaInterimCagr5Y": 9.54,
    "enterpriseValue": 94739.848,
    "epsAnnual": 1.2275,
    "epsBasicExclExtraItemsAnnual": 1.2275,
    "epsBasicExclExtraItemsTTM": 1.3979000000000001,
    "epsExclExtraItemsAnnual": 1.2275,
    "epsExclExtraItemsTTM": 1.3979000000000001,
    "epsGrowth3Y": 13,
    "epsGrowth5Y": null,
    "epsGrowthQuarterlyYoy": 33.63,
    "epsGrowthTTMYoy": 24.89,
    "epsInclExtraItemsAnnual": 1.2275,
    "epsInclExtraItemsTTM": 1.3979000000000001,
    "epsNormalizedAnnual": 1.2275,
    "epsTTM": 1.3979000000000001,
    "evEbitdaTTM": 9.6105,
    "evRevenueTTM": 3.6668,
    "focfCagr5Y": null,
    "forwardPE": 10.22545,
    "forwardPEG": 1.09951,
    "grossMarginTTM": 35.88346,
    "inventoryTurnoverAnnual": 4.5317,
    "inventoryTurnoverTTM": 4.9445,
    "longTermDebt/equityAnnual": 1.7636,
    "longTermDebt/equityQuarterly": 1.822,
    "marketCapitalization": 31493.848,
    "monthToDatePriceReturnDaily": 7.7619,
    "netIncomeEmployeeAnnual": 270.3,
    "netIncomeEmployeeTTM": 316.6,
    "netInterestCoverageAnnual": 2.0427,
    "netInterestCoverageTTM": 1.9661,
    "netMarginGrowth5Y": null,
    "netProfitMargin5Y": 7.66,
    "netProfitMarginAnnual": 10.84,
    "netProfitMarginTTM": 12.25,
    "operatingMargin5Y": 13.16,
    "operatingMarginAnnual": 19.05,
    "operatingMarginTTM": 19.99,
    "payoutRatioAnnual": 11.73,
    "payoutRatioTTM": 13.49,
    "pb": 0.929,
    "pbAnnual": 1.0854,
    "pbQuarterly": 1.0926,
    "pcfShareAnnual": 3.6133,
    "pcfShareTTM": 3.8657,
    "peAnnual": 11.6514,
    "peBasicExclExtraTTM": 9.9475,
    "peExclExtraAnnual": 21.34363,
    "peExclExtraTTM": 9.9475,
    "peInclExtraTTM": 9.9475,
    "peNormalizedAnnual": 11.6514,
    "peTTM": 9.9475,
    "pegTTM": 1.39517,
    "pfcfShareAnnual": 93.7317,
    "pfcfShareTTM": 42.6168,
    "pretaxMargin5Y": 5.57,
    "pretaxMarginAnnual": 9.72,
    "pretaxMarginTTM": 10.68,
    "priceRelativeToS&P50013Week": -16.7125,
    "priceRelativeToS&P50026Week": -37.6269,
    "priceRelativeToS&P5004Week": -15.7124,
    "priceRelativeToS&P50052Week": -24.2313,
    "priceRelativeToS&P500Ytd": -23.9586,
    "psAnnual": 1.263,
    "psTTM": 1.2189,
    "ptbvAnnual": 1.3277,
    "ptbvQuarterly": 1.94989,
    "quickRatioAnnual": 0.9209,
    "quickRatioQuarterly": 1.1486,
    "receivablesTurnoverAnnual": 11.1143,
    "receivablesTurnoverTTM": 13.2192,
    "revenueEmployeeAnnual": 2493.5,
    "revenueEmployeeTTM": 2583.7,
    "revenueGrowth3Y": 4.77,
    "revenueGrowth5Y": 6.19,
    "revenueGrowthQuarterlyYoy": 0.07,
    "revenueGrowthTTMYoy": 5.66,
    "revenuePerShareAnnual": 11.3238,
    "revenuePerShareTTM": 11.3072,
    "revenueShareGrowth5Y": -5.08,
    "roa5Y": 1.4,
    "roaRfy": 1.91,
    "roaTTM": 2.23,
    "roe5Y": 6.64,
    "roeRfy": 8.309999999999999,
    "roeTTM": 9.62,
    "roi5Y": 2.16,
    "roiAnnual": 2.8899999999999997,
    "roiTTM": 3.35,
    "tangibleBookValuePerShareAnnual": 30.2123,
    "tangibleBookValuePerShareQuarterly": 11.31095,
    "tbvCagr5Y": 3.49607,
    "totalDebt/totalEquityAnnual": 1.8711,
    "totalDebt/totalEquityQuarterly": 1.8943,
    "yearToDatePriceReturnDaily": -11.0143
  },
  "source_status": {
    "local_research": false,
    "local_news": false,
    "local_sec_filings": false,
    "finnhub_news": true,
    "polygon_news": false,
    "earnings": false,
    "fundamentals": true
  }
}
```

## CCL
Trading candidate:
```json
{
  "symbol": "CCL",
  "score": 31.5,
  "direction": "WATCH",
  "sector": "Consumer Discretionary",
  "components": {
    "market": 100.0,
    "sector": 53.67,
    "relative_strength": 0.0,
    "vwap": 0.0,
    "trend": 0.0,
    "volume": 63.908081840973644,
    "momentum": 22.400664192225083,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 100.0
  }
}
```
Evidence packet (source-labelled; missing sources must remain uncertain):
```json
{
  "local_research": [],
  "local_news": [],
  "local_sec_filings": [],
  "finnhub_news": [
    {
      "category": "company",
      "datetime": 1788738273,
      "headline": "I'm Buying Consumer Experience Like Delta, Carnival, And Avoiding Discretionary Stocks",
      "id": 141652147,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/2128192721/image_2128192721.jpg?io=getty-c-w1536",
      "related": "CCL",
      "source": "SeekingAlpha",
      "summary": "Travel demand is robust among boomers, and inflation risks are monitored. Click here to see why consumer experience stocks are constructive.",
      "url": "https://finnhub.io/api/news?id=1582ef2d0582b3ed5928ab2cc1a284c1b649982bd24e5b3d62a524023d8373cd"
    },
    {
      "category": "company",
      "datetime": 1788530160,
      "headline": "Carnival Stock Just Hit a 52-Week Low. Why It\u2019s Time to Buy.",
      "id": 141438151,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "CCL",
      "source": "Yahoo",
      "summary": "Carnival  is caught in a perfect storm.  Carnival\u2019s stock hit a 52-week low on Tuesday, as the debt-logged cruise line navigates higher oil prices, a hantavirus scare for the cruise industry, and a geopolitical environment that\u2019s keeping more travelers close to home.",
      "url": "https://finnhub.io/api/news?id=c5510488bad0060711d6ae1f68d050b698cd5fefa626256f6a589d7e6804bc07"
    },
    {
      "category": "company",
      "datetime": 1788496800,
      "headline": "Software Rebound Extends Moat Index Gains",
      "id": 141410253,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/1725655946/image_1725655946.jpg?io=getty-c-w1536",
      "related": "CCL",
      "source": "SeekingAlpha",
      "summary": "The S&P 500 gained 2.72% and reached a record high in August, with energy leading the market as crude prices rose. Read more here.",
      "url": "https://finnhub.io/api/news?id=814e73db5d703af98ad84b037219310746d8c95d98095282138f68b72379680b"
    },
    {
      "category": "company",
      "datetime": 1788429780,
      "headline": "Reimagined Ocean Bar Debuts on Oosterdam with Expanded Entertainment",
      "id": 141399334,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "CCL",
      "source": "Yahoo",
      "summary": "Holland America Line Evolution is bringing a new chapter to Ocean Bar aboard Oosterdam. Inspired by the glamour of the golden age of ocean travel, the redesigned venue brings live entertainment, cocktails and conversation together in a sophisticated new setting, featuring a new stage, refreshed lounge spaces and a reimagined layout designed to connect guests more closely with the performances.",
      "url": "https://finnhub.io/api/news?id=1b1c67aacc17124d699105cc9f7d0bf58fbe52885bcc64c0f8e5afbcef058ae4"
    },
    {
      "category": "company",
      "datetime": 1788393863,
      "headline": "3 S&P 500 Stocks That Fall Short",
      "id": 141388067,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "CCL",
      "source": "Yahoo",
      "summary": "The S&P 500 (^GSPC) is home to the biggest and most well-known companies in the market, making it a go-to index for investors seeking stability. But not all large-cap stocks are created equal - some are struggling with slowing growth, declining margins, or increased competition.",
      "url": "https://finnhub.io/api/news?id=04556937173c6b929cbe355d04281b67fc53b5223be4696cbb0647e417f9920f"
    }
  ],
  "polygon_news": [
    {
      "id": "b48c89cd1f2c0a3aff01c748ec2d68ee205558ae20ffc2110ef3bef29b26ceac",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Will Carnival (CCL) Beat Estimates Again in Its Next Earnings Report?",
      "author": "Zacks.Com",
      "published_utc": "2026-09-07T16:10:01Z",
      "article_url": "https://www.zacks.com/stock/news/2986007/will-carnival-ccl-beat-estimates-again-in-its-next-earnings-report?cid=CS-ZC-FT-fundamental_analysis|yseop_template_7-2986007",
      "tickers": [
        "CCL"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default194.jpg",
      "description": "Carnival (CCL) has demonstrated a strong track record of beating earnings estimates, surpassing consensus by an average of 14.13% over the last two quarters. With a positive Earnings ESP of +0.32% and a Zacks Rank #3 (Hold), the cruise operator appears positioned for another earnings beat, as stocks with this combination historically beat estimates nearly 70% of the time.",
      "keywords": [
        "earnings beat",
        "Carnival",
        "cruise operator",
        "Earnings ESP",
        "earnings estimates",
        "Zacks Rank"
      ],
      "insights": [
        {
          "ticker": "CCL",
          "sentiment": "positive",
          "sentiment_reasoning": "Carnival has consistently beaten earnings estimates in recent quarters (17.14% and 11.11% surprises), maintains a positive Earnings ESP of +0.32%, and holds a Zacks Rank #3 (Hold). The combination of these factors suggests strong potential for another earnings beat, with historical data showing ~70% success rate for stocks with similar metrics."
        }
      ]
    },
    {
      "id": "4b5c2335283d323322152d3cae6801b238df81ab97491174488625ba2deeb7e0",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Carnival (CCL) Sees a More Significant Dip Than Broader Market: Some Facts to Know",
      "author": "Zacks.Com",
      "published_utc": "2026-08-31T21:45:01Z",
      "article_url": "https://www.zacks.com/stock/news/2982824/carnival-ccl-sees-a-more-significant-dip-than-broader-market-some-facts-to-know?cid=CS-ZC-FT-fundamental_analysis|yseop_template_6-2982824",
      "tickers": [
        "CCL"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default122.jpg",
      "description": "Carnival stock declined 3.51% to $23.89, significantly underperforming the S&P 500's 0.33% loss. The cruise operator has fallen 10.97% over the past month while the broader market gained 3.87%. Analysts expect upcoming earnings of $1.36 per share (down 4.9% YoY) with revenue of $8.36 billion (up 2.59% YoY). Carnival holds a Zacks Rank of #3 (Hold) with a Forward P/E of 11.1, trading at a discount to its industry average.",
      "keywords": [
        "cruise operator",
        "earnings decline",
        "stock underperformance",
        "valuation discount",
        "consumer discretionary",
        "leisure and recreation"
      ],
      "insights": [
        {
          "ticker": "CCL",
          "sentiment": "negative",
          "sentiment_reasoning": "Stock significantly underperformed the broader market with a 3.51% daily decline and 10.97% monthly decline. Expected earnings are declining 4.9% year-over-year despite modest revenue growth. The company's industry ranks in the bottom 29% of all industries. While the stock trades at a valuation discount, the negative earnings trajectory and weak industry positioning support a negative outlook."
        }
      ]
    },
    {
      "id": "9012464911dbd7d004c39b721386a4cc4ba41b963ef6ed1bbe87eafe7a9dd5f1",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Boomers Are Getting Rich and Retiring Early. 1 No-Brainer Stock To Buy Now",
      "author": "Jeremy Bowman",
      "published_utc": "2026-08-12T02:32:18Z",
      "article_url": "https://www.fool.com/investing/2026/08/11/boomers-are-getting-rich-and-retiring-early-1-no-b/?source=iedfolrf0000001",
      "tickers": [
        "VIK",
        "CCL",
        "RCL",
        "NCLH",
        "ABNB"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F882933%2Flongship-vidar-rhine-river-koblenz.jpg&w=1200&op=resize",
      "description": "Rising stock markets and home prices are giving baby boomers significant disposable income, leading many to retire early. This demographic shift creates investment opportunities for companies targeting affluent older travelers. Viking Holdings, a luxury cruise line focused on adults 55+, is positioned to capitalize on this trend with strong revenue growth and differentiated offerings compared to traditional cruise competitors.",
      "keywords": [
        "baby boomers",
        "early retirement",
        "disposable income",
        "cruise lines",
        "luxury travel",
        "demographic trends",
        "stock market wealth"
      ],
      "insights": [
        {
          "ticker": "VIK",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong financial performance with 17.5% revenue growth and 43.9% EBITDA growth in Q1. Stock has appreciated significantly since IPO ($24 to $101+). Well-positioned to benefit from growing boomer wealth and spending power. Differentiated business model targeting underserved affluent 55+ demographic with expected 30% EPS compound annual growth rate."
        },
        {
          "ticker": "CCL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a traditional cruise line peer but not highlighted as a primary investment opportunity. Article emphasizes Viking's differentiation from Carnival and other competitors."
        },
        {
          "ticker": "RCL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a traditional cruise line peer but not highlighted as a primary investment opportunity. Article emphasizes Viking's differentiation from Royal Caribbean and other competitors."
        },
        {
          "ticker": "NCLH",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a traditional cruise line peer but not highlighted as a primary investment opportunity. Article emphasizes Viking's differentiation from Norwegian and other competitors."
        },
        {
          "ticker": "ABNB",
          "sentiment": "positive",
          "sentiment_reasoning": "Referenced as evidence that travel demand continues to boom despite economic concerns, supporting the broader thesis of strong discretionary spending by affluent demographics."
        }
      ]
    },
    {
      "id": "b434f83f312f4ead1dbb035d0667c31ac70444fd6815b50472ee0833c7c35680",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Norwegian Cruise Line Is Down 19% This Year and Reports Earnings July 30. Is Now the Time to Buy?",
      "author": "Thomas Niel",
      "published_utc": "2026-07-27T18:15:00Z",
      "article_url": "https://www.fool.com/investing/2026/07/27/norwegian-cruise-line-is-down-19-this-year-and-rep/?source=iedfolrf0000001",
      "tickers": [
        "NCLH",
        "CCL",
        "RCL"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F880212%2Fcruise-ship-luxury-travel-1200x675-128554e.jpg&w=1200&op=resize",
      "description": "Norwegian Cruise Line shares have declined 19% this year due to Mideast geopolitical tensions affecting fuel prices and passenger demand. While the company reports earnings on July 30, analyst Thomas Niel recommends Carnival as a stronger alternative in the cruise industry, citing Carnival's lower leverage, dividend yield of 1.7%, and better risk/reward proposition compared to Norwegian's steeper valuation discount.",
      "keywords": [
        "cruise lines",
        "earnings report",
        "geopolitical tensions",
        "fuel prices",
        "dividend yield",
        "leverage",
        "valuation"
      ],
      "insights": [
        {
          "ticker": "NCLH",
          "sentiment": "negative",
          "sentiment_reasoning": "Stock down 19% year-to-date; management lowered 2026 earnings guidance significantly; analyst recommends skipping the stock despite potential post-earnings rally; trades at steep discount but with higher leverage and no dividend"
        },
        {
          "ticker": "CCL",
          "sentiment": "positive",
          "sentiment_reasoning": "Recommended as stronger alternative to Norwegian; trades at similar forward earnings multiple but with lower leverage; currently pays dividend with 1.7% yield; represents better risk/reward proposition for cruise industry investors"
        },
        {
          "ticker": "RCL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as competitor trading at premium valuation (17x forward earnings vs Norwegian's 11x); no specific recommendation or criticism provided"
        }
      ]
    },
    {
      "id": "3bb455085ff5f093c0207d1c2594970b8ee212d575da56517e5eab07f61935b4",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Carnival Reported Earnings on June 23, Royal Caribbean Is Next on July 28, Then Norwegian Cruise Line on July 30. Here's My Top Buy of the Bunch.",
      "author": "Jeff Siegel",
      "published_utc": "2026-07-19T11:05:00Z",
      "article_url": "https://www.fool.com/investing/2026/07/19/carnival-reports-earnings-on-july-23-followed-by-r/?source=iedfolrf0000001",
      "tickers": [
        "RCL",
        "CCL",
        "NCLH"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F878825%2Fcruise-vacation-travel-boat-water-ocean.jpg&w=1200&op=resize",
      "description": "The cruise industry has completed its post-pandemic recovery with healthy occupancy rates and pricing. Among the three largest cruise operators, Royal Caribbean is recommended as the top buy due to its strongest financial results, industry-leading profitability, record bookings, and healthier balance sheet compared to Carnival and Norwegian Cruise Line, which both carry higher debt levels relative to their earnings.",
      "keywords": [
        "cruise industry",
        "earnings reports",
        "post-pandemic recovery",
        "occupancy rates",
        "balance sheet",
        "debt management",
        "booking trends",
        "profitability",
        "onboard spending"
      ],
      "insights": [
        {
          "ticker": "RCL",
          "sentiment": "positive",
          "sentiment_reasoning": "Strongest financial performer with $4.54B Q1 revenue, highest profitability margins, record bookings at higher prices, accelerating demand, and the healthiest balance sheet among the three competitors."
        },
        {
          "ticker": "CCL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Turnaround gaining momentum with record operating income and strong bookings, but carries significantly higher debt ($23.4B) relative to peers, creating execution risk despite positive operational trends."
        },
        {
          "ticker": "NCLH",
          "sentiment": "neutral",
          "sentiment_reasoning": "Fleet modernization and occupancy recovery are positive, but the company operates with substantial leverage ($15.2B debt) and generates considerably less revenue and EBITDA than competitors, leaving limited margin for error."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 20.60838,
    "13WeekPriceReturnDaily": -15.5835,
    "26WeekPriceReturnDaily": -17.5955,
    "3MonthADReturnStd": 42.478516,
    "3MonthAverageTradingVolume": 23.51452,
    "52WeekHigh": 34.03,
    "52WeekHighDate": "2026-02-06",
    "52WeekLow": 23.075,
    "52WeekLowDate": "2026-09-01",
    "52WeekPriceReturnDaily": -25.5306,
    "5DayPriceReturnDaily": -1.5906,
    "assetTurnoverAnnual": 0.5151,
    "assetTurnoverTTM": 0.5295,
    "beta": 2.5201573,
    "bookValuePerShareAnnual": 9.3628,
    "bookValuePerShareQuarterly": 9.4519,
    "bookValueShareGrowth5Y": -13.12,
    "capexCagr5Y": -0.05,
    "cashFlowPerShareAnnual": 1.987,
    "cashFlowPerShareQuarterly": 2.3316,
    "cashFlowPerShareTTM": 0.55476,
    "cashPerSharePerShareAnnual": 1.4695,
    "cashPerSharePerShareQuarterly": 1.6348,
    "currentDividendYieldTTM": 1.2857,
    "currentEv/freeCashFlowAnnual": 21.0381,
    "currentEv/freeCashFlowTTM": 17.1449,
    "currentRatioAnnual": 0.3223,
    "currentRatioQuarterly": 0.3344,
    "dividendGrowthRate5Y": null,
    "dividendIndicatedAnnual": 0.6,
    "dividendPerShareAnnual": null,
    "dividendPerShareTTM": 0.3085,
    "ebitdPerShareAnnual": 4.8959,
    "ebitdPerShareTTM": 5.1348,
    "ebitdaCagr5Y": null,
    "ebitdaInterimCagr5Y": null,
    "enterpriseValue": 54846.451,
    "epsAnnual": 1.9686,
    "epsBasicExclExtraItemsAnnual": 1.9686,
    "epsBasicExclExtraItemsTTM": 2.193,
    "epsExclExtraItemsAnnual": 1.9686,
    "epsExclExtraItemsTTM": 2.193,
    "epsGrowth3Y": null,
    "epsGrowth5Y": null,
    "epsGrowthQuarterlyYoy": -4.31,
    "epsGrowthTTMYoy": 21.77,
    "epsInclExtraItemsAnnual": 1.9686,
    "epsInclExtraItemsTTM": 2.193,
    "epsNormalizedAnnual": 1.9686,
    "epsTTM": 2.193,
    "evEbitdaTTM": 7.6473,
    "evRevenueTTM": 2.0082,
    "focfCagr5Y": null,
    "forwardPE": 11.13169,
    "forwardPEG": 1.20669,
    "grossMargin5Y": 29.18,
    "grossMarginAnnual": 54.76,
    "grossMarginTTM": 54.91,
    "inventoryTurnoverAnnual": 23.8004,
    "inventoryTurnoverTTM": 23.9591,
    "longTermDebt/equityAnnual": 1.9568,
    "longTermDebt/equityQuarterly": 1.8058,
    "marketCapitalization": 32200.451,
    "monthToDatePriceReturnDaily": -1.5906,
    "netIncomeEmployeeAnnual": 0.0242,
    "netIncomeEmployeeTTM": 0.0269,
    "netInterestCoverageAnnual": 3.6875,
    "netInterestCoverageTTM": 3.1356,
    "netMarginGrowth5Y": null,
    "netProfitMargin5Y": -106.07,
    "netProfitMarginAnnual": 10.37,
    "netProfitMarginTTM": 11.23,
    "operatingMargin5Y": -80.97,
    "operatingMarginAnnual": 15.3,
    "operatingMarginTTM": 15.78,
    "payoutRatioTTM": 52.08,
    "pb": 2.4831,
    "pbAnnual": 2.746,
    "pbQuarterly": 2.6284,
    "pcfShareAnnual": 5.1786,
    "pcfShareTTM": 4.7402,
    "peAnnual": 11.6668,
    "peBasicExclExtraTTM": 10.4956,
    "peExclExtraTTM": 10.4956,
    "peInclExtraTTM": 10.4956,
    "peNormalizedAnnual": 11.6668,
    "peTTM": 10.4956,
    "pegTTM": 1.341,
    "pfcfShareAnnual": 12.3515,
    "pfcfShareTTM": 10.0658,
    "pretaxMargin5Y": -106.25,
    "pretaxMarginAnnual": 10.41,
    "pretaxMarginTTM": 11.34,
    "priceRelativeToS&P50013Week": -17.3138,
    "priceRelativeToS&P50026Week": -30.8038,
    "priceRelativeToS&P5004Week": -14.9119,
    "priceRelativeToS&P50052Week": -44.5266,
    "priceRelativeToS&P500Ytd": -35.9633,
    "psAnnual": 1.2095,
    "psTTM": 1.179,
    "ptbvAnnual": 3.037,
    "ptbvQuarterly": 2.8917,
    "quickRatioAnnual": 0.2013,
    "quickRatioQuarterly": 0.2154,
    "receivablesTurnoverAnnual": 41.9905,
    "receivablesTurnoverTTM": 45.4426,
    "revenueEmployeeAnnual": 0.2335,
    "revenueEmployeeTTM": 0.2396,
    "revenueGrowth3Y": 29.82,
    "revenueGrowth5Y": 36.61,
    "revenueGrowthQuarterlyYoy": 5.29,
    "revenueGrowthTTMYoy": 5.16,
    "revenuePerShareAnnual": 18.9886,
    "revenuePerShareTTM": 19.6765,
    "revenueShareGrowth5Y": 21.34,
    "roa5Y": -4.1,
    "roaRfy": 5.34,
    "roaTTM": 5.949999999999999,
    "roe5Y": -24.48,
    "roeRfy": 22.470000000000002,
    "roeTTM": 24.44,
    "roi5Y": -4.7,
    "roiAnnual": 7.090000000000001,
    "roiTTM": 7.99,
    "tangibleBookValuePerShareAnnual": 8.4657,
    "tangibleBookValuePerShareQuarterly": 8.5911,
    "tbvCagr5Y": -10.53,
    "totalDebt/totalEquityAnnual": 2.1687,
    "totalDebt/totalEquityQuarterly": 1.9193,
    "yearToDatePriceReturnDaily": -23.019
  },
  "source_status": {
    "local_research": false,
    "local_news": false,
    "local_sec_filings": false,
    "finnhub_news": true,
    "polygon_news": true,
    "earnings": false,
    "fundamentals": true
  }
}
```