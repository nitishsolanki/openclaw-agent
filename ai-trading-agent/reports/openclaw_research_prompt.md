# OpenClaw Candidate Research Handoff

Review each candidate using the supplied trading data and evidence packet. Do not place orders. Return only JSON in this format:

```json
{"research":[{"symbol":"MSFT","research_score":0,"conviction":"Low","catalysts":[],"risks":[],"summary":""}]}
```

Use a 0-100 research score. Do not invent facts or infer fundamentals from technical data. Treat missing data as uncertainty, name the missing source in risks, and use only dated/source-labelled news, earnings, filings, or fundamentals. Keep Python's technical score authoritative; this research score is a 30% adjustment.

## HPQ
Trading candidate:
```json
{
  "symbol": "HPQ",
  "score": 76.2,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 50.0,
    "sector": 56.09,
    "relative_strength": 100.0,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 34.922348734181575,
    "momentum": 93.72875921769794,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 32.12640373605035,
    "relative_strength_acceleration": 68.61818311712602,
    "trend_acceleration": 85,
    "compression": 0.0,
    "volatility_contraction": 41.543465405085755,
    "volume_accumulation": 50.154147268437086,
    "breakout_distance": 2.1289178001182165,
    "support_quality": 0.0,
    "momentum_improvement": 68.73385952371629,
    "early_setup_score": 43.65,
    "entry_timing_score": 33.3,
    "opportunity_score": 63.33,
    "extended": false,
    "return_5d": 8.43,
    "return_10d": 12.66,
    "return_20d": 14.99,
    "distance_to_breakout": 4.89,
    "atr_extension": 1.54
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
      "datetime": 1789546320,
      "headline": "New Strong Buy Stocks for September 16th",
      "id": 142184181,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPQ",
      "source": "Yahoo",
      "summary": "ANF, APH, PARR, HPQ and SBLK have been added to the Zacks Rank #1 (Strong Buy) List on September 16th, 2026.",
      "url": "https://finnhub.io/api/news?id=9d867ee798491e88cb65eaada9a202740c8297882db3ed55e70cf24d669c52fb"
    },
    {
      "category": "company",
      "datetime": 1789542300,
      "headline": "Best Income Stocks to Buy for September 16th",
      "id": 142186699,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPQ",
      "source": "Yahoo",
      "summary": "SBLK, TXO, HPQ made it to the Zacks Rank #1 (Strong Buy) income stocks list on September 16th, 2026.",
      "url": "https://finnhub.io/api/news?id=b402f7da59b93d3d7995a31671b60a3f807729dfb09ea1a3fb722532ba5df984"
    },
    {
      "category": "company",
      "datetime": 1789490520,
      "headline": "Lenovo vs. HP: Which PC Giant Stock Has Better Prospects?",
      "id": 142166226,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPQ",
      "source": "Yahoo",
      "summary": "HP's stronger price gains, capital returns and cash-flow stability give it an edge, while Lenovo targets $100B in revenues within two years.",
      "url": "https://finnhub.io/api/news?id=dded21d7384b212a48fd8e78dbff4f074a1a636d6bac90fa404b923c1e57c9f2"
    },
    {
      "category": "company",
      "datetime": 1789489800,
      "headline": "3BL Announces the 100 Best Corporate Citizens of 2026",
      "id": 142165942,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPQ",
      "source": "Yahoo",
      "summary": "Hewlett Packard Enterprise takes the No. 1 spot, followed by Owens Corning, Trane Technologies, HP Inc.",
      "url": "https://finnhub.io/api/news?id=bf60b7dba69671ec64fa1d403c1c14b6e0f4b9841c5f4f128ffa901d9f027d1f"
    },
    {
      "category": "company",
      "datetime": 1789484506,
      "headline": "Would You Still Want Dell If The AI Orders Slowed?",
      "id": 142165297,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPQ",
      "source": "Yahoo",
      "summary": "Dell Technologies (DELL) has returned more than 330% over the past twelve months, and it still cannot build as much as its customers want. You can be paid today for agreeing to buy the stock well below today's price, and the payment is yours whether or not you ever own the shares. The catch is whether you would want the shares at that lower price.",
      "url": "https://finnhub.io/api/news?id=5a8e825d5b6b1a58f26c80c4b1e7a5fe78c20d99d9894cf42440cfec84d1de1a"
    }
  ],
  "polygon_news": [
    {
      "id": "035b4d9c1a11843b0049cc837362f70f1142fecee6f7bbb31b5eb1ba3386cc53",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "New Strong Buy Stocks for September 16th",
      "author": "Na",
      "published_utc": "2026-09-16T08:12:00Z",
      "article_url": "https://www.zacks.com/commentary/2989564/new-strong-buy-stocks-for-september-16th?cid=CS-ZC-FT-zacks_1_rank_additions-2989564",
      "tickers": [
        "ANF",
        "APH",
        "PARR",
        "HPQ",
        "SBLK"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/96/678.jpg",
      "description": "Five companies have been added to the Zacks Rank #1 (Strong Buy) list today based on increasing consensus earnings estimates over the last 60 days. The stocks include Abercrombie & Fitch (8% earnings estimate increase), Amphenol Corporation (9% increase), Par Pacific Holdings (19.5% increase), HP Inc. (8.4% increase), and Star Bulk Carriers Corp. (14.6% increase).",
      "keywords": [
        "Zacks Rank #1",
        "Strong Buy",
        "earnings estimates",
        "stock recommendations",
        "consensus estimates"
      ],
      "insights": [
        {
          "ticker": "ANF",
          "sentiment": "positive",
          "sentiment_reasoning": "Added to Zacks Rank #1 (Strong Buy) list with 8% increase in consensus earnings estimates over 60 days, indicating positive analyst sentiment and improving financial outlook."
        },
        {
          "ticker": "APH",
          "sentiment": "positive",
          "sentiment_reasoning": "Added to Zacks Rank #1 (Strong Buy) list with 9% increase in consensus earnings estimates over 60 days, reflecting growing confidence in the company's financial performance."
        },
        {
          "ticker": "PARR",
          "sentiment": "positive",
          "sentiment_reasoning": "Added to Zacks Rank #1 (Strong Buy) list with the highest earnings estimate increase at 19.5% over 60 days, indicating strong positive analyst revisions."
        },
        {
          "ticker": "HPQ",
          "sentiment": "positive",
          "sentiment_reasoning": "Added to Zacks Rank #1 (Strong Buy) list with 8.4% increase in consensus earnings estimates over 60 days, showing positive analyst sentiment."
        },
        {
          "ticker": "SBLK",
          "sentiment": "positive",
          "sentiment_reasoning": "Added to Zacks Rank #1 (Strong Buy) list with 14.6% increase in consensus earnings estimates over 60 days, indicating strong positive outlook from analysts."
        }
      ]
    },
    {
      "id": "d081ff5ed9ec3858f82b168fd8f0230c1c9deeb0fce4838d1ecf70d63f260562",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Best Income Stocks to Buy for September 16th",
      "author": "Na",
      "published_utc": "2026-09-16T07:05:00Z",
      "article_url": "https://www.zacks.com/commentary/2990290/best-income-stocks-to-buy-for-september-16th?cid=CS-ZC-FT-zacks_1_rank_additions|income_additions-2990290",
      "tickers": [
        "SBLK",
        "HPQ"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/96/294.jpg",
      "description": "Zacks highlights three Rank #1 stocks with strong income potential: Star Bulk Carriers (SBLK) with an 11.7% dividend yield and 14.6% earnings estimate increase; TXO Partners (TXO) with a 10.5% dividend yield and 288.2% earnings estimate increase; and HP Inc. (HPQ) with a 3.5% dividend yield and 8.4% earnings estimate increase.",
      "keywords": [
        "dividend yield",
        "income stocks",
        "Zacks Rank #1",
        "earnings estimates",
        "strong buy"
      ],
      "insights": [
        {
          "ticker": "SBLK",
          "sentiment": "positive",
          "sentiment_reasoning": "Zacks Rank #1 rating with 14.6% earnings estimate increase over 60 days and exceptional 11.7% dividend yield, significantly above industry average of 1.3%"
        },
        {
          "ticker": "HPQ",
          "sentiment": "positive",
          "sentiment_reasoning": "Zacks Rank #1 rating with 8.4% earnings estimate increase and 3.5% dividend yield, notably higher than industry average of 0.4%"
        }
      ]
    },
    {
      "id": "f15608cb8811ee8eb600bd1a0488ffffc042db58c06b95640b6f49914c3be520",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Should iShares Select Dividend ETF (DVY) Be on Your Investing Radar?",
      "author": "Zacks.Com",
      "published_utc": "2026-09-15T10:20:02Z",
      "article_url": "https://www.zacks.com/stock/news/2989567/should-ishares-select-dividend-etf-dvy-be-on-your-investing-radar?cid=CS-ZC-FT-style_box_etf-2989567",
      "tickers": [
        "DVY",
        "SCHD",
        "VTV",
        "PFH",
        "PRH",
        "PRS",
        "PRU",
        "HPQ",
        "PFE"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default196.jpg",
      "description": "The iShares Select Dividend ETF (DVY) is a large-cap value ETF with $23.60 billion in assets and a 0.38% expense ratio. It has delivered 16.75% returns year-to-date and 18.11% over the past year, with a 3.24% dividend yield. The ETF holds 106 stocks with heavy exposure to Financials (25.7%), Utilities, and Consumer Staples. While rated a 'Hold' by Zacks, investors should consider lower-cost alternatives like SCHD (0.06% expense ratio) and VTV (0.03% expense ratio).",
      "keywords": [
        "dividend ETF",
        "large-cap value",
        "passive investing",
        "expense ratio",
        "dividend yield",
        "ETF comparison"
      ],
      "insights": [
        {
          "ticker": "DVY",
          "sentiment": "neutral",
          "sentiment_reasoning": "The ETF shows solid performance (16.75% YTD, 18.11% 1-year) and reasonable dividend yield (3.24%), but receives a 'Hold' rating. The 0.38% expense ratio is higher than comparable alternatives, which is a notable drawback for cost-conscious investors."
        },
        {
          "ticker": "SCHD",
          "sentiment": "positive",
          "sentiment_reasoning": "Presented as a superior alternative with significantly lower expense ratio (0.06% vs DVY's 0.38%) and substantially larger assets ($111.66 billion), making it more attractive for dividend-focused investors."
        },
        {
          "ticker": "VTV",
          "sentiment": "positive",
          "sentiment_reasoning": "Highlighted as the best alternative option with the lowest expense ratio (0.03%) and the largest asset base ($190.58 billion), representing the most cost-efficient choice in the large-cap value segment."
        },
        {
          "ticker": "PFH",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as the largest individual holding in DVY (2.21% of assets) with no specific performance commentary, serving only as a portfolio composition reference."
        },
        {
          "ticker": "PRH",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as the largest individual holding in DVY (2.21% of assets) with no specific performance commentary, serving only as a portfolio composition reference."
        },
        {
          "ticker": "PRS",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as the largest individual holding in DVY (2.21% of assets) with no specific performance commentary, serving only as a portfolio composition reference."
        },
        {
          "ticker": "PRU",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as the largest individual holding in DVY (2.21% of assets) with no specific performance commentary, serving only as a portfolio composition reference."
        },
        {
          "ticker": "HPQ",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a top holding in DVY with no specific analysis or commentary provided."
        },
        {
          "ticker": "PFE",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a top holding in DVY with no specific analysis or commentary provided."
        }
      ]
    },
    {
      "id": "9b0448b52550b8bf50adc4592a8d7fe32ccb0fa2c4f20bb649af755b0a227d67",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Best Income Stocks to Buy for September 14th",
      "author": "Na",
      "published_utc": "2026-09-14T09:28:00Z",
      "article_url": "https://www.zacks.com/commentary/2988838/best-income-stocks-to-buy-for-september-14th?cid=CS-ZC-FT-zacks_1_rank_additions|income_additions-2988838",
      "tickers": [
        "TX",
        "HPQ",
        "TAK"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/e7/288.jpg",
      "description": "Zacks highlights three Rank #1 stocks with strong income potential: Ternium S.A. (TX) with a 4.5% dividend yield and 26.7% earnings estimate increase; HP Inc. (HPQ) with a 3.4% dividend yield and 8.4% earnings estimate increase; and Takeda Pharmaceutical Company Limited (TAK) with a 2.6% dividend yield and 10.7% earnings estimate increase.",
      "keywords": [
        "dividend yield",
        "Zacks Rank #1",
        "income stocks",
        "earnings estimates",
        "strong buy"
      ],
      "insights": [
        {
          "ticker": "TX",
          "sentiment": "positive",
          "sentiment_reasoning": "Zacks Rank #1 rating with highest dividend yield (4.5%) among the three stocks and significant 26.7% earnings estimate increase over 60 days, indicating strong financial performance and investor confidence."
        },
        {
          "ticker": "HPQ",
          "sentiment": "positive",
          "sentiment_reasoning": "Zacks Rank #1 rating with solid 3.4% dividend yield and 8.4% earnings estimate increase, demonstrating positive earnings momentum and attractive income generation for investors."
        },
        {
          "ticker": "TAK",
          "sentiment": "positive",
          "sentiment_reasoning": "Zacks Rank #1 rating with 10.7% earnings estimate increase over 60 days and 2.6% dividend yield, showing strong earnings growth and income potential in the pharmaceutical sector."
        }
      ]
    },
    {
      "id": "606182747eda1cb3da82e01a064b61024cda8382d23a436c4cc2d368ef382ff1",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Is iShares Select Dividend ETF (DVY) a Strong ETF Right Now?",
      "author": "Na",
      "published_utc": "2026-09-11T10:20:02Z",
      "article_url": "https://www.zacks.com/stock/news/2988131/is-ishares-select-dividend-etf-dvy-a-strong-etf-right-now?cid=CS-ZC-FT-smart_beta_etf-2988131",
      "tickers": [
        "DVY",
        "SCHD",
        "VTV",
        "PFH",
        "PRH",
        "PRS",
        "PRU",
        "HPQ",
        "PFE"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default336.jpg",
      "description": "The article examines DVY, a smart beta ETF managed by BlackRock that tracks the Dow Jones U.S. Select Dividend Index. With $23.53 billion in assets and a 0.38% expense ratio, DVY offers exposure to high-dividend-yielding large-cap stocks with a 3.25% trailing dividend yield. The fund has delivered 16.28% returns and trades at medium risk (beta 0.66). However, cheaper alternatives like SCHD (0.06% expense ratio) and VTV (0.03% expense ratio) are available for cost-conscious investors.",
      "keywords": [
        "smart beta ETF",
        "dividend yield",
        "large cap value",
        "expense ratio",
        "dividend stocks"
      ],
      "insights": [
        {
          "ticker": "DVY",
          "sentiment": "positive",
          "sentiment_reasoning": "DVY is presented as a reasonable option with solid fundamentals: $23.53B in assets, competitive 0.38% expense ratio, 3.25% dividend yield, and 16.28% returns. The fund effectively diversifies risk with 106 holdings and medium risk profile (beta 0.66)."
        },
        {
          "ticker": "SCHD",
          "sentiment": "positive",
          "sentiment_reasoning": "SCHD is highlighted as a superior alternative with significantly lower expense ratio (0.06% vs DVY's 0.38%) and substantially larger assets ($110.18B), making it more attractive for cost-conscious investors."
        },
        {
          "ticker": "VTV",
          "sentiment": "positive",
          "sentiment_reasoning": "VTV is presented as another strong alternative with the lowest expense ratio (0.03%) and the largest asset base ($190.16B), representing the most cost-efficient option for large-cap value exposure."
        },
        {
          "ticker": "PFH",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as DVY's largest individual holding (2.21% of portfolio) without qualitative assessment; serves as factual disclosure of fund composition."
        },
        {
          "ticker": "PRH",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as DVY's largest individual holding (2.21% of portfolio) without qualitative assessment; serves as factual disclosure of fund composition."
        },
        {
          "ticker": "PRS",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as DVY's largest individual holding (2.21% of portfolio) without qualitative assessment; serves as factual disclosure of fund composition."
        },
        {
          "ticker": "PRU",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as DVY's largest individual holding (2.21% of portfolio) without qualitative assessment; serves as factual disclosure of fund composition."
        },
        {
          "ticker": "HPQ",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as a top holding in DVY without qualitative assessment; included for transparency regarding fund holdings."
        },
        {
          "ticker": "PFE",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a top holding in DVY without qualitative assessment; included for transparency regarding fund holdings."
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
      "epsEstimate": 0.761,
      "epsActual": null,
      "revenueEstimate": 15598287570,
      "revenueActual": null
    }
  ],
  "fundamentals": {
    "10DayAverageTradingVolume": 16.26663,
    "13WeekPriceReturnDaily": 33.9937,
    "26WeekPriceReturnDaily": 83.2069,
    "3MonthADReturnStd": 48.500774,
    "3MonthAverageTradingVolume": 17.79066,
    "52WeekHigh": 36.225,
    "52WeekHighDate": "2026-09-11",
    "52WeekLow": 17.56,
    "52WeekLowDate": "2026-02-25",
    "52WeekPriceReturnDaily": 21.8739,
    "5DayPriceReturnDaily": 4.4149,
    "assetTurnoverAnnual": 1.3238,
    "assetTurnoverTTM": 1.3763,
    "beta": 1.1837364,
    "bookValuePerShareAnnual": 15.3925,
    "bookValuePerShareQuarterly": 15.3925,
    "bookValueShareGrowth5Y": -3.46,
    "capexCagr5Y": 9.11,
    "cashFlowPerShareAnnual": 3.0402,
    "cashFlowPerShareQuarterly": 4.2437,
    "cashFlowPerShareTTM": 4.11043,
    "cashPerSharePerShareAnnual": 4.0065,
    "cashPerSharePerShareQuarterly": 4.5587,
    "currentDividendYieldTTM": 3.5903,
    "currentEv/freeCashFlowAnnual": 12.6748,
    "currentEv/freeCashFlowTTM": 9.1444,
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
    "enterpriseValue": 35489.572,
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
    "evEbitdaTTM": 10.2334,
    "evRevenueTTM": 0.5999,
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
    "marketCapitalization": 30498.572,
    "monthToDatePriceReturnDaily": 12.6582,
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
    "pb": 1.0983,
    "pbAnnual": 0.8956,
    "pbQuarterly": 0.8956,
    "pcfShareAnnual": 8.2495,
    "pcfShareTTM": 6.5335,
    "peAnnual": 12.0595,
    "peBasicExclExtraTTM": 12.4433,
    "peExclExtraAnnual": 8.7772,
    "peExclExtraTTM": 12.4433,
    "peInclExtraTTM": 12.4433,
    "peNormalizedAnnual": 12.0595,
    "peTTM": 12.4433,
    "pegTTM": 2.95806,
    "pfcfShareAnnual": 10.8923,
    "pfcfShareTTM": 7.8584,
    "pretaxMargin5Y": 7.04,
    "pretaxMarginAnnual": 4.83,
    "pretaxMarginTTM": 4.73,
    "priceRelativeToS&P50013Week": 31.8852,
    "priceRelativeToS&P50026Week": 71.2216,
    "priceRelativeToS&P5004Week": 14.1946,
    "priceRelativeToS&P50052Week": 7.2758,
    "priceRelativeToS&P500Ytd": 40.728,
    "psAnnual": 0.5516,
    "psTTM": 0.5155,
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
    "yearToDatePriceReturnDaily": 51.7953
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

## PFE
Trading candidate:
```json
{
  "symbol": "PFE",
  "score": 56.41,
  "direction": "LONG",
  "sector": "Healthcare",
  "components": {
    "market": 50.0,
    "sector": 56.67,
    "relative_strength": 62.34689539766923,
    "vwap": 100.0,
    "trend": 0.0,
    "volume": 57.83579779933843,
    "momentum": 53.330935251798564,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 46.78414634494633,
    "trend_acceleration": 25,
    "compression": 35.52368850971152,
    "volatility_contraction": 79.83559370380934,
    "volume_accumulation": 38.14520668517189,
    "breakout_distance": 0.0,
    "support_quality": 89.65329460882192,
    "momentum_improvement": 43.78067464122522,
    "early_setup_score": 35.45,
    "entry_timing_score": 35.45,
    "opportunity_score": 50.12,
    "extended": false,
    "return_5d": -0.92,
    "return_10d": -3.25,
    "return_20d": 2.55,
    "distance_to_breakout": 5.37,
    "atr_extension": -1.17
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
      "datetime": 1789565158,
      "headline": "How a Roth IRA Can Keep Thousands More of Your High-Yield Dividend Income Compounding",
      "id": 142195281,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "Where you hold a high-yield dividend stock matters almost as much as which one you pick, and for ordinary-income payers like BDCs and REITs, the wrong account quietly erodes a portion of every distribution before it ever compounds.",
      "url": "https://finnhub.io/api/news?id=696beaf84ba82f283bd674d00abe3894302551bce23d1b48376bcfafbc92b9ae"
    },
    {
      "category": "company",
      "datetime": 1789559100,
      "headline": "Creative Spirit Hosts 2026 \"Gen Neu\" Gala at the New York Stock Exchange, Unveils Workplace Technology Partnership",
      "id": 142194194,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "Pfizer named 2026 Corporate Champion of Neurodiversity; Colgate-Palmolive's Jesma Johnson and Agency Search Kaizen's Lisa Colantuono honored as Individual ChampionsNEW YORK CITY, NY / ACCESS Newswire / September 16, 2026 / , the nonprofit dedicated to normalizing neurodiversity in the workplace and creating employment opportunities for individuals with disabilities, hosted its 2026 gala on September 10 at the New York Stock Exchange. This year's event, themed Gen Neu, honored corporate and indiv",
      "url": "https://finnhub.io/api/news?id=c59728d2525481616d22a447782180379370d5f211326dfeb1c7a6449285b8b7"
    },
    {
      "category": "company",
      "datetime": 1789553509,
      "headline": "1 Stock Under $50 to Target This Week and 2 That Underwhelm",
      "id": 142189108,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "Stocks trading between $10 and $50 can be particularly interesting as they frequently represent businesses that have survived their early challenges. However, investors should remain vigilant as some may still have unproven business models, leaving them vulnerable to the ebbs and flows of the broader market.",
      "url": "https://finnhub.io/api/news?id=d737c2770d120a3748e74221e127603a75e0edd3c86886dc2467ed082cf26d35"
    },
    {
      "category": "company",
      "datetime": 1789552020,
      "headline": "The Zacks Analyst Blog Highlights Pfizer, Novartis, Candel and Janux",
      "id": 142188378,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "Prostate cancer awareness spotlights Pfizer's Xtandi, Novartis' Pluvicto and clinical-stage programs from Candel and Janux.",
      "url": "https://finnhub.io/api/news?id=7a65af2a722af63aa6507d9b2c881e6e4a2669f2ae221018fe49f5343f6b7b6a"
    },
    {
      "category": "company",
      "datetime": 1789519473,
      "headline": "Merck Stock: Is The $70 Billion Pipeline Worth the Premium?",
      "id": 142172297,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "A powerful drug pipeline is fueling a stock trend that ranks in the top 6% of US stocks worth more than $1 billion, but the ticket price for investors is steep and the clock is ticking on its biggest star.",
      "url": "https://finnhub.io/api/news?id=bd676c4b44a7da2d7f11725925ca1f235568cd8910e075fe2bc5a17b09e1dee6"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 32.20685,
    "13WeekPriceReturnDaily": 5.9228,
    "26WeekPriceReturnDaily": 2.0619,
    "3MonthADReturnStd": 22.510906,
    "3MonthAverageTradingVolume": 39.61402,
    "52WeekHigh": 29.21,
    "52WeekHighDate": "2026-09-03",
    "52WeekLow": 23.58,
    "52WeekLowDate": "2025-09-25",
    "52WeekPriceReturnDaily": 16.129,
    "5DayPriceReturnDaily": -0.2519,
    "assetTurnoverAnnual": 0.3006,
    "assetTurnoverTTM": 0.3086,
    "beta": 0.2789568,
    "bookValuePerShareAnnual": 15.2086,
    "bookValuePerShareQuarterly": 14.9482,
    "bookValueShareGrowth5Y": 6.01,
    "capexCagr5Y": -1.19,
    "cashFlowPerShareAnnual": 1.5962,
    "cashFlowPerShareQuarterly": 1.9277,
    "cashFlowPerShareTTM": 2.91656,
    "cashPerSharePerShareAnnual": 2.3911,
    "cashPerSharePerShareQuarterly": 2.0528,
    "currentDividendYieldTTM": 6.2315,
    "currentEv/freeCashFlowAnnual": 24.1565,
    "currentEv/freeCashFlowTTM": 19.9567,
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
    "enterpriseValue": 219244,
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
    "evEbitdaTTM": 23.9742,
    "evRevenueTTM": 3.4421,
    "focfCagr5Y": -4.81,
    "forwardPE": 8.64266,
    "grossMargin5Y": 69.76,
    "grossMarginAnnual": 75.81,
    "grossMarginTTM": 74.71,
    "inventoryTurnoverAnnual": 1.408,
    "inventoryTurnoverTTM": 1.4903,
    "longTermDebt/equityAnnual": 0.7128,
    "longTermDebt/equityQuarterly": 0.7101,
    "marketCapitalization": 157026,
    "monthToDatePriceReturnDaily": -2.6001,
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
    "pb": 1.8432,
    "pbAnnual": 1.6371,
    "pbQuarterly": 1.6304,
    "pcfShareAnnual": 13.4153,
    "pcfShareTTM": 11.7166,
    "peAnnual": 20.2093,
    "peBasicExclExtraTTM": 36.2396,
    "peExclExtraAnnual": 5.57472,
    "peExclExtraTTM": 36.2396,
    "peInclExtraTTM": 36.2396,
    "peNormalizedAnnual": 20.2093,
    "peTTM": 36.2396,
    "pegTTM": -2.72351,
    "pfcfShareAnnual": 17.3012,
    "pfcfShareTTM": 14.2933,
    "pretaxMargin5Y": 18.13,
    "pretaxMarginAnnual": 12.02,
    "pretaxMarginTTM": 6.61,
    "priceRelativeToS&P50013Week": 2.789,
    "priceRelativeToS&P50026Week": -10.2982,
    "priceRelativeToS&P5004Week": 4.6893,
    "priceRelativeToS&P50052Week": 0.39,
    "priceRelativeToS&P500Ytd": -0.2538,
    "psAnnual": 2.5092,
    "psTTM": 2.4653,
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
    "yearToDatePriceReturnDaily": 11.3253
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

## WMT
Trading candidate:
```json
{
  "symbol": "WMT",
  "score": 47.15,
  "direction": "WATCH",
  "sector": "Unknown",
  "components": {
    "market": 50.0,
    "sector": 50.0,
    "relative_strength": 56.43517161693174,
    "vwap": 0.0,
    "trend": 50.0,
    "volume": 39.49449723667249,
    "momentum": 67.61689291101052,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 63.66606909592015,
    "trend_acceleration": 55,
    "compression": 62.92321924144307,
    "volatility_contraction": 81.50522003435975,
    "volume_accumulation": 30.889935965596155,
    "breakout_distance": 0.0,
    "support_quality": 49.306197964847456,
    "momentum_improvement": 63.07430064233816,
    "early_setup_score": 50.71,
    "entry_timing_score": 50.71,
    "opportunity_score": 48.22,
    "extended": false,
    "return_5d": 1.9,
    "return_10d": 3.12,
    "return_20d": -5.46,
    "distance_to_breakout": 6.57,
    "atr_extension": 0.86
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
      "datetime": 1789564562,
      "headline": "Walmart partners with SCAN Health on Medicare Advantage plans",
      "id": 142195109,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WMT",
      "source": "Yahoo",
      "summary": "The co-branded plans will be available to more than 2 million Medicare enrollees in two states when open enrollment begins Oct. 15",
      "url": "https://finnhub.io/api/news?id=e9768683f2e594f889cdc41989accd90441037ee6b62f4e47b57770299a94fd7"
    },
    {
      "category": "company",
      "datetime": 1789561980,
      "headline": "Raspberry AI Transforms How Fashion Brands Go From Concept To Commerce With Launch Of New Agentic Platform",
      "id": 142195110,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WMT",
      "source": "Yahoo",
      "summary": "Raspberry AI, the company helping brands move at the speed of inspiration, today announced a major expansion of its platform that brings the entire fashion product lifecycle into one AI-powered agentic workflow. In a first for the fashion industry, Raspberry AI is unifying AI agents across design, merchandising, wholesale, marketing and e-commerce, creating an entirely new path from initial concept to commerce, and transforming how brands bring products to life in the physical world.",
      "url": "https://finnhub.io/api/news?id=0550ebed0d24465ac07b3c803551173d9237b088f17e6cea5e02fc7034436a64"
    },
    {
      "category": "company",
      "datetime": 1789550012,
      "headline": "Walmart adds Citgo locations to membership fuel benefits",
      "id": 142195111,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WMT",
      "source": "Yahoo",
      "summary": "Customers filling up at Citgo stations can combine the Walmart+ 10-cent discount with further offers from Club Citgo memberships.",
      "url": "https://finnhub.io/api/news?id=f70f27d763abb06b4e1b53b656a72386d7baedd2486d734e5f213558e0ee0882"
    },
    {
      "category": "company",
      "datetime": 1789546318,
      "headline": "How Investors Are Reacting To Walmart (WMT) Expanding Its Digital Marketplace With ADT Blu And RocketSports",
      "id": 142188302,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WMT",
      "source": "Yahoo",
      "summary": "Earlier this month, ADT Inc. said its ADT Blu DIY home security system became available on Walmart.com, while RocketSports-1 women\u2019s activewear rolled out to 37 Walmart stores across 18 states and nationwide online. These additions broaden Walmart\u2019s marketplace assortment in higher-value categories like connected home and fitness apparel, reinforcing its push into fee-generating digital retail partnerships. We\u2019ll explore how Walmart\u2019s expanded third-party marketplace, including ADT Blu\u2019s...",
      "url": "https://finnhub.io/api/news?id=fb0b9f3dba42eda2160bfa182f302805873100a2487e7abec5a731bd3a66ce12"
    },
    {
      "category": "company",
      "datetime": 1789543800,
      "headline": "Casey's General Stores: A $100+ Post-Earnings Sell-Off - Why I'm Not Buying Yet",
      "id": 142193153,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/614026982/image_614026982.jpg?io=getty-c-w1536",
      "related": "WMT",
      "source": "SeekingAlpha",
      "summary": "Casey's General Stores delivered a double-beat quarter, but shares plunged over $100 post-earnings due to valuation and growth concerns. See why CASY stock is a Hold.",
      "url": "https://finnhub.io/api/news?id=68c9b6d8d07d776139782d011d278ac2b6a9ff96d98c120c09c462045315571e"
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
      "epsEstimate": 0.6438,
      "epsActual": null,
      "revenueEstimate": 189188688542,
      "revenueActual": null
    }
  ],
  "fundamentals": {
    "10DayAverageTradingVolume": 22.37804,
    "13WeekPriceReturnDaily": -9.4772,
    "26WeekPriceReturnDaily": -12.8197,
    "3MonthADReturnStd": 28.140177,
    "3MonthAverageTradingVolume": 24.15195,
    "52WeekHigh": 135.16,
    "52WeekHighDate": "2026-05-19",
    "52WeekLow": 98.88,
    "52WeekLowDate": "2025-11-14",
    "52WeekPriceReturnDaily": 5.4015,
    "5DayPriceReturnDaily": 2.8571,
    "assetTurnoverAnnual": 2.5052,
    "assetTurnoverTTM": 2.5443,
    "beta": 0.5590074,
    "bookValuePerShareAnnual": 12.5006,
    "bookValuePerShareQuarterly": 12.3444,
    "bookValueShareGrowth5Y": 5.51,
    "capexCagr5Y": 21.02,
    "cashFlowPerShareAnnual": 1.8726,
    "cashFlowPerShareQuarterly": 1.6975,
    "cashFlowPerShareTTM": 10.33484,
    "cashPerSharePerShareAnnual": 1.3461,
    "cashPerSharePerShareQuarterly": 1.4487,
    "currentDividendYieldTTM": 0.9054,
    "currentEv/freeCashFlowAnnual": 60.0291,
    "currentEv/freeCashFlowTTM": 66.3125,
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
    "enterpriseValue": 895814.94,
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
    "evEbitdaTTM": 18.9098,
    "evRevenueTTM": 1.2174,
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
    "marketCapitalization": 850100.94,
    "monthToDatePriceReturnDaily": 4.0145,
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
    "pb": 8.6535,
    "pbAnnual": 9.9258,
    "pbQuarterly": 9.0081,
    "pcfShareAnnual": 20.4523,
    "pcfShareTTM": 19.8053,
    "peAnnual": 38.8298,
    "peBasicExclExtraTTM": 38.5079,
    "peExclExtraAnnual": 36.52979,
    "peExclExtraTTM": 38.5079,
    "peInclExtraTTM": 38.5079,
    "peNormalizedAnnual": 38.8298,
    "peTTM": 38.5079,
    "pegTTM": 4.005,
    "pfcfShareAnnual": 56.9658,
    "pfcfShareTTM": 55.0049,
    "pretaxMargin5Y": 3.48,
    "pretaxMarginAnnual": 4.13,
    "pretaxMarginTTM": 3.98,
    "priceRelativeToS&P50013Week": -12.611,
    "priceRelativeToS&P50026Week": -25.1798,
    "priceRelativeToS&P5004Week": -3.0661,
    "priceRelativeToS&P50052Week": -10.3375,
    "priceRelativeToS&P500Ytd": -13.6705,
    "psAnnual": 1.192,
    "psTTM": 1.1553,
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
    "yearToDatePriceReturnDaily": -2.0914
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

## NFLX
Trading candidate:
```json
{
  "symbol": "NFLX",
  "score": 48.4,
  "direction": "WATCH",
  "sector": "Communication Services",
  "components": {
    "market": 50.0,
    "sector": 92.74,
    "relative_strength": 74.19402075859858,
    "vwap": 0.0,
    "trend": 0.0,
    "volume": 51.15901095236961,
    "momentum": 65.91145833333337,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 55.21208901313549,
    "trend_acceleration": 25,
    "compression": 0.0,
    "volatility_contraction": 69.55704845613104,
    "volume_accumulation": 41.89323426088194,
    "breakout_distance": 0.0,
    "support_quality": 75.5565535382049,
    "momentum_improvement": 53.41260911915568,
    "early_setup_score": 29.86,
    "entry_timing_score": 29.86,
    "opportunity_score": 42.84,
    "extended": false,
    "return_5d": 1.48,
    "return_10d": -3.86,
    "return_20d": 2.5,
    "distance_to_breakout": 6.13,
    "atr_extension": -0.87
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
      "datetime": 1789565131,
      "headline": "The Bull Case for Netflix\u2019s (NFLX) New Growth Engine",
      "id": 142195146,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NFLX",
      "source": "Yahoo",
      "summary": "Weitz Investment Management, an investment management firm, released its second-quarter Q2 2026 investor letter for the \u201cMulti Cap Equity Fund\u201d. The letter can be downloaded here. The Multi Cap Equity Fund\u2019s Institutional Class returned 7.90% in Q2, underperforming the Bloomberg U.S. 3000 Index\u2019s 15.71% gain. Markets rose in the quarter on hopes of de-escalating Middle East [\u2026]",
      "url": "https://finnhub.io/api/news?id=bb15f7ee74ed7db4656e5d0a01b9b4ae0924173785c4a31c1bb18e0c57cc4310"
    },
    {
      "category": "company",
      "datetime": 1789554001,
      "headline": "Bill Ackman\u2019s Pershing Square Capital Management Sold Alphabet and Bought These 2 Beaten-Down Stocks",
      "id": 142193935,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NFLX",
      "source": "Yahoo",
      "summary": "Does Ackman know something Wall Street doesn't?",
      "url": "https://finnhub.io/api/news?id=f1229b3ea5dcf46baabe0ca81fb0cb02ddded5c8ae32bdbe7aae09ba2c0764d8"
    },
    {
      "category": "company",
      "datetime": 1789535618,
      "headline": "Netflix (NFLX) Could Be 5% Undervalued As Live Events And Ads Shape The Next Phase",
      "id": 142177695,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NFLX",
      "source": "Yahoo",
      "summary": "Netflix (NFLX) shares moved about 3% higher after Evercore highlighted live events, short form video and the ad supported tier as key levers to deepen engagement beyond traditional series and films. For context, Netflix shares have drifted lower this year, with a year-to-date share price return down about 14%, even though the 3-year total shareholder return is a little over 100%. This indicates that recent momentum looks softer than the longer-term record. Scan beyond Netflix and see how...",
      "url": "https://finnhub.io/api/news?id=86a30abc9e5928f30954ea2c7416feabcd16b696cf4bea644d7f8ed11487c0ef"
    },
    {
      "category": "company",
      "datetime": 1789508705,
      "headline": "Netflix (NFLX) Suffers a Larger Drop Than the General Market: Key Insights",
      "id": 142168545,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NFLX",
      "source": "Yahoo",
      "summary": "Netflix (NFLX) concluded the recent trading session at $77.91, signifying a -3% move from its prior day's close.",
      "url": "https://finnhub.io/api/news?id=3ec5a3d9c3dd3d4ea2c21aa58cc87944f22914fb4dd35a27c08cd1d6f8e508c4"
    },
    {
      "category": "company",
      "datetime": 1789502421,
      "headline": "Netflix Options Call A One-Third Drop Ordinary, So How Much Stock Should You Hold?",
      "id": 142168383,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NFLX",
      "source": "Yahoo",
      "summary": "Netflix (NFLX) trades at about $80, and its own options put a price on how far that can travel over the twelve months ahead: a floor near $54.21 and a ceiling near $119. The options market is charging nothing unusual for that range. Ordinary, for Netflix, already means a range wide enough to take a third of your money.",
      "url": "https://finnhub.io/api/news?id=d634cb229e11fe66344cd56f723b9e4ceb5da9a6bcf7c72f4e744d802933a87a"
    }
  ],
  "polygon_news": [
    {
      "id": "c7121571cf9f385980de8f499ea93e75738a4d674614197d4206de0d71932b06",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Netflix (NFLX) Suffers a Larger Drop Than the General Market: Key Insights",
      "author": "Zacks.Com",
      "published_utc": "2026-09-15T21:45:05Z",
      "article_url": "https://www.zacks.com/stock/news/2990203/netflix-nflx-suffers-a-larger-drop-than-the-general-market-key-insights?cid=CS-ZC-FT-fundamental_analysis|yseop_template_6-2990203",
      "tickers": [
        "NFLX"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default192.jpg",
      "description": "Netflix stock declined 3% on September 15, 2026, underperforming the broader market. Despite a 5.66% monthly gain, the company faces upcoming earnings on October 20 with analyst expectations of $0.82 EPS (39% YoY growth) and $12.88B revenue (11.9% YoY growth). Netflix holds a Zacks Rank #3 (Hold) with a Forward P/E of 22.35, trading at a premium to its industry average.",
      "keywords": [
        "Netflix stock decline",
        "earnings report",
        "valuation metrics",
        "Zacks Rank",
        "market underperformance",
        "Forward P/E ratio",
        "analyst estimates"
      ],
      "insights": [
        {
          "ticker": "NFLX",
          "sentiment": "neutral",
          "sentiment_reasoning": "Netflix experienced a larger daily decline (-3%) than the broader market, but maintains positive momentum with a 5.66% monthly gain. Strong earnings growth expectations (39% YoY) are offset by a premium valuation (Forward P/E 22.35 vs. industry 11.54) and a Hold rating from Zacks. The neutral sentiment reflects mixed signals between fundamentals and valuation."
        }
      ]
    },
    {
      "id": "c19e09f1fef8baed137d5a90fc335f6e74f074b503efe207beafb6635eb1e6ea",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Netflix Stock Rose 4% While the AI Trade Sold Off on Monday. Its Capital Goes Into Shows, Not Silicon.",
      "author": "Daniel Sparks",
      "published_utc": "2026-09-14T19:27:01Z",
      "article_url": "https://www.fool.com/investing/2026/09/14/netflix-stock-rose-4-while-the-ai-trade-sold-off-on-monday-its-capital-goes-into-shows-not-silicon/?source=iedfolrf0000001",
      "tickers": [
        "NFLX",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "MU",
        "ARM",
        "NVDA"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F295ad00e3230175efddf90d098ff5057f682b0db-2000x1200.jpg%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "Netflix stock rose 4% on Monday as AI-related stocks sold off following calls from Anthropic and OpenAI leaders to slow AI development. Unlike major AI infrastructure spenders like Alphabet, Netflix invests primarily in content ($9.9B in H1 2026) rather than capital equipment ($415M), generating strong free cash flow of $12.5B expected for 2026. However, the stock remains down 36% from its 52-week high due to slowing revenue growth.",
      "keywords": [
        "Netflix",
        "AI stocks",
        "capital expenditure",
        "free cash flow",
        "content spending",
        "revenue growth slowdown",
        "stock buybacks"
      ],
      "insights": [
        {
          "ticker": "NFLX",
          "sentiment": "positive",
          "sentiment_reasoning": "Stock rose 4% Monday; generates strong free cash flow ($12.5B expected for 2026, up 30% YoY); not dependent on AI infrastructure spending; executing large buyback program ($4.7B in Q2). However, sentiment is tempered by slowing revenue growth (13-14% expected, down from prior quarters)."
        },
        {
          "ticker": "GOOG",
          "sentiment": "negative",
          "sentiment_reasoning": "Stock fell as part of AI trade selloff; massive capital expenditure commitments ($195-205B planned for 2026) create cash flow strain; payoff on data center investments may be years away; slower AI industry development would ease but not eliminate cash pressure."
        },
        {
          "ticker": "GOOGL",
          "sentiment": "negative",
          "sentiment_reasoning": "Stock fell as part of AI trade selloff; massive capital expenditure commitments ($195-205B planned for 2026) create cash flow strain; payoff on data center investments may be years away; slower AI industry development would ease but not eliminate cash pressure."
        },
        {
          "ticker": "GOOGM",
          "sentiment": "negative",
          "sentiment_reasoning": "Stock fell as part of AI trade selloff; massive capital expenditure commitments ($195-205B planned for 2026) create cash flow strain; payoff on data center investments may be years away; slower AI industry development would ease but not eliminate cash pressure."
        },
        {
          "ticker": "GOOGN",
          "sentiment": "negative",
          "sentiment_reasoning": "Stock fell as part of AI trade selloff; massive capital expenditure commitments ($195-205B planned for 2026) create cash flow strain; payoff on data center investments may be years away; slower AI industry development would ease but not eliminate cash pressure."
        },
        {
          "ticker": "MU",
          "sentiment": "negative",
          "sentiment_reasoning": "Stock fell ~5% Monday as part of AI hardware selloff following calls to slow AI development pace; directly dependent on continued AI infrastructure build-out."
        },
        {
          "ticker": "ARM",
          "sentiment": "negative",
          "sentiment_reasoning": "Stock dropped ~9% Monday as part of AI trade selloff; chip designer dependent on sustained AI infrastructure spending."
        },
        {
          "ticker": "NVDA",
          "sentiment": "negative",
          "sentiment_reasoning": "Stock slid ~3% Monday as part of broader AI hardware selloff following industry leaders' calls to slow AI development."
        }
      ]
    },
    {
      "id": "6df0ee9b475ebbf18247e0860c5f1368868256a3d646525253ec07d3c4e71551",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "GTN vs. NFLX: Which Stock Is the Better Value Option?",
      "author": "Na",
      "published_utc": "2026-09-14T15:40:03Z",
      "article_url": "https://www.zacks.com/stock/news/2989296/gtn-vs-nflx-which-stock-is-the-better-value-option?cid=CS-ZC-FT-fundamental_analysis|yseop_template_3-2989296",
      "tickers": [
        "GTN",
        "GTN.A",
        "NFLX"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default241.jpg",
      "description": "Gray Media (GTN) and Netflix (NFLX) are compared as potential value stock investments in the Broadcast Radio and Television sector. Gray Media emerges as the superior value option with a Zacks Rank #2 (Buy) rating, forward P/E of 2.08, and Value grade of A, compared to Netflix's Zacks Rank #3 (Hold), forward P/E of 21.54, and Value grade of D. GTN's improving earnings outlook and significantly lower valuation metrics make it the more attractive choice for value investors.",
      "keywords": [
        "value investing",
        "stock comparison",
        "valuation metrics",
        "P/E ratio",
        "Zacks Rank",
        "earnings outlook"
      ],
      "insights": [
        {
          "ticker": "GTN",
          "sentiment": "positive",
          "sentiment_reasoning": "Gray Media has a superior Zacks Rank #2 (Buy), significantly lower valuation metrics (P/E of 2.08, PEG of 0.10, P/B of 0.23), an improving earnings outlook, and a Value grade of A, making it the recommended choice for value investors."
        },
        {
          "ticker": "GTN.A",
          "sentiment": "positive",
          "sentiment_reasoning": "Gray Media has a superior Zacks Rank #2 (Buy), significantly lower valuation metrics (P/E of 2.08, PEG of 0.10, P/B of 0.23), an improving earnings outlook, and a Value grade of A, making it the recommended choice for value investors."
        },
        {
          "ticker": "NFLX",
          "sentiment": "negative",
          "sentiment_reasoning": "Netflix has a lower Zacks Rank #3 (Hold), substantially higher valuation multiples (P/E of 21.54, PEG of 1.09, P/B of 10.69), and a Value grade of D, indicating it is less attractive as a value investment compared to Gray Media."
        }
      ]
    },
    {
      "id": "f4699a2afdc81d3a1a467337c337fa12eb3f45ccc537d94dcf25086838e1981e",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Walt Disney vs. Roblox: Which Media Stock Is a Better Buy in 2026?",
      "author": "Sara Appino",
      "published_utc": "2026-09-14T14:19:14Z",
      "article_url": "https://www.fool.com/coverage/better-buy/2026/09/14/walt-disney-vs-roblox-which-media-stock-is-a-better-buy-in-2026/?source=iedfolrf0000001",
      "tickers": [
        "DIS",
        "RBLX",
        "NFLX",
        "AAPL",
        "MSFT",
        "AMZN"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2Fdf62d03add0a26cc05ef3d45b8f39a15145fe783-1200x800.png%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "The article compares Walt Disney and Roblox as investment options for 2026. Disney is recommended as the better choice due to its profitability, strong cash flows, and momentum across streaming, theme parks, and sports divisions. Roblox, while building an engaged gaming platform with 111.8 million daily active users, is currently unprofitable with a negative net margin of 21.8% and is guiding for a sharp decline in bookings, asking investors to wait for long-term returns.",
      "keywords": [
        "media stocks",
        "streaming platforms",
        "user-generated content",
        "profitability",
        "cash flow",
        "valuation",
        "investment comparison"
      ],
      "insights": [
        {
          "ticker": "DIS",
          "sentiment": "positive",
          "sentiment_reasoning": "Disney demonstrates strong financial performance with $94.4B revenue, $12.4B net income, 13.1% net margin, positive free cash flow of $10.1B, and successful operations across streaming (132M Disney+ subscribers), theme parks (record revenue), and sports. The company is executing well across all divisions and returning capital to shareholders through buybacks."
        },
        {
          "ticker": "RBLX",
          "sentiment": "neutral",
          "sentiment_reasoning": "Roblox shows impressive growth (35.8% YoY revenue increase) and high user engagement (111.8M daily active users), but faces significant challenges including $1.1B net loss, negative 21.8% net margin, high debt-to-equity ratio of 4.6x, and guidance for sharp bookings decline. The company prioritizes long-term platform expansion over profitability, requiring investor patience."
        },
        {
          "ticker": "NFLX",
          "sentiment": "neutral",
          "sentiment_reasoning": "Netflix is mentioned as a competitor to Disney in the streaming space, representing competitive pressure on Disney's streaming business model."
        },
        {
          "ticker": "AAPL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Apple is mentioned as a major distribution partner for Roblox and a key stakeholder in app store rules that affect Roblox's operations, representing both opportunity and dependency risk."
        },
        {
          "ticker": "MSFT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Microsoft is mentioned as a major distribution partner for Roblox's platform expansion."
        },
        {
          "ticker": "AMZN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Amazon is mentioned as both a distribution partner for Roblox and a critical infrastructure provider, representing dependency risk for Roblox's operations."
        }
      ]
    },
    {
      "id": "600e64b2c863613bb60b40cae3139cbd154173d9979408ff7b93956b102f1ccd",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "3 Reasons I Bought AMC Stock This Month",
      "author": "Rick Munarriz",
      "published_utc": "2026-09-14T13:03:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/14/3-reasons-i-bought-amc-stock-this-month/?source=iedfolrf0000001",
      "tickers": [
        "AMC",
        "CNK",
        "IMAX",
        "NFLX"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F887370%2Fgettyimages-187999774.jpg&w=1200&op=resize",
      "description": "Despite AMC Entertainment's poor 5-year track record with 99.5% stock decline and shareholder dilution, analyst Rick Munarriz bought shares citing three reasons: strong box office recovery with six $1B+ movies in 2026, AMC's valuation discount versus peers despite higher revenue growth, and the company's efforts to improve the moviegoing experience through premium services like AMC Stubs A-List and high-margin concessions.",
      "keywords": [
        "box office recovery",
        "theatrical exhibition",
        "shareholder dilution",
        "streaming vs theaters",
        "premium memberships",
        "concessions revenue",
        "valuation discount"
      ],
      "insights": [
        {
          "ticker": "AMC",
          "sentiment": "positive",
          "sentiment_reasoning": "Author identifies emerging fundamentals improvement, strong box office momentum, attractive valuation relative to peers, and new revenue initiatives (premium memberships, concessions, collectibles, live concerts) despite acknowledging significant historical challenges and risks."
        },
        {
          "ticker": "CNK",
          "sentiment": "neutral",
          "sentiment_reasoning": "Presented as the conservative, safer alternative to AMC with superior track record (doubled in 5 years, profitable for 4 consecutive years, pays dividend), but lacks the upside potential and growth momentum of AMC."
        },
        {
          "ticker": "IMAX",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as another beneficiary of theatrical revival that has tripled in value, but not the focus of investment thesis; presented as a peer comparison point rather than a primary recommendation."
        },
        {
          "ticker": "NFLX",
          "sentiment": "neutral",
          "sentiment_reasoning": "Referenced as shifting strategy to support theatrical releases (45-day window before streaming) rather than cannibalizing box office, indicating adaptation to cinema's resurgence rather than direct investment recommendation."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 26.80569,
    "13WeekPriceReturnDaily": -1.1689,
    "26WeekPriceReturnDaily": -17.1446,
    "3MonthADReturnStd": 37.89922,
    "3MonthAverageTradingVolume": 38.80107,
    "52WeekHigh": 124.86,
    "52WeekHighDate": "2025-10-21",
    "52WeekLow": 65.08,
    "52WeekLowDate": "2026-07-17",
    "52WeekPriceReturnDaily": -32.4133,
    "5DayPriceReturnDaily": 4.6242,
    "assetTurnoverAnnual": 0.8127,
    "assetTurnoverTTM": 0.8412,
    "beta": 1.5969851,
    "bookValuePerShareAnnual": 6.3038,
    "bookValuePerShareQuarterly": 7.2412,
    "bookValueShareGrowth5Y": 20.33,
    "capexCagr5Y": 6.69,
    "cashFlowPerShareAnnual": 2.2408,
    "cashFlowPerShareQuarterly": 2.6782,
    "cashFlowPerShareTTM": 41.88707,
    "cashPerSharePerShareAnnual": 2.1464,
    "cashPerSharePerShareQuarterly": 2.1921,
    "currentDividendYieldTTM": null,
    "currentEv/freeCashFlowAnnual": 34.851,
    "currentEv/freeCashFlowTTM": 29.5666,
    "currentRatioAnnual": 1.1857,
    "currentRatioQuarterly": 1.1416,
    "dividendIndicatedAnnual": 0,
    "dividendPerShareTTM": null,
    "ebitdPerShareAnnual": 3.1447,
    "ebitdPerShareTTM": 4.072,
    "ebitdaCagr5Y": 23.78,
    "ebitdaInterimCagr5Y": 17.88,
    "enterpriseValue": 329726.734,
    "epsAnnual": 2.528,
    "epsBasicExclExtraItemsAnnual": 2.528,
    "epsBasicExclExtraItemsTTM": 3.1742,
    "epsExclExtraItemsAnnual": 2.528,
    "epsExclExtraItemsTTM": 3.1742,
    "epsGrowth3Y": 36.44,
    "epsGrowth5Y": 32.98,
    "epsGrowthQuarterlyYoy": 11.06,
    "epsGrowthTTMYoy": 35.26,
    "epsInclExtraItemsAnnual": 2.528,
    "epsInclExtraItemsTTM": 3.1742,
    "epsNormalizedAnnual": 2.528,
    "epsTTM": 3.1742,
    "evEbitdaTTM": 18.8126,
    "evRevenueTTM": 6.8167,
    "focfCagr5Y": 37.44,
    "forwardPE": 19.66124,
    "forwardPEG": 0.93319,
    "grossMargin5Y": 43.42,
    "grossMarginAnnual": 48.49,
    "grossMarginTTM": 49.12,
    "longTermDebt/equityAnnual": 0.5059,
    "longTermDebt/equityQuarterly": 0.3922,
    "marketCapitalization": 324516.66,
    "monthToDatePriceReturnDaily": -0.9007,
    "netIncomeEmployeeAnnual": 0.6863,
    "netIncomeEmployeeTTM": 0.8531,
    "netInterestCoverageAnnual": 25.9252,
    "netInterestCoverageTTM": 22.062,
    "netMarginGrowth5Y": 17.07,
    "netProfitMargin5Y": 18.82,
    "netProfitMarginAnnual": 24.3,
    "netProfitMarginTTM": 28.22,
    "operatingMargin5Y": 23.1,
    "operatingMarginAnnual": 29.49,
    "operatingMarginTTM": 35.46,
    "payoutRatioAnnual": null,
    "payoutRatioTTM": null,
    "pb": 10.7627,
    "pbAnnual": 16.0972,
    "pbQuarterly": 9.8602,
    "pcfShareAnnual": 31.9744,
    "pcfShareTTM": 27.1089,
    "peAnnual": 29.552,
    "peBasicExclExtraTTM": 23.7747,
    "peExclExtraAnnual": 52.4917,
    "peExclExtraTTM": 23.7747,
    "peInclExtraTTM": 23.7747,
    "peNormalizedAnnual": 29.552,
    "peTTM": 23.7747,
    "pegTTM": 1.09409,
    "pfcfShareAnnual": 34.3003,
    "pfcfShareTTM": 29.0994,
    "pretaxMargin5Y": 21.69,
    "pretaxMarginAnnual": 28.16,
    "pretaxMarginTTM": 34.1,
    "priceRelativeToS&P50013Week": -4.3027,
    "priceRelativeToS&P50026Week": -29.5047,
    "priceRelativeToS&P5004Week": 7.1823,
    "priceRelativeToS&P50052Week": -48.1523,
    "priceRelativeToS&P500Ytd": -25.9136,
    "psAnnual": 7.1823,
    "psTTM": 6.7089,
    "ptbvAnnual": 84.0879,
    "ptbvQuarterly": 159.7585,
    "quickRatioAnnual": 1.1404,
    "quickRatioQuarterly": 1.0934,
    "receivablesTurnoverAnnual": 26.8405,
    "receivablesTurnoverTTM": 26.994,
    "revenueEmployeeAnnual": 2.8239,
    "revenueEmployeeTTM": 3.0232,
    "revenueGrowth3Y": 12.64,
    "revenueGrowth5Y": 12.57,
    "revenueGrowthQuarterlyYoy": 13.37,
    "revenueGrowthTTMYoy": 16.02,
    "revenuePerShareAnnual": 10.4016,
    "revenuePerShareTTM": 11.3512,
    "revenueShareGrowth5Y": 13.58,
    "roa5Y": 13.56,
    "roaRfy": 19.75,
    "roaTTM": 23.74,
    "roe5Y": 31.33,
    "roeRfy": 41.260000000000005,
    "roeTTM": 47.96,
    "roi5Y": 18.58,
    "roiAnnual": 26.729999999999997,
    "roiTTM": 31.85,
    "tangibleBookValuePerShareAnnual": 0.0296,
    "tangibleBookValuePerShareQuarterly": 0.0213,
    "tbvCagr5Y": -8.34,
    "totalDebt/totalEquityAnnual": 0.5434,
    "totalDebt/totalEquityQuarterly": 0.4746,
    "yearToDatePriceReturnDaily": -14.3345
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

## SMCI
Trading candidate:
```json
{
  "symbol": "SMCI",
  "score": 37.94,
  "direction": "WATCH",
  "sector": "Technology",
  "components": {
    "market": 50.0,
    "sector": 56.09,
    "relative_strength": 0.0,
    "vwap": 100.0,
    "trend": 0.0,
    "volume": 30.501346581468265,
    "momentum": 20.0,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 83.10171388257048,
    "relative_strength_acceleration": 18.075317322303793,
    "trend_acceleration": 25,
    "compression": 0.0,
    "volatility_contraction": 35.00481000481,
    "volume_accumulation": 31.692708668658565,
    "breakout_distance": 0.0,
    "support_quality": 86.25140291806953,
    "momentum_improvement": 10.970584329633752,
    "early_setup_score": 15.83,
    "entry_timing_score": 15.83,
    "opportunity_score": 31.31,
    "extended": false,
    "return_5d": -11.48,
    "return_10d": -4.39,
    "return_20d": -6.87,
    "distance_to_breakout": 12.96,
    "atr_extension": -1.01
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
      "datetime": 1789508702,
      "headline": "Super Micro Computer (SMCI) Dips More Than Broader Market: What You Should Know",
      "id": 142168780,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SMCI",
      "source": "Yahoo",
      "summary": "Super Micro Computer (SMCI) closed the most recent trading day at $35.62, moving 3.06% from the previous trading session.",
      "url": "https://finnhub.io/api/news?id=e3b2dd4f55977319001bbb9f3a22df4829b8fd116dcb5a4af92a8833de7bf0ff"
    },
    {
      "category": "company",
      "datetime": 1789497617,
      "headline": "3 Artificial Intelligence (AI) Stocks That Turned $10,000 Into More Than $100,000 in 5 Years (Hint: They've All Outperformed Nvidia)",
      "id": 142168452,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SMCI",
      "source": "Yahoo",
      "summary": "These stocks are all up more than 900% since September 2021.",
      "url": "https://finnhub.io/api/news?id=75902daeccf027004b14c0037cbf4377b7ea06e16b678d9d07c172cfaa71daae"
    },
    {
      "category": "company",
      "datetime": 1789490104,
      "headline": "The AI Slowdown Call: Another Reason To Hedge, Not To Exit",
      "id": 142167699,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/2215491795/image_2215491795.jpg?io=getty-c-w1536",
      "related": "SMCI",
      "source": "SeekingAlpha",
      "summary": "AI development slowdown calls are shaking stocks, but hedging AI exposure, favoring equipment, and selective optical/networking plays for alpha. Click for more.",
      "url": "https://finnhub.io/api/news?id=1769e710bf16759e8159b120b039f7700b90b14575028e52fc8b1dd564547911"
    },
    {
      "category": "company",
      "datetime": 1789486180,
      "headline": "Dell Jumps 5.8% as Europe's AI Chip Challenger Enters Its Servers",
      "id": 142165834,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SMCI",
      "source": "Yahoo",
      "summary": "Axelera adds inference choice, although its maximum sales opportunity remains small beside Dell's enormous backlog.",
      "url": "https://finnhub.io/api/news?id=81b4cfb4227b83e252d133bbdf2574b9eede0f2fdef15ad03cf676e898b118a5"
    },
    {
      "category": "company",
      "datetime": 1789486029,
      "headline": "Hewlett Packard Enterprise Rises 4% a Day After Evercore ISI Downgrade; Dell Climbs 4%, Super Micro Holds Steady",
      "id": 142165685,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SMCI",
      "source": "Yahoo",
      "summary": "Evercore ISI stepped back from HPE one session ago and the stock is already fighting back, but the real question is whether an Oracle networking deal changes the calculus that spooked analysts in the first place.",
      "url": "https://finnhub.io/api/news?id=f540447a645138ed85bcfb5edd9345af4835af3a86a5d6c92b5eab149094c7e6"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 35.78607,
    "13WeekPriceReturnDaily": 14.9202,
    "26WeekPriceReturnDaily": 15.5709,
    "3MonthADReturnStd": 96.99268,
    "3MonthAverageTradingVolume": 53.25734,
    "52WeekHigh": 58.78,
    "52WeekHighDate": "2025-10-09",
    "52WeekLow": 19.48,
    "52WeekLowDate": "2026-03-23",
    "52WeekPriceReturnDaily": -18.3556,
    "5DayPriceReturnDaily": -8.7432,
    "assetTurnoverAnnual": 1.3045,
    "assetTurnoverTTM": 1.6313,
    "beta": 2.197964,
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
    "enterpriseValue": 27543.125,
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
    "evEbitdaTTM": 9.7527,
    "evRevenueTTM": 0.7051,
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
    "marketCapitalization": 26344.312,
    "monthToDatePriceReturnDaily": -1.4485,
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
    "pb": 1.8194,
    "pbAnnual": 1.3102,
    "pbQuarterly": 1.3102,
    "pcfShareAnnual": null,
    "pcfShareTTM": null,
    "peAnnual": 11.8112,
    "peBasicExclExtraTTM": 11.8112,
    "peExclExtraAnnual": 24.98282,
    "peExclExtraTTM": 11.8112,
    "peInclExtraTTM": 11.8112,
    "peNormalizedAnnual": 11.8112,
    "peTTM": 11.8112,
    "pegTTM": 0.31154,
    "pfcfShareAnnual": 17.1925,
    "pfcfShareTTM": 36.6539,
    "pretaxMargin5Y": 7.57,
    "pretaxMarginAnnual": 7.14,
    "pretaxMarginTTM": 7.14,
    "priceRelativeToS&P50013Week": 11.7864,
    "priceRelativeToS&P50026Week": 3.2108,
    "priceRelativeToS&P5004Week": -2.4971,
    "priceRelativeToS&P50052Week": -34.0946,
    "priceRelativeToS&P500Ytd": 13.9419,
    "psAnnual": 0.6744,
    "psTTM": 0.6744,
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
    "yearToDatePriceReturnDaily": 25.521
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

## CMCSA
Trading candidate:
```json
{
  "symbol": "CMCSA",
  "score": 33.33,
  "direction": "WATCH",
  "sector": "Communication Services",
  "components": {
    "market": 50.0,
    "sector": 92.74,
    "relative_strength": 12.398624087758865,
    "vwap": 0.0,
    "trend": 0.0,
    "volume": 53.32531247018697,
    "momentum": 28.620611121654964,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 30.521240882601475,
    "trend_acceleration": 25,
    "compression": 0.0,
    "volatility_contraction": 69.60847427869142,
    "volume_accumulation": 52.74258547922411,
    "breakout_distance": 0.0,
    "support_quality": 100.0,
    "momentum_improvement": 25.194496969973954,
    "early_setup_score": 24.6,
    "entry_timing_score": 24.6,
    "opportunity_score": 30.71,
    "extended": false,
    "return_5d": -7.34,
    "return_10d": -8.27,
    "return_20d": -4.57,
    "distance_to_breakout": 11.45,
    "atr_extension": -2.92
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
      "datetime": 1789552065,
      "headline": "B of A Securities Maintains Buy on Comcast, Lowers Price Target to $35",
      "id": 142194856,
      "image": "",
      "related": "CMCSA",
      "source": "Benzinga",
      "summary": "B of A Securities  analyst Jessica Reif Cohen   maintains Comcast (NASDAQ:CMCSA) with a Buy and lowers the price target from $37 to $35.",
      "url": "https://finnhub.io/api/news?id=5e6f429d7ae43e5bf47ffed00a62e5ef83426299c2bb38d5eb96fd3c6c9315ae"
    },
    {
      "category": "company",
      "datetime": 1789525555,
      "headline": "Is Comcast Stock Cheap Or Just Shrinking?",
      "id": 142174569,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "CMCSA",
      "source": "Yahoo",
      "summary": "Comcast (CMCSA) generated free cash over the past twelve months worth 20.1% of its market value. The median S&P 500 company manages 4.4%. Part of that gap is Comcast's debt. The rest means one of two things: the market has made a mistake, or the cash is about to get smaller. Comcast keeps losing broadband customers, and that is the market's answer.",
      "url": "https://finnhub.io/api/news?id=22d53a7e20031e50fdae1d2d5a77f33f5ac44bb8aeb568d4926e047c84be0abf"
    },
    {
      "category": "company",
      "datetime": 1789509003,
      "headline": "Comcast (CMCSA) Suffers a Larger Drop Than the General Market: Key Insights",
      "id": 142168671,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "CMCSA",
      "source": "Yahoo",
      "summary": "In the most recent trading session, Comcast (CMCSA) closed at $24.41, indicating a -1.91% shift from the previous trading day.",
      "url": "https://finnhub.io/api/news?id=aff4016ccb8d4df4d5f25836af002b08a0154e181361d8d9ffca6948fe9047c5"
    },
    {
      "category": "company",
      "datetime": 1789502421,
      "headline": "Netflix Options Call A One-Third Drop Ordinary, So How Much Stock Should You Hold?",
      "id": 142168383,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "CMCSA",
      "source": "Yahoo",
      "summary": "Netflix (NFLX) trades at about $80, and its own options put a price on how far that can travel over the twelve months ahead: a floor near $54.21 and a ceiling near $119. The options market is charging nothing unusual for that range. Ordinary, for Netflix, already means a range wide enough to take a third of your money.",
      "url": "https://finnhub.io/api/news?id=d634cb229e11fe66344cd56f723b9e4ceb5da9a6bcf7c72f4e744d802933a87a"
    },
    {
      "category": "company",
      "datetime": 1789491600,
      "headline": "Comcast to Host Third Quarter 2026 Earnings Conference Call",
      "id": 142165968,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "CMCSA",
      "source": "Yahoo",
      "summary": "PHILADELPHIA, September 15, 2026--Comcast Corporation will host a conference call with the financial community to discuss financial results for the third quarter on Thursday, October 22, 2026, at 8:30 a.m. Eastern Time (ET). Comcast will issue a press release reporting its results earlier that morning.",
      "url": "https://finnhub.io/api/news?id=b994134ef17f1c86ff3ec78760c31efb39f9f07257599faceea537b1ec09e467"
    }
  ],
  "polygon_news": [
    {
      "id": "68479bba1fc7d9929e791cfd1ff290152830ea9ebb5461a7b3231d6355235a41",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Should State Street SPDR Russell 1000 Yield Focus ETF (ONEY) Be on Your Investing Radar?",
      "author": "Zacks.Com",
      "published_utc": "2026-09-09T10:20:02Z",
      "article_url": "https://www.zacks.com/stock/news/2986754/should-state-street-spdr-russell-1000-yield-focus-etf-oney-be-on-your-investing-radar?cid=CS-ZC-FT-style_box_etf-2986754",
      "tickers": [
        "ONEY",
        "VTV",
        "SCHD",
        "PGR",
        "CCZ",
        "CMCSA",
        "ALL",
        "ALLpB",
        "ALLpH",
        "ALLpI",
        "ALLpJ"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default314.jpg",
      "description": "The State Street SPDR Russell 1000 Yield Focus ETF (ONEY) offers broad exposure to large-cap value stocks with a low 0.2% expense ratio and 2.77% dividend yield. The ETF has gained 18.54% year-to-date and holds approximately 302 stocks with heaviest allocation to Financials. It carries a Zacks ETF Rank of 3 (Hold), positioning it as a reasonable option for large-cap value investors, though competitors like Vanguard Morningstar Value ETF and Schwab U.S. Dividend Equity ETF offer lower expense ratios.",
      "keywords": [
        "large-cap value ETF",
        "dividend yield",
        "expense ratio",
        "Russell 1000",
        "passive management",
        "financial sector exposure"
      ],
      "insights": [
        {
          "ticker": "ONEY",
          "sentiment": "neutral",
          "sentiment_reasoning": "The ETF is presented as a reasonable option with solid fundamentals (low costs, good performance, diversification), but receives a Hold rating rather than a Buy recommendation. The article acknowledges it as an average-sized fund with competitive advantages but also notes superior alternatives exist."
        },
        {
          "ticker": "VTV",
          "sentiment": "positive",
          "sentiment_reasoning": "Presented as a superior alternative with significantly larger assets ($192.55 billion) and a lower expense ratio (0.03% vs ONEY's 0.2%), making it a more attractive option for cost-conscious investors."
        },
        {
          "ticker": "SCHD",
          "sentiment": "positive",
          "sentiment_reasoning": "Highlighted as a comparable alternative with substantially larger assets ($111.24 billion) and a much lower expense ratio (0.06% vs ONEY's 0.2%), offering better value for similar market exposure."
        },
        {
          "ticker": "PGR",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a top holding (3.48% of ONEY's portfolio) without qualitative assessment; included for informational purposes only."
        },
        {
          "ticker": "CCZ",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as a top holding in ONEY without qualitative assessment; included for informational purposes only."
        },
        {
          "ticker": "CMCSA",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as a top holding in ONEY without qualitative assessment; included for informational purposes only."
        },
        {
          "ticker": "ALL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as a top holding in ONEY without qualitative assessment; included for informational purposes only."
        },
        {
          "ticker": "ALLpB",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as a top holding in ONEY without qualitative assessment; included for informational purposes only."
        },
        {
          "ticker": "ALLpH",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as a top holding in ONEY without qualitative assessment; included for informational purposes only."
        },
        {
          "ticker": "ALLpI",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as a top holding in ONEY without qualitative assessment; included for informational purposes only."
        },
        {
          "ticker": "ALLpJ",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as a top holding in ONEY without qualitative assessment; included for informational purposes only."
        }
      ]
    },
    {
      "id": "c79cca05346cc1c1cabb9f0f17ab1358c88c39cc5d72fc8c5cd64380ca310cba",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Did Apple Go Too Far This Time?",
      "author": "Rick Munarriz",
      "published_utc": "2026-08-31T12:08:00Z",
      "article_url": "https://www.fool.com/investing/2026/08/31/did-apple-go-too-far-this-time/?source=iedfolrf0000001",
      "tickers": [
        "AAPL",
        "NFLX",
        "DIS",
        "AMZN",
        "CCZ",
        "CMCSA"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F885752%2Fgettyimages-1290369115.jpg&w=1200&op=resize",
      "description": "Apple has raised Apple TV+ prices to $14.99/month, tripling the cost since launch in 2019. The article argues this aggressive pricing strategy\u2014a 79% increase across major streaming services in five years\u2014is unsustainable and risks losing subscribers during economic downturns, especially compared to larger competitors whose prices have risen more moderately.",
      "keywords": [
        "streaming services",
        "price increases",
        "Apple TV+",
        "cord-cutting",
        "subscriber retention",
        "streaming competition"
      ],
      "insights": [
        {
          "ticker": "AAPL",
          "sentiment": "negative",
          "sentiment_reasoning": "Apple TV+ has tripled its price in four years, far exceeding inflation and stock performance. The aggressive pricing strategy is criticized as potentially damaging to growth and subscriber retention, particularly among smaller services that will be cut from budgets during economic downturns."
        },
        {
          "ticker": "NFLX",
          "sentiment": "neutral",
          "sentiment_reasoning": "Netflix has raised prices 23-58% over five years, which is significant but more moderate than Apple TV+. As the market leader with strong content, it has more pricing power and is mentioned as a comparison point for sustainable pricing strategies."
        },
        {
          "ticker": "DIS",
          "sentiment": "neutral",
          "sentiment_reasoning": "Disney+ launched with aggressive pricing ($6.99/month) and has raised prices moderately (within the 23-58% range). The company's vast content library provides justification for pricing, making it a more defensible position than Apple TV+."
        },
        {
          "ticker": "AMZN",
          "sentiment": "positive",
          "sentiment_reasoning": "Prime Video has seen only a 15% price increase over five years, the most modest among major services. This restrained approach is presented as a sustainable strategy that maintains value proposition and customer loyalty."
        },
        {
          "ticker": "CCZ",
          "sentiment": "neutral",
          "sentiment_reasoning": "Peacock Premium Plus is mentioned as a smaller service with initial pricing at $9.99, but lacks detailed analysis of its pricing trajectory or performance."
        },
        {
          "ticker": "CMCSA",
          "sentiment": "neutral",
          "sentiment_reasoning": "Peacock Premium Plus is mentioned as a smaller service with initial pricing at $9.99, but lacks detailed analysis of its pricing trajectory or performance."
        }
      ]
    },
    {
      "id": "6a6643356fb6279db461c83e4ce2d47311da4b5eb234ed89df8180986c683cbd",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Constellation's New Power Deals Are Piling Up. Here's Why the Stock Isn't Reflecting It Yet.",
      "author": "James Halley",
      "published_utc": "2026-08-26T20:05:00Z",
      "article_url": "https://www.fool.com/investing/2026/08/26/constellations-new-power-deals-are-piling-up-heres/?source=iedfolrf0000001",
      "tickers": [
        "CEG",
        "MSFT",
        "CCZ",
        "CMCSA",
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
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F884229%2Fnuclear-power.jpg&w=1200&op=resize",
      "description": "Constellation Energy has secured 920 megawatts of new power purchase agreements with major clients like Microsoft, Comcast, and Bank of America to support AI data center growth. However, the stock has declined 51% from its 52-week high due to delayed cash flows (2027-2032), significant debt from the $26.6 billion Calpine acquisition, and regulatory approval timelines. Despite near-term headwinds, the company's stable utility revenue and long-term AI power demand position it for future growth.",
      "keywords": [
        "AI data centers",
        "nuclear energy",
        "power purchase agreements",
        "debt concerns",
        "regulatory delays",
        "Three Mile Island restart",
        "utility stocks"
      ],
      "insights": [
        {
          "ticker": "CEG",
          "sentiment": "neutral",
          "sentiment_reasoning": "Strong deal pipeline and revenue growth (+18.6% YoY) are offset by significant debt concerns (64% YoY increase), delayed cash flows from PPAs (2027-2032), and regulatory hurdles. Stock down 51% from highs despite positive fundamentals, suggesting market has priced in future growth but remains cautious on near-term execution and debt management."
        },
        {
          "ticker": "MSFT",
          "sentiment": "positive",
          "sentiment_reasoning": "Secured a 20-year PPA with Constellation to restart Three Mile Island (Crane Energy Center), demonstrating commitment to securing reliable clean energy for AI infrastructure expansion."
        },
        {
          "ticker": "CCZ",
          "sentiment": "positive",
          "sentiment_reasoning": "Entered into a 20-year power purchase agreement with Constellation in June 2025, securing long-term clean energy supply for data center operations."
        },
        {
          "ticker": "CMCSA",
          "sentiment": "positive",
          "sentiment_reasoning": "Entered into a 20-year power purchase agreement with Constellation in June 2025, securing long-term clean energy supply for data center operations."
        },
        {
          "ticker": "BAC",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "BACpB",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "BACpE",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "BACpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "BACpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "BACpM",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "BACpN",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "BACpO",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "BACpP",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "BACpQ",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "BACpS",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "BMLpG",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "BMLpH",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "BMLpJ",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "BMLpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        },
        {
          "ticker": "MERpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Signed a 15-year PPA with Constellation in 2022, securing stable long-term energy supply for data center and operational needs."
        }
      ]
    },
    {
      "id": "ec5b6e3661cf09e4a2ce0f206c24b2647c89f70dbfb1185ced9b5600ea7d6536",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "3 Magnificent High-Yield Dividend Stocks to Buy That Are Near 52-Week Lows",
      "author": "Thomas Niel",
      "published_utc": "2026-08-16T12:20:00Z",
      "article_url": "https://www.fool.com/investing/2026/08/16/3-magnificent-high-yield-dividend-stocks-to-buy-th/?source=iedfolrf0000001",
      "tickers": [
        "CCZ",
        "CMCSA",
        "GIS",
        "VICI"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F882434%2Fcopy-of-dividends-blackboard-sketch-doodle-1201x849-0ca0aea.jpg&w=1200&op=resize",
      "description": "The article highlights three high-yield dividend stocks trading near 52-week lows that the author believes represent buying opportunities: Comcast (5% yield, benefiting from upcoming media spinoff), General Mills (6.3% yield, undergoing cost-cutting restructuring), and Vici Properties (6.8% yield, a Las Vegas casino REIT with strong tenant relationships despite tourism concerns).",
      "keywords": [
        "high-yield dividends",
        "52-week lows",
        "dividend growth",
        "value opportunity",
        "REIT",
        "spinoff",
        "restructuring"
      ],
      "insights": [
        {
          "ticker": "CCZ",
          "sentiment": "positive",
          "sentiment_reasoning": "Trading near 52-week lows with a 5% dividend yield and 18-year dividend-hiking streak. Upcoming spinoff expected to unlock ~30% shareholder value according to Deutsche Bank analysts, positioning it as a pure-play telecom company."
        },
        {
          "ticker": "CMCSA",
          "sentiment": "positive",
          "sentiment_reasoning": "Trading near 52-week lows with a 5% dividend yield and 18-year dividend-hiking streak. Upcoming spinoff expected to unlock ~30% shareholder value according to Deutsche Bank analysts, positioning it as a pure-play telecom company."
        },
        {
          "ticker": "GIS",
          "sentiment": "positive",
          "sentiment_reasoning": "Despite headwinds from private label competition and GLP-1 drugs, the company offers a 6.3% forward yield and is executing a $3 billion cost-reduction program targeting $750 million in savings by 2027, which could drive earnings growth and dividend expansion."
        },
        {
          "ticker": "VICI",
          "sentiment": "positive",
          "sentiment_reasoning": "REIT hit 52-week lows due to Las Vegas tourism concerns, but fundamentals remain strong with 5.7% revenue growth and 7.8% AFFO growth last quarter. Zero tenant defaults even during pandemic, 6.8% forward yield, and mid-single-digit annual dividend growth history."
        }
      ]
    },
    {
      "id": "9800d6806eacfb16401b1377a8c0b6d3f4b3c9916159b0f34028560c54f1314a",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Amazon.com vs. Comcast: Which Stock Is a Better Buy in 2026?",
      "author": "Sara Appino",
      "published_utc": "2026-08-14T19:12:58Z",
      "article_url": "https://www.fool.com/coverage/better-buy/2026/08/14/amazon-com-vs-comcast-which-stock-is-a-better-buy-in-2026/?source=iedfolrf0000001",
      "tickers": [
        "AMZN",
        "CCZ",
        "CMCSA",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "WMT"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F3caa0e2607e9485862b0d89e5f6f6be899ae6c41-1200x800.png%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "The article compares Amazon and Comcast as investment options for 2026. Amazon demonstrates stronger growth with accelerating AWS, advertising, and retail divisions, while Comcast generates substantial free cash flow but faces structural headwinds from declining broadband subscribers and increased competition. The author recommends Amazon for long-term investors seeking growth, though Comcast appeals to those prioritizing steady cash flows and dividends.",
      "keywords": [
        "stock comparison",
        "cloud computing",
        "e-commerce",
        "broadband",
        "valuation",
        "growth vs value",
        "free cash flow",
        "AI infrastructure"
      ],
      "insights": [
        {
          "ticker": "AMZN",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong revenue growth (12.4% YoY), accelerating AWS for fifth consecutive quarter, surging advertising business, operating income growing at double the rate of revenue, aggressive AI infrastructure investments, and dominant market position across multiple high-margin divisions."
        },
        {
          "ticker": "CCZ",
          "sentiment": "neutral",
          "sentiment_reasoning": "Generates substantial free cash flow ($21.9B) and maintains reliable dividend (4.96% yield), with Peacock turning profitable and recent earnings beat. However, faces structural headwinds including declining broadband subscribers, increased competition from fiber and fixed wireless providers, and complexity from planned NBCUniversal spinoff."
        },
        {
          "ticker": "CMCSA",
          "sentiment": "neutral",
          "sentiment_reasoning": "Generates substantial free cash flow ($21.9B) and maintains reliable dividend (4.96% yield), with Peacock turning profitable and recent earnings beat. However, faces structural headwinds including declining broadband subscribers, increased competition from fiber and fixed wireless providers, and complexity from planned NBCUniversal spinoff."
        },
        {
          "ticker": "GOOG",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a well-funded competitor to Amazon in the competitive landscape, but no specific analysis provided in the article."
        },
        {
          "ticker": "GOOGL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a well-funded competitor to Amazon in the competitive landscape, but no specific analysis provided in the article."
        },
        {
          "ticker": "GOOGM",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a well-funded competitor to Amazon in the competitive landscape, but no specific analysis provided in the article."
        },
        {
          "ticker": "GOOGN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a well-funded competitor to Amazon in the competitive landscape, but no specific analysis provided in the article."
        },
        {
          "ticker": "WMT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a well-funded competitor to Amazon in e-commerce, but no specific analysis provided in the article."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 25.64531,
    "13WeekPriceReturnDaily": -0.3265,
    "26WeekPriceReturnDaily": -20.1178,
    "3MonthADReturnStd": 36.209457,
    "3MonthAverageTradingVolume": 32.16986,
    "52WeekHigh": 32.86,
    "52WeekHighDate": "2026-02-12",
    "52WeekLow": 21.28,
    "52WeekLowDate": "2026-07-24",
    "52WeekPriceReturnDaily": -20.1178,
    "5DayPriceReturnDaily": -0.6913,
    "assetTurnoverAnnual": 0.4538,
    "assetTurnoverTTM": 0.4699,
    "beta": 0.72855896,
    "bookValuePerShareAnnual": 26.8858,
    "bookValuePerShareQuarterly": 25.311,
    "bookValueShareGrowth5Y": 6.4,
    "capexCagr5Y": 4.37,
    "cashFlowPerShareAnnual": 5.3368,
    "cashFlowPerShareQuarterly": 5.0242,
    "cashFlowPerShareTTM": 6.91354,
    "cashPerSharePerShareAnnual": 2.6305,
    "cashPerSharePerShareQuarterly": 2.1602,
    "currentDividendYieldTTM": 5.5911,
    "currentEv/freeCashFlowAnnual": 8.8232,
    "currentEv/freeCashFlowTTM": 9.5249,
    "currentRatioAnnual": 0.882,
    "currentRatioQuarterly": 0.7958,
    "dividendGrowthRate5Y": 7.87,
    "dividendIndicatedAnnual": 1.32,
    "dividendPerShareAnnual": 1.3241,
    "dividendPerShareTTM": 1.3428,
    "dividendYieldIndicatedAnnual": 2.72428,
    "ebitdPerShareAnnual": 9.9442,
    "ebitdPerShareTTM": 9.3924,
    "ebitdaCagr5Y": 3.81,
    "ebitdaInterimCagr5Y": -0.09,
    "enterpriseValue": 169714.82,
    "epsAnnual": 5.3917,
    "epsBasicExclExtraItemsAnnual": 5.3917,
    "epsBasicExclExtraItemsTTM": 3.0877999999999997,
    "epsExclExtraItemsAnnual": 5.3917,
    "epsExclExtraItemsTTM": 3.0877999999999997,
    "epsGrowth3Y": 64.46,
    "epsGrowth5Y": 18.8,
    "epsGrowthQuarterlyYoy": -66.91,
    "epsGrowthTTMYoy": -49,
    "epsInclExtraItemsAnnual": 5.3917,
    "epsInclExtraItemsTTM": 3.0877999999999997,
    "epsNormalizedAnnual": 5.3917,
    "epsTTM": 3.0877999999999997,
    "evEbitdaTTM": 4.9802,
    "evRevenueTTM": 1.3588,
    "focfCagr5Y": 7.98,
    "forwardPE": 6.64456,
    "grossMargin5Y": 69.42,
    "grossMarginAnnual": 71.75,
    "grossMarginTTM": 69.39,
    "inventoryTurnoverAnnual": 5.472,
    "inventoryTurnoverTTM": 11.613,
    "longTermDebt/equityAnnual": 0.9595,
    "longTermDebt/equityQuarterly": 0.9387,
    "marketCapitalization": 86994.82,
    "monthToDatePriceReturnDaily": -8.2645,
    "netIncomeEmployeeAnnual": 0.1117,
    "netIncomeEmployeeTTM": 0.0626,
    "netInterestCoverageAnnual": 3.7799,
    "netInterestCoverageTTM": 6.1327,
    "netMarginGrowth5Y": 9.72,
    "netProfitMargin5Y": 11.7,
    "netProfitMarginAnnual": 16.17,
    "netProfitMarginTTM": 8.97,
    "operatingMargin5Y": 16.83,
    "operatingMarginAnnual": 16.71,
    "operatingMarginTTM": 14.66,
    "payoutRatioAnnual": 24.47,
    "payoutRatioTTM": 43.43,
    "pb": 0.9692,
    "pbAnnual": 1.124,
    "pbQuarterly": 0.977,
    "pcfShareAnnual": 2.5858,
    "pcfShareTTM": 2.6753,
    "peAnnual": 4.3502,
    "peBasicExclExtraTTM": 7.7681,
    "peExclExtraAnnual": 35.12651,
    "peExclExtraTTM": 7.7681,
    "peInclExtraTTM": 7.7681,
    "peNormalizedAnnual": 4.3502,
    "peTTM": 7.7681,
    "pegTTM": -1.46279,
    "pfcfShareAnnual": 4.5227,
    "pfcfShareTTM": 4.8824,
    "pretaxMargin5Y": 15.36,
    "pretaxMarginAnnual": 20.83,
    "pretaxMarginTTM": 11.19,
    "priceRelativeToS&P50013Week": -2.435,
    "priceRelativeToS&P50026Week": -32.1031,
    "priceRelativeToS&P5004Week": -5.4831,
    "priceRelativeToS&P50052Week": -34.7159,
    "priceRelativeToS&P500Ytd": -23.8842,
    "psAnnual": 0.7032,
    "psTTM": 0.6965,
    "ptbvAnnual": 38.2296,
    "ptbvQuarterly": 359.4189,
    "quickRatioAnnual": 0.882,
    "quickRatioQuarterly": 0.7958,
    "receivablesTurnoverAnnual": 8.9871,
    "receivablesTurnoverTTM": 9.2539,
    "revenueEmployeeAnnual": 0.6911,
    "revenueEmployeeTTM": 0.6978,
    "revenueGrowth3Y": 0.62,
    "revenueGrowth5Y": 3.62,
    "revenueGrowthQuarterlyYoy": -1.23,
    "revenueGrowthTTMYoy": 0.58,
    "revenuePerShareAnnual": 33.3532,
    "revenuePerShareTTM": 34.9874,
    "revenueShareGrowth5Y": 8.29,
    "roa5Y": 5.29,
    "roaRfy": 7.340000000000001,
    "roaTTM": 4.21,
    "roe5Y": 15.91,
    "roeRfy": 20.64,
    "roeTTM": 12.04,
    "roi5Y": 7.55,
    "roiAnnual": 10.209999999999999,
    "roiTTM": 5.93,
    "tangibleBookValuePerShareAnnual": 0.7905,
    "tangibleBookValuePerShareQuarterly": 0.0688,
    "totalDebt/totalEquityAnnual": 1.021,
    "totalDebt/totalEquityQuarterly": 1.0069,
    "yearToDatePriceReturnDaily": -12.8169
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

## NKE
Trading candidate:
```json
{
  "symbol": "NKE",
  "score": 30.96,
  "direction": "WATCH",
  "sector": "Consumer Discretionary",
  "components": {
    "market": 50.0,
    "sector": 56.82,
    "relative_strength": 17.646124629036485,
    "vwap": 0.0,
    "trend": 0.0,
    "volume": 55.257583695729764,
    "momentum": 27.21257052880202,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 41.27406241503482,
    "trend_acceleration": 25,
    "compression": 16.51021535063491,
    "volatility_contraction": 74.3354105861008,
    "volume_accumulation": 36.689224243775385,
    "breakout_distance": 0.0,
    "support_quality": 100.0,
    "momentum_improvement": 37.48343586418349,
    "early_setup_score": 29.53,
    "entry_timing_score": 29.53,
    "opportunity_score": 30.53,
    "extended": false,
    "return_5d": -4.95,
    "return_10d": -7.28,
    "return_20d": -7.27,
    "distance_to_breakout": 13.32,
    "atr_extension": -3.18
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
      "datetime": 1789529092,
      "headline": "Why Did OPEN, NKE, CCL Stocks Crash To 52-Week Lows Today?",
      "id": 142174606,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NKE",
      "source": "Yahoo",
      "summary": "Housing weakness, a prolonged athleticwear turnaround, and rising cruise fuel costs weighed on investor sentiment.",
      "url": "https://finnhub.io/api/news?id=aa88ef2a86ed34652268134123020d2cd8b6e3ab8cf49c91718ca057440ae9f5"
    },
    {
      "category": "company",
      "datetime": 1789509004,
      "headline": "Nike (NKE) Sees a More Significant Dip Than Broader Market: Some Facts to Know",
      "id": 142168737,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NKE",
      "source": "Yahoo",
      "summary": "Nike (NKE) closed the most recent trading day at $36.22, moving 2.25% from the previous trading session.",
      "url": "https://finnhub.io/api/news?id=38f713a88ac9f55e8084efab80d78ae7acd2a8dd497d73fb6973b58778ab9c44"
    },
    {
      "category": "company",
      "datetime": 1789504690,
      "headline": "Stock Market Today: Dow Dives With Fed Seen Doing This; Senate Vote Hits These Crypto Stocks",
      "id": 142168403,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NKE",
      "source": "Yahoo",
      "summary": "The Dow Jones index drops on the stock market today as yields and oil spike. Bitcoin and crypto stocks fall after a key vote.",
      "url": "https://finnhub.io/api/news?id=a95b23d9616d1f85988b1597674f2c01d32653ec2a16a42c86f1b8ec2f49cec7"
    },
    {
      "category": "company",
      "datetime": 1789499406,
      "headline": "Discover which dow jones stocks are making waves on Tuesday.",
      "id": 142167114,
      "image": "https://www.chartmill.com/images/uploads/CM_Top_Movers_Small_free_2b4ff2fc22.webp",
      "related": "NKE",
      "source": "ChartMill",
      "summary": "Stay updated with the movement of dow jones stocks in today's session. Discover which dow jones stocks are making waves on Tuesday.",
      "url": "https://finnhub.io/api/news?id=a2fd6ceef859ea3281feda9ce6737beeb691937977ad1252cfc372c6ed60226b"
    },
    {
      "category": "company",
      "datetime": 1789493811,
      "headline": "Nike's Stock Is Down 80% - I'm Buying",
      "id": 142168183,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/2194507170/image_2194507170.jpg?io=getty-c-w1536",
      "related": "NKE",
      "source": "SeekingAlpha",
      "summary": "Nike appears to be nearing a bottom after years of declining net income and a significant stock sell-off. Click here to read my latest analysis of NKE stock.",
      "url": "https://finnhub.io/api/news?id=e15f9a7089883776ec07958588a19cdfbd97946bdd42e4b68853f75297207b27"
    }
  ],
  "polygon_news": [
    {
      "id": "d27f4a716e34411025782e3d02a19ce372e5d87889f2e71ca269e28c00cfe1a9",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Global Wholesale Weakness Lingers: Can NIKE Reignite Sales?",
      "author": "Na",
      "published_utc": "2026-09-15T15:09:00Z",
      "article_url": "https://www.zacks.com/stock/news/2989996/global-wholesale-weakness-lingers-can-nike-reignite-sales?cid=CS-ZC-FT-analyst_blog|quick_take-2989996",
      "tickers": [
        "NKE",
        "LULU",
        "ADDYY"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/33/96.jpg",
      "description": "NIKE's Q4 wholesale revenues grew 1% overall, with strong North America performance (+10%) offset by significant international weakness, particularly in Greater China (-19%). The company is implementing product innovation, franchise refreshes, and reduced promotions to rebuild demand, though the turnaround is expected to take time amid cautious consumer spending and intense competition.",
      "keywords": [
        "wholesale revenue",
        "North America growth",
        "Greater China decline",
        "inventory management",
        "product innovation",
        "promotional strategy",
        "consumer demand"
      ],
      "insights": [
        {
          "ticker": "NKE",
          "sentiment": "negative",
          "sentiment_reasoning": "While North America wholesale showed strength (+10%), significant weakness in Greater China (-19%) and EMEA (-1%) indicates broader challenges. The company faces elevated inventory, promotional pressure, cautious consumer demand, and intense competition. Stock has declined 31% in six months. Though management is implementing turnaround strategies, execution risks remain high and recovery is expected to take considerable time."
        },
        {
          "ticker": "LULU",
          "sentiment": "positive",
          "sentiment_reasoning": "Mentioned as a peer company with strong fundamentals including intensified focus on product innovation, strong international demand particularly in China, and continued investment in digital ecosystem capabilities to enhance customer engagement and drive long-term growth."
        },
        {
          "ticker": "ADDYY",
          "sentiment": "positive",
          "sentiment_reasoning": "Presented as a peer company pursuing broad-based growth strategy with focus on product innovation, athlete-led development, and strengthening key performance categories like Running and Football, while maintaining lifestyle portfolio appeal across markets."
        }
      ]
    },
    {
      "id": "52f8a53d1fb544bcc12940a789d43cbd7a062e26bcf5fcad37ddbf7419557623",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Nike's Chief Legal Officer Sells 3,646 Shares as the Stock Falls to a 52-Week Low",
      "author": "Robert Izquierdo",
      "published_utc": "2026-09-15T04:16:42Z",
      "article_url": "https://www.fool.com/coverage/filings/2026/09/15/nike-s-chief-legal-officer-sells-3-646-shares-as-the-stock-falls-to-a-52-week-low/?source=iedfolrf0000001",
      "tickers": [
        "NKE"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F7c4db55a3ec93213c3928bb0037d6c8d15157943-1401x1251.png%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "Nike's Chief Legal Officer Robert Leinwand sold 3,646 shares worth approximately $137,053 on September 9, 2026, as part of a pre-established Rule 10b5-1 trading plan. The sale occurred amid Nike's significant struggles, including a 49% stock decline over the past year, driven by an 11% sales drop in China, flat full-year results, and removal from the S&P 100. Despite the sale, Leinwand maintains a substantial equity position of 89,265 shares, demonstrating continued alignment with shareholder interests.",
      "keywords": [
        "insider trading",
        "stock decline",
        "Rule 10b5-1 plan",
        "China sales",
        "S&P 100 removal",
        "athletic footwear",
        "52-week low"
      ],
      "insights": [
        {
          "ticker": "NKE",
          "sentiment": "negative",
          "sentiment_reasoning": "Nike faces significant headwinds including a 49% one-year stock price decline, 11% sales drop in China, flat full-year results, removal from the S&P 100, and broader industry downturn in the sneaker sector. The stock has fallen to a 52-week low, reflecting deteriorating business fundamentals and market challenges."
        }
      ]
    },
    {
      "id": "1080f19e89955fa629662687100f4d046ba631d65f15ff8f26538ae4bfa99254",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "3 Unstoppable Dow Stocks Worth Buying Right Now",
      "author": "Jennifer Saibil",
      "published_utc": "2026-09-13T08:02:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/13/3-unstoppable-dow-stocks-worth-buying-right-now/?source=iedfolrf0000001",
      "tickers": [
        "NVDA",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "AXP",
        "AAPL",
        "MSFT",
        "AMZN",
        "NKE",
        "PG"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F886812%2Fperson-biking-on-google-campus-with-google-logo-reflection-in-background_alphabet_google.jpg&w=1200&op=resize",
      "description": "The article recommends three Dow Jones stocks as strong buys: Nvidia, which expects 70% revenue growth next year and trades at an attractive 14x forward earnings; Alphabet, with 24% revenue growth and 82% Google Cloud growth, trading at 22x forward earnings; and American Express, showing 10% revenue growth and 14% EPS growth with a 15x forward earnings valuation. All three are positioned to benefit from AI investments and strong market demand despite recent market pullbacks.",
      "keywords": [
        "Dow Jones stocks",
        "artificial intelligence",
        "revenue growth",
        "valuation",
        "investment recommendation"
      ],
      "insights": [
        {
          "ticker": "NVDA",
          "sentiment": "positive",
          "sentiment_reasoning": "Largest company in the world, leading AI chip designer with 70% expected revenue growth, supply-constrained demand, new efficient platforms, and attractive 14x forward earnings valuation despite strong performance."
        },
        {
          "ticker": "GOOG",
          "sentiment": "positive",
          "sentiment_reasoning": "24% year-over-year revenue growth, 82% Google Cloud growth, 9 million developers using tools, strong AI platform momentum with 40% increase in daily active users, and attractive 22x forward earnings valuation despite recent market disappointment."
        },
        {
          "ticker": "GOOGL",
          "sentiment": "positive",
          "sentiment_reasoning": "24% year-over-year revenue growth, 82% Google Cloud growth, 9 million developers using tools, strong AI platform momentum with 40% increase in daily active users, and attractive 22x forward earnings valuation despite recent market disappointment."
        },
        {
          "ticker": "GOOGM",
          "sentiment": "positive",
          "sentiment_reasoning": "24% year-over-year revenue growth, 82% Google Cloud growth, 9 million developers using tools, strong AI platform momentum with 40% increase in daily active users, and attractive 22x forward earnings valuation despite recent market disappointment."
        },
        {
          "ticker": "GOOGN",
          "sentiment": "positive",
          "sentiment_reasoning": "24% year-over-year revenue growth, 82% Google Cloud growth, 9 million developers using tools, strong AI platform momentum with 40% increase in daily active users, and attractive 22x forward earnings valuation despite recent market disappointment."
        },
        {
          "ticker": "AXP",
          "sentiment": "positive",
          "sentiment_reasoning": "10% revenue growth, 14% EPS growth, highest cardmember spending in three years, raised full-year guidance, unique closed-loop business model with strong profitability, and attractive 15x forward earnings valuation."
        },
        {
          "ticker": "AAPL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as existing Dow component but not featured in main recommendation; no specific performance metrics or analysis provided in the article."
        },
        {
          "ticker": "MSFT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as existing Dow component but not featured in main recommendation; no specific performance metrics or analysis provided in the article."
        },
        {
          "ticker": "AMZN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as existing Dow component but not featured in main recommendation; no specific performance metrics or analysis provided in the article."
        },
        {
          "ticker": "NKE",
          "sentiment": "negative",
          "sentiment_reasoning": "Explicitly mentioned as struggling lately, contrasting with the recommended stocks' strong performance."
        },
        {
          "ticker": "PG",
          "sentiment": "negative",
          "sentiment_reasoning": "Noted as reporting only single-digit sales increases, indicating weak growth compared to recommended stocks."
        }
      ]
    },
    {
      "id": "bb0ae59cc0aff9eccd5946ee9f821aa53cdb48e9afc3c91152184fa15da6dfc4",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Nike Is Being Deleted From the S&P 100. Is Its Seat in the Dow Jones Industrial Average in Jeopardy?",
      "author": "Daniel Foelber",
      "published_utc": "2026-09-12T09:15:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/12/nike-just-got-deleted-from-the-sp-100-is-its-seat/?source=iedfolrf0000001",
      "tickers": [
        "NKE",
        "DELL",
        "PANW",
        "ANET",
        "SNDK",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "SPG",
        "SPGpJ",
        "CL"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F886728%2Fnke.png&w=1200&op=resize",
      "description": "Nike has been removed from the S&P 100 effective September 21 as part of quarterly rebalancing, marking a significant decline for the company. With stock prices at 12-year lows, declining revenue and earnings, and operating margins plummeting, Nike is now the lowest-ranked component in the Dow Jones Industrial Average, putting its membership in jeopardy. The article suggests investors should wait for concrete signs of a sustained turnaround before buying the stock.",
      "keywords": [
        "S&P 100 removal",
        "Dow Jones Industrial Average",
        "index rebalancing",
        "turnaround plan",
        "dividend stock",
        "market underperformance"
      ],
      "insights": [
        {
          "ticker": "NKE",
          "sentiment": "negative",
          "sentiment_reasoning": "Stock at 12-year lows, declining revenue and earnings, operating margins collapsed from mid-teens to under 9%, removed from S&P 100, facing competition and China slowdown, at risk of Dow removal, turnaround uncertain"
        },
        {
          "ticker": "DELL",
          "sentiment": "positive",
          "sentiment_reasoning": "Being added to S&P 100, ranked in top 50 S&P 500 components by market cap, contributing to index gains"
        },
        {
          "ticker": "PANW",
          "sentiment": "positive",
          "sentiment_reasoning": "Being added to S&P 100, ranked in top 50 S&P 500 components by market cap"
        },
        {
          "ticker": "ANET",
          "sentiment": "positive",
          "sentiment_reasoning": "Being added to S&P 100, ranked in top 50 S&P 500 components by market cap, significant stock appreciation"
        },
        {
          "ticker": "SNDK",
          "sentiment": "positive",
          "sentiment_reasoning": "Being added to S&P 100, ranked in top 50 S&P 500 components by market cap"
        },
        {
          "ticker": "GOOG",
          "sentiment": "positive",
          "sentiment_reasoning": "Recently added to Dow Jones Industrial Average, replacing Verizon, reflects tech-focused shift in index composition"
        },
        {
          "ticker": "GOOGL",
          "sentiment": "positive",
          "sentiment_reasoning": "Recently added to Dow Jones Industrial Average, replacing Verizon, reflects tech-focused shift in index composition"
        },
        {
          "ticker": "GOOGM",
          "sentiment": "positive",
          "sentiment_reasoning": "Recently added to Dow Jones Industrial Average, replacing Verizon, reflects tech-focused shift in index composition"
        },
        {
          "ticker": "GOOGN",
          "sentiment": "positive",
          "sentiment_reasoning": "Recently added to Dow Jones Industrial Average, replacing Verizon, reflects tech-focused shift in index composition"
        },
        {
          "ticker": "SPG",
          "sentiment": "neutral",
          "sentiment_reasoning": "Being removed from S&P 100 as part of routine rebalancing, no specific performance issues mentioned"
        },
        {
          "ticker": "SPGpJ",
          "sentiment": "neutral",
          "sentiment_reasoning": "Being removed from S&P 100 as part of routine rebalancing, no specific performance issues mentioned"
        },
        {
          "ticker": "CL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Being removed from S&P 100 as part of routine rebalancing, no specific performance issues mentioned"
        }
      ]
    },
    {
      "id": "21c5927e3bd6aa60429426bca74511945d5f6bef1d77dfd6e00bab7c205ec1c0",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "NIKE Near 52-Week Low: Should Investors Buy or Stay Cautious?",
      "author": "Na",
      "published_utc": "2026-09-08T15:05:00Z",
      "article_url": "https://www.zacks.com/stock/news/2986501/nike-near-52-week-low-should-investors-buy-or-stay-cautious?cid=CS-ZC-FT-analyst_blog|most_popular_stocks-2986501",
      "tickers": [
        "NKE",
        "ADDYY",
        "WWW",
        "SHOO"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/42/95.jpg",
      "description": "NIKE shares fell to a 52-week low of $37.95 as softer consumer demand, persistent Sportswear weakness, and regional pressures in Greater China and EMEA weigh on the business. The company expects Q1 FY27 revenues to decline in the low-to-mid single digits. However, NIKE Running continues strong momentum with five consecutive quarters of double-digit growth, and new product launches are planned for the second half of FY27.",
      "keywords": [
        "NIKE",
        "52-week low",
        "Sportswear weakness",
        "consumer demand",
        "Greater China",
        "EMEA",
        "NIKE Running",
        "business reset",
        "revenue decline",
        "product innovation"
      ],
      "insights": [
        {
          "ticker": "NKE",
          "sentiment": "negative",
          "sentiment_reasoning": "Stock hit 52-week low of $37.95, down 50.1% from 52-week high. Q4 FY26 revenues declined 1% YoY, with NIKE Direct down 9%. Greater China revenues fell 17% and EMEA down 6%. Company expects Q1 FY27 revenues to decline in low-to-mid single digits. Sportswear category declined double digits. However, some positive factors include NIKE Running's five consecutive quarters of double-digit growth and planned new product launches, which provide some offset to near-term challenges."
        },
        {
          "ticker": "ADDYY",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a peer comparison, down 10.7% in the past three months, outperforming NIKE's 14% decline. Trading at a lower P/E multiple (13.54X) than NIKE, suggesting better relative valuation, but no specific company performance details provided."
        },
        {
          "ticker": "WWW",
          "sentiment": "positive",
          "sentiment_reasoning": "Stock jumped 21.7% in the past three months, significantly outperforming NIKE and the broader market. Trading at a lower P/E multiple (11X) than NIKE, indicating stronger relative performance among peers."
        },
        {
          "ticker": "SHOO",
          "sentiment": "negative",
          "sentiment_reasoning": "Down 21.7% in the past three months, underperforming both NIKE and the broader Consumer Discretionary sector, indicating weakness in the footwear/apparel industry."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 27.03131,
    "13WeekPriceReturnDaily": -19.3864,
    "26WeekPriceReturnDaily": -33.9337,
    "3MonthADReturnStd": 33.07771,
    "3MonthAverageTradingVolume": 24.54672,
    "52WeekHigh": 76.97,
    "52WeekHighDate": "2025-10-02",
    "52WeekLow": 36.55,
    "52WeekLowDate": "2026-09-10",
    "52WeekPriceReturnDaily": -49.2466,
    "5DayPriceReturnDaily": -2.7559,
    "assetTurnoverAnnual": 1.208,
    "assetTurnoverTTM": 1.2324,
    "beta": 1.0580528,
    "bookValuePerShareAnnual": 10.0379,
    "bookValuePerShareQuarterly": 10.0379,
    "bookValueShareGrowth5Y": 4.41,
    "capexCagr5Y": -0.32,
    "cashFlowPerShareAnnual": 1.4748,
    "cashFlowPerShareQuarterly": 1.4748,
    "cashFlowPerShareTTM": 3.82458,
    "cashPerSharePerShareAnnual": 6.0957,
    "cashPerSharePerShareQuarterly": 6.0957,
    "currentDividendYieldTTM": 4.479,
    "currentEv/freeCashFlowAnnual": 24.7796,
    "currentEv/freeCashFlowTTM": 24.7796,
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
    "enterpriseValue": 54118.74,
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
    "evEbitdaTTM": 11.9099,
    "evRevenueTTM": 1.1664,
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
    "marketCapitalization": 53739.74,
    "monthToDatePriceReturnDaily": -5.1459,
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
    "pb": 3.6152,
    "pbAnnual": 4.5757,
    "pbQuarterly": 4.5757,
    "pcfShareAnnual": 18.7377,
    "pcfShareTTM": 18.7377,
    "peAnnual": 17.2908,
    "peBasicExclExtraTTM": 17.2908,
    "peExclExtraAnnual": 33.32807,
    "peExclExtraTTM": 17.2908,
    "peInclExtraTTM": 17.2908,
    "peNormalizedAnnual": 17.2908,
    "peTTM": 17.2908,
    "pegTTM": 2.44825,
    "pfcfShareAnnual": 24.6061,
    "pfcfShareTTM": 24.6061,
    "pretaxMargin5Y": 11.24,
    "pretaxMarginAnnual": 8.41,
    "pretaxMarginTTM": 8.41,
    "priceRelativeToS&P50013Week": -22.5202,
    "priceRelativeToS&P50026Week": -46.2938,
    "priceRelativeToS&P5004Week": -3.6928,
    "priceRelativeToS&P50052Week": -64.9856,
    "priceRelativeToS&P500Ytd": -53.425,
    "psAnnual": 1.1582,
    "psTTM": 1.1582,
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
    "yearToDatePriceReturnDaily": -41.8459
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

## CCL
Trading candidate:
```json
{
  "symbol": "CCL",
  "score": 29.7,
  "direction": "AVOID",
  "sector": "Consumer Discretionary",
  "components": {
    "market": 50.0,
    "sector": 56.82,
    "relative_strength": 0.0,
    "vwap": 0.0,
    "trend": 0.0,
    "volume": 67.2296526954444,
    "momentum": 37.21499353726844,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 53.51628424704471,
    "trend_acceleration": 25,
    "compression": 10.759493670886101,
    "volatility_contraction": 66.40402996641694,
    "volume_accumulation": 52.93777309966947,
    "breakout_distance": 0.0,
    "support_quality": 100.0,
    "momentum_improvement": 51.474546529337644,
    "early_setup_score": 32.36,
    "entry_timing_score": 32.36,
    "opportunity_score": 30.5,
    "extended": false,
    "return_5d": -4.7,
    "return_10d": -7.43,
    "return_20d": -20.26,
    "distance_to_breakout": 25.41,
    "atr_extension": -3.52
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
      "datetime": 1789549818,
      "headline": "Rapport Therapeutics To Rally Around 76%? Here Are 10 Top Analyst Forecasts For Wednesday",
      "id": 142194797,
      "image": "https://cdn.benzinga.com/files/images/story/2026/09/16/Crypto-Trader-Investor-Broker-Using-Smar.jpg?width=2048&height=1536",
      "related": "CCL",
      "source": "Benzinga",
      "summary": "Analysts raised targets for RAPP, ALLR, UNP and ALVO; cut targets for NU, CLLS and JBHT, with several rating upgrades and downgrades.",
      "url": "https://finnhub.io/api/news?id=262760f490b82bacdb25acb24dc2f4f16b3b49f7ec9afa8c22b1e8190fd61178"
    },
    {
      "category": "company",
      "datetime": 1789529092,
      "headline": "Why Did OPEN, NKE, CCL Stocks Crash To 52-Week Lows Today?",
      "id": 142174606,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "CCL",
      "source": "Yahoo",
      "summary": "Housing weakness, a prolonged athleticwear turnaround, and rising cruise fuel costs weighed on investor sentiment.",
      "url": "https://finnhub.io/api/news?id=aa88ef2a86ed34652268134123020d2cd8b6e3ab8cf49c91718ca057440ae9f5"
    },
    {
      "category": "company",
      "datetime": 1789514402,
      "headline": "Trip.com (TCOM) Beats Q2 Earnings and Revenue Estimates",
      "id": 142169793,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "CCL",
      "source": "Yahoo",
      "summary": "Trip.com (TCOM) delivered earnings and revenue surprises of +9.18% and +0.78%, respectively, for the quarter ended June 2026. Do the numbers hold clues to what lies ahead for the stock?",
      "url": "https://finnhub.io/api/news?id=ff9eaa7cfaf7b7c4279b7bb3bd9ca7dd7d114a234730d26e90dbfdbf4115b846"
    },
    {
      "category": "company",
      "datetime": 1789509003,
      "headline": "Why Carnival (CCL) Dipped More Than Broader Market Today",
      "id": 142168769,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "CCL",
      "source": "Yahoo",
      "summary": "In the latest trading session, Carnival (CCL) closed at $22.09, marking a -2.11% move from the previous day.",
      "url": "https://finnhub.io/api/news?id=19b77c6dcc94dc1464e63ea7caace79868e1a6424c615cb7d061eade892a425d"
    },
    {
      "category": "company",
      "datetime": 1789490214,
      "headline": "Norwegian Falls 3% as Wells Fargo Trims Carnival Target on Caribbean Pricing Pressure; Carnival Slips, Royal Caribbean Dips",
      "id": 142166062,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "CCL",
      "source": "Yahoo",
      "summary": "A Wells Fargo note about Carnival is hitting Norwegian Cruise Line the hardest, and the reason why reveals exactly which operator the market sees as most exposed to the Caribbean pricing storm now moving through the sector.",
      "url": "https://finnhub.io/api/news?id=c65841d5a32d241cee239dccb8ceb79f38e55ecad2bd75523686bee8dfb1a7d1"
    }
  ],
  "polygon_news": [
    {
      "id": "29cead4be807d869c792b386b45ab42f96287587d06b91a113fc11ff7df153ee",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Carnival vs. Uber Technologies: Which Consumer Stock Is a Better Buy in 2026?",
      "author": "Sara Appino",
      "published_utc": "2026-09-15T15:00:52Z",
      "article_url": "https://www.fool.com/coverage/better-buy/2026/09/15/carnival-vs-uber-technologies-which-consumer-stock-is-a-better-buy-in-2026/?source=iedfolrf0000001",
      "tickers": [
        "CCL",
        "UBER",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "LYFT",
        "DASH"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F93f4fcd8f1072083ee446c545b2c796e8edc7e8a-1200x800.png%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "The article compares Carnival Corp. and Uber Technologies as investment options for 2026. Carnival shows strong cruise demand recovery with improving margins but faces significant debt burden, high fuel costs, and geopolitical risks. Uber demonstrates faster growth, stronger cash generation, and a healthier balance sheet through its asset-light platform model. The author recommends Uber as the better long-term investment due to its superior growth trajectory, profitability, and lower financial risk.",
      "keywords": [
        "cruise industry",
        "ridesharing",
        "debt-to-equity ratio",
        "free cash flow",
        "net margins",
        "valuation comparison",
        "balance sheet strength",
        "geopolitical risk"
      ],
      "insights": [
        {
          "ticker": "CCL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Carnival shows positive operational metrics with 12 consecutive quarters of record net yields and improving net margins to 10.4%. However, this is significantly offset by structural challenges including a high debt-to-equity ratio of 2.3x, tight liquidity (0.3x current ratio), rising fuel costs, and geopolitical headwinds. The company has credible recovery momentum but faces material financial constraints."
        },
        {
          "ticker": "UBER",
          "sentiment": "positive",
          "sentiment_reasoning": "Uber demonstrates strong fundamentals with 18.3% revenue growth, healthy 19.3% net margins, and robust free cash flow of $9.8 billion. The company maintains a lean balance sheet with a 0.4x debt-to-equity ratio and 1.1x current ratio. Its asset-light platform model scales efficiently across multiple business lines (mobility, delivery, freight) with double-digit gross bookings growth. Primary risks are legal/regulatory rather than financial."
        },
        {
          "ticker": "GOOG",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as a platform partner through which Uber distributes its software. No independent analysis or sentiment assessment provided in the article."
        },
        {
          "ticker": "GOOGL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as a platform partner through which Uber distributes its software. No independent analysis or sentiment assessment provided in the article."
        },
        {
          "ticker": "GOOGM",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as a platform partner through which Uber distributes its software. No independent analysis or sentiment assessment provided in the article."
        },
        {
          "ticker": "GOOGN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as a platform partner through which Uber distributes its software. No independent analysis or sentiment assessment provided in the article."
        },
        {
          "ticker": "LYFT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a well-funded competitor to Uber in the mobility space, representing a competitive risk factor for Uber rather than being evaluated as an investment option."
        },
        {
          "ticker": "DASH",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a well-funded competitor to Uber in the delivery space, representing a competitive risk factor for Uber rather than being evaluated as an investment option."
        }
      ]
    },
    {
      "id": "233c2f2bff7e61891399d08f966b1870436fd8fa8f65ec6b5fae3915d16b0f73",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Carnival Stock Declines 16% in a Month: Should You Buy or Wait?",
      "author": "Na",
      "published_utc": "2026-09-09T12:41:00Z",
      "article_url": "https://www.zacks.com/stock/news/2986828/carnival-stock-declines-16-in-a-month-should-you-buy-or-wait?cid=CS-ZC-FT-analyst_blog|rank_focused-2986828",
      "tickers": [
        "CCL",
        "NCLH",
        "RCL"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default177.jpg",
      "description": "Carnival Corporation's stock fell 16.1% over the past month due to concerns about European travel demand and geopolitical uncertainty, particularly affecting Mediterranean deployments. However, the company maintains strong long-term fundamentals with historic 2027 booking highs, disciplined fleet expansion, exclusive destination investments, and improving cost structure. Analysts recommend existing shareholders hold while new investors adopt a wait-and-watch approach pending evidence of European demand stabilization.",
      "keywords": [
        "cruise industry",
        "European travel demand",
        "geopolitical uncertainty",
        "forward bookings",
        "fleet modernization",
        "cost savings",
        "deleveraging"
      ],
      "insights": [
        {
          "ticker": "CCL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Stock declined 16.1% due to near-term European demand concerns and geopolitical headwinds, but underlying fundamentals remain constructive with historic 2027 bookings at high prices/occupancy, disciplined capacity expansion, fleet modernization, exclusive destinations, and improving leverage. Rating is Hold (Zacks Rank #3), suggesting balanced risk/reward with near-term uncertainty offsetting long-term positives."
        },
        {
          "ticker": "NCLH",
          "sentiment": "negative",
          "sentiment_reasoning": "Stock declined 17% over the same period as Carnival, indicating similar industry headwinds. Additionally, earnings for 2026 are expected to decline 25.6% year-over-year, significantly worse than Carnival's 0.9% decline, suggesting weaker operational performance."
        },
        {
          "ticker": "RCL",
          "sentiment": "negative",
          "sentiment_reasoning": "Stock declined 14.1% amid industry-wide travel demand concerns. While 2026 earnings are expected to grow 13.7% year-over-year (better than Carnival), the stock decline and near-term uncertainty around European demand and geopolitical factors create negative near-term sentiment."
        }
      ]
    },
    {
      "id": "8abed958c500415508212310a5459accfaa715b01969037a8d8ce6eba352385e",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Here's Why Carnival (CCL) Fell More Than Broader Market",
      "author": "Na",
      "published_utc": "2026-09-08T21:45:07Z",
      "article_url": "https://www.zacks.com/stock/news/2986657/here-s-why-carnival-ccl-fell-more-than-broader-market?cid=CS-ZC-FT-fundamental_analysis|yseop_template_6-2986657",
      "tickers": [
        "CCL"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default315.jpg",
      "description": "Carnival (CCL) closed down 1.32% at $23.20, underperforming the S&P 500. The cruise operator has declined 15.28% over the past month. While revenue is expected to grow 2.59% next quarter, EPS is projected to decline 4.9% year-over-year. The company holds a Zacks Rank #3 (Hold) with a forward P/E of 10.53, trading at a discount to its industry average of 16.15.",
      "keywords": [
        "cruise operator",
        "earnings decline",
        "valuation discount",
        "consumer discretionary",
        "stock performance"
      ],
      "insights": [
        {
          "ticker": "CCL",
          "sentiment": "negative",
          "sentiment_reasoning": "Stock declined 1.32% on the day and 15.28% over the past month, significantly underperforming the S&P 500. Earnings per share are projected to decrease 4.9% year-over-year despite modest revenue growth. The company's industry ranks in the bottom 18% of sectors, and it holds a neutral Zacks Rank #3 (Hold) rating, indicating limited upside potential."
        }
      ]
    },
    {
      "id": "ac3db100deceeb9d8e93f65ba79b307fbf25b5eb7e9441456a46a87abed7c73d",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Carnival's Record Booking Curve Extends: Will Pricing Momentum Last?",
      "author": "Na",
      "published_utc": "2026-09-08T13:13:00Z",
      "article_url": "https://www.zacks.com/stock/news/2986251/carnival-s-record-booking-curve-extends-will-pricing-momentum-last?cid=CS-ZC-FT-analyst_blog|quick_take-2986251",
      "tickers": [
        "CCL",
        "RCL",
        "NCLH"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/c5/1267.jpg",
      "description": "Carnival Corporation has 93% of its 2026 business booked at record pricing with $9 billion in customer deposits, and expects record H2 2026 yields as European headwinds ease. However, geopolitical uncertainty and uneven regional demand pose challenges. Royal Caribbean shows strong momentum with record 2026 pricing and historical highs for 2027, while Norwegian Cruise Line faces softer demand and is implementing a turnaround strategy with revised revenue management.",
      "keywords": [
        "cruise industry",
        "booking trends",
        "pricing momentum",
        "geopolitical uncertainty",
        "European demand",
        "yield growth",
        "revenue management"
      ],
      "insights": [
        {
          "ticker": "CCL",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong forward bookings with 93% of 2026 business booked at record pricing, $9 billion customer deposits at all-time high, record Q2 yields, and expectations for record H2 2026 yields. Recent booking trends show easing European headwinds and improved outlook."
        },
        {
          "ticker": "RCL",
          "sentiment": "positive",
          "sentiment_reasoning": "Reported net yield growth of 1.2%, record 2026 pricing, 2027 bookings pacing ahead of historical levels at historical highs for price and occupancy. Strong demand momentum across portfolio with full-year net yield growth guidance of 1.75%-2.25%."
        },
        {
          "ticker": "NCLH",
          "sentiment": "negative",
          "sentiment_reasoning": "Reported 2.6% decline in Q2 net yields with full-year net yield decline expected of approximately 5%. Facing softer demand environment and marketing challenges, requiring turnaround initiatives that will take time to show results."
        }
      ]
    },
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
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 19.6626,
    "13WeekPriceReturnDaily": -24.2289,
    "26WeekPriceReturnDaily": -14.8633,
    "3MonthADReturnStd": 36.696728,
    "3MonthAverageTradingVolume": 22.10403,
    "52WeekHigh": 34.03,
    "52WeekHighDate": "2026-02-06",
    "52WeekLow": 21.93,
    "52WeekLowDate": "2026-09-15",
    "52WeekPriceReturnDaily": -29.2254,
    "5DayPriceReturnDaily": -2.5991,
    "assetTurnoverAnnual": 0.5151,
    "assetTurnoverTTM": 0.5295,
    "beta": 2.5258193,
    "bookValuePerShareAnnual": 9.3628,
    "bookValuePerShareQuarterly": 9.4519,
    "bookValueShareGrowth5Y": -13.12,
    "capexCagr5Y": -0.05,
    "cashFlowPerShareAnnual": 1.987,
    "cashFlowPerShareQuarterly": 2.3316,
    "cashFlowPerShareTTM": 0.55476,
    "cashPerSharePerShareAnnual": 1.4695,
    "cashPerSharePerShareQuarterly": 1.6348,
    "currentDividendYieldTTM": 1.3659,
    "currentEv/freeCashFlowAnnual": 20.3131,
    "currentEv/freeCashFlowTTM": 16.554,
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
    "enterpriseValue": 52956.336,
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
    "evEbitdaTTM": 7.3838,
    "evRevenueTTM": 1.939,
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
    "marketCapitalization": 30310.336,
    "monthToDatePriceReturnDaily": -7.4508,
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
    "pb": 2.3373,
    "pbAnnual": 2.746,
    "pbQuarterly": 2.6284,
    "pcfShareAnnual": 4.8746,
    "pcfShareTTM": 4.462,
    "peAnnual": 10.982,
    "peBasicExclExtraTTM": 9.8795,
    "peExclExtraTTM": 9.8795,
    "peInclExtraTTM": 9.8795,
    "peNormalizedAnnual": 10.982,
    "peTTM": 9.8795,
    "pegTTM": 1.341,
    "pfcfShareAnnual": 11.6265,
    "pfcfShareTTM": 9.4749,
    "pretaxMargin5Y": -106.25,
    "pretaxMarginAnnual": 10.41,
    "pretaxMarginTTM": 11.34,
    "priceRelativeToS&P50013Week": -26.3374,
    "priceRelativeToS&P50026Week": -26.8486,
    "priceRelativeToS&P5004Week": -17.6111,
    "priceRelativeToS&P50052Week": -43.8235,
    "priceRelativeToS&P500Ytd": -38.6704,
    "psAnnual": 1.1385,
    "psTTM": 1.1098,
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
    "yearToDatePriceReturnDaily": -27.6031
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