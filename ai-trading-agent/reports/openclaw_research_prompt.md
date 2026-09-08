# OpenClaw Candidate Research Handoff

Review each candidate using the supplied trading data and evidence packet. Do not place orders. Return only JSON in this format:

```json
{"research":[{"symbol":"MSFT","research_score":0,"conviction":"Low","catalysts":[],"risks":[],"summary":""}]}
```

Use a 0-100 research score. Do not invent facts or infer fundamentals from technical data. Treat missing data as uncertainty, name the missing source in risks, and use only dated/source-labelled news, earnings, filings, or fundamentals. Keep Python's technical score authoritative; this research score is a 30% adjustment.

## SMCI
Trading candidate:
```json
{
  "symbol": "SMCI",
  "score": 82.57,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 100.0,
    "sector": 83.0,
    "relative_strength": 100.0,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 17.685646062154866,
    "momentum": 100.0,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 0.0
  }
}
```
Evidence packet (source-labelled; missing sources must remain uncertain):
```json
{
  "local_research": [
    "[SMCI.md]\n# SMCI \u2014 2026-08-12\n\n**View:** Watchlist coverage; conviction is conditional on valuation and company-specific verification. **Theme:** AI/infrastructure, software, fintech, mobility or space depending on issuer.\n\n**Bull case:** Continued AI/data-center spending, easing inflation, and resilient equity demand can support growth names and infrastructure suppliers.\n\n**Bear case:** 4.68% long yields, Brent near $89, geopolitical disruption, crowded AI positioning, execution risk and any financing/dilution could compress multiples.\n\n**Catalysts / checks:** next earnings, guidance, customer wins, backlog, margins, cash burn and SEC filings. No ticker-specific filing was independently verified in today\u2019s collection window.\n\n**Rating:** Medium conviction only after fresh company-level verification; not investment advice.\n"
  ],
  "local_news": [
    "[2026-08-14.md]\n# Market News \u2014 2026-08-14\n\n- U.S. index futures were mixed before the open: S&P 500 futures +0.1%, Nasdaq futures +0.1%, Dow futures -0.1% (AP, 05:58 UTC).\n- Thursday closed at records after softer July PPI and falling oil supported growth shares.\n- Oil rebounded into Friday after reports that two UAE tankers were attacked while crossing the Strait of Hormuz; geopolitical energy risk remains active.\n- Applied Materials' record quarter and stronger outlook remain a positive read-through for AI infrastructure, semiconductors, servers, and storage, although the stock's weak reaction highlights elevated expectations.\n- Watchlist market snapshots around 11:45 UTC: NVDA $225.30 (+0.5%), ORCL $156.22 (+1.9%), SMCI $39.16 (+4.0%), WDC $487.29 (+7.3%), VST $146.40 (-0.2%). Quotes are time-stamped snapshots, not end-of-day closes.\n\nSources: https://apnews.com/article/5d9870d6c5ae735f9b74bf4ceefaa3ec ; https://ir.appliedmaterials.com/\n",
    "[2026-08-13.md]\n# Market News \u2014 2026-08-13\n\n## Executive read\n\nU.S. stocks closed at records as benign July PPI and lower oil supported growth shares. AI and semiconductor leadership remained dominant, while Applied Materials\u2019 post-close results reinforced the equipment and AI-capex thesis. The tape is constructive but expectations and geopolitical risks are elevated.\n\n## Market-moving developments\n\n1. The S&P 500 rose 0.7% to 7,798.99 and the Nasdaq rose 0.8% to 26,803.03; both set record closes. The Dow gained 0.1% and Russell 2000 gained 0.2%. [AP](https://apnews.com/article/892c5409d8ed26bfd5965eb2a89d9005)\n2. July PPI was flat month over month and core PPI rose 0.2%, slightly below forecasts, supporting hopes that rate pressure can ease. [Axios](https://www.axios.com/2026/08/13/inflation-july-ppi)\n3. Brent fell 2.1%, helping duration-sensitive equities, but the Iran/Hormuz disruption remains a material inflation and supply-chain risk.\n4. Applied Materials reported record Q3 revenue of about $9.12B and adjusted EPS of about $3.50, above consensus, with above-estimate forward guidance reported in market coverage. The read-through is positive for semiconductor equipment and AI infrastructure, though after-hours weakness highlights valuation risk.\n\n## Watchlist implications\n\n- Favor profitable AI infrastructure, cloud, storage, and power names.\n- Treat speculative space, EV, leveraged crypto, and fintech as satellite exposures.\n- No additions or removals; raise priority on NVDA, AMD, AVGO, SMCI, WDC, and ORCL.\n"
  ],
  "local_sec_filings": [
    "[2026-08-13.md]\n# SEC Filings \u2014 2026-08-13\n\nNo fresh ticker-specific SEC filing was independently verified for the watchlist in this collection window. This is a data-quality limitation, not evidence that no filing exists. Priority checks remain SMCI, NVDA, ORCL, AMD, AVGO, and financing/dilution disclosures for MSTR, ASTS, RKLB, RIVN, UPST, and POET.\n",
    "[2026-08-12.md]\n# SEC Filings \u2014 2026-08-12\n\nNo ticker-specific filing was independently verified in today\u2019s collection window. Treat this as a data-quality limitation, not evidence that no filing exists. Priority checks for the next run: 10-Q/8-K for SMCI, NVDA, AMD, ORCL, CRM and financing/ATM disclosures for MSTR, ASTS, RKLB, RIVN and UPST.\n"
  ],
  "finnhub_news": [
    {
      "category": "company",
      "datetime": 1788890700,
      "headline": "Which S&P500 stocks are the most active on Tuesday?",
      "id": 141952860,
      "image": "https://www.chartmill.com/images/uploads/CM_Most_Active_Stocks_Small_free_fec0650b7f.webp",
      "related": "SMCI",
      "source": "ChartMill",
      "summary": "Stay informed about the most active stocks in the S&P500 index on Tuesday's session. Discover the stocks that are generating the highest trading volume and driving market activity.",
      "url": "https://finnhub.io/api/news?id=71df634472679672cbba113b47bdb93092bfd0fa038e96e7e1e616b1bf5b7146"
    },
    {
      "category": "company",
      "datetime": 1788881597,
      "headline": "Super Micro Climbs 4%, Hewlett Packard Enterprise Advances 5%: Is the Margin Beat Already Guided Away?",
      "id": 141950612,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SMCI",
      "source": "Yahoo",
      "summary": "AI server stocks are surging while the broader market sits flat, but the margin beat driving the biggest gain carries a built-in expiration date that management already acknowledged on the earnings call.",
      "url": "https://finnhub.io/api/news?id=c33631a4e58a0d6eb5c8c0a9dbf3bbd26cc9f3016563fda923f9edfb171be5b1"
    },
    {
      "category": "company",
      "datetime": 1788877229,
      "headline": "SMCI Outworks Its Peers And Costs Less",
      "id": 141950100,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SMCI",
      "source": "Yahoo",
      "summary": "In the world of AI hardware, one company is delivering top-tier growth from the bargain bin, forcing investors to ask if the market sees a flaw they are missing.",
      "url": "https://finnhub.io/api/news?id=2eec56b8e8bbea93472ac3ae78a7f43f0f48d04a4298a23b5549b645ad238e7b"
    },
    {
      "category": "company",
      "datetime": 1788874521,
      "headline": "10 Information Technology Stocks Whale Activity In Today\u2019s Session",
      "id": 141953002,
      "image": "https://cdn.benzinga.com/files/images/story/2025/11/06/aggregated_options_1.jpg?width=2048&height=1536",
      "related": "SMCI",
      "source": "Benzinga",
      "summary": "This whale alert can help traders discover the next big trading opportunities.\nWhales are entities with large sums of money and we track their transactions here at Benzinga on our options activity scanner.\nTraders will",
      "url": "https://finnhub.io/api/news?id=e0b852f5173246d14fa26532ac5af45a58c2c5529e897f666f55e5e3c90b2557"
    },
    {
      "category": "company",
      "datetime": 1788872405,
      "headline": "Investors Heavily Search Super Micro Computer, Inc. (SMCI): Here is What You Need to Know",
      "id": 141951249,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SMCI",
      "source": "Yahoo",
      "summary": "Super Micro (SMCI) has been one of the stocks most watched by Zacks.com users lately. So, it is worth exploring what lies ahead for the stock.",
      "url": "https://finnhub.io/api/news?id=2cbaaae008f811736a236aa5c4daa973914d11cd7b9d73e6d0f88987a0bad0b1"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 36.36662,
    "13WeekPriceReturnDaily": -15.5864,
    "26WeekPriceReturnDaily": 29.0417,
    "3MonthADReturnStd": 113.19198,
    "3MonthAverageTradingVolume": 52.92452,
    "52WeekHigh": 58.78,
    "52WeekHighDate": "2025-10-09",
    "52WeekLow": 19.48,
    "52WeekLowDate": "2026-03-23",
    "52WeekPriceReturnDaily": -2.0292,
    "5DayPriceReturnDaily": 6.1964,
    "assetTurnoverAnnual": 1.3045,
    "assetTurnoverTTM": 1.6313,
    "beta": 2.1902804,
    "bookValuePerShareAnnual": 22.3852,
    "bookValuePerShareQuarterly": 22.3852,
    "bookValueShareGrowth5Y": 59.52,
    "capexCagr5Y": 22.8,
    "cashFlowPerShareAnnual": -10.7785,
    "cashFlowPerShareQuarterly": -10.7785,
    "cashFlowPerShareTTM": 11.5173,
    "cashPerSharePerShareAnnual": 11.6282,
    "cashPerSharePerShareQuarterly": 11.6282,
    "currentDividendYieldTTM": null,
    "currentEv/freeCashFlowAnnual": 23.49868,
    "currentEv/freeCashFlowTTM": 23.83992,
    "currentRatioAnnual": 3.8723,
    "currentRatioQuarterly": 3.8723,
    "dividendIndicatedAnnual": 0,
    "dividendPerShareTTM": null,
    "ebitdPerShareAnnual": 4.0499,
    "ebitdPerShareTTM": 4.1013,
    "ebitdaCagr5Y": 79.36,
    "ebitdaInterimCagr5Y": 100.86,
    "enterpriseValue": 27208.073,
    "epsAnnual": 3.1985,
    "epsBasicExclExtraItemsAnnual": 3.1985,
    "epsBasicExclExtraItemsTTM": 3.2003999999999997,
    "epsExclExtraItemsAnnual": 3.1985,
    "epsExclExtraItemsTTM": 3.2003999999999997,
    "epsGrowth3Y": 40.9,
    "epsGrowth5Y": 72.55,
    "epsGrowthQuarterlyYoy": 446.14,
    "epsGrowthTTMYoy": 94.1,
    "epsInclExtraItemsAnnual": 3.1985,
    "epsInclExtraItemsTTM": 3.2003999999999997,
    "epsNormalizedAnnual": 3.1985,
    "epsTTM": 3.2003999999999997,
    "evEbitdaTTM": 9.634,
    "evRevenueTTM": 0.6965,
    "focfCagr5Y": null,
    "forwardPE": 8.36473,
    "forwardPEG": 0.17247,
    "grossMargin5Y": 13.81,
    "grossMarginAnnual": 10.82,
    "grossMarginTTM": 10.82,
    "inventoryTurnoverAnnual": 3.9639,
    "inventoryTurnoverTTM": 3.9639,
    "longTermDebt/equityAnnual": 0.4614,
    "longTermDebt/equityQuarterly": 0.4614,
    "marketCapitalization": 26009.26,
    "monthToDatePriceReturnDaily": 6.1964,
    "netIncomeEmployeeAnnual": 0.3576,
    "netIncomeEmployeeTTM": 0.3576,
    "netInterestCoverageAnnual": 28.0274,
    "netInterestCoverageTTM": 365.4191,
    "netMarginGrowth5Y": 12.7,
    "netProfitMargin5Y": 6.53,
    "netProfitMarginAnnual": 5.71,
    "netProfitMarginTTM": 5.71,
    "operatingMargin5Y": 7.57,
    "operatingMarginAnnual": 7.09,
    "operatingMarginTTM": 7.09,
    "payoutRatioAnnual": null,
    "payoutRatioTTM": null,
    "pb": 1.7963,
    "pbAnnual": 1.3102,
    "pbQuarterly": 1.3102,
    "pcfShareAnnual": null,
    "pcfShareTTM": null,
    "peAnnual": 11.661,
    "peBasicExclExtraTTM": 11.661,
    "peExclExtraAnnual": 24.98282,
    "peExclExtraTTM": 11.661,
    "peInclExtraTTM": 11.661,
    "peNormalizedAnnual": 11.661,
    "peTTM": 11.661,
    "pegTTM": 0.31154,
    "pfcfShareAnnual": 16.9739,
    "pfcfShareTTM": 36.1878,
    "pretaxMargin5Y": 7.57,
    "pretaxMarginAnnual": 7.14,
    "pretaxMarginTTM": 7.14,
    "priceRelativeToS&P50013Week": -17.3167,
    "priceRelativeToS&P50026Week": 15.8334,
    "priceRelativeToS&P5004Week": 26.2097,
    "priceRelativeToS&P50052Week": -21.0252,
    "priceRelativeToS&P500Ytd": 22.3136,
    "psAnnual": 0.6658,
    "psTTM": 0.6658,
    "ptbvAnnual": 7.72314,
    "ptbvQuarterly": 7.03345,
    "quickRatioAnnual": 1.906,
    "quickRatioQuarterly": 1.906,
    "receivablesTurnoverAnnual": 9.3796,
    "receivablesTurnoverTTM": 9.3796,
    "revenueEmployeeAnnual": 6.2621,
    "revenueEmployeeTTM": 6.2621,
    "revenueGrowth3Y": 76.34,
    "revenueGrowth5Y": 61.48,
    "revenueGrowthQuarterlyYoy": 93.16,
    "revenueGrowthTTMYoy": 77.79,
    "revenuePerShareAnnual": 56.0166,
    "revenuePerShareTTM": 55.4085,
    "revenueShareGrowth5Y": 53.15,
    "roa5Y": 10.6,
    "roaRfy": 7.449999999999999,
    "roaTTM": 9.31,
    "roe5Y": 21.15,
    "roeRfy": 15.4,
    "roeTTM": 25.080000000000002,
    "roi5Y": 15.33,
    "roiAnnual": 9.610000000000001,
    "roiTTM": 14.23,
    "tangibleBookValuePerShareAnnual": 37.27727,
    "tangibleBookValuePerShareQuarterly": 40.63004,
    "tbvCagr5Y": 18.51276,
    "totalDebt/totalEquityAnnual": 0.6023,
    "totalDebt/totalEquityQuarterly": 0.6023,
    "yearToDatePriceReturnDaily": 35.2579
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

## INTC
Trading candidate:
```json
{
  "symbol": "INTC",
  "score": 79.82,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 100.0,
    "sector": 83.0,
    "relative_strength": 100.0,
    "vwap": 100.0,
    "trend": 50.0,
    "volume": 15.172614564223894,
    "momentum": 100.0,
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
      "datetime": 1788890700,
      "headline": "Which S&P500 stocks are the most active on Tuesday?",
      "id": 141952860,
      "image": "https://www.chartmill.com/images/uploads/CM_Most_Active_Stocks_Small_free_fec0650b7f.webp",
      "related": "INTC",
      "source": "ChartMill",
      "summary": "Stay informed about the most active stocks in the S&P500 index on Tuesday's session. Discover the stocks that are generating the highest trading volume and driving market activity.",
      "url": "https://finnhub.io/api/news?id=71df634472679672cbba113b47bdb93092bfd0fa038e96e7e1e616b1bf5b7146"
    },
    {
      "category": "company",
      "datetime": 1788890400,
      "headline": "Curious about the most active stocks on Tuesday?",
      "id": 141952859,
      "image": "https://www.chartmill.com/images/uploads/CM_Most_Active_Stocks_Small_free_fec0650b7f.webp",
      "related": "INTC",
      "source": "ChartMill",
      "summary": "These stocks are making the most noise in today's session. Stay tuned for the latest updates!",
      "url": "https://finnhub.io/api/news?id=e7ff2c19b1ea0dd0b5fc7c743285265a03298aa5dceb13fe5ea04cab8325a641"
    },
    {
      "category": "company",
      "datetime": 1788889306,
      "headline": "Sector Update: Tech Stocks Gain Tuesday Afternoon",
      "id": 141952526,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "INTC",
      "source": "Yahoo",
      "summary": "Tech stocks were higher Tuesday afternoon, with the State Street Technology Select Sector SPDR ETF (",
      "url": "https://finnhub.io/api/news?id=36fcd8baf08f803b3dfd780713c80799ffe2fc5d5abc3464db5d761d1a0c9975"
    },
    {
      "category": "company",
      "datetime": 1788888467,
      "headline": "Top Midday Gainers",
      "id": 141952587,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "INTC",
      "source": "Yahoo",
      "summary": "Roivant Sciences (ROIV) shares soared 19% after the company said its Pulmovant unit's phase 2 PHocus",
      "url": "https://finnhub.io/api/news?id=0847765489fd164b7ba68471321ee4879f1e66ee636697799778159c6a302678"
    },
    {
      "category": "company",
      "datetime": 1788888396,
      "headline": "Intel Stock Jumps on Major Analyst Upgrade",
      "id": 141952548,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "INTC",
      "source": "Yahoo",
      "summary": "Intel Stock Jumps as Northland Turns Bullish and CPU Price Hike Looms",
      "url": "https://finnhub.io/api/news?id=49a3447dff7403c9eca797433ba74d6f3d682c62f57a8bcc013d2782d463f1f3"
    }
  ],
  "polygon_news": [
    {
      "id": "6b574868ff3b4e14dd9ebf1307aab4b872d6033f89c858b6313310c1097bc3c1",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Why Intel Stock Rallied Tuesday Morning",
      "author": "Danny Vena, Cpa",
      "published_utc": "2026-09-08T15:29:06Z",
      "article_url": "https://www.fool.com/investing/2026/09/08/why-intel-stock-rallied-tuesday-morning/?source=iedfolrf0000001",
      "tickers": [
        "INTC"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F886635%2Fthe-intel-logo-superimposed-over-a-picture-of-the-companys-headquarters.png&w=1200&op=resize",
      "description": "Intel stock surged 8-9% on reports of planned 10% CPU price increases aimed at improving gross margins. Northland Securities upgraded Intel to 'outperform' with a $120 price target, citing material progress in the company's turnaround and foundry ambitions. However, analysts note the stock is already expensive at 68x forward earnings.",
      "keywords": [
        "Intel price increase",
        "CPU pricing",
        "gross margin improvement",
        "analyst upgrade",
        "foundry business",
        "semiconductor",
        "valuation concerns"
      ],
      "insights": [
        {
          "ticker": "INTC",
          "sentiment": "positive",
          "sentiment_reasoning": "Stock rallied 8-9% on price increase announcements and analyst upgrade to 'outperform' with 25% upside potential. Analyst cited material progress in turnaround and foundry ambitions, plus near-term pricing power from CPU shortage. However, positive sentiment is tempered by concerns about high valuation multiples (68x forward earnings)."
        }
      ]
    },
    {
      "id": "c27b327886fc79eaf2ac3cb806a2910bd3fb724375349e78b393f3d15051d187",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Why Rigetti Computing Popped Today",
      "author": "Jeremy Bowman",
      "published_utc": "2026-09-08T14:40:28Z",
      "article_url": "https://www.fool.com/investing/2026/09/08/why-rigetti-computing-popped-today/?source=iedfolrf0000001",
      "tickers": [
        "RGTI",
        "RGTIW",
        "QBTS",
        "INTC",
        "GFS"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F886606%2Fquantum-computing.jpg&w=1200&op=resize",
      "description": "Rigetti Computing's stock surged up to 12.2% after securing $100 million in CHIPS Act funding from the Department of Commerce to advance superconducting quantum computing research. The government will receive a minority, non-controlling equity stake in the company. While the funding is a positive development for the quantum computing sector, Rigetti remains speculative as it generates minimal revenue ($5.1 million in Q2) and quantum computing is still an emerging technology.",
      "keywords": [
        "CHIPS Act",
        "quantum computing",
        "federal funding",
        "superconducting quantum computers",
        "R&D acceleration"
      ],
      "insights": [
        {
          "ticker": "RGTI",
          "sentiment": "positive",
          "sentiment_reasoning": "Company received $100 million in government funding to advance quantum computing research, demonstrating sector validation and providing capital for R&D. Stock price increased significantly (up to 12.2%). However, sentiment is tempered by minimal revenue generation and speculative nature of the business."
        },
        {
          "ticker": "RGTIW",
          "sentiment": "positive",
          "sentiment_reasoning": "Company received $100 million in government funding to advance quantum computing research, demonstrating sector validation and providing capital for R&D. Stock price increased significantly (up to 12.2%). However, sentiment is tempered by minimal revenue generation and speculative nature of the business."
        },
        {
          "ticker": "QBTS",
          "sentiment": "positive",
          "sentiment_reasoning": "Peer company also received CHIPS Act funding alongside Rigetti, indicating broader government support for the quantum computing sector. Stock showed positive movement (+9.62%)."
        },
        {
          "ticker": "INTC",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a previous recipient of government investment through CHIPS Act, but not directly impacted by this announcement."
        },
        {
          "ticker": "GFS",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a previous recipient of government investment through CHIPS Act, but not directly impacted by this announcement."
        }
      ]
    },
    {
      "id": "885343645292468818937a44c29eb3677c7b20e4a90334780e7b30c546f41b08",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Buy Super Micro Computer for Handsome Returns & Attractive Valuations",
      "author": "Zacks.Com",
      "published_utc": "2026-09-08T12:23:00Z",
      "article_url": "https://www.zacks.com/stock/news/2986259/buy-super-micro-computer-for-handsome-returns-attractive-valuations?cid=CS-ZC-FT-analyst_blog|investment_ideas-2986259",
      "tickers": [
        "SMCI",
        "SMCIP",
        "NVDA",
        "AMD",
        "INTC"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/3f/989.jpg",
      "description": "Super Micro Computer (SMCI) reported fiscal 2026 revenues nearly doubled to $39.1 billion with record backlog levels. The company projects fiscal 2027 sales of $65-$72 billion driven by AI infrastructure demand. SMCI is expanding its Data Center Building Block Solutions strategy, strengthening liquid-cooling capabilities, and benefits from partnerships with major chip manufacturers. The stock trades at attractive valuations with a forward P/E of 8.94X versus industry average of 10.36X, earning a Zacks Rank #1 (Strong Buy) rating.",
      "keywords": [
        "AI infrastructure",
        "data center",
        "server systems",
        "liquid cooling",
        "GPU platforms",
        "backlog",
        "valuation",
        "revenue growth"
      ],
      "insights": [
        {
          "ticker": "SMCI",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong fiscal 2026 results with nearly doubled revenues to $39.1B, record backlog, robust guidance for fiscal 2027 ($65-$72B), Zacks Rank #1 rating, attractive valuation metrics, and strategic positioning in high-growth AI infrastructure market with expanding product portfolio and customer partnerships."
        },
        {
          "ticker": "SMCIP",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong fiscal 2026 results with nearly doubled revenues to $39.1B, record backlog, robust guidance for fiscal 2027 ($65-$72B), Zacks Rank #1 rating, attractive valuation metrics, and strategic positioning in high-growth AI infrastructure market with expanding product portfolio and customer partnerships."
        },
        {
          "ticker": "NVDA",
          "sentiment": "positive",
          "sentiment_reasoning": "SMCI is shipping volume products across multiple NVIDIA GPU platforms (GB300, HGX B300, B200, RTX 6000 Pro) and preparing systems for upcoming Vera platforms, indicating strong demand and partnership benefits from AI infrastructure expansion."
        },
        {
          "ticker": "AMD",
          "sentiment": "positive",
          "sentiment_reasoning": "SMCI launched AMD's Helios product line and MI450 Total Solution while supporting MI350 and MI355X systems, demonstrating active partnership and volume shipments benefiting from AI infrastructure demand."
        },
        {
          "ticker": "INTC",
          "sentiment": "neutral",
          "sentiment_reasoning": "SMCI is shipping Intel Xeon 6+ platforms in volume and developing systems for Arm-based AGI processors, showing continued partnership but with less emphasis compared to NVIDIA and AMD in the article's discussion."
        }
      ]
    },
    {
      "id": "4da31e5a9d3f4efe56a1aea669b2f8afb74736e6275d93333f519f590d131172",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "NVIDIA's Hugging Face Buyout: Can It Further Strengthen AI Dominance?",
      "author": "Zacks.Com",
      "published_utc": "2026-09-07T13:02:00Z",
      "article_url": "https://www.zacks.com/stock/news/2985672/nvidia-s-hugging-face-buyout-can-it-further-strengthen-ai-dominance?cid=CS-ZC-FT-analyst_blog|quick_take-2985672",
      "tickers": [
        "NVDA",
        "AMD",
        "INTC"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/93/534.jpg",
      "description": "NVIDIA's proposed $12.93 billion acquisition of Hugging Face would expand its AI leadership beyond chips into the open-model ecosystem, giving it access to 18 million users, 3 million models, and 500,000 datasets. The deal strengthens NVIDIA's software and developer ecosystem while AMD and Intel challenge its dominance with their own AI platforms. NVIDIA trades at a forward P/E of 18.07 with strong earnings growth estimates.",
      "keywords": [
        "AI acquisition",
        "open-source models",
        "data center",
        "AI accelerators",
        "developer ecosystem",
        "competitive advantage"
      ],
      "insights": [
        {
          "ticker": "NVDA",
          "sentiment": "positive",
          "sentiment_reasoning": "The acquisition of Hugging Face is strategically sound and expands NVIDIA's reach into the open-model ecosystem. Strong Q2 fiscal 2027 results with 106% revenue growth and 117% Data Center revenue surge support continued dominance. Forward P/E of 18.07 is below sector average, and earnings estimates show 93.3% and 64% growth for fiscal 2027 and 2028 respectively. Rated Zacks Rank #1 (Strong Buy)."
        },
        {
          "ticker": "AMD",
          "sentiment": "positive",
          "sentiment_reasoning": "AMD is strengthening its AI offerings with the Helios rack-scale platform and Instinct accelerators. Q2 2026 Data Center revenues rose 107% year-over-year to $6.7 billion with Instinct sales more than doubling. Major deals from Anthropic and Microsoft deployment on Azure demonstrate competitive traction. Expected Data Center revenue more than doubling in 2027."
        },
        {
          "ticker": "INTC",
          "sentiment": "positive",
          "sentiment_reasoning": "Intel is gaining momentum in data center AI with Q2 revenues up 25% and Data Center/AI revenues surging 59% to $6.26 billion. Launched Xeon 6+ and expanded OpenVINO framework. Purpose-built silicon revenues nearly tripled year-over-year and approaching $2 billion run rate with $4 billion target, demonstrating strong growth trajectory."
        }
      ]
    },
    {
      "id": "9b57bfd340bf363436ade3cf05bcacf88180f45adfa73eea90facd477a0329e2",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "History Says What Nvidia's Last Big Acquisition Became. Hugging Face Will Cost Nearly Twice as Much.",
      "author": "Daniel Sparks",
      "published_utc": "2026-09-07T03:18:01Z",
      "article_url": "https://www.fool.com/investing/2026/09/06/history-says-what-nvidia-s-last-big-acquisition-became-hugging-face-will-cost-nearly-twice-as-much/?source=iedfolrf0000001",
      "tickers": [
        "NVDA",
        "INTC"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2Fa01b6ce9077ca602af1404120164875e7d2d5081-2000x1200.png%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "Nvidia announced a $12.9 billion acquisition of Hugging Face, nearly double its previous largest acquisition of Mellanox for $7 billion in 2020. While Mellanox's networking business grew into a $31.4 billion revenue line, Hugging Face currently generates ~$150 million annually at an 86x revenue multiple. The deal's success depends on Hugging Face driving developers toward Nvidia's hardware and software ecosystem rather than standalone growth.",
      "keywords": [
        "acquisition",
        "Hugging Face",
        "Mellanox",
        "AI models platform",
        "data center networking",
        "valuation multiple",
        "ecosystem strategy"
      ],
      "insights": [
        {
          "ticker": "NVDA",
          "sentiment": "neutral",
          "sentiment_reasoning": "The acquisition is strategically sound based on Mellanox's success, but Hugging Face's 86x revenue valuation is significantly higher than Mellanox's 5x multiple. The deal's success depends on indirect returns through chip sales rather than standalone growth. Author notes management has earned patience but wouldn't recommend buying/selling on this deal alone."
        },
        {
          "ticker": "INTC",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only in a headline reference; no substantive analysis provided in the article content."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 81.95262,
    "13WeekPriceReturnDaily": -14.2959,
    "26WeekPriceReturnDaily": 122.2738,
    "3MonthADReturnStd": 81.34328,
    "3MonthAverageTradingVolume": 122.10119,
    "52WeekHigh": 142.35,
    "52WeekHighDate": "2026-06-30",
    "52WeekLow": 24.05,
    "52WeekLowDate": "2025-09-12",
    "52WeekPriceReturnDaily": 291.1801,
    "5DayPriceReturnDaily": 7.0271,
    "assetTurnoverAnnual": 0.25,
    "assetTurnoverTTM": 0.277,
    "beta": 2.3932192,
    "bookValuePerShareAnnual": 22.8837,
    "bookValuePerShareQuarterly": 17.3591,
    "bookValueShareGrowth5Y": 2.78,
    "capexCagr5Y": 0.27,
    "cashFlowPerShareAnnual": -0.991,
    "cashFlowPerShareQuarterly": 0.5614,
    "cashFlowPerShareTTM": 2.09114,
    "cashPerSharePerShareAnnual": 7.4922,
    "cashPerSharePerShareQuarterly": 5.8947,
    "currentDividendYieldTTM": 2.8485,
    "currentEv/freeCashFlowTTM": 191.115,
    "currentRatioAnnual": 2.017,
    "currentRatioQuarterly": 1.604,
    "dividendGrowthRate5Y": null,
    "dividendIndicatedAnnual": 0,
    "dividendPerShareAnnual": 0,
    "dividendPerShareTTM": 3.0444,
    "dividendYieldIndicatedAnnual": 1.1374,
    "ebitdPerShareAnnual": 3.0611,
    "ebitdPerShareTTM": 3.4296,
    "ebitdaCagr5Y": -10.31,
    "ebitdaInterimCagr5Y": -9.66,
    "enterpriseValue": 541046.62,
    "epsAnnual": -0.0589,
    "epsBasicExclExtraItemsAnnual": -0.0589,
    "epsBasicExclExtraItemsTTM": -2.1202,
    "epsExclExtraItemsAnnual": -0.0589,
    "epsExclExtraItemsTTM": -2.1202,
    "epsGrowth3Y": null,
    "epsGrowth5Y": null,
    "epsGrowthQuarterlyYoy": null,
    "epsGrowthTTMYoy": null,
    "epsInclExtraItemsAnnual": -0.0589,
    "epsInclExtraItemsTTM": -2.1202,
    "epsNormalizedAnnual": -0.0589,
    "epsTTM": -2.1202,
    "evEbitdaTTM": 32.2512,
    "evRevenueTTM": 9.4867,
    "focfCagr5Y": null,
    "forwardPE": 51.38288,
    "forwardPEG": 0.64132,
    "grossMargin5Y": 41.4,
    "grossMarginAnnual": 34.77,
    "grossMarginTTM": 38.6,
    "inventoryTurnoverAnnual": 2.8954,
    "inventoryTurnoverTTM": 2.9339,
    "longTermDebt/equityAnnual": 0.3858,
    "longTermDebt/equityQuarterly": 0.5546,
    "marketCapitalization": 503383.62,
    "monthToDatePriceReturnDaily": 7.0271,
    "netIncomeEmployeeAnnual": -0.0032,
    "netIncomeEmployeeTTM": -0.1357,
    "netInterestCoverageAnnual": 0.3599,
    "netInterestCoverageTTM": 2.1398,
    "netMarginGrowth5Y": null,
    "netProfitMargin5Y": 1.03,
    "netProfitMarginAnnual": -0.51,
    "netProfitMarginTTM": -19.79,
    "operatingMargin5Y": 2.79,
    "operatingMarginAnnual": 5.88,
    "operatingMarginTTM": 9.36,
    "payoutRatioAnnual": 74.83154,
    "pb": 5.7502,
    "pbAnnual": 1.531,
    "pbQuarterly": 7.5624,
    "pcfShareAnnual": 51.9113,
    "pcfShareTTM": 33.7027,
    "peAnnual": null,
    "peBasicExclExtraTTM": null,
    "peExclExtraAnnual": 22.61631,
    "peExclExtraTTM": null,
    "peInclExtraTTM": null,
    "peNormalizedAnnual": null,
    "peTTM": null,
    "pfcfShareAnnual": 55.1532,
    "pfcfShareTTM": 93.7225,
    "pretaxMargin5Y": 4.61,
    "pretaxMarginAnnual": 2.95,
    "pretaxMarginTTM": -17.28,
    "priceRelativeToS&P50013Week": -16.0262,
    "priceRelativeToS&P50026Week": 109.0655,
    "priceRelativeToS&P5004Week": -1.3963,
    "priceRelativeToS&P50052Week": 272.1841,
    "priceRelativeToS&P500Ytd": 146.6763,
    "psAnnual": 9.5242,
    "psTTM": 8.8263,
    "ptbvAnnual": 1.5691,
    "ptbvQuarterly": 7.7888,
    "quickRatioAnnual": 1.6491,
    "quickRatioQuarterly": 1.2537,
    "receivablesTurnoverAnnual": 14.4466,
    "receivablesTurnoverTTM": 17.842,
    "revenueEmployeeAnnual": 0.6353,
    "revenueEmployeeTTM": 0.6855,
    "revenueGrowth3Y": -5.71,
    "revenueGrowth5Y": -7.46,
    "revenueGrowthQuarterlyYoy": 25.42,
    "revenueGrowthTTMYoy": 7.47,
    "revenuePerShareAnnual": 11.6673,
    "revenuePerShareTTM": 11.174,
    "revenueShareGrowth5Y": -8.71,
    "roa5Y": 1.48,
    "roaRfy": -0.13,
    "roaTTM": -5.48,
    "roe5Y": 2.24,
    "roeRfy": -0.22999999999999998,
    "roeTTM": -10.76,
    "roi5Y": 1.77,
    "roiAnnual": -0.16999999999999998,
    "roiTTM": -7.42,
    "tangibleBookValuePerShareAnnual": 22.3286,
    "tangibleBookValuePerShareQuarterly": 16.8545,
    "tbvCagr5Y": 9.14,
    "totalDebt/totalEquityAnnual": 0.4076,
    "totalDebt/totalEquityQuarterly": 0.5773,
    "yearToDatePriceReturnDaily": 159.6206
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

## HPE
Trading candidate:
```json
{
  "symbol": "HPE",
  "score": 79.59,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 100.0,
    "sector": 83.0,
    "relative_strength": 76.18356088889131,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 16.403936874060722,
    "momentum": 79.02574409034355,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 80.15290163683107
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
      "datetime": 1788885301,
      "headline": "These S&P500 stocks are moving in today's session",
      "id": 141952072,
      "image": "https://www.chartmill.com/images/uploads/CM_Top_Movers_Small_free_2b4ff2fc22.webp",
      "related": "HPE",
      "source": "ChartMill",
      "summary": "Uncover the latest developments among S&P500 stocks in today's session. Stay tuned to the S&P500 index's top gainers and losers on Tuesday.",
      "url": "https://finnhub.io/api/news?id=4f341f3695cce0e1c75c9e82065703aa89431c0b92533b280737ef8d0233cb27"
    },
    {
      "category": "company",
      "datetime": 1788881597,
      "headline": "Super Micro Climbs 4%, Hewlett Packard Enterprise Advances 5%: Is the Margin Beat Already Guided Away?",
      "id": 141950612,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPE",
      "source": "Yahoo",
      "summary": "AI server stocks are surging while the broader market sits flat, but the margin beat driving the biggest gain carries a built-in expiration date that management already acknowledged on the earnings call.",
      "url": "https://finnhub.io/api/news?id=c33631a4e58a0d6eb5c8c0a9dbf3bbd26cc9f3016563fda923f9edfb171be5b1"
    },
    {
      "category": "company",
      "datetime": 1788879858,
      "headline": "Hewlett Packard Enterprise Company (HPE) Jumps on Surging AI Infrastructure Demand",
      "id": 141950933,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPE",
      "source": "Yahoo",
      "summary": "Harbor Funds, an investment management company, released its Q2 2026 investor letter for \u201cHarbor Mid Cap Value Fund\u201d. The letter can be downloaded here. Global equities experienced a sharp rally in Q2 2026, with the S&P 500 returning 15.2%, its strongest quarter since 2020, driven by a shift from software to hardware in the Artificial [\u2026]",
      "url": "https://finnhub.io/api/news?id=0450b50ae0be1e92d967dde8e4a0f783dfc774967ef325404d3f43880c659c02"
    },
    {
      "category": "company",
      "datetime": 1788877229,
      "headline": "SMCI Outworks Its Peers And Costs Less",
      "id": 141950100,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPE",
      "source": "Yahoo",
      "summary": "In the world of AI hardware, one company is delivering top-tier growth from the bargain bin, forcing investors to ask if the market sees a flaw they are missing.",
      "url": "https://finnhub.io/api/news?id=2eec56b8e8bbea93472ac3ae78a7f43f0f48d04a4298a23b5549b645ad238e7b"
    },
    {
      "category": "company",
      "datetime": 1788798960,
      "headline": "NetApp Q1 Beat and Raised Guidance Put AI Storage Growth in Focus",
      "id": 141772583,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPE",
      "source": "Yahoo",
      "summary": "NetApp's fiscal Q1 beat and raised 2027 outlook spotlight AI storage demand, record flash and cloud sales, and the margin test ahead.",
      "url": "https://finnhub.io/api/news?id=4824c960c8e42964504600f596bb569e370fa1cc4f80ea9594e07e0a2b3f7d59"
    }
  ],
  "polygon_news": [
    {
      "id": "d4e923ca32b570b4a0c4b248e45db949f7f072b91bb1b84c886260da4425d5e8",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Should You Buy NetApp Stock as AI Growth Meets a Premium Valuation?",
      "author": "Na",
      "published_utc": "2026-09-07T16:23:00Z",
      "article_url": "https://www.zacks.com/stock/news/2986067/should-you-buy-netapp-stock-as-ai-growth-meets-a-premium-valuation?cid=CS-ZC-FT-analyst_blog_plus|zer_report_insights-2986067",
      "tickers": [
        "NTAP",
        "DELL",
        "HPE",
        "HPEpC"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/46/91388.jpg",
      "description": "NetApp raised its fiscal 2027 revenue guidance to $7.975-$8.225 billion (17% growth midpoint) driven by accelerating AI, flash storage, and cloud demand. All-flash revenues surged 46.6% to $1.31B in Q1 FY2027 with approximately 350 AI deals added. However, the stock trades at a premium valuation of 19.5X forward earnings versus its sub-industry average of 10.7X, with gross margin pressure from higher component costs and product mix shifts limiting upside.",
      "keywords": [
        "NetApp",
        "AI demand",
        "flash storage",
        "revenue guidance",
        "valuation premium",
        "gross margin pressure",
        "enterprise storage"
      ],
      "insights": [
        {
          "ticker": "NTAP",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong AI and flash storage growth with 46.6% all-flash revenue increase and 350 new AI deals in Q1. Revenue guidance raised to 17% growth midpoint. However, positive sentiment is tempered by premium valuation (19.5X forward earnings) and gross margin compression, creating execution risk."
        },
        {
          "ticker": "DELL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive threat with expanded AI Data Platform with NVIDIA for demanding AI workloads, indicating competitive pressure in enterprise AI storage market."
        },
        {
          "ticker": "HPE",
          "sentiment": "neutral",
          "sentiment_reasoning": "Noted as competitor adding native file storage and AI-driven data-management capabilities to Alletra Storage MP X10000, reinforcing competitive pressure in enterprise AI storage space."
        },
        {
          "ticker": "HPEpC",
          "sentiment": "neutral",
          "sentiment_reasoning": "Noted as competitor adding native file storage and AI-driven data-management capabilities to Alletra Storage MP X10000, reinforcing competitive pressure in enterprise AI storage space."
        }
      ]
    },
    {
      "id": "0d9a63516012bca4dd4e7280ad9d1010d6600d44138f4724c92a044b53f03bcb",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "NTAP Stock Up 14.8% in 3 Months Can AI Momentum Keep It Climbing?",
      "author": "Na",
      "published_utc": "2026-09-07T16:18:00Z",
      "article_url": "https://www.zacks.com/stock/news/2986063/ntap-stock-up-14-8-in-3-months-can-ai-momentum-keep-it-climbing?cid=CS-ZC-FT-analyst_blog_plus|zer_report_insights-2986063",
      "tickers": [
        "NTAP",
        "DELL",
        "HPE",
        "HPEpC"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/7f/211.jpg",
      "description": "NetApp shares gained 14.8% over three months driven by record all-flash revenue growth of 46.6%, approximately 350 new AI and data lake modernization deals, and a strong Q1 earnings beat. The company raised fiscal 2027 revenue guidance to $7.975-$8.225 billion and earnings to $9.73-$10.03 per share. However, margin pressures from component costs and demand timing risks remain concerns.",
      "keywords": [
        "NetApp",
        "AI storage",
        "all-flash growth",
        "earnings beat",
        "guidance raise",
        "margin pressure",
        "data lake modernization"
      ],
      "insights": [
        {
          "ticker": "NTAP",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong Q1 earnings beat (9.9% revenue beat, 21.1% EPS beat), record all-flash revenue growth of 46.6%, approximately 350 new AI deals with customers moving to production workloads, and significantly raised fiscal 2027 guidance ($650M above prior guidance). Zacks Rank #2 (Buy) with Momentum Score of A supports positive outlook."
        },
        {
          "ticker": "DELL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive threat expanding its AI Data Platform with file, object and parallel-file storage capabilities, indicating active competition in the AI storage market but no specific performance data provided."
        },
        {
          "ticker": "HPE",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive threat advancing Alletra Storage MP X10000 with AI data pipeline capabilities, indicating active competition in the AI storage market but no specific performance data provided."
        },
        {
          "ticker": "HPEpC",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive threat advancing Alletra Storage MP X10000 with AI data pipeline capabilities, indicating active competition in the AI storage market but no specific performance data provided."
        }
      ]
    },
    {
      "id": "b6bb95290d505b25c8336bcef21b58452f435b5777c898940294272a48b2a9cc",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Interpreting Hewlett Packard Enterprise (HPE) International Revenue Trends",
      "author": "Zacks.Com",
      "published_utc": "2026-09-07T13:15:02Z",
      "article_url": "https://www.zacks.com/stock/news/2985679/interpreting-hewlett-packard-enterprise-hpe-international-revenue-trends?cid=CS-ZC-FT-fundamental_analysis|nfm_international_revenues-2985679",
      "tickers": [
        "HPE",
        "HPEpC"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default286.jpg",
      "description": "HPE reported Q3 2026 total revenue of $12.21 billion, up 33.7% year-over-year, with strong international performance. Europe, Middle East and Africa generated $4.2 billion (34.4% of total), beating analyst expectations by 3.48%, while Asia Pacific and Japan contributed $2.67 billion (21.8%), exceeding estimates by 4.16%. Analysts project continued growth with FY2026 revenue expected at $46.04 billion, up 34.3% annually. HPE holds a Zacks Rank #1 (Strong Buy) rating, though the stock declined 2.3% over the past month.",
      "keywords": [
        "international revenue",
        "quarterly earnings",
        "Europe Middle East Africa",
        "Asia Pacific Japan",
        "revenue growth",
        "analyst estimates",
        "stock rating"
      ],
      "insights": [
        {
          "ticker": "HPE",
          "sentiment": "positive",
          "sentiment_reasoning": "HPE exceeded analyst expectations in both major international segments (EMEA and APAC), demonstrated strong year-over-year revenue growth of 33.7%, and received a Zacks Rank #1 (Strong Buy) rating. Projected full-year revenue growth of 34.3% indicates continued positive momentum, despite recent short-term stock price decline."
        },
        {
          "ticker": "HPEpC",
          "sentiment": "positive",
          "sentiment_reasoning": "HPE exceeded analyst expectations in both major international segments (EMEA and APAC), demonstrated strong year-over-year revenue growth of 33.7%, and received a Zacks Rank #1 (Strong Buy) rating. Projected full-year revenue growth of 34.3% indicates continued positive momentum, despite recent short-term stock price decline."
        }
      ]
    },
    {
      "id": "03dcc644faebb5eae87659a81f248ebc9da6b619429422c2459744cf5146a7bc",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Stock Market News for Sep 4, 2026",
      "author": "Na",
      "published_utc": "2026-09-04T09:09:00Z",
      "article_url": "https://www.zacks.com/stock/news/2984866/stock-market-news-for-sep-4-2026?cid=CS-ZC-FT-market_news-2984866",
      "tickers": [
        "SNOW",
        "HPE",
        "HPEpC",
        "XLB",
        "XLC"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/25/169734.webp",
      "description": "U.S. stock markets rose on Thursday as Treasury yields declined globally, easing Fed rate hike concerns. The Dow Jones gained 1.2%, Nasdaq Composite advanced 1.4%, and S&P 500 rose 1.1%. Strong earnings from Snowflake and Hewlett Packard Enterprise drove gains, though economic data showed mixed signals with initial jobless claims rising slightly and the trade deficit exceeding expectations.",
      "keywords": [
        "stock market",
        "Treasury yields",
        "Fed funds rate",
        "earnings results",
        "jobless claims",
        "trade deficit",
        "Dow Jones",
        "Nasdaq",
        "S&P 500"
      ],
      "insights": [
        {
          "ticker": "SNOW",
          "sentiment": "positive",
          "sentiment_reasoning": "Beat earnings estimates ($0.62 vs $0.45 consensus) and revenue expectations (4.91% above estimate). Stock jumped 16.6% and carries Zacks Rank #2 (Buy)."
        },
        {
          "ticker": "HPE",
          "sentiment": "positive",
          "sentiment_reasoning": "Exceeded earnings estimates ($1.11 vs $0.95 consensus) and revenue expectations (1% above estimate). Stock rose 5% and carries Zacks Rank #2 (Buy)."
        },
        {
          "ticker": "HPEpC",
          "sentiment": "positive",
          "sentiment_reasoning": "Exceeded earnings estimates ($1.11 vs $0.95 consensus) and revenue expectations (1% above estimate). Stock rose 5% and carries Zacks Rank #2 (Buy)."
        },
        {
          "ticker": "XLB",
          "sentiment": "positive",
          "sentiment_reasoning": "Sector rose 1.7% on the day as part of broad market gains."
        },
        {
          "ticker": "XLC",
          "sentiment": "positive",
          "sentiment_reasoning": "Sector rose 1.4% on the day as part of broad market gains."
        }
      ]
    },
    {
      "id": "175552d3c83c1e9d7a26b8e9c8d0d897f87a4594958fd124fd8b23595732e079",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "AI Infrastructure Demand Remains Red-Hot: HPE, AVGO, DELL Deliver",
      "author": "Na",
      "published_utc": "2026-09-03T22:02:00Z",
      "article_url": "https://www.zacks.com/stock/news/2984815/ai-infrastructure-demand-remains-red-hot-hpe-avgo-dell-deliver?cid=CS-ZC-FT-stocks_in_the_news-2984815",
      "tickers": [
        "HPE",
        "HPEpC",
        "AVGO",
        "DELL"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/63/173536.webp",
      "description": "Hewlett Packard Enterprise, Broadcom, and Dell Technologies all reported strong quarterly earnings driven by AI infrastructure demand. HPE posted record revenue of $12.2B with 34% YoY growth and raised FY26-27 guidance. Broadcom delivered $29.6B revenue (86% YoY growth) with AI semiconductor revenue surging 221% YoY. Dell achieved record $47B revenue (58% YoY growth) with a massive $95B AI server backlog. All three companies provided upbeat forward guidance, though market reactions were mixed as expectations remain sky-high.",
      "keywords": [
        "AI infrastructure",
        "earnings results",
        "server demand",
        "networking products",
        "custom accelerators",
        "guidance raise",
        "backlog growth"
      ],
      "insights": [
        {
          "ticker": "HPE",
          "sentiment": "positive",
          "sentiment_reasoning": "Record quarterly revenue of $12.2B with 34% YoY growth, strong AI Systems orders of $2.4B, backlog of $6.8B, and raised FY26-27 revenue and EPS guidance. Zacks Rank #2 (Buy) rating supports positive outlook."
        },
        {
          "ticker": "HPEpC",
          "sentiment": "positive",
          "sentiment_reasoning": "Record quarterly revenue of $12.2B with 34% YoY growth, strong AI Systems orders of $2.4B, backlog of $6.8B, and raised FY26-27 revenue and EPS guidance. Zacks Rank #2 (Buy) rating supports positive outlook."
        },
        {
          "ticker": "AVGO",
          "sentiment": "positive",
          "sentiment_reasoning": "Exceptional $29.6B revenue (86% YoY growth) with AI semiconductor revenue surging 221% YoY. Strong forward guidance with $21.7B AI semiconductor revenue expected next quarter and $115B for FY27. However, stock traded lower post-earnings due to sky-high expectations already priced in."
        },
        {
          "ticker": "DELL",
          "sentiment": "positive",
          "sentiment_reasoning": "Record $47B revenue (58% YoY growth) with AI-Optimized Server revenue doubling to $16.4B. Record $60.9B AI server orders and massive $95B backlog provide strong visibility. Raised FY27 revenue guidance by $25B and boosted AI server revenue expectations. Zacks Rank #2 (Buy) rating."
        }
      ]
    }
  ],
  "earnings": [
    {
      "symbol": "HPE",
      "date": "2026-12-02",
      "hour": "amc",
      "quarter": 4,
      "year": 2026,
      "epsEstimate": 1.0796,
      "epsActual": null,
      "revenueEstimate": 13090231330,
      "revenueActual": null
    }
  ],
  "fundamentals": {
    "10DayAverageTradingVolume": 27.37653,
    "13WeekPriceReturnDaily": -3.1477,
    "26WeekPriceReturnDaily": 140.2957,
    "3MonthADReturnStd": 57.576866,
    "3MonthAverageTradingVolume": 24.28093,
    "52WeekHigh": 64.25,
    "52WeekHighDate": "2026-06-02",
    "52WeekLow": 19.84,
    "52WeekLowDate": "2026-02-24",
    "52WeekPriceReturnDaily": 121.0884,
    "5DayPriceReturnDaily": -0.4594,
    "assetTurnoverAnnual": 0.4518,
    "assetTurnoverTTM": 0.5321,
    "beta": 1.470885,
    "bookValuePerShareAnnual": 18.7273,
    "bookValuePerShareQuarterly": 19.9654,
    "bookValueShareGrowth5Y": 8.47,
    "capexCagr5Y": -0.78,
    "cashFlowPerShareAnnual": 0.4756,
    "cashFlowPerShareQuarterly": 3.1295,
    "cashFlowPerShareTTM": 2.79077,
    "cashPerSharePerShareAnnual": 4.3792,
    "cashPerSharePerShareQuarterly": 4.6807,
    "currentDividendYieldTTM": 1.2417,
    "currentEv/freeCashFlowAnnual": 132.1955,
    "currentEv/freeCashFlowTTM": 19.9438,
    "currentRatioAnnual": 1.0142,
    "currentRatioQuarterly": 1.1127,
    "dividendGrowthRate5Y": 4.91,
    "dividendIndicatedAnnual": 0.57,
    "dividendPerShareAnnual": 0.6087,
    "dividendPerShareTTM": 0.6461,
    "dividendYieldIndicatedAnnual": 3.03222,
    "ebitdPerShareAnnual": 0.2032,
    "ebitdPerShareTTM": 3.019,
    "ebitdaCagr5Y": null,
    "ebitdaInterimCagr5Y": 37.3,
    "enterpriseValue": 82886.58,
    "epsAnnual": 0.0431,
    "epsBasicExclExtraItemsAnnual": 0.0431,
    "epsBasicExclExtraItemsTTM": 1.9631999999999998,
    "epsExclExtraItemsAnnual": 0.0431,
    "epsExclExtraItemsTTM": 1.9631999999999998,
    "epsGrowth3Y": -59.66,
    "epsGrowth5Y": null,
    "epsGrowthQuarterlyYoy": 395.25,
    "epsGrowthTTMYoy": 128.23,
    "epsInclExtraItemsAnnual": 0.0431,
    "epsInclExtraItemsTTM": 1.9631999999999998,
    "epsNormalizedAnnual": 0.0431,
    "epsTTM": 1.9631999999999998,
    "evEbitdaTTM": 19.7161,
    "evRevenueTTM": 1.9796,
    "focfCagr5Y": null,
    "forwardPE": 12.12384,
    "forwardPEG": 0.38125,
    "grossMargin5Y": 33.06,
    "grossMarginAnnual": 30.26,
    "grossMarginTTM": 36.76,
    "inventoryTurnoverAnnual": 3.3779,
    "inventoryTurnoverTTM": 2.7893,
    "longTermDebt/equityAnnual": 0.7182,
    "longTermDebt/equityQuarterly": 0.6541,
    "marketCapitalization": 68858.58,
    "monthToDatePriceReturnDaily": -0.4594,
    "netIncomeEmployeeAnnual": 0.0009,
    "netIncomeEmployeeTTM": 0.0417,
    "netInterestCoverageAnnual": 9.4391,
    "netInterestCoverageTTM": -0.993,
    "netMarginGrowth5Y": null,
    "netProfitMargin5Y": 6.21,
    "netProfitMarginAnnual": 0.17,
    "netProfitMarginTTM": 6.67,
    "operatingMargin5Y": 6.33,
    "operatingMarginAnnual": -0.71,
    "operatingMarginTTM": 7.03,
    "payoutRatioAnnual": 1396.49,
    "payoutRatioTTM": 30.63,
    "pb": 2.5971,
    "pbAnnual": 1.3047,
    "pbQuarterly": 2.3923,
    "pcfShareAnnual": 23.5898,
    "pcfShareTTM": 10.2866,
    "peAnnual": 1208.0453,
    "peBasicExclExtraTTM": 24.6717,
    "peExclExtraAnnual": 24.10978,
    "peExclExtraTTM": 24.6717,
    "peInclExtraTTM": 24.6717,
    "peNormalizedAnnual": 1208.0453,
    "peTTM": 24.6717,
    "pegTTM": 1.38299,
    "pfcfShareAnnual": 109.8223,
    "pfcfShareTTM": 16.5685,
    "pretaxMargin5Y": 6.52,
    "pretaxMarginAnnual": -0.83,
    "pretaxMarginTTM": 6.29,
    "priceRelativeToS&P50013Week": -4.878,
    "priceRelativeToS&P50026Week": 127.0874,
    "priceRelativeToS&P5004Week": -4.5338,
    "priceRelativeToS&P50052Week": 102.0924,
    "priceRelativeToS&P500Ytd": 103.542,
    "psAnnual": 2.0078,
    "psTTM": 1.6445,
    "ptbvAnnual": 1.7582,
    "ptbvQuarterly": 1.9604,
    "quickRatioAnnual": 0.7565,
    "quickRatioQuarterly": 0.7242,
    "receivablesTurnoverAnnual": 7.7593,
    "receivablesTurnoverTTM": 7.0722,
    "revenueEmployeeAnnual": 0.5119,
    "revenueEmployeeTTM": 0.6249,
    "revenueGrowth3Y": 6.37,
    "revenueGrowth5Y": 4.91,
    "revenueGrowthQuarterlyYoy": 33.68,
    "revenueGrowthTTMYoy": 26.59,
    "revenuePerShareAnnual": 25.9033,
    "revenuePerShareTTM": 28.8965,
    "revenueShareGrowth5Y": 4.43,
    "roa5Y": 2.94,
    "roaRfy": 0.08,
    "roaTTM": 3.55,
    "roe5Y": 8.34,
    "roeRfy": 0.22999999999999998,
    "roeTTM": 11.020000000000001,
    "roi5Y": 5.02,
    "roiAnnual": 0.12,
    "roiTTM": 5.9799999999999995,
    "tangibleBookValuePerShareAnnual": 13.8968,
    "tangibleBookValuePerShareQuarterly": 14.7148,
    "tbvCagr5Y": 4.15,
    "totalDebt/totalEquityAnnual": 0.9059,
    "totalDebt/totalEquityQuarterly": 0.7635,
    "yearToDatePriceReturnDaily": 116.4863
  },
  "source_status": {
    "local_research": false,
    "local_news": false,
    "local_sec_filings": false,
    "finnhub_news": true,
    "polygon_news": true,
    "earnings": true,
    "fundamentals": true
  }
}
```

## NVDA
Trading candidate:
```json
{
  "symbol": "NVDA",
  "score": 79.54,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 100.0,
    "sector": 83.0,
    "relative_strength": 79.54165686072787,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 12.83559201459996,
    "momentum": 72.4784931630897,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 86.00058171704516
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
      "datetime": 1788890700,
      "headline": "Which S&P500 stocks are the most active on Tuesday?",
      "id": 141952860,
      "image": "https://www.chartmill.com/images/uploads/CM_Most_Active_Stocks_Small_free_fec0650b7f.webp",
      "related": "NVDA",
      "source": "ChartMill",
      "summary": "Stay informed about the most active stocks in the S&P500 index on Tuesday's session. Discover the stocks that are generating the highest trading volume and driving market activity.",
      "url": "https://finnhub.io/api/news?id=71df634472679672cbba113b47bdb93092bfd0fa038e96e7e1e616b1bf5b7146"
    },
    {
      "category": "company",
      "datetime": 1788890400,
      "headline": "Curious about the most active stocks on Tuesday?",
      "id": 141952859,
      "image": "https://www.chartmill.com/images/uploads/CM_Most_Active_Stocks_Small_free_fec0650b7f.webp",
      "related": "NVDA",
      "source": "ChartMill",
      "summary": "These stocks are making the most noise in today's session. Stay tuned for the latest updates!",
      "url": "https://finnhub.io/api/news?id=e7ff2c19b1ea0dd0b5fc7c743285265a03298aa5dceb13fe5ea04cab8325a641"
    },
    {
      "category": "company",
      "datetime": 1788889797,
      "headline": "Does Michael Burry Have It Wrong? Nvidia Chips Retain Value, Data Shows",
      "id": 141952505,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NVDA",
      "source": "Yahoo",
      "summary": "Six-year-old A100 chips from Nvidia Corp. (NASDAQ:NVDA) are still valued at nearly $5,000 each, complicating Michael Burry\u2019s warning that Big Tech may be overstating profits by depreciating AI hardware over five or six years. Silicon Data estimates the A100\u2019s residual...",
      "url": "https://finnhub.io/api/news?id=a620b1afece6eac95e5ea96128771a32ec6085f430adeab8403f7c5d1b0bb56c"
    },
    {
      "category": "company",
      "datetime": 1788888901,
      "headline": "The Earnings Report That Could Move the Market",
      "id": 141952491,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NVDA",
      "source": "Yahoo",
      "summary": "The earnings report for Nvidia, the world's most valuable company, could have huge economic ramifications.",
      "url": "https://finnhub.io/api/news?id=fe8f338510a9436ca464629f930125d69fbab8a9f51f1c7db990cde157ab9092"
    },
    {
      "category": "company",
      "datetime": 1788888900,
      "headline": "Forget Occidental Petroleum. Buy This Pipeline Stock in September Instead.",
      "id": 141952500,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NVDA",
      "source": "Yahoo",
      "summary": "The Williams Companies is a more stable investment than the upstream company.",
      "url": "https://finnhub.io/api/news?id=d7b4b1d7a2a84e52d0b3f55ca76193f9b883d73bdc64d683d17fb5459e91c0a5"
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

## HPQ
Trading candidate:
```json
{
  "symbol": "HPQ",
  "score": 78.97,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 100.0,
    "sector": 83.0,
    "relative_strength": 84.71272156158881,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 13.732236173443408,
    "momentum": 71.38907395069955,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 54.250848361539035
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
      "datetime": 1788873000,
      "headline": "Best Income Stocks to Buy for September 8th",
      "id": 141951207,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPQ",
      "source": "Yahoo",
      "summary": "HPQ, E and VAC made it to the Zacks Rank #1 (Strong Buy) income stocks list on September 8, 2026.",
      "url": "https://finnhub.io/api/news?id=489571dd3f7e575abd3edee9fa5ca36f177d1da2b5e4e9d3a5cfe3f89dbf56d3"
    },
    {
      "category": "company",
      "datetime": 1788871638,
      "headline": "3 Reasons HPQ is Risky and 1 Stock to Buy Instead",
      "id": 141951208,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPQ",
      "source": "Yahoo",
      "summary": "What a fantastic six months it\u2019s been for HP. Shares of the company have skyrocketed 72.5%, setting a new 52-week high of $32.65. This was partly due to its solid quarterly results, and the run-up might have investors contemplating their next move.",
      "url": "https://finnhub.io/api/news?id=af0e42462bc96858cd3e2547f3af93ca20836858d2d390f90cb5edc689be331c"
    },
    {
      "category": "company",
      "datetime": 1788850202,
      "headline": "Why Lenovo Is A Better Buy Than Dell And HP Inc.",
      "id": 141925484,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/2277199191/image_2277199191.jpg?io=getty-c-w1536",
      "related": "HPQ",
      "source": "SeekingAlpha",
      "summary": "Lenovo Group is rapidly transitioning from a traditional PC maker to a leading AI and data center infrastructure provider. Read more on LNVGY stock here.",
      "url": "https://finnhub.io/api/news?id=55fb7be51bd71099957556c9e2ff5d7ecc98673779ecec431ab8db877bd914e8"
    },
    {
      "category": "company",
      "datetime": 1788799800,
      "headline": "DELL Expands Consumer PC Reach: Can It Challenge HPQ & AAPL?",
      "id": 141771352,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPQ",
      "source": "Yahoo",
      "summary": "Dell Technologies broadens its consumer PC reach with the affordable Dell 14S as PC demand improves and competition from HP and Apple intensifies.",
      "url": "https://finnhub.io/api/news?id=4827504f7d6cf76007c1a9eb3a66bf9032af94ad171d57b69d8f65e679074aeb"
    },
    {
      "category": "company",
      "datetime": 1788712877,
      "headline": "Wall Street Brunch: Make Or Break Inflation For The Fed",
      "id": 141592954,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/2165462299/image_2165462299.jpg?io=getty-c-w1536",
      "related": "HPQ",
      "source": "SeekingAlpha",
      "summary": "Listen on the go! A daily podcast of Wall Street Breakfast will be available by 8:00 a.m.",
      "url": "https://finnhub.io/api/news?id=07e2229b955b49ac631b54d0a8f3eab1902e7f0d9aaa160b4e9c708385a77726"
    }
  ],
  "polygon_news": [
    {
      "id": "d29ea6357f286f70507c2c959a59cc9e25a8857bea43fe72afc3ee1696875b5e",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Best Income Stocks to Buy for September 8th",
      "author": "Na",
      "published_utc": "2026-09-08T13:10:00Z",
      "article_url": "https://www.zacks.com/commentary/2986428/best-income-stocks-to-buy-for-september-8th?cid=CS-ZC-FT-zacks_1_rank_additions|income_additions-2986428",
      "tickers": [
        "HPQ",
        "E",
        "VAC"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/61/32891.jpg",
      "description": "Zacks highlights three Rank #1 (Strong Buy) stocks with attractive dividend yields: HP Inc. (3.7% yield), Eni (3.2% yield), and Marriott Vacations Worldwide (3% yield). All three companies have seen their consensus earnings estimates increase over the last 60 days, making them suitable for income-focused investors.",
      "keywords": [
        "dividend yield",
        "strong buy",
        "income stocks",
        "earnings growth",
        "Zacks Rank #1"
      ],
      "insights": [
        {
          "ticker": "HPQ",
          "sentiment": "positive",
          "sentiment_reasoning": "Zacks Rank #1 (Strong Buy) rating with 8.4% earnings estimate increase over 60 days and dividend yield of 3.7%, significantly above industry average of 0.5%"
        },
        {
          "ticker": "E",
          "sentiment": "positive",
          "sentiment_reasoning": "Zacks Rank #1 rating with 14.5% earnings estimate increase over 60 days and dividend yield of 3.2%, above industry average of 1.3%"
        },
        {
          "ticker": "VAC",
          "sentiment": "positive",
          "sentiment_reasoning": "Zacks Rank #1 rating with 12.2% earnings estimate increase over 60 days and dividend yield of 3%, compared to industry average of 0.0%"
        }
      ]
    },
    {
      "id": "a4e058b4e26d8841f31c034b280bcce7bcbebbae4ce6a2d8fbba8829ff8c9aff",
      "publisher": {
        "name": "GlobeNewswire Inc.",
        "homepage_url": "https://www.globenewswire.com",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/globenewswire.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/globenewswire.ico"
      },
      "title": "HP Announces New OmniBook PCs to Help Build the Next Generation of AI Experiences",
      "author": "Hp Inc.",
      "published_utc": "2026-09-04T18:00:00Z",
      "article_url": "https://www.globenewswire.com/news-release/2026/09/04/3356745/0/en/hp-announces-new-omnibook-pcs-to-help-build-the-next-generation-of-ai-experiences.html",
      "tickers": [
        "NVDA",
        "HPQ"
      ],
      "image_url": "https://ml.globenewswire.com/Resource/Download/1a361f11-9579-42e3-87fd-57c5caea29fc",
      "description": "HP Inc. unveiled its new HP OmniBook Ultra 16 and HP OmniBook X 14 laptops, along with the upcoming HP OmniDesk, all powered by NVIDIA RTX Spark technology. These devices are designed for creators, developers, gamers, and AI users, featuring personal agents, local AI capabilities, advanced content creation tools, and premium designs. The OmniBook Ultra 16 offers up to 128GB memory and sustained AI workload support, while the OmniBook X 14 provides portability with AI capabilities. Both laptops are expected to launch this fall.",
      "keywords": [
        "AI PCs",
        "NVIDIA RTX Spark",
        "OmniBook Ultra 16",
        "OmniBook X 14",
        "OmniDesk",
        "personal agents",
        "local AI",
        "content creation",
        "Windows",
        "thin laptops"
      ],
      "insights": [
        {
          "ticker": "NVDA",
          "sentiment": "positive",
          "sentiment_reasoning": "NVIDIA's RTX Spark platform is being prominently featured as the core technology powering HP's new premium AI PC lineup. The partnership demonstrates NVIDIA's successful expansion into mainstream consumer AI computing and validates its full-stack AI platform strategy. The integration into multiple device categories (laptops and desktops) shows broad adoption and market traction for NVIDIA's AI technologies."
        },
        {
          "ticker": "HPQ",
          "sentiment": "positive",
          "sentiment_reasoning": "HP is expanding its AI PC portfolio with innovative new products featuring cutting-edge NVIDIA RTX Spark technology. The announcement demonstrates strong product development, premium design capabilities, and strategic positioning in the growing AI computing market. The devices address multiple user segments (creators, developers, gamers) and feature impressive specifications (up to 128GB memory, extended battery life, thin designs), indicating competitive strength and market confidence."
        }
      ]
    },
    {
      "id": "c2d62b22670a931552c86d857be2cab3fadcb36f8f7a02642a112091262242a9",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Dell Technologies Inc. (DELL) Hit a 52 Week High, Can the Run Continue?",
      "author": "Zacks.Com",
      "published_utc": "2026-09-04T13:15:03Z",
      "article_url": "https://www.zacks.com/stock/news/2984979/dell-technologies-inc-dell-hit-a-52-week-high-can-the-run-continue?cid=CS-ZC-FT-52_week_high-2984979",
      "tickers": [
        "DELL",
        "HPQ"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default345.jpg",
      "description": "Dell Technologies has surged 310.2% year-to-date, hitting a new 52-week high of $530.78. The stock maintains a Zacks Rank #1 (Strong Buy) rating driven by consistent earnings beats and strong growth projections. While valuation metrics show the stock trading in line with peer averages, its PEG ratio of 0.76 and favorable analyst revisions suggest potential for continued gains in the coming weeks and months.",
      "keywords": [
        "52-week high",
        "earnings surprise",
        "Zacks Rank #1",
        "valuation metrics",
        "growth stock",
        "technology sector"
      ],
      "insights": [
        {
          "ticker": "DELL",
          "sentiment": "positive",
          "sentiment_reasoning": "Stock up 310.2% YTD with consistent earnings beats (4 consecutive quarters), Zacks Rank #1 (Strong Buy), strong EPS growth projections (98.83% current year, 21.62% next year), and favorable analyst estimate revisions. PEG ratio of 0.76 suggests reasonable valuation despite 52-week high."
        },
        {
          "ticker": "HPQ",
          "sentiment": "positive",
          "sentiment_reasoning": "Zacks Rank #2 (Buy) with strong Value Score of A and Momentum Score of A. Beat earnings consensus by 10.67% last quarter. Trading at attractive forward P/E of 9.88X and P/CF of 7.68X, outperforming DELL on valuation metrics."
        }
      ]
    },
    {
      "id": "dfa5ee8eb2e2e8f9259f1effd7c85c18325086e72a150e72bab455b6613b3eb6",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Apple's Shares Rise 2.6% as John Ternus Takes Over as CEO",
      "author": "Na",
      "published_utc": "2026-09-02T12:07:00Z",
      "article_url": "https://www.zacks.com/stock/news/2983545/apple-s-shares-rise-2-6-as-john-ternus-takes-over-as-ceo?cid=CS-ZC-FT-analyst_blog|company_news_corporate_actions-2983545",
      "tickers": [
        "AAPL",
        "DELL",
        "HPQ"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/94/53.jpg",
      "description": "John Ternus officially took over as Apple's CEO on September 1, succeeding Tim Cook after nearly 15 years. The leadership transition boosted Apple shares by 2.6%. Ternus, who joined Apple in 2001 and led hardware engineering, faces pressure to accelerate the company's AI strategy while maintaining its product ecosystem. Cook transitioned to executive chairman focusing on government relations. The market welcomed the succession, viewing it as providing continuity while enabling innovation.",
      "keywords": [
        "Apple CEO transition",
        "John Ternus",
        "Tim Cook",
        "AI strategy",
        "leadership change",
        "executive chairman",
        "product innovation"
      ],
      "insights": [
        {
          "ticker": "AAPL",
          "sentiment": "positive",
          "sentiment_reasoning": "Stock gained 2.6% on the CEO transition announcement. Investors welcomed the succession as providing continuity while enabling acceleration of AI strategy. Ternus's long tenure and experience with key products (iPad, Mac, AirPods, Vision Pro) suggests confidence in his leadership capability."
        },
        {
          "ticker": "DELL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a peer comparison with strong performance (237.6% YTD gain) and Zacks Rank #1 rating, but no direct news or sentiment drivers related to this article's main topic."
        },
        {
          "ticker": "HPQ",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a peer comparison with moderate performance (40.6% YTD gain) and Zacks Rank #2 rating, but no direct news or sentiment drivers related to this article's main topic."
        }
      ]
    },
    {
      "id": "67c22598e51be4533235b444f35902dfb038b48d8479f5a6319234856fb2bede",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Earnings Estimates Moving Higher for HP (HPQ): Time to Buy?",
      "author": "Na",
      "published_utc": "2026-08-31T16:20:02Z",
      "article_url": "https://www.zacks.com/stock/news/2982728/earnings-estimates-moving-higher-for-hp-hpq-time-to-buy?cid=CS-ZC-FT-fundamental_analysis|yseop_template_8-2982728",
      "tickers": [
        "HPQ"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default183.jpg",
      "description": "HP (HPQ) has received positive analyst attention with upward earnings estimate revisions, earning a Zacks Rank #2 (Buy) rating. The company's consensus estimates for the current quarter and full year have improved significantly over the past month, with the stock gaining 11.9% in four weeks. Analysts expect HP to earn $0.74 per share for the current quarter and $3.15 for the full year.",
      "keywords": [
        "earnings estimate revisions",
        "Zacks Rank",
        "consensus estimates",
        "stock performance",
        "analyst ratings"
      ],
      "insights": [
        {
          "ticker": "HPQ",
          "sentiment": "positive",
          "sentiment_reasoning": "HP received multiple upward earnings estimate revisions over the past month with no negative revisions. The company earned a Zacks Rank #2 (Buy) rating based on improving consensus estimates for both the current quarter and full year. The stock has gained 11.9% over four weeks, reflecting investor confidence in its earnings growth prospects."
        }
      ]
    }
  ],
  "earnings": [
    {
      "symbol": "HPQ",
      "date": "2026-11-23",
      "hour": "amc",
      "quarter": 4,
      "year": 2026,
      "epsEstimate": 0.7038,
      "epsActual": null,
      "revenueEstimate": 15418810399,
      "revenueActual": null
    }
  ],
  "fundamentals": {
    "10DayAverageTradingVolume": 18.1084,
    "13WeekPriceReturnDaily": 24.1065,
    "26WeekPriceReturnDaily": 71.6991,
    "3MonthADReturnStd": 44.1315,
    "3MonthAverageTradingVolume": 17.64388,
    "52WeekHigh": 32.78,
    "52WeekHighDate": "2026-09-04",
    "52WeekLow": 17.56,
    "52WeekLowDate": "2026-02-25",
    "52WeekPriceReturnDaily": 11.2474,
    "5DayPriceReturnDaily": 8.7275,
    "assetTurnoverAnnual": 1.3238,
    "assetTurnoverTTM": 1.3763,
    "beta": 1.2074418,
    "bookValuePerShareAnnual": 15.3925,
    "bookValuePerShareQuarterly": 15.3925,
    "bookValueShareGrowth5Y": -3.46,
    "capexCagr5Y": 9.11,
    "cashFlowPerShareAnnual": 3.0402,
    "cashFlowPerShareQuarterly": 4.2437,
    "cashFlowPerShareTTM": 4.11043,
    "cashPerSharePerShareAnnual": 4.0065,
    "cashPerSharePerShareQuarterly": 4.5587,
    "currentDividendYieldTTM": 3.7201,
    "currentEv/freeCashFlowAnnual": 12.2948,
    "currentEv/freeCashFlowTTM": 8.8703,
    "currentRatioAnnual": 0.7674,
    "currentRatioQuarterly": 0.7875,
    "dividendGrowthRate5Y": 10.14,
    "dividendIndicatedAnnual": 1.2,
    "dividendPerShareAnnual": 1.1699,
    "dividendPerShareTTM": 1.1815,
    "dividendYieldIndicatedAnnual": 3.84916,
    "ebitdPerShareAnnual": 3.6789,
    "ebitdPerShareTTM": 3.718,
    "ebitdaCagr5Y": -0.16,
    "ebitdaInterimCagr5Y": -7.23,
    "enterpriseValue": 34425.459,
    "epsAnnual": 2.6537,
    "epsBasicExclExtraItemsAnnual": 2.6537,
    "epsBasicExclExtraItemsTTM": 2.6239,
    "epsExclExtraItemsAnnual": 2.6537,
    "epsExclExtraItemsTTM": 2.6239,
    "epsGrowth3Y": -3.82,
    "epsGrowth5Y": 5.79,
    "epsGrowthQuarterlyYoy": -10.84,
    "epsGrowthTTMYoy": -4.42,
    "epsInclExtraItemsAnnual": 2.6537,
    "epsInclExtraItemsTTM": 2.6239,
    "epsNormalizedAnnual": 2.6537,
    "epsTTM": 2.6239,
    "evEbitdaTTM": 9.9266,
    "evRevenueTTM": 0.5819,
    "focfCagr5Y": -5.6,
    "forwardPE": 8.9253,
    "forwardPEG": 2.66427,
    "grossMargin5Y": 20.94,
    "grossMarginAnnual": 20.6,
    "grossMarginTTM": 19.87,
    "inventoryTurnoverAnnual": 5.4094,
    "inventoryTurnoverTTM": 5.0759,
    "longTermDebt/equityAnnual": 0.2405,
    "longTermDebt/equityQuarterly": 0.2405,
    "marketCapitalization": 29434.459,
    "monthToDatePriceReturnDaily": 8.7275,
    "netIncomeEmployeeAnnual": 0.046,
    "netIncomeEmployeeTTM": 0.0446,
    "netInterestCoverageAnnual": 8.1327,
    "netInterestCoverageTTM": 8.824,
    "netMarginGrowth5Y": -1.86,
    "netProfitMargin5Y": 6.22,
    "netProfitMarginAnnual": 4.57,
    "netProfitMarginTTM": 4.14,
    "operatingMargin5Y": 7.78,
    "operatingMarginAnnual": 5.83,
    "operatingMarginTTM": 5.45,
    "payoutRatioAnnual": 43.02,
    "payoutRatioTTM": 44.68,
    "pb": 1.06,
    "pbAnnual": 0.8956,
    "pbQuarterly": 0.8956,
    "pcfShareAnnual": 7.9617,
    "pcfShareTTM": 6.3056,
    "peAnnual": 11.6388,
    "peBasicExclExtraTTM": 12.0092,
    "peExclExtraAnnual": 8.7772,
    "peExclExtraTTM": 12.0092,
    "peInclExtraTTM": 12.0092,
    "peNormalizedAnnual": 11.6388,
    "peTTM": 12.0092,
    "pegTTM": 2.95806,
    "pfcfShareAnnual": 10.5123,
    "pfcfShareTTM": 7.5842,
    "pretaxMargin5Y": 7.04,
    "pretaxMarginAnnual": 4.83,
    "pretaxMarginTTM": 4.73,
    "priceRelativeToS&P50013Week": 22.3762,
    "priceRelativeToS&P50026Week": 58.4908,
    "priceRelativeToS&P5004Week": 9.8976,
    "priceRelativeToS&P50052Week": -7.7486,
    "priceRelativeToS&P500Ytd": 33.5548,
    "psAnnual": 0.5323,
    "psTTM": 0.4975,
    "ptbvAnnual": 2.7217,
    "ptbvQuarterly": 2.2243,
    "quickRatioAnnual": 0.4226,
    "quickRatioQuarterly": 0.4836,
    "receivablesTurnoverAnnual": 10.2313,
    "receivablesTurnoverTTM": 9.6269,
    "revenueEmployeeAnnual": 1.0054,
    "revenueEmployeeTTM": 1.0757,
    "revenueGrowth3Y": -4.21,
    "revenueGrowth5Y": -0.48,
    "revenueGrowthQuarterlyYoy": 12.53,
    "revenueGrowthTTMYoy": 8.14,
    "revenuePerShareAnnual": 58.022,
    "revenuePerShareTTM": 63.8209,
    "revenueShareGrowth5Y": 7.78,
    "roa5Y": 9.38,
    "roaRfy": 6.05,
    "roaTTM": 5.7,
    "roe5Y": 3.17,
    "roeRfy": 16.400000000000002,
    "roeTTM": 16.85,
    "roi5Y": 3.77,
    "roiAnnual": 12.43,
    "roiTTM": 9.98,
    "tangibleBookValuePerShareAnnual": 13.3764,
    "tangibleBookValuePerShareQuarterly": 13.7624,
    "tbvCagr5Y": -6.22,
    "totalDebt/totalEquityAnnual": 0.3195,
    "totalDebt/totalEquityQuarterly": 0.3195,
    "yearToDatePriceReturnDaily": 46.4991
  },
  "source_status": {
    "local_research": false,
    "local_news": false,
    "local_sec_filings": false,
    "finnhub_news": true,
    "polygon_news": true,
    "earnings": true,
    "fundamentals": true
  }
}
```

## CMG
Trading candidate:
```json
{
  "symbol": "CMG",
  "score": 74.96,
  "direction": "LONG",
  "sector": "Consumer Discretionary",
  "components": {
    "market": 100.0,
    "sector": 49.44,
    "relative_strength": 81.81184684877627,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 13.621233616891043,
    "momentum": 51.900065746219624,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 92.03194517961111
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
      "datetime": 1788870900,
      "headline": "These S&P500 stocks are moving in today's pre-market session",
      "id": 141949006,
      "image": "https://www.chartmill.com/images/uploads/CM_Premarket_Movers_Small_free_90289f6b81.webp",
      "related": "CMG",
      "source": "ChartMill",
      "summary": "Stay updated with the S&P500 stocks that are on the move in today's pre-market session.",
      "url": "https://finnhub.io/api/news?id=00df6df6df67101935570b3d09b4f6fb117c7f4bf5fcbd493dfc9d008f76108f"
    },
    {
      "category": "company",
      "datetime": 1788861444,
      "headline": "Yum! Brands: Life After The Outbreak",
      "id": 141949256,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/1449640858/image_1449640858.jpg?io=getty-c-w1536",
      "related": "CMG",
      "source": "SeekingAlpha",
      "summary": "Yum! Brands, Inc. shifts to a leaner portfolio after the Pizza Hut sale, using $2.3B for debt paydown and buybacks. Click for this YUM update.",
      "url": "https://finnhub.io/api/news?id=a6e2a4d5d500b14c8c59f5c3bc2e8d9eb763dc0e5539da13380ca18c8d519b31"
    },
    {
      "category": "company",
      "datetime": 1788784203,
      "headline": "If You Invested $1000 in Chipotle Mexican Grill a Decade Ago, This is How Much It'd Be Worth Now",
      "id": 141762976,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "CMG",
      "source": "Yahoo",
      "summary": "Why investing for the long run, especially if you buy certain popular stocks, could reap huge rewards.",
      "url": "https://finnhub.io/api/news?id=5ed08fda2262bcad0f932e000fb668447a65c54309b40141a755e245cfbcbdaa"
    },
    {
      "category": "company",
      "datetime": 1788752868,
      "headline": "Is the Stock Market Open on Labor Day 2026? Here's What's Open and What's Closed",
      "id": 141769139,
      "image": "https://cdn.benzinga.com/files/images/story/2026/09/07/Wall-Street.jpg?width=2048&height=1536",
      "related": "CMG",
      "source": "Benzinga",
      "summary": "Find out what&#39;s open and closed on Labor Day, Sept. 7. Stock markets, banks, and mail are closed, but most stores and restaurants stay open.",
      "url": "https://finnhub.io/api/news?id=6ee8ed5a1b4e18dc3f5369fb4f078bb4e9a3c00d27aa8feb63155957422d8fe5"
    },
    {
      "category": "company",
      "datetime": 1788721865,
      "headline": "McDonald's (MCD) Exit From A 90% Restaurant Stake Still Haunts Investors",
      "id": 141593718,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "CMG",
      "source": "Yahoo",
      "summary": "McDonald's (NYSE:MCD) previously owned about 90% of Chipotle before exiting the investment in 2006. The company sold its stake as part of a refocus on its core fast food operations, leaving Chipotle to list and expand independently. A recent look back highlights how much long-term market value McDonald's did not capture by selling its Chipotle holding. Investors are using this episode to compare McDonald's approach with Chipotle's different growth and brand strategies over time. McDonald's...",
      "url": "https://finnhub.io/api/news?id=930c05457ffaffe29ef4239bc38e25cf2232a538c49f42ed1788b8e894bc3f60"
    }
  ],
  "polygon_news": [
    {
      "id": "e7e7c9ea90c4b948de6c3a2e4a600333a4fa05982361d4584e5ea34569b1919c",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "If You Invested $1000 in Chipotle Mexican Grill a Decade Ago, This is How Much It'd Be Worth Now",
      "author": "Zacks.Com",
      "published_utc": "2026-09-07T12:30:03Z",
      "article_url": "https://www.zacks.com/stock/news/2985604/if-you-invested-1000-in-chipotle-mexican-grill-a-decade-ago-this-is-how-much-it-d-be-worth-now?cid=CS-ZC-FT-fundamental_analysis|investing_$1000-2985604",
      "tickers": [
        "CMG"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default311.jpg",
      "description": "A $1,000 investment in Chipotle Mexican Grill made in September 2016 would be worth $4,524.86 as of September 2026, representing a 352.49% gain. This significantly outperformed the S&P 500's 254.07% gain over the same period. Chipotle's growth is driven by digital platform expansion, Chipotlane rollout, menu innovation, and international expansion, with analysts expecting continued upside despite macro uncertainties.",
      "keywords": [
        "Chipotle Mexican Grill",
        "stock performance",
        "digital ordering",
        "Chipotlane",
        "Recipe for Growth strategy",
        "comparable sales",
        "restaurant expansion"
      ],
      "insights": [
        {
          "ticker": "CMG",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong historical performance with 352.49% return over 10 years, outperforming S&P 500. Positive momentum with 12.72% gain in past four weeks, increased earnings estimates, successful digital platform adoption (38.3% of revenues), HEEP rollout expansion, and analyst optimism regarding Recipe for Growth strategy and international expansion. Company raised comparable-sales outlook and expects 350-370 restaurant openings in 2026."
        }
      ]
    },
    {
      "id": "90077de84876de6e2c4043c8a47f4f96153d93b92a99e0e7d1713db63ed0f580",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Why Is Dutch Bros (BROS) Down 13.3% Since Last Earnings Report?",
      "author": "Na",
      "published_utc": "2026-09-04T15:30:36Z",
      "article_url": "https://www.zacks.com/stock/news/2985276/why-is-dutch-bros-bros-down-13-3-since-last-earnings-report?cid=CS-ZC-FT-realtime_blog-2985276",
      "tickers": [
        "BROS",
        "CMG"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default180.jpg",
      "description": "Dutch Bros reported strong Q2 2026 results with earnings and revenue beating consensus estimates, driven by new shop growth and comparable-shop momentum. The company raised its 2026 outlook for revenue, same-shop sales growth, and adjusted EBITDA. However, shares have underperformed the S&P 500 by 13.3% since the earnings report, with analyst estimates trending downward over the past month. The stock holds a Zacks Rank #3 (Hold) rating.",
      "keywords": [
        "earnings beat",
        "revenue growth",
        "same-shop sales",
        "margin pressure",
        "guidance raise",
        "estimate revisions",
        "stock underperformance"
      ],
      "insights": [
        {
          "ticker": "BROS",
          "sentiment": "neutral",
          "sentiment_reasoning": "While the company delivered strong Q2 earnings and revenue beats with raised guidance, the stock has significantly underperformed the market post-earnings. Downward estimate revisions in the past month and a Hold rating suggest investor skepticism despite operational strength, indicating a disconnect between fundamentals and market sentiment."
        },
        {
          "ticker": "CMG",
          "sentiment": "positive",
          "sentiment_reasoning": "Chipotle gained 11.5% over the past month, outperforming Dutch Bros. The company showed solid revenue growth of 9.3% year-over-year, though earnings remained flat. The positive stock performance indicates investor confidence in the company's trajectory."
        }
      ]
    },
    {
      "id": "7beb4c1adf97382d5d23a6f05f78a7f39975b587c7901d7ddbbc9893b5c06928",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Chipotle Mexican Grill (CMG) Stock Falls Amid Market Uptick: What Investors Need to Know",
      "author": "Zacks.Com",
      "published_utc": "2026-09-03T21:45:03Z",
      "article_url": "https://www.zacks.com/stock/news/2984796/chipotle-mexican-grill-cmg-stock-falls-amid-market-uptick-what-investors-need-to-know?cid=CS-ZC-FT-fundamental_analysis|yseop_template_6-2984796",
      "tickers": [
        "CMG"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default101.jpg",
      "description": "Chipotle Mexican Grill (CMG) declined 2.47% to $37.57 while broader markets gained, underperforming the S&P 500's 1.06% rise. Despite a strong monthly gain of 11.65%, the stock trades at a premium valuation with a Forward P/E of 33.63 versus the industry average of 21.36. Upcoming Q3 earnings on October 28, 2026 are expected to show flat EPS at $0.29 but revenue growth of 9.35% year-over-year. CMG holds a Zacks Rank of #3 (Hold).",
      "keywords": [
        "Chipotle Mexican Grill",
        "stock decline",
        "earnings forecast",
        "valuation premium",
        "market performance",
        "restaurant industry"
      ],
      "insights": [
        {
          "ticker": "CMG",
          "sentiment": "neutral",
          "sentiment_reasoning": "While CMG underperformed the market on the trading day and carries a premium valuation (Forward P/E of 33.63 vs. industry 21.36), the stock showed strong monthly gains of 11.65% and revenue growth expectations of 9.35%. The Zacks Rank of #3 (Hold) reflects a balanced outlook with modest positive estimate revisions (0.12% higher) but no earnings growth expected for the full year, warranting a neutral stance."
        }
      ]
    },
    {
      "id": "12d5e4e4d8f363bb358d242eec98b0bfeb4b85e8cbcbfaa1f4230814c9488484",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "YUMC or CMG: Which Is the Better Value Stock Right Now?",
      "author": "Na",
      "published_utc": "2026-09-03T15:40:02Z",
      "article_url": "https://www.zacks.com/stock/news/2984622/yumc-or-cmg-which-is-the-better-value-stock-right-now?cid=CS-ZC-FT-fundamental_analysis|yseop_template_3-2984622",
      "tickers": [
        "YUMC",
        "CMG"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default21.jpg",
      "description": "In a comparison of two retail restaurant stocks, Yum China Holdings (YUMC) emerges as the better value option for investors. YUMC has a Zacks Rank of #2 (Buy) with improving earnings outlook, a forward P/E of 15.16, and a Value grade of A. In contrast, Chipotle Mexican Grill (CMG) has a Zacks Rank of #3 (Hold), a forward P/E of 33.63, and a Value grade of F, making it significantly more expensive on traditional valuation metrics.",
      "keywords": [
        "value investing",
        "stock comparison",
        "P/E ratio",
        "Zacks Rank",
        "restaurant sector",
        "valuation metrics"
      ],
      "insights": [
        {
          "ticker": "YUMC",
          "sentiment": "positive",
          "sentiment_reasoning": "YUMC has a Zacks Rank #2 (Buy) with improving earnings estimates, lower forward P/E ratio (15.16), lower PEG ratio (1.18), lower P/B ratio (2.58), and a Value grade of A, indicating it is undervalued compared to peers."
        },
        {
          "ticker": "CMG",
          "sentiment": "negative",
          "sentiment_reasoning": "CMG has a Zacks Rank #3 (Hold), significantly higher forward P/E ratio (33.63), higher PEG ratio (2.36), much higher P/B ratio (22.16), and a Value grade of F, indicating it is overvalued relative to its fundamentals."
        }
      ]
    },
    {
      "id": "074dd772bc85a612fa2f0644c5d357c40ca97108b519a5e2b043d9fbad9ad478",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Can CAVA's 2024 Cohort Support Its Next Phase of Unit Growth?",
      "author": "Na",
      "published_utc": "2026-09-02T16:24:00Z",
      "article_url": "https://www.zacks.com/stock/news/2984000/can-cava-s-2024-cohort-support-its-next-phase-of-unit-growth?cid=CS-ZC-FT-analyst_blog|quick_take-2984000",
      "tickers": [
        "CAVA",
        "CMG",
        "SG"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/ed/86131.jpg",
      "description": "CAVA Group is experiencing strong performance from its newer restaurant locations, with its 2024 cohort generating double-digit same-store sales and representing its highest-performing vintage. The company ended Q2 2026 with 476 restaurants and new unit productivity above 100%, supporting its target of 75-77 net new restaurants in 2026. Meanwhile, competitors Chipotle and Sweetgreen are taking different expansion approaches, with Chipotle maintaining aggressive growth and Sweetgreen adopting a more conservative strategy.",
      "keywords": [
        "restaurant expansion",
        "same-store sales",
        "new unit economics",
        "quick-service restaurant",
        "unit growth",
        "comparable sales"
      ],
      "insights": [
        {
          "ticker": "CAVA",
          "sentiment": "positive",
          "sentiment_reasoning": "CAVA's 2024 restaurant cohort is generating double-digit same-store sales (highest-performing vintage), new restaurant productivity exceeds 100%, and the company is expanding with 75-77 net new restaurants targeted for 2026. Strong performance across geographies and formats supports positive momentum."
        },
        {
          "ticker": "CMG",
          "sentiment": "positive",
          "sentiment_reasoning": "Chipotle opened 101 restaurants in Q2 2026 with 80 Chipotlanes, maintains established new-unit economics with ~80% productivity and 60% second-year cash-on-cash returns, and expects ~350 openings for the full year, supporting long-term potential for 7,000+ restaurants."
        },
        {
          "ticker": "SG",
          "sentiment": "neutral",
          "sentiment_reasoning": "Sweetgreen is taking a measured, conservative approach to expansion (opened 4, closed 2 in Q2 2026) while refining prototype design and focusing on profitability and return thresholds. This cautious strategy reflects challenges but demonstrates disciplined capital allocation."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 12.25969,
    "13WeekPriceReturnDaily": 31.1568,
    "26WeekPriceReturnDaily": 0.0812,
    "3MonthADReturnStd": 49.746353,
    "3MonthAverageTradingVolume": 18.80561,
    "52WeekHigh": 42.82,
    "52WeekHighDate": "2025-10-15",
    "52WeekLow": 28.035,
    "52WeekLowDate": "2026-06-04",
    "52WeekPriceReturnDaily": -9.9854,
    "5DayPriceReturnDaily": -2.8136,
    "assetTurnoverAnnual": 1.3259,
    "assetTurnoverTTM": 1.3826,
    "beta": 0.9858801,
    "bookValuePerShareAnnual": 2.1701,
    "bookValuePerShareQuarterly": 1.7351,
    "bookValueShareGrowth5Y": 8.5,
    "capexCagr5Y": 12.28,
    "cashFlowPerShareAnnual": 1.1098,
    "cashFlowPerShareQuarterly": 1.2375,
    "cashFlowPerShareTTM": 53.21617,
    "cashPerSharePerShareAnnual": 0.8043,
    "cashPerSharePerShareQuarterly": 0.5347,
    "currentDividendYieldTTM": null,
    "currentEv/freeCashFlowAnnual": 32.1511,
    "currentEv/freeCashFlowTTM": 29.6635,
    "currentRatioAnnual": 1.2347,
    "currentRatioQuarterly": 0.7153,
    "dividendPerShareTTM": null,
    "ebitdPerShareAnnual": 1.711,
    "ebitdPerShareTTM": 1.678,
    "ebitdaCagr5Y": 34.15,
    "ebitdaInterimCagr5Y": 15.19,
    "enterpriseValue": 46541.649,
    "epsAnnual": 1.1439,
    "epsBasicExclExtraItemsAnnual": 1.1439,
    "epsBasicExclExtraItemsTTM": 1.0840999999999998,
    "epsExclExtraItemsAnnual": 1.1439,
    "epsExclExtraItemsTTM": 1.0840999999999998,
    "epsGrowth3Y": 21.31,
    "epsGrowth5Y": 35.5,
    "epsGrowthQuarterlyYoy": -2.32,
    "epsGrowthTTMYoy": -4.17,
    "epsInclExtraItemsAnnual": 1.1439,
    "epsInclExtraItemsTTM": 1.0840999999999998,
    "epsNormalizedAnnual": 1.1439,
    "epsTTM": 1.0840999999999998,
    "evEbitdaTTM": 21.1705,
    "evRevenueTTM": 3.7462,
    "focfCagr5Y": 37.88,
    "forwardPE": 32.162539169813165,
    "grossMargin5Y": 33.01,
    "grossMarginAnnual": 33.68,
    "grossMarginTTM": 29.48,
    "inventoryTurnoverAnnual": 160.6774,
    "inventoryTurnoverTTM": 201.3463,
    "longTermDebt/equityAnnual": null,
    "longTermDebt/equityQuarterly": null,
    "marketCapitalization": 46769.848,
    "monthToDatePriceReturnDaily": -2.8136,
    "netIncomeEmployeeAnnual": 0.0118,
    "netIncomeEmployeeTTM": 0.0109,
    "netInterestCoverageAnnual": 1268.1445,
    "netInterestCoverageTTM": 409.0572,
    "netMarginGrowth5Y": 16.74,
    "netProfitMargin5Y": 11.59,
    "netProfitMarginAnnual": 12.88,
    "netProfitMarginTTM": 11.42,
    "operatingMargin5Y": 14.61,
    "operatingMarginAnnual": 16.23,
    "operatingMarginTTM": 14.65,
    "payoutRatioAnnual": null,
    "payoutRatioTTM": null,
    "pb": 21.261,
    "pbAnnual": 17.284,
    "pbQuarterly": 19.826,
    "pcfShareAnnual": 22.1246,
    "pcfShareTTM": 20.0942,
    "peAnnual": 30.4539,
    "peBasicExclExtraTTM": 32.9503,
    "peExclExtraAnnual": 69.27852,
    "peExclExtraTTM": 32.9503,
    "peInclExtraTTM": 32.9503,
    "peNormalizedAnnual": 30.4539,
    "peTTM": 32.9503,
    "pfcfShareAnnual": 32.3088,
    "pfcfShareTTM": 29.809,
    "pretaxMargin5Y": 15.1,
    "pretaxMarginAnnual": 16.85,
    "pretaxMarginTTM": 15.05,
    "priceRelativeToS&P50013Week": 29.4265,
    "priceRelativeToS&P50026Week": -13.1271,
    "priceRelativeToS&P5004Week": 15.3643,
    "priceRelativeToS&P50052Week": -28.9814,
    "priceRelativeToS&P500Ytd": -13.0524,
    "psAnnual": 3.9218,
    "psTTM": 3.7645,
    "ptbvAnnual": 25.96586,
    "ptbvQuarterly": 21.2675,
    "quickRatioAnnual": 1.1104,
    "quickRatioQuarterly": 0.5917,
    "receivablesTurnoverAnnual": 79.3905,
    "receivablesTurnoverTTM": 121.0238,
    "revenueEmployeeAnnual": 0.0915,
    "revenueEmployeeTTM": 0.0953,
    "revenueGrowth3Y": 11.36,
    "revenueGrowth5Y": 14.79,
    "revenueGrowthQuarterlyYoy": 9.31,
    "revenueGrowthTTMYoy": 7.31,
    "revenuePerShareAnnual": 8.8824,
    "revenuePerShareTTM": 9.7132,
    "revenueShareGrowth5Y": 16.09,
    "roa5Y": 14.36,
    "roaRfy": 17.07,
    "roaTTM": 15.8,
    "roe5Y": 40.55,
    "roeRfy": 54.26,
    "roeTTM": 53.26,
    "roi5Y": 40.55,
    "roiAnnual": 54.26,
    "roiTTM": 53.26,
    "tangibleBookValuePerShareAnnual": 84.91997,
    "tangibleBookValuePerShareQuarterly": 104.2159,
    "tbvCagr5Y": 11.81124,
    "totalDebt/totalEquityAnnual": 0,
    "totalDebt/totalEquityQuarterly": 0,
    "yearToDatePriceReturnDaily": -0.1081
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

## T
Trading candidate:
```json
{
  "symbol": "T",
  "score": 70.37,
  "direction": "LONG",
  "sector": "Communication Services",
  "components": {
    "market": 100.0,
    "sector": 52.23,
    "relative_strength": 66.43477274754387,
    "vwap": 88.2648885203065,
    "trend": 100.0,
    "volume": 13.756142683160554,
    "momentum": 57.68205524434999,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 79.62829532932092
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
    "[2026-09-03.md]\n# Market News \u2014 2026-09-03\n\n- U.S. futures were broadly muted early Thursday as investors weighed higher oil prices and Middle East escalation; Brent was near $97 and WTI near $93.\n- Wall Street recovered Wednesday: the Nasdaq gained about 0.5%, while Nvidia rose more than 3%; breadth remains sensitive to rates and energy prices.\n- Broadcom fell in premarket trading after its fourth-quarter revenue forecast missed lofty expectations, reinforcing the high bar for AI-infrastructure earnings.\n- The market remains vulnerable to an oil-driven inflation shock and higher Treasury yields; leadership is concentrated in AI/technology and energy.\n- Sources: https://apnews.com/article/7e1bffd68c53b54806be950f01181994 ; https://apnews.com/article/7cb0aefedfd933d048b8b3e5843449f8 ; https://www.investing.com/news/economy-news/wall-st-futures-subdued-as-investors-weigh-earnings-oil-prices-4887340\n",
    "[2026-08-31.md]\n# Market News \u2014 2026-08-31\n\n- U.S. futures were modestly lower Monday as geopolitical escalation around the Strait of Hormuz pushed Brent crude above $91 and WTI above $86; European equities were mixed.\n- Nasdaq had recently shown relative strength, helped by Nvidia, but breadth remained uneven and late-summer liquidity raises volatility risk.\n- AI infrastructure remains the dominant leadership theme, with semiconductor and cybersecurity names showing the strongest recent participation.\n- Sources: https://apnews.com/article/00f872327d65e5330598054a234dc25a ; https://apnews.com/article/b4216a1f191d0304b4ed59e6912e23a ; https://articles.dailytickers.com/daily/20260827/\n"
  ],
  "local_sec_filings": [
    "[2026-09-03.md]\n# SEC Filing Review \u2014 2026-09-03\n\n- No fresh ticker-specific SEC filing was independently verified in this collection window for the watchlist.\n- Filing status: unavailable for a complete same-day watchlist sweep; treat company-specific filing catalysts as unconfirmed until checked in EDGAR.\n",
    "[2026-08-31.md]\n# SEC Filing Review \u2014 2026-08-31\n\n- AMD: SEC EDGAR filing index shows an August 13, 2026 filing with associated XBRL exhibits; this is the only fresh ticker-specific filing independently verified in the current collection window.\n- NVDA: an August 26, 2026 8-K is listed by a secondary filing index; verify the primary EDGAR document before relying on details.\n- For the remaining watchlist names, no new material filing was independently verified in this run. Treat filing status as unavailable rather than clean.\n- Source: https://www.sec.gov/Archives/edgar/data/2488/000119312526354029/0001193125-26-354029-index.htm\n"
  ],
  "finnhub_news": [
    {
      "category": "company",
      "datetime": 1788889245,
      "headline": "EchoStar Shares Could Follow SpaceX's Catalyst Path, UBS Securities Says",
      "id": 141952669,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "T",
      "source": "Yahoo",
      "summary": "EchoStar's (ECHO) stock upside could be primarily driven by its expected 2% stake in SpaceX's (SPCX)",
      "url": "https://finnhub.io/api/news?id=c2c8b77511d2839e7a6ef609201b212db53ea175af963f6a1d1a76efef38375f"
    },
    {
      "category": "company",
      "datetime": 1788887012,
      "headline": "T, AMZN Stocks In Focus \u2014 AT&T, Amazon Leo Partner To Expand Satellite Broadband For Businesses",
      "id": 141952520,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "T",
      "source": "Yahoo",
      "summary": "AT&T says it will be the first major U.S. telecom provider to integrate Leo satellite services with fiber and 5G.",
      "url": "https://finnhub.io/api/news?id=d6fc5e09f0abc2e9a89105bf9a273cf915a182bb2146a3e24e640c1485f1b38c"
    },
    {
      "category": "company",
      "datetime": 1788878940,
      "headline": "Can AT&T's Latest Smartphone Offers Boost Customer Satisfaction?",
      "id": 141950414,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "T",
      "source": "Yahoo",
      "summary": "T expands its smartphone lineup with the Samsung Galaxy S26 FE, pairing flexible pricing, upgrade options and customer-focused benefits.",
      "url": "https://finnhub.io/api/news?id=52c97abe3a3c6fd6902b9588d33822be6ae1883a0d8adbc38733b8971feae220"
    },
    {
      "category": "company",
      "datetime": 1788877080,
      "headline": "The Zacks Analyst Blog Highlights SpaceX, Verizon and AT&T",
      "id": 141950420,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "T",
      "source": "Yahoo",
      "summary": "SpaceX briefly reclaimed a $2 trillion valuation as Starlink growth, launch dominance and AI investments bolster its long-term growth story.",
      "url": "https://finnhub.io/api/news?id=71c7f65aa12ff9faa4f265dd20664e88b58866c254c8fee35ae8ad58f2aab3f7"
    },
    {
      "category": "company",
      "datetime": 1788875467,
      "headline": "Amazon and AT&T partner to challenge SpaceX Starlink dominance",
      "id": 141949837,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "T",
      "source": "Yahoo",
      "summary": "AT&T becomes the first U.S. wireless carrier to use Amazon Leo's low-Earth-orbit satellite network to serve business customers",
      "url": "https://finnhub.io/api/news?id=2ca545d0c1ccab4b40622058ae6b9ccc0033129447009f825319fe58e2880bbe"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 29.32582,
    "13WeekPriceReturnDaily": 12.78,
    "26WeekPriceReturnDaily": -10.429,
    "3MonthADReturnStd": 29.400875,
    "3MonthAverageTradingVolume": 53.91477,
    "52WeekHigh": 29.79,
    "52WeekHighDate": "2025-09-15",
    "52WeekLow": 19.89,
    "52WeekLowDate": "2026-07-02",
    "52WeekPriceReturnDaily": -13.2139,
    "5DayPriceReturnDaily": -0.8111,
    "assetTurnoverAnnual": 0.299,
    "assetTurnoverTTM": 0.3006,
    "beta": 0.27361485,
    "bookValuePerShareAnnual": 15.7063,
    "bookValuePerShareQuarterly": 16.0552,
    "bookValueShareGrowth5Y": -7.09,
    "capexCagr5Y": 7.25,
    "cashFlowPerShareAnnual": 2.7626,
    "cashFlowPerShareQuarterly": 2.5664,
    "cashFlowPerShareTTM": 1.14693,
    "cashPerSharePerShareAnnual": 2.591,
    "cashPerSharePerShareQuarterly": 2.5542,
    "currentDividendYieldTTM": 4.5565,
    "currentEv/freeCashFlowAnnual": 15.5516,
    "currentEv/freeCashFlowTTM": 17.1266,
    "currentRatioAnnual": 0.9061,
    "currentRatioQuarterly": 0.971,
    "dividendGrowthRate5Y": -11.16,
    "dividendIndicatedAnnual": 1.11,
    "dividendPerShareAnnual": 1.151,
    "dividendPerShareTTM": 1.1421,
    "dividendYieldIndicatedAnnual": 6.84762,
    "ebitdPerShareAnnual": 6.275,
    "ebitdPerShareTTM": 6.5107,
    "ebitdaCagr5Y": 7.83,
    "ebitdaInterimCagr5Y": 0,
    "enterpriseValue": 302353.27,
    "epsAnnual": 3.0579,
    "epsBasicExclExtraItemsAnnual": 3.0579,
    "epsBasicExclExtraItemsTTM": 3.0432,
    "epsExclExtraItemsAnnual": 3.0579,
    "epsExclExtraItemsTTM": 3.0432,
    "epsGrowth3Y": null,
    "epsGrowth5Y": null,
    "epsGrowthQuarterlyYoy": 6.85,
    "epsGrowthTTMYoy": 72.22,
    "epsInclExtraItemsAnnual": 3.0579,
    "epsInclExtraItemsTTM": 3.0432,
    "epsNormalizedAnnual": 3.0579,
    "epsTTM": 3.0432,
    "evEbitdaTTM": 6.5758,
    "evRevenueTTM": 2.3763,
    "focfCagr5Y": -7.32,
    "forwardPE": 9.39139,
    "forwardPEG": 0.87402,
    "grossMargin5Y": 58.24,
    "grossMarginAnnual": 59.55,
    "grossMarginTTM": 59.72,
    "inventoryTurnoverAnnual": 21.6716,
    "inventoryTurnoverTTM": 21.6931,
    "longTermDebt/equityAnnual": 1.139,
    "longTermDebt/equityQuarterly": 1.219,
    "marketCapitalization": 175969.27,
    "monthToDatePriceReturnDaily": -0.8111,
    "netIncomeEmployeeAnnual": 0.1656,
    "netIncomeEmployeeTTM": 0.1626,
    "netInterestCoverageAnnual": 4.6419,
    "netInterestCoverageTTM": 6.5973,
    "netMarginGrowth5Y": null,
    "netProfitMargin5Y": 9.22,
    "netProfitMarginAnnual": 17.47,
    "netProfitMarginTTM": 16.94,
    "operatingMargin5Y": 13.9,
    "operatingMarginAnnual": 19.23,
    "operatingMarginTTM": 20.12,
    "payoutRatioAnnual": 37.26,
    "payoutRatioTTM": 37.19,
    "pb": 1.5933,
    "pbAnnual": 1.5932,
    "pbQuarterly": 1.3023,
    "pcfShareAnnual": 4.3682,
    "pcfShareTTM": 4.4104,
    "peAnnual": 8.0157,
    "peBasicExclExtraTTM": 8.1626,
    "peExclExtraTTM": 8.1626,
    "peInclExtraTTM": 8.1626,
    "peNormalizedAnnual": 8.0157,
    "peTTM": 8.1626,
    "pegTTM": 0.712,
    "pfcfShareAnnual": 9.051,
    "pfcfShareTTM": 9.9677,
    "pretaxMargin5Y": 14.11,
    "pretaxMarginAnnual": 21.49,
    "pretaxMarginTTM": 20.54,
    "priceRelativeToS&P50013Week": 11.0497,
    "priceRelativeToS&P50026Week": -23.6373,
    "priceRelativeToS&P5004Week": 7.1449,
    "priceRelativeToS&P50052Week": -32.2099,
    "priceRelativeToS&P500Ytd": -9.5627,
    "psAnnual": 1.4005,
    "psTTM": 1.383,
    "ptbvAnnual": 3.7288,
    "ptbvQuarterly": 16.5315,
    "quickRatioAnnual": 0.6838,
    "quickRatioQuarterly": 0.6761,
    "receivablesTurnoverAnnual": 9.4983,
    "receivablesTurnoverTTM": 9.8792,
    "revenueEmployeeAnnual": 0.9476,
    "revenueEmployeeTTM": 0.9596,
    "revenueGrowth3Y": 1.34,
    "revenueGrowth5Y": -2.56,
    "revenueGrowthQuarterlyYoy": 2.3,
    "revenueGrowthTTMYoy": 2.63,
    "revenuePerShareAnnual": 17.5022,
    "revenuePerShareTTM": 18.3183,
    "revenueShareGrowth5Y": -2.62,
    "roa5Y": 2.61,
    "roaRfy": 5.220000000000001,
    "roaTTM": 5.09,
    "roe5Y": 9.52,
    "roeRfy": 19.86,
    "roeTTM": 19.54,
    "roi5Y": 4.38,
    "roiAnnual": 8.9,
    "roiTTM": 8.63,
    "tangibleBookValuePerShareAnnual": 6.5972,
    "tangibleBookValuePerShareQuarterly": 1.4262,
    "tbvCagr5Y": 49.66,
    "totalDebt/totalEquityAnnual": 1.2313,
    "totalDebt/totalEquityQuarterly": 1.3034,
    "yearToDatePriceReturnDaily": 3.3816
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

## WBD
Trading candidate:
```json
{
  "symbol": "WBD",
  "score": 70.2,
  "direction": "LONG",
  "sector": "Communication Services",
  "components": {
    "market": 100.0,
    "sector": 52.23,
    "relative_strength": 59.24895863620909,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 10.427570688915734,
    "momentum": 45.85964912280698,
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
      "datetime": 1788872404,
      "headline": "Investors Heavily Search Warner Bros. Discovery, Inc. (WBD): Here is What You Need to Know",
      "id": 141950926,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WBD",
      "source": "Yahoo",
      "summary": "Recently, Zacks.com users have been paying close attention to Warner Bros. Discovery (WBD). This makes it worthwhile to examine what the stock has in store.",
      "url": "https://finnhub.io/api/news?id=613156c50304ef03432caeab07671da8d38acccbdca68cc66b82a98e9eabb804"
    },
    {
      "category": "company",
      "datetime": 1788869388,
      "headline": "Netflix: The Buying Opportunity Of The Last Five Years",
      "id": 141951829,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/2258061480/image_2258061480.jpg?io=getty-c-w1536",
      "related": "WBD",
      "source": "SeekingAlpha",
      "summary": "Netflix (NFLX) has lagged the S&P 500\u00e2\u0080\u0094explore fundamentals, risks, valuation, and a best-case $132 fair value target.",
      "url": "https://finnhub.io/api/news?id=82dc76bdd1d35c94731ffd74dfa060583ebad50c4b96e6fe93be4c74958679e6"
    },
    {
      "category": "company",
      "datetime": 1788784435,
      "headline": "Netflix Has Momentum Despite Being Down in 2026. One Analyst\u2019s Price Target Implies 70% Upside",
      "id": 141762398,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WBD",
      "source": "Yahoo",
      "summary": "Netflix has shed more than a third of its value while the broader market climbs, yet one Wall Street analyst sees a path back that would leave today's sellers deeply regretting their exits.",
      "url": "https://finnhub.io/api/news?id=8abdb4cf56a069812eadf109c149712c0e763851025b53657df246ba7aa1e96d"
    },
    {
      "category": "company",
      "datetime": 1788728741,
      "headline": "Paramount (PSKY)\u2019s CEO Has Cleared 68 Countries for His Warner Bros (WBD) Deal. California Still Won\u2019t Budge",
      "id": 141593783,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WBD",
      "source": "Yahoo",
      "summary": "CNBC reported that Paramount Skydance Corporation (NASDAQ:PSKY) CEO David Ellison has cleared regulatory approval in 68 jurisdictions for his $110 billion bid to acquire Warner Bros. Discovery, Inc. (NASDAQ:WBD), but a lawsuit from 12 state attorneys general remains the final obstacle. California Attorney General Rob Bonta, who leads the states\u2019 case, canceled a planned settlement [\u2026]",
      "url": "https://finnhub.io/api/news?id=ab1223afab16e5abb76a042066ae1aa65e4dbfb93b9291a4e2dab9657d73ee58"
    },
    {
      "category": "company",
      "datetime": 1788674817,
      "headline": "Warner Bros. Discovery (WBD) Expands Gremlins Tie Up Following Fresh Questions On Valuation",
      "id": 141593784,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WBD",
      "source": "Yahoo",
      "summary": "Gemmy Industries and Warner Bros. Discovery (WBD) are expanding their Gremlins partnership with new animatronic Halloween decorations at The Home Depot, putting fresh attention on how WBD monetizes its classic intellectual property. For investors, the Gremlins expansion comes during a mixed stretch for Warner Bros. Discovery, with the share price down over the past week but showing a 30 day share price return of 5.49% and a 90 day share price return of 6.72%. Over longer horizons, total...",
      "url": "https://finnhub.io/api/news?id=b24f9e21478c82bf0344511f1d895be5c1998bfff01eb4d2cf4b22307241df41"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 16.97469,
    "13WeekPriceReturnDaily": 4.6296,
    "26WeekPriceReturnDaily": 0.1773,
    "3MonthADReturnStd": 20.285341,
    "3MonthAverageTradingVolume": 20.68744,
    "52WeekHigh": 30,
    "52WeekHighDate": "2025-12-12",
    "52WeekLow": 11.77,
    "52WeekLowDate": "2025-09-05",
    "52WeekPriceReturnDaily": 133.2783,
    "5DayPriceReturnDaily": -0.9814,
    "assetTurnoverAnnual": 0.3726,
    "assetTurnoverTTM": 0.3651,
    "beta": 1.650373,
    "bookValuePerShareAnnual": 14.4835,
    "bookValuePerShareQuarterly": 13.0933,
    "bookValueShareGrowth5Y": 9.82223,
    "capexCagr5Y": 25.09,
    "cashFlowPerShareAnnual": 1.2452,
    "cashFlowPerShareQuarterly": 0.8692,
    "cashFlowPerShareTTM": 6.85075,
    "cashPerSharePerShareAnnual": 1.8411,
    "cashPerSharePerShareQuarterly": 1.3433,
    "currentDividendYieldTTM": null,
    "currentEv/freeCashFlowAnnual": 32.2479,
    "currentEv/freeCashFlowTTM": 45.6795,
    "currentRatioAnnual": 1.0565,
    "currentRatioQuarterly": 0.7767,
    "dividendIndicatedAnnual": 0,
    "dividendPerShareTTM": null,
    "ebitdPerShareAnnual": 3.7024,
    "ebitdPerShareTTM": 1.4728,
    "ebitdaCagr5Y": 19.91,
    "ebitdaInterimCagr5Y": 3.37,
    "enterpriseValue": 99581.37,
    "epsAnnual": 0.2874,
    "epsBasicExclExtraItemsAnnual": 0.2874,
    "epsBasicExclExtraItemsTTM": -1.2734999999999999,
    "epsExclExtraItemsAnnual": 0.2874,
    "epsExclExtraItemsTTM": -1.2734999999999999,
    "epsGrowth3Y": null,
    "epsGrowth5Y": -30.82,
    "epsGrowthQuarterlyYoy": -90.84,
    "epsGrowthTTMYoy": null,
    "epsInclExtraItemsAnnual": 0.2874,
    "epsInclExtraItemsTTM": -1.2734999999999999,
    "epsNormalizedAnnual": 0.2874,
    "epsTTM": -1.2734999999999999,
    "evEbitdaTTM": 26.9722,
    "evRevenueTTM": 2.7573,
    "focfCagr5Y": 5.73,
    "grossMargin5Y": 46.05,
    "grossMarginAnnual": 44,
    "grossMarginTTM": 47.67,
    "longTermDebt/equityAnnual": 0.9028,
    "longTermDebt/equityQuarterly": 0.9297,
    "marketCapitalization": 70927.37,
    "monthToDatePriceReturnDaily": -0.9814,
    "netIncomeEmployeeAnnual": 0.0205,
    "netIncomeEmployeeTTM": -0.0892,
    "netInterestCoverageAnnual": -0.6698,
    "netInterestCoverageTTM": 1.7771,
    "netMarginGrowth5Y": -29.78,
    "netProfitMargin5Y": -9.59,
    "netProfitMarginAnnual": 1.95,
    "netProfitMarginTTM": -8.77,
    "operatingMargin5Y": -4.62,
    "operatingMarginAnnual": 9.88,
    "operatingMarginTTM": -3.83,
    "pb": 2.1599,
    "pbAnnual": 1.9886,
    "pbQuarterly": 2.0355,
    "pcfShareAnnual": 16.4222,
    "pcfShareTTM": 20.7208,
    "peAnnual": 97.5617,
    "peBasicExclExtraTTM": null,
    "peExclExtraTTM": null,
    "peInclExtraTTM": null,
    "peNormalizedAnnual": 97.5617,
    "peTTM": null,
    "pfcfShareAnnual": 22.9687,
    "pfcfShareTTM": 26.7046,
    "pretaxMargin5Y": -9.73,
    "pretaxMarginAnnual": 4.39,
    "pretaxMarginTTM": -10.44,
    "priceRelativeToS&P50013Week": 2.8993,
    "priceRelativeToS&P50026Week": -13.031,
    "priceRelativeToS&P5004Week": 5.5032,
    "priceRelativeToS&P50052Week": 114.2823,
    "priceRelativeToS&P500Ytd": -14.9221,
    "psAnnual": 1.9017,
    "psTTM": 1.9639,
    "ptbvQuarterly": 5.6953,
    "quickRatioAnnual": 0.7888,
    "quickRatioQuarterly": 0.5157,
    "receivablesTurnoverAnnual": 7.2837,
    "receivablesTurnoverTTM": 6.9889,
    "revenueEmployeeAnnual": 1.0506,
    "revenueEmployeeTTM": 1.0173,
    "revenueGrowth3Y": 3.32,
    "revenueGrowth5Y": 28.44,
    "revenueGrowthQuarterlyYoy": -11.16,
    "revenueGrowthTTMYoy": -6.05,
    "revenuePerShareAnnual": 14.7415,
    "revenuePerShareTTM": 14.0252,
    "revenueShareGrowth5Y": -1.48,
    "roa5Y": -3.04,
    "roaRfy": 0.73,
    "roaTTM": -3.2,
    "roe5Y": -9.02,
    "roeRfy": 2.02,
    "roeTTM": -9.22,
    "roi5Y": -4.32,
    "roiAnnual": 1.06,
    "roiTTM": -4.73,
    "tangibleBookValuePerShareAnnual": -24.27037,
    "tangibleBookValuePerShareQuarterly": 4.3811,
    "totalDebt/totalEquityAnnual": 0.9067,
    "totalDebt/totalEquityQuarterly": 0.9752,
    "yearToDatePriceReturnDaily": -1.9778
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

## PFE
Trading candidate:
```json
{
  "symbol": "PFE",
  "score": 69.21,
  "direction": "LONG",
  "sector": "Healthcare",
  "components": {
    "market": 100.0,
    "sector": 52.41,
    "relative_strength": 53.88183098854408,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 9.413617971490499,
    "momentum": 54.02880224798036,
    "volatility": 50.0,
    "options": 50.0,
    "extension": 86.87351293268864
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
      "datetime": 1788887331,
      "headline": "Is AbbVie Stock Too Reliant On Skyrizi?",
      "id": 141952570,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "AbbVie (ABBV) trades at $256.46, roughly 96% of its 52-week high, after returning 24.1% over the past twelve months against 19.7% for the S&P 500. That price buys a business where about a third of guided 2026 revenue comes from one drug. The market reads that concentration as strength. It is worth reading it the other way too.",
      "url": "https://finnhub.io/api/news?id=5705e6aac332197632f6883717364f774adac3cf64f03b6da96a17c69f795736"
    },
    {
      "category": "company",
      "datetime": 1788887100,
      "headline": "Move Aside, Pfizer: This Stock Is the Smarter Dividend Buy Right Now",
      "id": 141952507,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "Pfizer's 6% dividend yield is enticing, but AbbVie's dividend growth is superior.",
      "url": "https://finnhub.io/api/news?id=5bc48b8fcb4082ca3a778081490904fe5568769496d5f9bf7ced0e48723eb43c"
    },
    {
      "category": "company",
      "datetime": 1788878400,
      "headline": "MRNA Stock Soars 143% in a Month: Time to Buy, Hold or Sell?",
      "id": 141950162,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "Moderna stock surges 143% in a month on positive cancer therapy results, but competition and valuation raise key questions for investors.",
      "url": "https://finnhub.io/api/news?id=70423431bc7b150e3630ade48f615f5dd07d0c36f4e85b7c28b19b44f9016e98"
    },
    {
      "category": "company",
      "datetime": 1788878194,
      "headline": "What Merck Stopped Saying About GARDASIL Should Change What You Watch",
      "id": 141949985,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "Merck (MRK) has returned about 85% over the past year and at about $150 trades roughly 4% below its 52-week high. A year ago, management spent earnings calls managing fallout from a steep drop in GARDASIL sales. That problem has left the lead. What management opens with instead is a much larger claim, and it settles years from now.",
      "url": "https://finnhub.io/api/news?id=23e22eca29f124149162f38fb98cc7d4fd8a268c0cb690d6bdce0f160f07e68b"
    },
    {
      "category": "company",
      "datetime": 1788876000,
      "headline": "Pfizer Invites Public to Listen to Webcast of Pfizer Discussion at Healthcare Conference",
      "id": 141950556,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "NEW YORK, September 08, 2026--Pfizer Inc. (NYSE: PFE) invites investors and the general public to listen to a webcast of a discussion with Albert Bourla, Chairman and Chief Executive Officer, at the Morgan Stanley 24th Annual Global Healthcare Conference on Monday, September 14, 2026 at 10:45 a.m. EDT.",
      "url": "https://finnhub.io/api/news?id=08300e39c77d680ab5e7a4f13974480802f6ddb9b5122762586f5dbd571da750"
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
  "score": 58.98,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 100.0,
    "sector": 83.0,
    "relative_strength": 55.510679067166315,
    "vwap": 100.0,
    "trend": 0.0,
    "volume": 12.867221073063032,
    "momentum": 57.93151289651259,
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
      "datetime": 1788886870,
      "headline": "TSMC, IBD Stock Of The Day, Rises Above Early Buy Point As Chip Stocks Rally",
      "id": 141952516,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "Taiwan Semiconductor Manufacturing is the IBD Stock Of The Day. TSM stock hit an early-entry buy point on Tuesday.",
      "url": "https://finnhub.io/api/news?id=4fb9351ff83ec74cef60c4d0d78b9bdf7b160384a183100f7de3e3c68dae94f7"
    },
    {
      "category": "company",
      "datetime": 1788886316,
      "headline": "Apple Falls Before Ternus's First $54 Billion iPhone Test",
      "id": 141952513,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "Tomorrow's launch must turn premium hardware into evidence that Apple can close its AI gap.",
      "url": "https://finnhub.io/api/news?id=3f9726212b39259306b2d0278e91135a5c6c3a307066401f71025d6f84effea2"
    },
    {
      "category": "company",
      "datetime": 1788885606,
      "headline": "What's going on in today's session: dow jones movers",
      "id": 141952073,
      "image": "https://www.chartmill.com/images/uploads/CM_Top_Movers_Small_free_2b4ff2fc22.webp",
      "related": "AAPL",
      "source": "ChartMill",
      "summary": "Wondering what's happening in today's session for the dow jones index? Stay informed with the top movers within the dow jones index on Tuesday.",
      "url": "https://finnhub.io/api/news?id=5ed9c9ef40acd5c017324f75f1cda8dd92993808c451df6bde6b702e36240df6"
    },
    {
      "category": "company",
      "datetime": 1788884340,
      "headline": "Apple expected to unveil first foldable iPhone as new CEO Ternus takes stage",
      "id": 141952514,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "Apple Inc (NASDAQ:AAPL, XETRA:APC) is set to unveil its first foldable iPhone alongside a refreshed Pro lineup, in John Ternus's first major product launch as CEO. The event, dubbed \"Surprise and shine,\" is scheduled for Wednesday at 1pm ET. Media reports cited in the note indicate the...",
      "url": "https://finnhub.io/api/news?id=a8c4fc81b70a48ca8c1bc29495bc1502f0dde9d52e28e524b625d99bb1bfa022"
    },
    {
      "category": "company",
      "datetime": 1788883086,
      "headline": "SK Hynix Jumps 7% as AI Diverts Memory From Phones, Micron Holds Steady, Apple Slips",
      "id": 141951786,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "AI data centers are pulling memory capacity away from smartphones, and the winners and losers splitting across the semiconductor complex reveal a supply war that could reshape device prices for years to come.",
      "url": "https://finnhub.io/api/news?id=8c4ce9a3fb432f08151ecdb249e4b10cb962fcba637c6cfcd28a7b41e81530e9"
    }
  ],
  "polygon_news": [
    {
      "id": "cdc39509aca5d35fa07c17c403d4e62a2fef02c21528a557aec82e383bbebba1",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Should Schwab U.S. Large-Cap Growth ETF (SCHG) Be on Your Investing Radar?",
      "author": "Zacks.Com",
      "published_utc": "2026-09-08T10:20:02Z",
      "article_url": "https://www.zacks.com/stock/news/2986135/should-schwab-u-s-large-cap-growth-etf-schg-be-on-your-investing-radar?cid=CS-ZC-FT-style_box_etf-2986135",
      "tickers": [
        "SCHG",
        "NVDA",
        "AAPL",
        "MSFT",
        "VUG",
        "QQQ"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default153.jpg",
      "description": "The Schwab U.S. Large-Cap Growth ETF (SCHG) is highlighted as an attractive option for investors seeking broad exposure to large-cap growth stocks. With $62.83 billion in assets, a low expense ratio of 0.04%, and a Zacks ETF Rank of 2 (Buy), SCHG offers diversified exposure to 197 holdings with heavy concentration in technology. The fund has returned 9.14% year-to-date and 15.78% over the past year, though it carries medium risk with a beta of 1.19.",
      "keywords": [
        "large-cap growth ETF",
        "passive management",
        "low expense ratio",
        "technology sector",
        "diversification",
        "ETF comparison"
      ],
      "insights": [
        {
          "ticker": "SCHG",
          "sentiment": "positive",
          "sentiment_reasoning": "The ETF is recommended as a 'Buy' with strong fundamentals including very low expense ratio (0.04%), substantial assets ($62.83B), solid year-to-date and one-year returns (9.14% and 15.78%), and effective diversification across 197 holdings."
        },
        {
          "ticker": "NVDA",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as the largest individual holding in SCHG at 10.51% of assets, but no specific sentiment is expressed about the company itself."
        },
        {
          "ticker": "AAPL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as the second-largest holding in SCHG, but no specific sentiment or analysis is provided."
        },
        {
          "ticker": "MSFT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Identified as a top-3 holding in SCHG, but no specific sentiment or analysis is provided."
        },
        {
          "ticker": "VUG",
          "sentiment": "neutral",
          "sentiment_reasoning": "Presented as an alternative option with slightly lower expense ratio (0.03%) and significantly larger assets ($227.51B), but no comparative advantage or disadvantage is stated."
        },
        {
          "ticker": "QQQ",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as an alternative with the largest assets ($489.99B) but higher expense ratio (0.18%), presented without clear recommendation."
        }
      ]
    },
    {
      "id": "4b7be6786f13daa354d8efc7e50352be344134a8b0a57d5ae979cbcaab4aab5f",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Warren Buffett's Hand-Picked Successor, Greg Abel, has 68% of Berkshire Hathaway's Portfolio Invested in Just 5 Stocks. Here's My Top Pick for September.",
      "author": "Adria Cimino",
      "published_utc": "2026-09-08T08:10:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/08/warren-buffett-successor-best-stock-september/?source=iedfolrf0000001",
      "tickers": [
        "AAPL",
        "AXP",
        "KO",
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
        "BRK.A",
        "BRK.B"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F886104%2Fgettyimages-1320686310.jpg&w=1200&op=resize",
      "description": "Greg Abel, Warren Buffett's successor as CEO of Berkshire Hathaway, maintains 68% of the portfolio in five major stocks: Apple, American Express, Coca-Cola, Alphabet, and Bank of America. Apple is highlighted as the top pick for September due to new CEO John Ternus's engineering background, upcoming product launches on Sept. 9 including AI-enhanced Siri, and the company's strong competitive moat despite trading at 36x forward earnings.",
      "keywords": [
        "Berkshire Hathaway",
        "Greg Abel",
        "portfolio concentration",
        "Apple CEO transition",
        "AI capabilities",
        "product innovation",
        "September launch event"
      ],
      "insights": [
        {
          "ticker": "AAPL",
          "sentiment": "positive",
          "sentiment_reasoning": "New CEO John Ternus brings strong engineering background; upcoming Sept. 9 product launches including AI-enhanced Siri and potential folding phone; strong competitive moat with loyal customer base; recurring services revenue; positioned for growth in AI despite being late adopter."
        },
        {
          "ticker": "AXP",
          "sentiment": "positive",
          "sentiment_reasoning": "Long-standing major holding in Berkshire Hathaway's portfolio, indicating continued confidence in the company's quality and performance."
        },
        {
          "ticker": "KO",
          "sentiment": "positive",
          "sentiment_reasoning": "Multi-decade core holding in Berkshire Hathaway's portfolio, demonstrating sustained belief in the company's quality and long-term value."
        },
        {
          "ticker": "GOOG",
          "sentiment": "positive",
          "sentiment_reasoning": "Recently added to Berkshire Hathaway's portfolio by Buffett and significantly increased by Abel in 2026, showing growing confidence in the tech company's long-term prospects."
        },
        {
          "ticker": "GOOGL",
          "sentiment": "positive",
          "sentiment_reasoning": "Recently added to Berkshire Hathaway's portfolio by Buffett and significantly increased by Abel in 2026, showing growing confidence in the tech company's long-term prospects."
        },
        {
          "ticker": "GOOGM",
          "sentiment": "positive",
          "sentiment_reasoning": "Recently added to Berkshire Hathaway's portfolio by Buffett and significantly increased by Abel in 2026, showing growing confidence in the tech company's long-term prospects."
        },
        {
          "ticker": "GOOGN",
          "sentiment": "positive",
          "sentiment_reasoning": "Recently added to Berkshire Hathaway's portfolio by Buffett and significantly increased by Abel in 2026, showing growing confidence in the tech company's long-term prospects."
        },
        {
          "ticker": "BAC",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BACpB",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BACpE",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BACpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BACpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BACpM",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BACpN",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BACpO",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BACpP",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BACpQ",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BACpS",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BMLpG",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BMLpH",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BMLpJ",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BMLpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "MERpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding in Berkshire Hathaway's concentrated portfolio, indicating continued confidence in the financial institution's quality."
        },
        {
          "ticker": "BRK.A",
          "sentiment": "positive",
          "sentiment_reasoning": "Successfully transitioned leadership to Greg Abel who pledges to continue Buffett's proven strategy of favoring quality businesses and long-term holding; portfolio concentration in five quality stocks demonstrates confidence in selective investment approach."
        },
        {
          "ticker": "BRK.B",
          "sentiment": "positive",
          "sentiment_reasoning": "Successfully transitioned leadership to Greg Abel who pledges to continue Buffett's proven strategy of favoring quality businesses and long-term holding; portfolio concentration in five quality stocks demonstrates confidence in selective investment approach."
        }
      ]
    },
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