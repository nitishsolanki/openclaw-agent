# OpenClaw Candidate Research Handoff

Review each candidate using the supplied trading data and evidence packet. Do not place orders. Return only JSON in this format:

```json
{"research":[{"symbol":"MSFT","research_score":0,"conviction":"Low","catalysts":[],"risks":[],"summary":""}]}
```

Use a 0-100 research score. Do not invent facts or infer fundamentals from technical data. Treat missing data as uncertainty, name the missing source in risks, and use only dated/source-labelled news, earnings, filings, or fundamentals. Keep Python's technical score authoritative; this research score is a 30% adjustment.

## AAPL
Trading candidate:
```json
{
  "symbol": "AAPL",
  "score": 74.03,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 50.0,
    "sector": 84.4,
    "relative_strength": 77.15875329904013,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 26.310856833186662,
    "momentum": 62.99176812292137,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 47.98347005990656,
    "trend_acceleration": 85,
    "compression": 22.31350640814999,
    "volatility_contraction": 73.31879425208376,
    "volume_accumulation": 59.35885306174356,
    "breakout_distance": 85.89908284288856,
    "support_quality": 23.938696860155844,
    "momentum_improvement": 45.46181213332967,
    "early_setup_score": 59.49,
    "entry_timing_score": 58.45,
    "opportunity_score": 69.36,
    "extended": false,
    "return_5d": 0.75,
    "return_10d": 1.98,
    "return_20d": 7.53,
    "distance_to_breakout": 0.71,
    "atr_extension": 1.63
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
      "datetime": 1789735620,
      "headline": "Apple, Nvidia, Microsoft, Alphabet, and Amazon: I Ranked the 5 Largest Companies by Market Cap, and 1 Stands Above the Rest",
      "id": 142254311,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "The names are not surprising. What is surprising, however, is just how big these companies have become, and how fast.",
      "url": "https://finnhub.io/api/news?id=54f0183b818e3fb4fb8de3fca140ff172eed4e4165c263693fe7a784031a06aa"
    },
    {
      "category": "company",
      "datetime": 1789734082,
      "headline": "How Apple's iPhone 18 price increases impact your trade-in value at Verizon, T-Mobile, or AT&T",
      "id": 142254178,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "Getting a new iPhone won't be cheap.",
      "url": "https://finnhub.io/api/news?id=56cf5280801daec218f30a849fb3bc763fc3c0d0f84252935e2f0e17ee16caf4"
    },
    {
      "category": "company",
      "datetime": 1789733663,
      "headline": "Apple iPhone Refresh Cycle Better-Than-Expected, Says Evercore As AAPL Stock Heads For 5th Straight Weekly Gain",
      "id": 142254312,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "Apple new iPhone 18 Pro and Pro Max hit the shelves today, with CEO John Ternus at the company\u2019s New York flagship store for the launch.",
      "url": "https://finnhub.io/api/news?id=f030797b65af02a39dc3cda3dc239d28d215994bf2f42f717d0da5946e2c1459"
    },
    {
      "category": "company",
      "datetime": 1789732779,
      "headline": "Stock Market Today: Dow Wavers As Oil Extends Losses; Apple, AMD In Buy Zones (Live Coverage)",
      "id": 142254050,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "Stock Market Today: The Dow Jones index falls Friday as oil prices continue to drop. Apple, AMD, Micron and Sandisk are key movers.",
      "url": "https://finnhub.io/api/news?id=3dc4f1e306677e2740a6241d7b8be0e21ce6ff8112825dab99650c5c48237329"
    },
    {
      "category": "company",
      "datetime": 1789730100,
      "headline": "BUZZ Investing: Rising Oil Prices And Treasury Yields Pressure Equities",
      "id": 142257468,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/2267617953/image_2267617953.jpg?io=getty-c-w1536",
      "related": "AAPL",
      "source": "SeekingAlpha",
      "summary": "The S&P 500 declined 2.5% and Nasdaq Composite 2.6% between selection dates (August 13 \u00e2\u0080\u0093 September 10, 2026), while the BUZZ Index held up better with a 0.8% decline. Read more here.",
      "url": "https://finnhub.io/api/news?id=c3ca3dc5987e7d6a378a62ad938c2434609b2581ee87556d3ed701fd6e7043a7"
    }
  ],
  "polygon_news": [
    {
      "id": "20825d6ee542ac8411502c6c09be66cfeea783e2cd589ea10503ada4a0a4dedf",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "31% of Berkshire Hathaway's Portfolio Is Concentrated in These 2 AI Stocks Under Greg Abel",
      "author": "Neil Patel",
      "published_utc": "2026-09-18T14:30:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/18/berkshire-hathaway-portfolio-2-ai-stocks-greg-abel/?source=iedfolrf0000001",
      "tickers": [
        "AAPL",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "BRK.A",
        "BRK.B"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F886849%2Fusing-ai-chatbot-on-smartphone.jpg&w=1200&op=resize",
      "description": "Berkshire Hathaway has concentrated 30.7% of its $365 billion equities portfolio in two AI stocks: Apple and Alphabet. Under new CEO Greg Abel, the conglomerate is signaling a bullish stance on AI, with Apple leveraging its 2.5 billion active devices for consumer AI adoption and Alphabet leading across AI research, chip design, and cloud services.",
      "keywords": [
        "Berkshire Hathaway",
        "AI stocks",
        "Apple",
        "Alphabet",
        "Greg Abel",
        "portfolio concentration",
        "artificial intelligence",
        "technology investment"
      ],
      "insights": [
        {
          "ticker": "AAPL",
          "sentiment": "positive",
          "sentiment_reasoning": "Described as Berkshire's largest holding and 'most lucrative capital allocation decision' with 1,000%+ gains over a decade. Positioned as an elite AI enterprise with 2.5 billion active devices providing distribution advantage for consumer AI adoption, strong iPhone demand (21.7% YoY growth), and new Siri AI capabilities."
        },
        {
          "ticker": "GOOG",
          "sentiment": "positive",
          "sentiment_reasoning": "Characterized as 'at the forefront of the AI revolution' with involvement across all phases of the industry. Highlighted strengths include Google DeepMind research lab, proprietary Tensor Processing Units, Google Cloud Platform with 82% revenue growth, Gemini AI models, and integration of AI across billions of users and advertising customers."
        },
        {
          "ticker": "GOOGL",
          "sentiment": "positive",
          "sentiment_reasoning": "Characterized as 'at the forefront of the AI revolution' with involvement across all phases of the industry. Highlighted strengths include Google DeepMind research lab, proprietary Tensor Processing Units, Google Cloud Platform with 82% revenue growth, Gemini AI models, and integration of AI across billions of users and advertising customers."
        },
        {
          "ticker": "GOOGM",
          "sentiment": "positive",
          "sentiment_reasoning": "Characterized as 'at the forefront of the AI revolution' with involvement across all phases of the industry. Highlighted strengths include Google DeepMind research lab, proprietary Tensor Processing Units, Google Cloud Platform with 82% revenue growth, Gemini AI models, and integration of AI across billions of users and advertising customers."
        },
        {
          "ticker": "GOOGN",
          "sentiment": "positive",
          "sentiment_reasoning": "Characterized as 'at the forefront of the AI revolution' with involvement across all phases of the industry. Highlighted strengths include Google DeepMind research lab, proprietary Tensor Processing Units, Google Cloud Platform with 82% revenue growth, Gemini AI models, and integration of AI across billions of users and advertising customers."
        },
        {
          "ticker": "BRK.A",
          "sentiment": "positive",
          "sentiment_reasoning": "Demonstrates strategic adaptation from traditional value investing by concentrating 31% of portfolio in AI stocks, signaling confidence in the technology trend and the long-term prospects of these dominant businesses under new CEO leadership."
        },
        {
          "ticker": "BRK.B",
          "sentiment": "positive",
          "sentiment_reasoning": "Demonstrates strategic adaptation from traditional value investing by concentrating 31% of portfolio in AI stocks, signaling confidence in the technology trend and the long-term prospects of these dominant businesses under new CEO leadership."
        }
      ]
    },
    {
      "id": "eedb3480bf35f1fb1a0b8ace4e98012cbcf6d2a6e6cf539f6fc985557ee91900",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Home Depot vs. Spotify Technology: Which Consumer Stock Is a Better Buy in 2026?",
      "author": "Sara Appino",
      "published_utc": "2026-09-18T12:05:01Z",
      "article_url": "https://www.fool.com/coverage/better-buy/2026/09/18/home-depot-vs-spotify-technology-which-consumer-stock-is-a-better-buy-in-2026/?source=iedfolrf0000001",
      "tickers": [
        "HD",
        "SPOT",
        "AAPL",
        "AMZN"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F3caa0e2607e9485862b0d89e5f6f6be899ae6c41-1200x800.png%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "The article compares Home Depot and Spotify Technology as investment options for 2026. Home Depot, the dominant home improvement retailer, offers steady returns and a 3.07% dividend yield but faces headwinds from a sluggish housing market. Spotify, the global audio streaming leader, demonstrates faster revenue growth (9.7%), record gross margins (32.7%), and improved profitability, making it the author's preferred choice for long-term investors seeking growth exposure.",
      "keywords": [
        "Home Depot",
        "Spotify Technology",
        "stock comparison",
        "consumer stocks",
        "investment analysis",
        "valuation metrics",
        "revenue growth",
        "housing market",
        "streaming services"
      ],
      "insights": [
        {
          "ticker": "HD",
          "sentiment": "neutral",
          "sentiment_reasoning": "Home Depot is described as a dependable, dominant retailer with a loyal customer base and reliable dividend (3.07% yield). However, it faces headwinds from a sluggish housing market and reduced consumer spending on large-ticket projects. The company shows modest revenue growth (3.2%) and higher leverage (5.1x debt-to-equity), making it less attractive than Spotify for growth-focused investors."
        },
        {
          "ticker": "SPOT",
          "sentiment": "positive",
          "sentiment_reasoning": "Spotify demonstrates strong fundamentals with accelerating revenue growth (9.7%), record gross margins (32.7%), and improved net margins (12.9%). The company crossed 300 million premium subscribers, operates with conservative debt (0.3x debt-to-equity), and generates substantial free cash flow ($3.3 billion). The author explicitly recommends Spotify as the better buy for long-term investors due to its superior growth trajectory and multiple monetization opportunities."
        },
        {
          "ticker": "AAPL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Apple is mentioned as a competitive threat to Spotify in the streaming market, with the ability to bundle music services with other products. No direct investment recommendation or analysis is provided."
        },
        {
          "ticker": "AMZN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Amazon is mentioned as a deep-pocketed competitor to Spotify in the streaming industry. No direct investment recommendation or analysis is provided."
        }
      ]
    },
    {
      "id": "889f870ddb41a0c38c1c84b6d9ac0479b7ecc0ed435a7e1be9e4d671474c03a9",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "1 Top Dividend ETF Worth Loading Up On With $1,000 Right Now",
      "author": "David Dierking",
      "published_utc": "2026-09-18T10:15:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/18/top-dividend-etf-worth-loading-up-right-now-fdvv/?source=iedfolrf0000001",
      "tickers": [
        "FDVV",
        "NVDA",
        "AAPL",
        "MSFT"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F886871%2Fgetty-dividend-income.jpg&w=1200&op=resize",
      "description": "The Fidelity High Dividend ETF (FDVV) is recommended as a strong buy for investors seeking total returns combining income and growth. With a 2.6% dividend yield and 13.5% average annual returns over a decade, the fund uniquely balances high dividend yield criteria with growth-oriented megacap tech holdings like Nvidia, Apple, and Microsoft. The portfolio's growth tilt positions it to benefit from expected strong corporate earnings growth driven by AI development.",
      "keywords": [
        "dividend ETF",
        "total return",
        "growth plus income",
        "corporate earnings",
        "artificial intelligence",
        "megacap tech"
      ],
      "insights": [
        {
          "ticker": "FDVV",
          "sentiment": "positive",
          "sentiment_reasoning": "Recommended as a strong buy with above-average dividend yield (2.6%), solid 10-year average annual return of 13.5%, and unique growth-plus-income profile that positions it well for outperformance given expected strong corporate earnings growth."
        },
        {
          "ticker": "NVDA",
          "sentiment": "positive",
          "sentiment_reasoning": "Top holding in FDVV with 7.3% weighting; highlighted as a growth driver benefiting from AI development boom, contributing to the fund's growth profile despite low individual dividend yield."
        },
        {
          "ticker": "AAPL",
          "sentiment": "positive",
          "sentiment_reasoning": "Second-largest holding in FDVV with 6.75% weighting, representing quality megacap tech exposure contributing to the fund's growth and income balance."
        },
        {
          "ticker": "MSFT",
          "sentiment": "positive",
          "sentiment_reasoning": "Third-largest holding in FDVV with 5.32% weighting, representing quality megacap tech exposure contributing to the fund's growth and income balance."
        }
      ]
    },
    {
      "id": "3b3ff30eb370e64a8b42c87d52565da0b6e27ee82bdfc8e95a8ebe9f28916d5e",
      "publisher": {
        "name": "GlobeNewswire Inc.",
        "homepage_url": "https://www.globenewswire.com",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/globenewswire.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/globenewswire.ico"
      },
      "title": "Sports Fan Analytics & Trends Study in the United States Examines U.S. Sports Fan Behavior Across 18 Sport Categories",
      "author": "Researchandmarkets.Com",
      "published_utc": "2026-09-18T08:20:00Z",
      "article_url": "https://www.globenewswire.com/news-release/2026/09/18/3364522/28124/en/sports-fan-analytics-trends-study-in-the-united-states-examines-u-s-sports-fan-behavior-across-18-sport-categories.html",
      "tickers": [
        "NKE",
        "KO",
        "AMZN",
        "AAPL"
      ],
      "image_url": "https://ml.globenewswire.com/Resource/Download/908fb457-7f8e-4a08-9081-5565e3dfb3d7",
      "description": "A comprehensive sports fan analytics study based on 6,666 U.S. consumers surveyed in January 2024 examines fandom trends across 18 sports categories, measuring viewership, attendance, social media engagement, sponsorship influence, and mobile consumption. The study identifies major brands and provides insights relevant to advertisers, sponsors, leagues, and media companies seeking to understand evolving fan behavior across streaming, mobile, and social channels.",
      "keywords": [
        "sports fandom",
        "fan behavior analytics",
        "sponsorship influence",
        "mobile consumption",
        "social media engagement",
        "fantasy sports",
        "sports betting",
        "consumer demographics",
        "viewership trends"
      ],
      "insights": [
        {
          "ticker": "NKE",
          "sentiment": "positive",
          "sentiment_reasoning": "Nike is identified as a major brand with significant influence in sports sponsorship and consumer product preferences, indicating strong market presence and relevance in sports fan engagement."
        },
        {
          "ticker": "KO",
          "sentiment": "positive",
          "sentiment_reasoning": "Featured as a key sponsor with established influence in sports marketing and consumer brand preferences among sports fans."
        },
        {
          "ticker": "AMZN",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as a major player in sports media consumption and streaming channels, benefiting from the shift in fan engagement toward digital platforms."
        },
        {
          "ticker": "AAPL",
          "sentiment": "positive",
          "sentiment_reasoning": "Listed among key companies in mobile device consumption patterns, positioning it well for sports fan engagement through mobile and streaming platforms."
        }
      ]
    },
    {
      "id": "667ac1ca8eebdbbbc6be1fcc9e8a6a8c37f09001576961c5cfa8e19538cfe952",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "A $100 Monthly Investment in QQQ Could Grow Into This Over 20 Years",
      "author": "Neil Patel",
      "published_utc": "2026-09-18T01:15:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/17/100-monthly-investment-qqq-grow-20-years/?source=iedfolrf0000001",
      "tickers": [
        "QQQ",
        "NVDA",
        "AAPL",
        "MSFT"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F887614%2Fpersons-hands-typing-on-keyboard-with-virtual-etf-sign-and-symbols-shown.jpg&w=1200&op=resize",
      "description": "A $100 monthly investment in the Invesco QQQ Trust ETF could grow to approximately $261,000 over 20 years if past decade performance continues, implying a 20.4% annualized return. However, the article cautions that elevated valuations, concentration risk in top holdings, and potential slowdown in earnings growth for already massive tech companies could limit future returns.",
      "keywords": [
        "QQQ ETF",
        "tech stocks",
        "artificial intelligence",
        "dollar-cost averaging",
        "long-term investing",
        "valuation risk",
        "earnings growth"
      ],
      "insights": [
        {
          "ticker": "QQQ",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong historical performance with 543% return over past decade, driven by tech sector success and secular trends like AI, mobile computing, and cloud computing. However, sentiment is tempered by caution about elevated P/E ratio of 34.5 and concentration risk."
        },
        {
          "ticker": "NVDA",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as a top performer and major holding (8.40%) in QQQ that has significantly outperformed the S&P 500, benefiting from AI and secular tech trends."
        },
        {
          "ticker": "AAPL",
          "sentiment": "positive",
          "sentiment_reasoning": "Second-largest holding (7.92%) in QQQ with strong historical performance, benefiting from mobile computing and other secular trends."
        },
        {
          "ticker": "MSFT",
          "sentiment": "positive",
          "sentiment_reasoning": "Third-largest holding (5.91%) in QQQ with 763% share price increase since mid-2016, driven by cloud computing and AI adoption."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 43.94532,
    "13WeekPriceReturnDaily": 12.1416,
    "26WeekPriceReturnDaily": 29.9695,
    "3MonthADReturnStd": 31.213873,
    "3MonthAverageTradingVolume": 52.19136,
    "52WeekHigh": 344.5699,
    "52WeekHighDate": "2026-07-29",
    "52WeekLow": 236.32,
    "52WeekLowDate": "2025-09-16",
    "52WeekPriceReturnDaily": 39.5801,
    "5DayPriceReturnDaily": 1.7883,
    "assetTurnoverAnnual": 1.1584,
    "assetTurnoverTTM": 1.2508,
    "beta": 1.0825855,
    "bookValuePerShareAnnual": 4.991,
    "bookValuePerShareQuarterly": 7.3599,
    "bookValueShareGrowth5Y": 5.34,
    "capexCagr5Y": 11.71,
    "cashFlowPerShareAnnual": 6.6855,
    "cashFlowPerShareQuarterly": 9.3561,
    "cashFlowPerShareTTM": 6.86253,
    "cashPerSharePerShareAnnual": 3.7024,
    "cashPerSharePerShareQuarterly": 4.2713,
    "currentDividendYieldTTM": 0.3224,
    "currentEv/freeCashFlowAnnual": 49.5717,
    "currentEv/freeCashFlowTTM": 35.8205,
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
    "enterpriseValue": 4896051,
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
    "evEbitdaTTM": 29.1503,
    "evRevenueTTM": 10.488,
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
    "marketCapitalization": 4851251,
    "monthToDatePriceReturnDaily": 4.9108,
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
    "pb": 45.1195,
    "pbAnnual": 50.978,
    "pbQuarterly": 38.486,
    "pcfShareAnnual": 43.516,
    "pcfShareTTM": 33.0638,
    "peAnnual": 43.3109,
    "peBasicExclExtraTTM": 37.627,
    "peExclExtraAnnual": 30.96975,
    "peExclExtraTTM": 37.627,
    "peInclExtraTTM": 37.627,
    "peNormalizedAnnual": 43.3109,
    "peTTM": 37.627,
    "pegTTM": 2.93443,
    "pfcfShareAnnual": 49.1181,
    "pfcfShareTTM": 35.4927,
    "pretaxMargin5Y": 30.64,
    "pretaxMarginAnnual": 31.89,
    "pretaxMarginTTM": 33.4,
    "priceRelativeToS&P50013Week": 12.2449,
    "priceRelativeToS&P50026Week": 16.759,
    "priceRelativeToS&P5004Week": 6.8692,
    "priceRelativeToS&P50052Week": 25.3301,
    "priceRelativeToS&P500Ytd": 11.695,
    "psAnnual": 11.6571,
    "psTTM": 10.3921,
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
    "yearToDatePriceReturnDaily": 22.2725
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

## NVDA
Trading candidate:
```json
{
  "symbol": "NVDA",
  "score": 70.09,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 50.0,
    "sector": 84.4,
    "relative_strength": 61.09845074779811,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 20.57136626519087,
    "momentum": 62.676811660631635,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 43.66,
    "extension": 100.0,
    "relative_strength_acceleration": 53.19119559608598,
    "trend_acceleration": 85,
    "compression": 0.0,
    "volatility_contraction": 74.25800534665444,
    "volume_accumulation": 24.862110370851827,
    "breakout_distance": 3.8382734599098285,
    "support_quality": 49.18726949870238,
    "momentum_improvement": 51.41349846039187,
    "early_setup_score": 40.7,
    "entry_timing_score": 40.7,
    "opportunity_score": 61.27,
    "extended": false,
    "return_5d": 0.67,
    "return_10d": -3.9,
    "return_20d": 1.26,
    "distance_to_breakout": 4.81,
    "atr_extension": 0.18
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
      "datetime": 1789735854,
      "headline": "NVIDIA (NASDAQ:NVDA): High-Growth Leadership and Strong Momentum",
      "id": 142254237,
      "image": "https://www.chartmill.com/images/uploads/thumbnail_article_o_neill_9796d922cc.webp",
      "related": "NVDA",
      "source": "ChartMill",
      "summary": "NVIDIA clears every CANSLIM hurdle with 111% EPS growth, strong fundamentals, and leadership. See the full breakout setup, risks, and key levels.",
      "url": "https://finnhub.io/api/news?id=b1cdd6c4cf40fa973147fcd5c8919a22f68e2178cacc9cf8f3dae63d41f1c770"
    },
    {
      "category": "company",
      "datetime": 1789734960,
      "headline": "Step Aside, Nvidia: 1 Reason Why Meta Platforms Could Be the Best AI Stock to Buy in 2026.",
      "id": 142254109,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NVDA",
      "source": "Yahoo",
      "summary": "In the long run, the infrastructure powering the AI boom could become commoditized, with more of the value going to the businesses creating applications.",
      "url": "https://finnhub.io/api/news?id=8a9685787b7ed25da2d03702cb226ab16ae1452dc02296b486215597dd7bac65"
    },
    {
      "category": "company",
      "datetime": 1789734659,
      "headline": "Prediction: This Is Where Nvidia Stock Could Be by the End of Next Year",
      "id": 142254123,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NVDA",
      "source": "Yahoo",
      "summary": "Nvidia shares have already delivered 900% over five years, but a specific multiple applied to a rising earnings estimate points to a price target that Wall Street has not yet penciled in. Here is the math behind the case for NVDA reaching a level that would shock most investors by late 2027.",
      "url": "https://finnhub.io/api/news?id=035567a326efdf5c5c693b7714fa844628accbd01f71161b0a95eeea6d106bea"
    },
    {
      "category": "company",
      "datetime": 1789734360,
      "headline": "Jensen Huang just gave Nvidia investors a massive 2027 signal",
      "id": 142254110,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NVDA",
      "source": "Yahoo",
      "summary": "Nvidia is already preparing investors for another unusually large jump in AI chip demand",
      "url": "https://finnhub.io/api/news?id=f2b9f4964bb2cb7be797fd6da07a62fbaa860e110cff1ce28fed983d460ca530"
    },
    {
      "category": "company",
      "datetime": 1789734360,
      "headline": "If a Recession Is Coming, History Says This 1 No-Brainer ETF Is the Smartest Buy Right Now",
      "id": 142253885,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NVDA",
      "source": "Yahoo",
      "summary": "Hopefully, a recession is averted, but if one arrives, the Invesco S&P 500 High Dividend Low Volatility ETF could help investors weather the storm.",
      "url": "https://finnhub.io/api/news?id=c673039233b478e23bba07fd14c687866878b51d10e3b82794b2d8514bf3f27f"
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
      "epsEstimate": 2.5231,
      "epsActual": null,
      "revenueEstimate": 111273704778,
      "revenueActual": null
    }
  ],
  "fundamentals": {
    "10DayAverageTradingVolume": 114.47784,
    "13WeekPriceReturnDaily": 0.6825,
    "26WeekPriceReturnDaily": 16.7959,
    "3MonthADReturnStd": 40.259518,
    "3MonthAverageTradingVolume": 142.40149,
    "52WeekHigh": 236.54,
    "52WeekHighDate": "2026-05-14",
    "52WeekLow": 164.27,
    "52WeekLowDate": "2026-03-30",
    "52WeekPriceReturnDaily": 22.3124,
    "5DayPriceReturnDaily": -2.0425,
    "assetTurnoverAnnual": 1.0442,
    "assetTurnoverTTM": 1.2788,
    "beta": 2.2250724,
    "bookValuePerShareAnnual": 6.4719,
    "bookValuePerShareQuarterly": 9.4829,
    "bookValueShareGrowth5Y": 56.87,
    "capexCagr5Y": 39.89,
    "cashFlowPerShareAnnual": 3.9778,
    "cashFlowPerShareQuarterly": 5.2597,
    "cashFlowPerShareTTM": 8.20683,
    "cashPerSharePerShareAnnual": 2.5739,
    "cashPerSharePerShareQuarterly": 4.1152,
    "currentDividendYieldTTM": 0.1282,
    "currentEv/freeCashFlowAnnual": 54.7914,
    "currentEv/freeCashFlowTTM": 41.7068,
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
    "enterpriseValue": 5297017,
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
    "evEbitdaTTM": 26.3343,
    "evRevenueTTM": 17.4837,
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
    "marketCapitalization": 5286094,
    "monthToDatePriceReturnDaily": -3.1162,
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
    "pb": 23.085,
    "pbAnnual": 28.8075,
    "pbQuarterly": 20.768,
    "pcfShareAnnual": 51.4622,
    "pcfShareTTM": 39.3428,
    "peAnnual": 44.0262,
    "peBasicExclExtraTTM": 27.4063,
    "peExclExtraAnnual": 274.2091,
    "peExclExtraTTM": 27.4063,
    "peInclExtraTTM": 27.4063,
    "peNormalizedAnnual": 44.0262,
    "peTTM": 27.4063,
    "pegTTM": 0.57728,
    "pfcfShareAnnual": 54.6785,
    "pfcfShareTTM": 41.6208,
    "pretaxMargin5Y": 47.57,
    "pretaxMarginAnnual": 65.5,
    "pretaxMarginTTM": 75.83,
    "priceRelativeToS&P50013Week": 0.7858,
    "priceRelativeToS&P50026Week": 3.5854,
    "priceRelativeToS&P5004Week": 0.2694,
    "priceRelativeToS&P50052Week": 8.0624,
    "priceRelativeToS&P500Ytd": 4.1142,
    "psAnnual": 24.4797,
    "psTTM": 17.4476,
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
    "yearToDatePriceReturnDaily": 14.6917
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

## SPCX
Trading candidate:
```json
{
  "symbol": "SPCX",
  "score": 68.64,
  "direction": "LONG",
  "sector": "Communication Services",
  "components": {
    "market": 50.0,
    "sector": 52.88,
    "relative_strength": 83.04884575424941,
    "vwap": 81.8752772849915,
    "trend": 100.0,
    "volume": 38.242359561388405,
    "momentum": 58.134241953091376,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 66.11290009800209,
    "relative_strength_acceleration": 39.546434602681444,
    "trend_acceleration": 85,
    "compression": 10.183461845254001,
    "volatility_contraction": 48.26603866752764,
    "volume_accumulation": 54.21718897462949,
    "breakout_distance": 42.23610741823984,
    "support_quality": 0.0,
    "momentum_improvement": 35.819485896500964,
    "early_setup_score": 45.32,
    "entry_timing_score": 40.69,
    "opportunity_score": 60.25,
    "extended": false,
    "return_5d": -0.47,
    "return_10d": 0.5,
    "return_20d": 12.31,
    "distance_to_breakout": 2.89,
    "atr_extension": 0.81
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
      "datetime": 1789733100,
      "headline": "Dario Amodei Just Admitted \"There Are Real Dangers\" in AI, Right as Anthropic Nears a $2 Trillion IPO With Back-to-Back Profitable Quarters. Should That Change How Investors Value the Listing?",
      "id": 142254125,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SPCX",
      "source": "Yahoo",
      "summary": "Will fears of AI crush Anthropic's IPO valuation prospects?",
      "url": "https://finnhub.io/api/news?id=01e1a471a7b002987ca7184268a53e689c6a2e3d892ee84b5e2d15a99c3b5d34"
    },
    {
      "category": "company",
      "datetime": 1789732467,
      "headline": "Rates Could Reach 4.5% On AI Spending, And Semiconductors Get Paid First",
      "id": 142257616,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/2292977505/image_2292977505.jpg?io=getty-c-w1536",
      "related": "SPCX",
      "source": "SeekingAlpha",
      "summary": "iShares Semiconductor ETF and VanEck Semiconductor ETF semiconductor funds remain Buys as AI-driven capex fuels demand. Click for more on SMH and SOXX.",
      "url": "https://finnhub.io/api/news?id=f04479a0d80616a98969ab04c76aeb7c4a6fbb2d9e4ad2bcf5e0391c8be6c99a"
    },
    {
      "category": "company",
      "datetime": 1789731968,
      "headline": "Dow Jones Futures: After S&P 500, Nasdaq Rebound, What's Next? Moderna, AMD, SpaceX Flash Buy Signals.",
      "id": 142252050,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SPCX",
      "source": "Yahoo",
      "summary": "The S&P 500 and Nasdaq regain their 50-day lines and Treasury yields fall in a bullish day two Fed reaction. SpaceX, AMD, Moderna are buys.",
      "url": "https://finnhub.io/api/news?id=8a29ce95b8561e45cc4eae2eca551ccca3c17ca7c92fdd223266bfff202193b6"
    },
    {
      "category": "company",
      "datetime": 1789730761,
      "headline": "2 Game-Changing AI Stocks That Can Plunge 48% and 54%, According to Select Wall Street Analysts",
      "id": 142252951,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SPCX",
      "source": "Yahoo",
      "summary": "Despite popular belief, optimism about the artificial intelligence (AI) revolution isn\u2019t universal on Wall Street.",
      "url": "https://finnhub.io/api/news?id=98f7e3745d1731726d1dbcda9e2ff197478a1640a685c3baecaf83a7dd70be59"
    },
    {
      "category": "company",
      "datetime": 1789727820,
      "headline": "Launch As Infrastructure: What SpaceX's 100th Mission Of 2026 Tells Investors",
      "id": 142256906,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/2181539697/image_2181539697.jpg?io=getty-c-w1536",
      "related": "SPCX",
      "source": "SeekingAlpha",
      "summary": "SpaceX reached 100 Falcon launches by August 22, 2026, reinforcing a shift in launch activity from occasional technological achievement toward high-cadence infrastructure.",
      "url": "https://finnhub.io/api/news?id=c6688655cfafbcc93c28839008d6991dd9d79f76b8c8de8fada3393142274713"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 87.40438,
    "13WeekPriceReturnDaily": -21.6208,
    "3MonthADReturnStd": 89.11323,
    "3MonthAverageTradingVolume": 109.95065,
    "52WeekHigh": 225.64,
    "52WeekHighDate": "2026-06-16",
    "52WeekLow": 104.83,
    "52WeekLowDate": "2026-08-03",
    "5DayPriceReturnDaily": 1.8221,
    "assetTurnoverAnnual": 0.2028,
    "beta": 5.391323,
    "bookValuePerShareQuarterly": 9.6557,
    "cashFlowPerShareAnnual": -1.067,
    "cashPerSharePerShareAnnual": 1.8926,
    "cashPerSharePerShareQuarterly": 7.5902,
    "currentRatioAnnual": 1.4464,
    "currentRatioQuarterly": 5.1154,
    "dividendIndicatedAnnual": 0,
    "ebitdPerShareAnnual": 0.3145,
    "ebitdPerShareTTM": 0.2137,
    "enterpriseValue": 1956396,
    "epsAnnual": -0.3776,
    "epsBasicExclExtraItemsAnnual": -0.3776,
    "epsBasicExclExtraItemsTTM": -0.7457,
    "epsExclExtraItemsAnnual": -0.3776,
    "epsExclExtraItemsTTM": -0.7457,
    "epsGrowthQuarterlyYoy": null,
    "epsInclExtraItemsAnnual": -0.3776,
    "epsInclExtraItemsTTM": -0.7457,
    "epsNormalizedAnnual": -0.3776,
    "epsTTM": -0.7457,
    "forwardPE": 718.07041,
    "forwardPEG": 11.61926,
    "grossMarginAnnual": 49.39,
    "grossMarginTTM": 50.82,
    "longTermDebt/equityAnnual": 0.5106,
    "longTermDebt/equityQuarterly": 0.2896,
    "marketCapitalization": 2010554,
    "monthToDatePriceReturnDaily": 5.0038,
    "netIncomeEmployeeAnnual": -0.2244,
    "netIncomeEmployeeTTM": -0.4434,
    "netInterestCoverageAnnual": -3.1072,
    "netInterestCoverageTTM": -1.6958,
    "netProfitMarginAnnual": -26.44,
    "netProfitMarginTTM": -31.28,
    "operatingMarginAnnual": -13.86,
    "operatingMarginTTM": -19.94,
    "pb": 15.8033,
    "pbQuarterly": 17.6726,
    "pcfShareAnnual": 296.3234,
    "pcfShareTTM": 203.0863,
    "peAnnual": null,
    "peBasicExclExtraTTM": null,
    "peExclExtraTTM": null,
    "peInclExtraTTM": null,
    "peNormalizedAnnual": null,
    "peTTM": null,
    "pfcfShareAnnual": 19148.1333,
    "pretaxMarginAnnual": -22.59,
    "pretaxMarginTTM": -28.89,
    "priceRelativeToS&P50013Week": -21.5175,
    "priceRelativeToS&P5004Week": 9.9932,
    "priceRelativeToS&P500Ytd": -7.9148,
    "psAnnual": 107.666,
    "psTTM": 64.478,
    "ptbvQuarterly": 17.8576,
    "quickRatioAnnual": 1.3335,
    "quickRatioQuarterly": 4.9867,
    "revenueEmployeeAnnual": 0.8488,
    "revenueEmployeeTTM": 1.4174,
    "revenueGrowthQuarterlyYoy": 91.94,
    "revenuePerShareAnnual": 1.4281,
    "revenuePerShareTTM": 2.3666,
    "roaRfy": -5.36,
    "roeRfy": -11.95,
    "roiAnnual": -7.6899999999999995,
    "tangibleBookValuePerShareQuarterly": 9.5557,
    "totalDebt/totalEquityAnnual": 0.554,
    "totalDebt/totalEquityQuarterly": 0.3094,
    "yearToDatePriceReturnDaily": -6.2566
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

## HPE
Trading candidate:
```json
{
  "symbol": "HPE",
  "score": 69.56,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 50.0,
    "sector": 84.4,
    "relative_strength": 77.13220757499943,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 12.542111392666714,
    "momentum": 49.62628865979383,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 60.81,
    "extension": 48.71763593668998,
    "relative_strength_acceleration": 30.450569267965907,
    "trend_acceleration": 85,
    "compression": 0.0,
    "volatility_contraction": 31.69930780316095,
    "volume_accumulation": 77.95951780121683,
    "breakout_distance": 46.75045477096083,
    "support_quality": 0.0,
    "momentum_improvement": 25.424211228254645,
    "early_setup_score": 42.34,
    "entry_timing_score": 33.72,
    "opportunity_score": 58.81,
    "extended": false,
    "return_5d": -2.59,
    "return_10d": 11.1,
    "return_20d": 14.2,
    "distance_to_breakout": 2.66,
    "atr_extension": 1.53
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
      "datetime": 1789732228,
      "headline": "Jim Cramer Says Hewlett Packard Enterprise (HPE) Has the \u201cHorses\u201d but Remains a Dell (DELL) \u201cFan\u201d",
      "id": 142253106,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPE",
      "source": "Yahoo",
      "summary": "Toward the end of the lightning round on September 14, when a caller inquired about Hewlett Packard Enterprise Company (NYSE:HPE), Mad Money host Jim Cramer said: Neri\u2019s good. Neri\u2019s good\u2026 I didn\u2019t think they had the horses. They do have the horses. The fact is that I\u2019m just a Dell fan, I guess, in the [\u2026]",
      "url": "https://finnhub.io/api/news?id=67dfbf48a6a71acee27b094448ea5714c9826436b6b0529cf997beaa168802cb"
    },
    {
      "category": "company",
      "datetime": 1789729960,
      "headline": "2 Safe-and-Steady Stocks for Long-Term Investors and 1 We Ignore",
      "id": 142252617,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPE",
      "source": "Yahoo",
      "summary": "A stock with low volatility can be reassuring, but it doesn\u2019t always mean strong long-term performance. Investors who prioritize stability may miss out on higher-reward opportunities elsewhere.",
      "url": "https://finnhub.io/api/news?id=3186fddab706627651ee04f25659ad2c4603bba3ff230a9ed1e065af4fdb63d9"
    },
    {
      "category": "company",
      "datetime": 1789727333,
      "headline": "Investing In Everpure: Growth Potential You Can't Ignore",
      "id": 142256909,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/1072407176/image_1072407176.jpg?io=getty-c-w1536",
      "related": "HPE",
      "source": "SeekingAlpha",
      "summary": "Everpure, Inc. (formerly Pure Storage) rebranded\u00e2\u0080\u0094see how its cloud storage lineup and AI-driven data-centric model support growth & valuation. Click for a P update.",
      "url": "https://finnhub.io/api/news?id=73ce1b1ff97b35e4eed68d64b1e3f9d01bcb3ed14288656fd097d6251a9b1ad5"
    },
    {
      "category": "company",
      "datetime": 1789671901,
      "headline": "What's going on in today's session: S&P500 movers",
      "id": 142229482,
      "image": "https://www.chartmill.com/images/uploads/CM_Top_Movers_Small_free_2b4ff2fc22.webp",
      "related": "HPE",
      "source": "ChartMill",
      "summary": "Curious about the top performers within the S&P500 index one hour before the close of the markets on Thursday? Dive into the list of today's session's top gainers and losers for a comprehensive overview.",
      "url": "https://finnhub.io/api/news?id=55f31429d3f26aac53f71cf95d0c731361353e893a3ade3b59802a6b3e5e7d80"
    },
    {
      "category": "company",
      "datetime": 1789669378,
      "headline": "Is Cisco Stock Priced For Orders That Are Not Yet Revenue?",
      "id": 142232181,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPE",
      "source": "Yahoo",
      "summary": "Cisco Systems (CSCO) grew revenue more slowly over the last twelve months than any other company in its peer group. Yet it trades on almost the same earnings multiple as Dell Technologies, the fastest grower of the five. Trailing growth does not explain that price on its own. Cisco's last quarter grew 18%, well ahead of its 11.8% twelve-month figure. The rest of the case rests on AI networking orders that are running well ahead of the revenue Cisco has booked from them.",
      "url": "https://finnhub.io/api/news?id=aa73d46983403a0ae1486af9daf9021957b63aac603ff0879895a295e9e467b4"
    }
  ],
  "polygon_news": [
    {
      "id": "39fe06a7ad0c6cc3a21e4f8c067cd0f26ee1a16d5d0834ff305887c0e61b38b6",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Stock Market News for Sep 14, 2026",
      "author": "Na",
      "published_utc": "2026-09-14T13:28:00Z",
      "article_url": "https://www.zacks.com/stock/news/2989018/stock-market-news-for-sep-14-2026?cid=CS-ZC-FT-market_news-2989018",
      "tickers": [
        "HPE",
        "HPEpC",
        "DELL",
        "XLC",
        "XLY",
        "XLK"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/15/1040.jpg",
      "description": "U.S. stock markets closed sharply higher on Friday as declining oil prices and moderate inflation data eased investor concerns about further rate hikes. The Dow Jones, S&P 500, and Nasdaq all gained around 1%, with technology and consumer discretionary stocks leading the rally. Tech stocks HPE and Dell surged over 12% each, while the VIX fell 11.2%, indicating reduced market volatility.",
      "keywords": [
        "stock market rally",
        "oil prices decline",
        "inflation data",
        "Federal Reserve rate hike",
        "technology stocks",
        "consumer discretionary",
        "market volatility"
      ],
      "insights": [
        {
          "ticker": "HPE",
          "sentiment": "positive",
          "sentiment_reasoning": "Stock soared 12.4% on Friday, driven by broad market rally in tech sector and retreat in oil prices. Company holds Zacks Rank #1 (Strong Buy) rating."
        },
        {
          "ticker": "HPEpC",
          "sentiment": "positive",
          "sentiment_reasoning": "Stock soared 12.4% on Friday, driven by broad market rally in tech sector and retreat in oil prices. Company holds Zacks Rank #1 (Strong Buy) rating."
        },
        {
          "ticker": "DELL",
          "sentiment": "positive",
          "sentiment_reasoning": "Stock surged 12% on Friday, benefiting from technology sector strength and moderation in Treasury yields. Company holds Zacks Rank #1 (Strong Buy) rating."
        },
        {
          "ticker": "XLC",
          "sentiment": "positive",
          "sentiment_reasoning": "ETF advanced 1.4% on Friday, outperforming broader market gains as investors returned to growth-oriented equities."
        },
        {
          "ticker": "XLY",
          "sentiment": "positive",
          "sentiment_reasoning": "ETF gained 1.1% on Friday as improved risk appetite and retreating oil prices boosted economically sensitive sectors."
        },
        {
          "ticker": "XLK",
          "sentiment": "positive",
          "sentiment_reasoning": "ETF advanced 1.1% on Friday, supported by moderation in Treasury yields which reduced borrowing costs for growth stocks."
        }
      ]
    },
    {
      "id": "a38de603025688e25e8f7bfa94e16afdbdf34b2917f5e0903eedfd65025f5325",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "HPE Surges 26% in 3 Months: Is it the Right Time to Buy the Stock?",
      "author": "Na",
      "published_utc": "2026-09-10T14:43:00Z",
      "article_url": "https://www.zacks.com/stock/news/2987783/hpe-surges-26-in-3-months-is-it-the-right-time-to-buy-the-stock?cid=CS-ZC-FT-analyst_blog|most_popular_stocks-2987783",
      "tickers": [
        "HPE",
        "HPEpC",
        "AMD",
        "INTC",
        "NVDA"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/3f/989.jpg",
      "description": "Hewlett Packard Enterprise (HPE) has outperformed its industry with a 25.9% gain over three months, driven by strong AI infrastructure demand. The company reported $2.4 billion in AI Systems orders and a record $7.6 billion total AI backlog in Q3 fiscal 2026. Cloud & AI revenues rose 25% with server revenues jumping 35%, while gross margins expanded to 40.4% and operating profit grew 155%. Despite the stock appreciation, HPE trades at a discount with a forward P/S ratio of 1.5 versus the industry average of 4.81, prompting analysts to recommend accumulation.",
      "keywords": [
        "AI infrastructure",
        "server demand",
        "cloud computing",
        "enterprise AI deployment",
        "hybrid cloud",
        "profitability growth",
        "valuation discount"
      ],
      "insights": [
        {
          "ticker": "HPE",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong AI infrastructure orders ($2.4B), record AI backlog ($7.6B), 25% Cloud & AI revenue growth, 35% server revenue growth, 155% operating profit increase, expanding gross margins (40.4%), and Zacks Rank #1 Strong Buy rating support positive outlook."
        },
        {
          "ticker": "HPEpC",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong AI infrastructure orders ($2.4B), record AI backlog ($7.6B), 25% Cloud & AI revenue growth, 35% server revenue growth, 155% operating profit increase, expanding gross margins (40.4%), and Zacks Rank #1 Strong Buy rating support positive outlook."
        },
        {
          "ticker": "AMD",
          "sentiment": "positive",
          "sentiment_reasoning": "HPE is expanding its ProLiant server portfolio with AMD EPYC processors, including latest Gen12 systems with up to 192 cores, indicating strong partnership and demand for AMD's AI-capable processors."
        },
        {
          "ticker": "INTC",
          "sentiment": "positive",
          "sentiment_reasoning": "HPE maintains a deep relationship with Intel and launched new ProLiant DL360 and DL380 Gen12 servers powered by Intel Xeon 6 processors, demonstrating continued demand for Intel's enterprise processors."
        },
        {
          "ticker": "NVDA",
          "sentiment": "positive",
          "sentiment_reasoning": "HPE and NVIDIA are expanding collaboration on AI infrastructure through HPE AI Factory and Private Cloud AI offerings, with HPE supporting NVIDIA's Blackwell, Rubin architectures and networking solutions across its portfolio."
        }
      ]
    },
    {
      "id": "440485b817d764d1babc8ce86f9bf38e925caa5b6b14703738db6d53811f8296",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Dell vs. HPE: Which Top AI Server Stock Is the Better Buy?",
      "author": "Na",
      "published_utc": "2026-09-09T17:14:00Z",
      "article_url": "https://www.zacks.com/stock/news/2986715/dell-vs-hpe-which-top-ai-server-stock-is-the-better-buy?cid=CS-ZC-FT-video_blog-2986715",
      "tickers": [
        "DELL",
        "HPE",
        "HPEpC",
        "NVDA"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default303.jpg",
      "description": "Dell Technologies and Hewlett Packard Enterprise both delivered record quarterly results driven by explosive AI-server demand. Dell posted 58% revenue growth with AI-optimized server revenue doubling, while HPE achieved 34% revenue growth with strong server and networking gains. Both companies raised full-year guidance significantly. Dell gets a slight edge as the better buy due to its larger AI-server position and stronger growth, though HPE offers better valuation metrics for value-oriented investors.",
      "keywords": [
        "AI infrastructure",
        "enterprise servers",
        "data center",
        "earnings growth",
        "hybrid cloud",
        "GPU computing",
        "hyperscale spending"
      ],
      "insights": [
        {
          "ticker": "DELL",
          "sentiment": "positive",
          "sentiment_reasoning": "Record Q2 revenue of $46.97B (+58% YoY), AI-server revenue doubled to $16.4B, adjusted EPS surged 203% to $7.04, and management raised FY27 guidance to $192B revenue (+69% YoY) with $25.50 EPS (+148% YoY). Market-leading 16.5% server OEM share and massive AI-server backlog support strong near-term growth."
        },
        {
          "ticker": "HPE",
          "sentiment": "positive",
          "sentiment_reasoning": "Record Q3 revenue of $12.21B (+34% YoY), adjusted EPS climbed to $1.11 from $0.44 YoY, Cloud & AI revenue up 25% with server revenue +35%, and networking revenue jumped 75% post-Juniper acquisition. Full-year guidance raised to 34%-37% revenue growth with 16%-20% EPS growth expected for FY27."
        },
        {
          "ticker": "HPEpC",
          "sentiment": "positive",
          "sentiment_reasoning": "Record Q3 revenue of $12.21B (+34% YoY), adjusted EPS climbed to $1.11 from $0.44 YoY, Cloud & AI revenue up 25% with server revenue +35%, and networking revenue jumped 75% post-Juniper acquisition. Full-year guidance raised to 34%-37% revenue growth with 16%-20% EPS growth expected for FY27."
        },
        {
          "ticker": "NVDA",
          "sentiment": "positive",
          "sentiment_reasoning": "Both Dell and HPE have extensive partnerships with Nvidia, integrating its accelerated computing technology into their AI factories and private-cloud infrastructure platforms, positioning Nvidia as a key beneficiary of the enterprise AI infrastructure boom."
        }
      ]
    },
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
    }
  ],
  "earnings": [
    {
      "symbol": "HPE",
      "date": "2026-12-02",
      "hour": "amc",
      "quarter": 4,
      "year": 2026,
      "epsEstimate": 1.2751,
      "epsActual": null,
      "revenueEstimate": 14460009551,
      "revenueActual": null
    }
  ],
  "fundamentals": {
    "10DayAverageTradingVolume": 35.81572,
    "13WeekPriceReturnDaily": 15.6263,
    "26WeekPriceReturnDaily": 162.6506,
    "3MonthADReturnStd": 65.639275,
    "3MonthAverageTradingVolume": 25.40727,
    "52WeekHigh": 64.25,
    "52WeekHighDate": "2026-06-02",
    "52WeekLow": 19.84,
    "52WeekLowDate": "2026-02-24",
    "52WeekPriceReturnDaily": 132.0098,
    "5DayPriceReturnDaily": 2.644,
    "assetTurnoverAnnual": 0.4518,
    "assetTurnoverTTM": 0.5321,
    "beta": 1.4481047,
    "bookValuePerShareAnnual": 18.7273,
    "bookValuePerShareQuarterly": 19.9654,
    "bookValueShareGrowth5Y": 8.47,
    "capexCagr5Y": -0.78,
    "cashFlowPerShareAnnual": 0.4756,
    "cashFlowPerShareQuarterly": 3.1295,
    "cashFlowPerShareTTM": 2.79077,
    "cashPerSharePerShareAnnual": 4.3792,
    "cashPerSharePerShareQuarterly": 4.6807,
    "currentDividendYieldTTM": 1.1364,
    "currentEv/freeCashFlowAnnual": 142.3743,
    "currentEv/freeCashFlowTTM": 21.4795,
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
    "enterpriseValue": 89268.7,
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
    "evEbitdaTTM": 21.2342,
    "evRevenueTTM": 2.132,
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
    "marketCapitalization": 75240.7,
    "monthToDatePriceReturnDaily": 8.4992,
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
    "pb": 2.8378,
    "pbAnnual": 1.3047,
    "pbQuarterly": 2.3923,
    "pcfShareAnnual": 25.7762,
    "pcfShareTTM": 11.24,
    "peAnnual": 1320.0123,
    "peBasicExclExtraTTM": 26.9583,
    "peExclExtraAnnual": 24.10978,
    "peExclExtraTTM": 26.9583,
    "peInclExtraTTM": 26.9583,
    "peNormalizedAnnual": 1320.0123,
    "peTTM": 26.9583,
    "pegTTM": 1.38299,
    "pfcfShareAnnual": 120.0011,
    "pfcfShareTTM": 18.1041,
    "pretaxMargin5Y": 6.52,
    "pretaxMarginAnnual": -0.83,
    "pretaxMarginTTM": 6.29,
    "priceRelativeToS&P50013Week": 15.7296,
    "priceRelativeToS&P50026Week": 149.4401,
    "priceRelativeToS&P5004Week": 8.6334,
    "priceRelativeToS&P50052Week": 117.7598,
    "priceRelativeToS&P500Ytd": 125.3925,
    "psAnnual": 2.1939,
    "psTTM": 1.797,
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
    "yearToDatePriceReturnDaily": 135.97
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

## INTC
Trading candidate:
```json
{
  "symbol": "INTC",
  "score": 71.45,
  "direction": "WATCH",
  "sector": "Technology",
  "components": {
    "market": 50.0,
    "sector": 84.4,
    "relative_strength": 100.0,
    "vwap": 100.0,
    "trend": 50.0,
    "volume": 21.406718981300518,
    "momentum": 76.1095996890789,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 63.57,
    "extension": 73.4375531264908,
    "relative_strength_acceleration": 51.88791303716653,
    "trend_acceleration": 55,
    "compression": 0.0,
    "volatility_contraction": 52.909781107604864,
    "volume_accumulation": 36.83787224315452,
    "breakout_distance": 68.523793956942,
    "support_quality": 0.0,
    "momentum_improvement": 49.924032678769635,
    "early_setup_score": 43.13,
    "entry_timing_score": 21.25,
    "opportunity_score": 56.39,
    "extended": true,
    "return_5d": 4.03,
    "return_10d": 16.81,
    "return_20d": 16.19,
    "distance_to_breakout": 1.57,
    "atr_extension": 2.69
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
      "datetime": 1789736278,
      "headline": "Options traders buy AI chip calls after Fed rate hike",
      "id": 142254589,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "INTC",
      "source": "Yahoo",
      "summary": "Intel options volume hit nearly 3 times its monthly average Thursday as tech stocks rebounded from the Fed's first rate increase since 2023",
      "url": "https://finnhub.io/api/news?id=a1e8a2e937cd8c7e1864bfaf795379cd71652f20a25c9f76e7419b0544f4bd24"
    },
    {
      "category": "company",
      "datetime": 1789734458,
      "headline": "One stock is up 540%, and it's not alone",
      "id": 142254046,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "INTC",
      "source": "Yahoo",
      "summary": "Some of the market's strongest large-cap performers are clustering around chips, memory and AI infrastructure.",
      "url": "https://finnhub.io/api/news?id=0c72cc273b3342ee387f3862c6dad73cce0f59455e76f8bab9d1f597e6593b9e"
    },
    {
      "category": "company",
      "datetime": 1789729500,
      "headline": "Intel, Netflix, Berkshire Hathaway, and More Stocks That Explain Today\u2019s Market",
      "id": 142251913,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "INTC",
      "source": "Yahoo",
      "summary": "FEATURE  Stock futures were rising on Friday, as investors carried on piling into tech following the Federal Reserve\u2019s first interest-rate increase in more than three years. The artificial-intelligence trade still has legs, judging by premarket moves.",
      "url": "https://finnhub.io/api/news?id=499c49aeb3fa0a1348ccccbc27623c722a54d6186230e4918f9d0df30f0a4e43"
    },
    {
      "category": "company",
      "datetime": 1789727987,
      "headline": "Jim Cramer Flags 'Boatload' of Bullish Option Buying in Micron, Sandisk, Intel",
      "id": 142257020,
      "image": "https://cdn.benzinga.com/files/images/story/2026/09/18/New-York-City---October-5-2017-The-Brook.jpg?width=2048&height=1536",
      "related": "INTC",
      "source": "Benzinga",
      "summary": "Jim Cramer flagged over $90M in short-dated chip calls, suggesting Leopold Aschenbrenner\u2019s fund may be behind the trades, though unconfirmed.",
      "url": "https://finnhub.io/api/news?id=7513d742c4927ad51ec33fe3fd5b8479f77815e80e1d79da440d4fb02ae91fdf"
    },
    {
      "category": "company",
      "datetime": 1789723800,
      "headline": "Can Trump\u2019s Deals Survive the Next Congress?",
      "id": 142253028,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "INTC",
      "source": "Yahoo",
      "summary": "Major initiatives of one administration inevitably attract scrutiny when political power changes hands, Y. David Scharf writes.",
      "url": "https://finnhub.io/api/news?id=d810676ffcfc5d7369f899ecb56f92e9684fb2ef98c9df5e10165aa74c20fae1"
    }
  ],
  "polygon_news": [
    {
      "id": "cf5e683410a2b53b8f4009ca04417018e8e3702fd481e9db7260125f60d948f9",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Micron Is Poised to Surge After Its Fiscal Year Ends",
      "author": "Harsh Chauhan",
      "published_utc": "2026-09-18T13:32:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/18/micron-is-poised-to-surge-after-its-fiscal-year-en/?source=iedfolrf0000001",
      "tickers": [
        "MU",
        "INTC"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F886795%2Fmicron-building-at-night-with-micron-logo-on-top_micron.jpg&w=1200&op=resize",
      "description": "Micron Technology is expected to deliver strong fiscal 2026 results on September 30, with revenue estimated to increase 3.5x to $129.7 billion and EPS rising 9x to $73.44. The company benefits from severe memory chip supply shortages driven by AI data center demand, with memory prices expected to continue rising into 2027. Analysts project 315% revenue growth for Q1 fiscal 2027, and Micron's attractive PEG ratio of 0.14 suggests the stock remains undervalued despite its 488% gain over the past year.",
      "keywords": [
        "memory chips",
        "AI data centers",
        "supply shortage",
        "earnings report",
        "semiconductor",
        "memory pricing",
        "fiscal 2026"
      ],
      "insights": [
        {
          "ticker": "MU",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong revenue and earnings growth projections (3.5x and 9x respectively), favorable memory market dynamics with supply shortages supporting price increases, attractive valuation with PEG ratio of 0.14, and expected continued growth momentum into fiscal 2027 driven by robust AI data center demand."
        },
        {
          "ticker": "INTC",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as a source of commentary from CEO Lip-Bu Tan regarding memory supply shortages and pricing trends; no direct investment thesis or performance analysis provided for Intel itself."
        }
      ]
    },
    {
      "id": "73cb3dc5cb9ac40183f78eee5164c6df4fc9111e189b4281e2b1be384eca46fc",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Stock Market News for Sep 18, 2026",
      "author": "Na",
      "published_utc": "2026-09-18T13:30:00Z",
      "article_url": "https://www.zacks.com/stock/news/2991913/stock-market-news-for-sep-18-2026?cid=CS-ZC-FT-market_news-2991913",
      "tickers": [
        "AMD",
        "INTC"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/e5/419.jpg",
      "description": "Wall Street closed sharply higher on Thursday, with the Nasdaq jumping 1.7% and the S&P 500 rising 1.1%, as investors looked past the Fed's 25-basis-point rate hike. Tech and discretionary stocks led the rally, supported by softer oil prices, declining Treasury yields, and strong jobs data that eased inflation and borrowing-cost concerns.",
      "keywords": [
        "Fed rate hike",
        "tech stocks rally",
        "Treasury yields decline",
        "jobless claims",
        "housing starts",
        "market recovery"
      ],
      "insights": [
        {
          "ticker": "AMD",
          "sentiment": "positive",
          "sentiment_reasoning": "Stock jumped 6.4% on Thursday as tech stocks benefited from lower Treasury yields and easing inflation concerns following the Fed rate hike."
        },
        {
          "ticker": "INTC",
          "sentiment": "positive",
          "sentiment_reasoning": "Stock jumped 7.7% on Thursday as part of the broad tech sector rally driven by lower Treasury yields and reduced inflation pressures."
        }
      ]
    },
    {
      "id": "b8cad376f4a2a54cb8728c76c3eeb1dd026bf4508a6c33283627d3194b7cf764",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "UMC Up 250% in the Past Year: Should Investors Bet on the Stock Now?",
      "author": "Zacks.Com",
      "published_utc": "2026-09-18T13:09:00Z",
      "article_url": "https://www.zacks.com/stock/news/2991877/umc-up-250-in-the-past-year-should-investors-bet-on-the-stock-now?cid=CS-ZC-FT-analyst_blog|investment_ideas-2991877",
      "tickers": [
        "UMC",
        "ASX",
        "DIOD",
        "INTC"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/19/1136.jpg",
      "description": "United Microelectronics Corporation (UMC) has surged 250% over the past year, driven by strong foundry demand, rising capacity utilization above 90%, and growing AI opportunities. The company expects AI-related revenues to approach $300M in 2026 and exceed $1B within three years, with new initiatives in silicon photonics and collaboration with Intel. Earnings estimates for 2026 have increased 75.7% in 60 days, and analysts rate UMC as a Strong Buy.",
      "keywords": [
        "semiconductor",
        "foundry",
        "AI infrastructure",
        "capacity utilization",
        "silicon photonics",
        "earnings estimates",
        "specialty technologies"
      ],
      "insights": [
        {
          "ticker": "UMC",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong 250% year-over-year stock performance, improving capacity utilization above 90%, robust demand for 22/28nm technologies, significant AI revenue growth potential ($300M in 2026, $1B+ within 3 years), positive earnings estimate revisions (+75.7% in 60 days), and strategic partnerships with Intel. Zacks Rank #1 Strong Buy rating."
        },
        {
          "ticker": "ASX",
          "sentiment": "positive",
          "sentiment_reasoning": "Stock gained 248.6% over the past year, demonstrating strong performance in the semiconductor industry alongside UMC."
        },
        {
          "ticker": "DIOD",
          "sentiment": "neutral",
          "sentiment_reasoning": "Stock up 60.5% over the past year, showing positive performance but significantly underperforming peers UMC and ASX in the same period."
        },
        {
          "ticker": "INTC",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a strategic partner collaborating with UMC on 12nm process platform with production expected to begin in Arizona in 2027. No direct sentiment indicators provided in the article."
        }
      ]
    },
    {
      "id": "34f54c338ebaa95a835993909c6542bd8a55810c998c60772ae29b581e460ed2",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Buy 3 Neuberger Funds With Diverse Investment Strategies",
      "author": "Na",
      "published_utc": "2026-09-18T10:24:00Z",
      "article_url": "https://www.zacks.com/stock/news/2991741/buy-3-neuberger-funds-with-diverse-investment-strategies?cid=CS-ZC-FT-mutual_fund_commentary-2991741",
      "tickers": [
        "INTC",
        "SCCO",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "AMZN",
        "NVDA",
        "NET",
        "VRT",
        "DDOG"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/09/344.jpg",
      "description": "Stock markets showed strong recovery with the Nasdaq positioned to close higher for the week and the S&P 500 following closely behind. The article highlights three Neuberger Berman mutual funds recommended for long-term investment, all with Zacks Rank #1 ratings and strong historical returns.",
      "keywords": [
        "stock market rally",
        "Nasdaq",
        "S&P 500",
        "mutual funds",
        "Neuberger Berman",
        "long-term investment"
      ],
      "insights": [
        {
          "ticker": "INTC",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a top holding (4.2%) in NBPTX fund with no specific performance commentary"
        },
        {
          "ticker": "SCCO",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a top holding (3.5%) in NBPTX fund with no specific performance commentary"
        },
        {
          "ticker": "GOOG",
          "sentiment": "positive",
          "sentiment_reasoning": "Top holding (10.5%) in NBSRX fund which has strong 3-year (23.9%) and 5-year (13.5%) annualized returns"
        },
        {
          "ticker": "GOOGL",
          "sentiment": "positive",
          "sentiment_reasoning": "Top holding (10.5%) in NBSRX fund which has strong 3-year (23.9%) and 5-year (13.5%) annualized returns"
        },
        {
          "ticker": "GOOGM",
          "sentiment": "positive",
          "sentiment_reasoning": "Top holding (10.5%) in NBSRX fund which has strong 3-year (23.9%) and 5-year (13.5%) annualized returns"
        },
        {
          "ticker": "GOOGN",
          "sentiment": "positive",
          "sentiment_reasoning": "Top holding (10.5%) in NBSRX fund which has strong 3-year (23.9%) and 5-year (13.5%) annualized returns"
        },
        {
          "ticker": "AMZN",
          "sentiment": "positive",
          "sentiment_reasoning": "Significant holding (8.6%) in NBSRX fund with strong historical performance metrics"
        },
        {
          "ticker": "NVDA",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding (8.1%) in NBSRX fund which demonstrates strong 3-year and 5-year returns"
        },
        {
          "ticker": "NET",
          "sentiment": "neutral",
          "sentiment_reasoning": "Top holding (4.9%) in NMGAX mid-cap growth fund with modest 3-year returns (12.1%)"
        },
        {
          "ticker": "VRT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Holding (3.9%) in NMGAX fund with no specific performance commentary"
        },
        {
          "ticker": "DDOG",
          "sentiment": "neutral",
          "sentiment_reasoning": "Holding (3.9%) in NMGAX fund with no specific performance commentary"
        }
      ]
    },
    {
      "id": "bca9d7a5591c514c577cb116ee1b4c4aec682ca483217fb5b9a9dd5d2111e257",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Why Intel Stock Jumped 7.6% Today",
      "author": "Johnny Rice",
      "published_utc": "2026-09-17T23:04:04Z",
      "article_url": "https://www.fool.com/investing/2026/09/17/why-intel-stock-jumped-76-today/?source=iedfolrf0000001",
      "tickers": [
        "INTC",
        "SKHY"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F887948%2Fcompany-intel-headquarters-with-blue-cube-logo-sign-neutral.jpg&w=1200&op=resize",
      "description": "Intel stock surged 7.6% after Reuters reported that SK Hynix is exploring a potential deal to lease or form a joint venture at Intel's Ohio manufacturing facility. While talks remain exploratory with no formal agreement, the news boosted Intel for two consecutive trading sessions. The potential partnership could provide a significant customer for Intel's struggling Foundry business, though regulatory hurdles remain a concern.",
      "keywords": [
        "Intel",
        "SK Hynix",
        "memory chips",
        "Ohio facility",
        "foundry business",
        "joint venture",
        "semiconductor manufacturing"
      ],
      "insights": [
        {
          "ticker": "INTC",
          "sentiment": "positive",
          "sentiment_reasoning": "Stock jumped 7.6% on news of potential SK Hynix partnership. Q2 revenue rose 25% to $16.1B with Data Center and AI revenue climbing 59%. The deal could provide a major customer for Intel's underperforming Foundry business and support CEO's turnaround efforts."
        },
        {
          "ticker": "SKHY",
          "sentiment": "neutral",
          "sentiment_reasoning": "Stock rose 4.64%, showing modest positive movement. The company is exploring manufacturing options in the U.S., which could diversify production but remains in preliminary discussion stages with no confirmed commitment."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 96.15573,
    "13WeekPriceReturnDaily": -20.9682,
    "26WeekPriceReturnDaily": 123.3149,
    "3MonthADReturnStd": 75.87079,
    "3MonthAverageTradingVolume": 117.32846,
    "52WeekHigh": 142.35,
    "52WeekHighDate": "2026-06-30",
    "52WeekLow": 24.45,
    "52WeekLowDate": "2025-09-17",
    "52WeekPriceReturnDaily": 299.8813,
    "5DayPriceReturnDaily": 0.7277,
    "assetTurnoverAnnual": 0.25,
    "assetTurnoverTTM": 0.277,
    "beta": 2.358909,
    "bookValuePerShareAnnual": 22.8837,
    "bookValuePerShareQuarterly": 17.3591,
    "bookValueShareGrowth5Y": 2.78,
    "capexCagr5Y": 0.27,
    "cashFlowPerShareAnnual": -0.991,
    "cashFlowPerShareQuarterly": 0.5614,
    "cashFlowPerShareTTM": 2.09114,
    "cashPerSharePerShareAnnual": 7.4922,
    "cashPerSharePerShareQuarterly": 5.8947,
    "currentDividendYieldTTM": 2.6844,
    "currentEv/freeCashFlowTTM": 201.9866,
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
    "enterpriseValue": 571823.94,
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
    "evEbitdaTTM": 34.0858,
    "evRevenueTTM": 10.0264,
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
    "marketCapitalization": 534160.94,
    "monthToDatePriceReturnDaily": 12.8924,
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
    "pb": 6.1018,
    "pbAnnual": 1.531,
    "pbQuarterly": 7.5624,
    "pcfShareAnnual": 55.0852,
    "pcfShareTTM": 35.7633,
    "peAnnual": null,
    "peBasicExclExtraTTM": null,
    "peExclExtraAnnual": 22.61631,
    "peExclExtraTTM": null,
    "peInclExtraTTM": null,
    "peNormalizedAnnual": null,
    "peTTM": null,
    "pfcfShareAnnual": 58.5254,
    "pfcfShareTTM": 99.4528,
    "pretaxMargin5Y": 4.61,
    "pretaxMarginAnnual": 2.95,
    "pretaxMarginTTM": -17.28,
    "priceRelativeToS&P50013Week": -20.8649,
    "priceRelativeToS&P50026Week": 110.1044,
    "priceRelativeToS&P5004Week": 10.8418,
    "priceRelativeToS&P50052Week": 285.6313,
    "priceRelativeToS&P500Ytd": 163.2707,
    "psAnnual": 10.1065,
    "psTTM": 9.366,
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
    "yearToDatePriceReturnDaily": 173.8482
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
  "score": 64.75,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 50.0,
    "sector": 84.4,
    "relative_strength": 52.02531583770835,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 33.880012703613176,
    "momentum": 45.883526624267375,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 26.8,
    "extension": 48.529762437032446,
    "relative_strength_acceleration": 34.32560620438931,
    "trend_acceleration": 85,
    "compression": 0.0,
    "volatility_contraction": 36.20180233417049,
    "volume_accumulation": 39.470844954928545,
    "breakout_distance": 14.16752843846929,
    "support_quality": 8.73836608066182,
    "momentum_improvement": 29.85282486988139,
    "early_setup_score": 35.05,
    "entry_timing_score": 35.05,
    "opportunity_score": 55.84,
    "extended": false,
    "return_5d": -3.53,
    "return_10d": 2.14,
    "return_20d": 6.03,
    "distance_to_breakout": 4.29,
    "atr_extension": 0.4
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
      "datetime": 1789742101,
      "headline": "What's going on in today's session: S&P500 gap up and gap down stocks",
      "id": 142257038,
      "image": "https://www.chartmill.com/images/uploads/CM_Gap_Stocks_Small_free_ad767b11cf.webp",
      "related": "SMCI",
      "source": "ChartMill",
      "summary": "Friday's session is showcasing interesting market movements in the S&P500 index, with notable gap up and gap down stocks. Stay updated with the gapping S&P500 stocks in today's session.",
      "url": "https://finnhub.io/api/news?id=de9f88db8ae2726d26e10bee3479a866feb120a32217c7ca85edb54a2492afcd"
    },
    {
      "category": "company",
      "datetime": 1789730100,
      "headline": "BUZZ Investing: Rising Oil Prices And Treasury Yields Pressure Equities",
      "id": 142257468,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/2267617953/image_2267617953.jpg?io=getty-c-w1536",
      "related": "SMCI",
      "source": "SeekingAlpha",
      "summary": "The S&P 500 declined 2.5% and Nasdaq Composite 2.6% between selection dates (August 13 \u00e2\u0080\u0093 September 10, 2026), while the BUZZ Index held up better with a 0.8% decline. Read more here.",
      "url": "https://finnhub.io/api/news?id=c3ca3dc5987e7d6a378a62ad938c2434609b2581ee87556d3ed701fd6e7043a7"
    },
    {
      "category": "company",
      "datetime": 1789727333,
      "headline": "Investing In Everpure: Growth Potential You Can't Ignore",
      "id": 142256909,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/1072407176/image_1072407176.jpg?io=getty-c-w1536",
      "related": "SMCI",
      "source": "SeekingAlpha",
      "summary": "Everpure, Inc. (formerly Pure Storage) rebranded\u00e2\u0080\u0094see how its cloud storage lineup and AI-driven data-centric model support growth & valuation. Click for a P update.",
      "url": "https://finnhub.io/api/news?id=73ce1b1ff97b35e4eed68d64b1e3f9d01bcb3ed14288656fd097d6251a9b1ad5"
    },
    {
      "category": "company",
      "datetime": 1789726380,
      "headline": "Zacks Investment Ideas feature highlights: NVIDIA, Advanced Micro Devices, Tempus, Moderna, Super Micro Computer and Aya Gold & Silver",
      "id": 142250074,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SMCI",
      "source": "Yahoo",
      "summary": "NVIDIA, Advanced Micro Devices, Tempus, Moderna, Super Micro Computer and Aya Gold & Silver have been highlighted in this Investment Ideas article.",
      "url": "https://finnhub.io/api/news?id=64b3da817a58392d7d1677e7e792a15381f254e560b2786fcec01a1bf78d67e8"
    },
    {
      "category": "company",
      "datetime": 1789719201,
      "headline": "Relief Rally: Wall Street Decides a Hawkish Fed It Understands Beats a Fed It Doesn't",
      "id": 142245353,
      "image": "https://www.chartmill.com/images/uploads/THUMBNAILS_CHARTMILL_1000_528_4_fc48c1fc85.webp",
      "related": "SMCI",
      "source": "ChartMill",
      "summary": "A day after the Federal Reserve's first rate hike in three years, US stocks rallied as yields eased and the tech names that had been sold hardest this week bounced back.",
      "url": "https://finnhub.io/api/news?id=ba02b2fc907acb035fced53dacc1e5cef6255a6e9bb64f62e530af3ea559ceb8"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 36.61992,
    "13WeekPriceReturnDaily": 19.4489,
    "26WeekPriceReturnDaily": 19.2557,
    "3MonthADReturnStd": 95.29607,
    "3MonthAverageTradingVolume": 51.8054,
    "52WeekHigh": 58.78,
    "52WeekHighDate": "2025-10-09",
    "52WeekLow": 19.48,
    "52WeekLowDate": "2026-03-23",
    "52WeekPriceReturnDaily": -17.947,
    "5DayPriceReturnDaily": -1.4179,
    "assetTurnoverAnnual": 1.3045,
    "assetTurnoverTTM": 1.6313,
    "beta": 2.1967804,
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
    "enterpriseValue": 25407.987,
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
    "evEbitdaTTM": 8.9967,
    "evRevenueTTM": 0.6504,
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
    "marketCapitalization": 24209.174,
    "monthToDatePriceReturnDaily": -1.1534,
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
    "pb": 1.672,
    "pbAnnual": 1.3102,
    "pbQuarterly": 1.3102,
    "pcfShareAnnual": null,
    "pcfShareTTM": null,
    "peAnnual": 10.8539,
    "peBasicExclExtraTTM": 10.8539,
    "peExclExtraAnnual": 24.98282,
    "peExclExtraTTM": 10.8539,
    "peInclExtraTTM": 10.8539,
    "peNormalizedAnnual": 10.8539,
    "peTTM": 10.8539,
    "pegTTM": 0.31154,
    "pfcfShareAnnual": 15.7991,
    "pfcfShareTTM": 33.6832,
    "pretaxMargin5Y": 7.57,
    "pretaxMarginAnnual": 7.14,
    "pretaxMarginTTM": 7.14,
    "priceRelativeToS&P50013Week": 19.5522,
    "priceRelativeToS&P50026Week": 6.0452,
    "priceRelativeToS&P5004Week": 2.6898,
    "priceRelativeToS&P50052Week": -32.197,
    "priceRelativeToS&P500Ytd": 15.3193,
    "psAnnual": 0.6197,
    "psTTM": 0.6197,
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
    "yearToDatePriceReturnDaily": 25.8968
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

## HPQ
Trading candidate:
```json
{
  "symbol": "HPQ",
  "score": 68.91,
  "direction": "WATCH",
  "sector": "Technology",
  "components": {
    "market": 50.0,
    "sector": 84.4,
    "relative_strength": 81.02517943843688,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 12.382060347915408,
    "momentum": 47.70965468639882,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 34.997357556872615,
    "relative_strength_acceleration": 26.57244702568185,
    "trend_acceleration": 85,
    "compression": 0.0,
    "volatility_contraction": 45.12141922349863,
    "volume_accumulation": 43.81057852140062,
    "breakout_distance": 36.600261742038484,
    "support_quality": 0.0,
    "momentum_improvement": 20.99207152278715,
    "early_setup_score": 37.75,
    "entry_timing_score": 23.63,
    "opportunity_score": 55.33,
    "extended": true,
    "return_5d": -3.07,
    "return_10d": 7.71,
    "return_20d": 16.72,
    "distance_to_breakout": 3.17,
    "atr_extension": 1.59
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
      "datetime": 1789735320,
      "headline": "American Tower Corporation Announces Election of Kristen M. Ludgate to Board of Directors and Declares Quarterly Distribution",
      "id": 142254926,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPQ",
      "source": "Yahoo",
      "summary": "BOSTON, September 18, 2026--American Tower Corporation (NYSE: AMT) announced that its Board of Directors has elected Kristen M. Ludgate as a director.",
      "url": "https://finnhub.io/api/news?id=62aeee7c790cdb3b12d03d4fcd497dc38eea5abf3cf79fe892ea9dfca75be42f"
    },
    {
      "category": "company",
      "datetime": 1789722937,
      "headline": "HP (HPQ) Puts A Local AI Factory In A 4.2 lb Workstation",
      "id": 142248414,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPQ",
      "source": "Yahoo",
      "summary": "HP (NYSE:HPQ) introduced the ZBook Ultra G3a mobile workstation as a local AI factory for professionals. The device is built to run extremely large AI models and multi-agent workflows directly on the machine rather than in the cloud. HP is targeting creative and technical users who want more control over proprietary data and AI performance on-premise. The launch of the ZBook Ultra G3a feeds into a wider pattern of AI hardware moves that recent research has highlighted. Our analysis turns up...",
      "url": "https://finnhub.io/api/news?id=3e8dc02297995a09380f5bcb316b2c78202b7a09477f3600bde2f5deace4636b"
    },
    {
      "category": "company",
      "datetime": 1789676444,
      "headline": "Should You Buy HP Stock For The Shares It Keeps Retiring?",
      "id": 142232073,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPQ",
      "source": "Yahoo",
      "summary": "HP (HPQ) stock has run hard over the past six months, gaining about 78%, and it still trades roughly 8% below its 52-week high. The steadier story is the share count. HP retires a slice of its own stock every year, so earnings per share grow faster than profits do. The question is whether a rising memory bill breaks that.",
      "url": "https://finnhub.io/api/news?id=6228ca08ca949c4dceced79ae889be5331ebebd72b0081956fc160f55e6f0aea"
    },
    {
      "category": "company",
      "datetime": 1789668780,
      "headline": "Lenovo, MemryX Partnership to Expand Sovereign Edge AI in Saudi Arabia",
      "id": 142233713,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPQ",
      "source": "Yahoo",
      "summary": "Lenovo is expanding Saudi Arabia's sovereign edge AI push with MemryX, pairing ThinkEdge servers with local AI processing and services opportunities.",
      "url": "https://finnhub.io/api/news?id=ceef5cc392f1abc89eb4201367272ce389a27d749bd915f45c2493a7b21f3c60"
    },
    {
      "category": "company",
      "datetime": 1789660802,
      "headline": "What Makes HP (HPQ) a Strong Momentum Stock: Buy Now?",
      "id": 142234026,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "HPQ",
      "source": "Yahoo",
      "summary": "Does HP (HPQ) have what it takes to be a top stock pick for momentum investors? Let's find out.",
      "url": "https://finnhub.io/api/news?id=8490d3af06bbdc410147e7435cdf99b31db2cefe4254b2b794df3131f8693824"
    }
  ],
  "polygon_news": [
    {
      "id": "93173fb41a9b9c0d3702f499265682476971fd0ead40a2f514ee98028d14f5d1",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Lenovo, MemryX Partnership to Expand Sovereign Edge AI in Saudi Arabia",
      "author": "Zacks.Com",
      "published_utc": "2026-09-17T18:13:00Z",
      "article_url": "https://www.zacks.com/stock/news/2991605/lenovo-memryx-partnership-to-expand-sovereign-edge-ai-in-saudi-arabia?cid=CS-ZC-FT-analyst_blog|quick_take-2991605",
      "tickers": [
        "LNVGY",
        "DELL",
        "HPQ"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/4f/2789.jpg",
      "description": "Lenovo and MemryX have signed a memorandum of understanding to expand sovereign edge AI deployments across Saudi Arabia. The partnership combines MemryX's Cascade 100P AI accelerator with Lenovo's ThinkEdge SE455 V3 servers to process video and sensor data locally, reducing latency and cloud reliance. The initiative is expected to drive demand for Lenovo's edge servers, strengthen its sovereign AI infrastructure position, and create recurring lifecycle services opportunities, with potential for regional expansion across the Middle East.",
      "keywords": [
        "edge AI",
        "sovereign AI",
        "Saudi Arabia",
        "ThinkEdge servers",
        "AI accelerator",
        "smart cities",
        "industrial automation",
        "AI infrastructure"
      ],
      "insights": [
        {
          "ticker": "LNVGY",
          "sentiment": "positive",
          "sentiment_reasoning": "Partnership expands edge AI deployment opportunities in Saudi Arabia, driving incremental demand for ThinkEdge servers, strengthening sovereign AI infrastructure position, and creating recurring lifecycle services revenue. Stock has outperformed industry with 262.4% YTD gains, though trading at valuation discount to peers."
        },
        {
          "ticker": "DELL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as peer benefiting from sustained AI infrastructure demand and data center modernization, but no direct involvement in this partnership announcement."
        },
        {
          "ticker": "HPQ",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as peer with exposure to AI PC market and edge-based workloads, but no direct involvement in this partnership announcement."
        }
      ]
    },
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
    "10DayAverageTradingVolume": 16.0773,
    "13WeekPriceReturnDaily": 32.9268,
    "26WeekPriceReturnDaily": 72.5594,
    "3MonthADReturnStd": 48.956093,
    "3MonthAverageTradingVolume": 17.71552,
    "52WeekHigh": 36.225,
    "52WeekHighDate": "2026-09-11",
    "52WeekLow": 17.56,
    "52WeekLowDate": "2026-02-25",
    "52WeekPriceReturnDaily": 17.9654,
    "5DayPriceReturnDaily": -0.0917,
    "assetTurnoverAnnual": 1.3238,
    "assetTurnoverTTM": 1.3763,
    "beta": 1.1855879,
    "bookValuePerShareAnnual": 15.3925,
    "bookValuePerShareQuarterly": 15.3925,
    "bookValueShareGrowth5Y": -3.46,
    "capexCagr5Y": 9.11,
    "cashFlowPerShareAnnual": 3.0402,
    "cashFlowPerShareQuarterly": 4.2437,
    "cashFlowPerShareTTM": 4.11043,
    "cashPerSharePerShareAnnual": 4.0065,
    "cashPerSharePerShareQuarterly": 4.5587,
    "currentDividendYieldTTM": 3.7133,
    "currentEv/freeCashFlowAnnual": 12.3141,
    "currentEv/freeCashFlowTTM": 8.8842,
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
    "enterpriseValue": 34479.566,
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
    "evEbitdaTTM": 9.9422,
    "evRevenueTTM": 0.5828,
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
    "marketCapitalization": 29488.566,
    "monthToDatePriceReturnDaily": 8.9274,
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
    "pb": 1.062,
    "pbAnnual": 0.8956,
    "pbQuarterly": 0.8956,
    "pcfShareAnnual": 7.9764,
    "pcfShareTTM": 6.3172,
    "peAnnual": 11.6602,
    "peBasicExclExtraTTM": 12.0312,
    "peExclExtraAnnual": 8.7772,
    "peExclExtraTTM": 12.0312,
    "peInclExtraTTM": 12.0312,
    "peNormalizedAnnual": 11.6602,
    "peTTM": 12.0312,
    "pegTTM": 2.95806,
    "pfcfShareAnnual": 10.5316,
    "pfcfShareTTM": 7.5982,
    "pretaxMargin5Y": 7.04,
    "pretaxMarginAnnual": 4.83,
    "pretaxMarginTTM": 4.73,
    "priceRelativeToS&P50013Week": 33.0301,
    "priceRelativeToS&P50026Week": 59.3489,
    "priceRelativeToS&P5004Week": 11.1701,
    "priceRelativeToS&P50052Week": 3.7154,
    "priceRelativeToS&P500Ytd": 36.1909,
    "psAnnual": 0.5333,
    "psTTM": 0.4984,
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
    "yearToDatePriceReturnDaily": 46.7684
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

## WBD
Trading candidate:
```json
{
  "symbol": "WBD",
  "score": 51.07,
  "direction": "LONG",
  "sector": "Communication Services",
  "components": {
    "market": 50.0,
    "sector": 52.88,
    "relative_strength": 50.68904505971235,
    "vwap": 100.0,
    "trend": 0.0,
    "volume": 27.206035971158553,
    "momentum": 54.788094813758676,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 51.73054672539525,
    "trend_acceleration": 25,
    "compression": 85.84197354308195,
    "volatility_contraction": 88.78390111854539,
    "volume_accumulation": 48.521922309254705,
    "breakout_distance": 36.00286020736506,
    "support_quality": 98.21237039685387,
    "momentum_improvement": 49.74418546531675,
    "early_setup_score": 54.13,
    "entry_timing_score": 54.13,
    "opportunity_score": 51.99,
    "extended": false,
    "return_5d": -0.3,
    "return_10d": -1.41,
    "return_20d": -0.96,
    "distance_to_breakout": 3.2,
    "atr_extension": -1.47
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
      "datetime": 1789736766,
      "headline": "Netflix Falls 4% as Wells Fargo Cuts Rating to Underweight With $57 Target; Disney Barely Budges",
      "id": 142255152,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WBD",
      "source": "Yahoo",
      "summary": "Wells Fargo just handed Netflix one of the street's most bearish ratings while a rival analyst pushed a price target nearly double that level, leaving investors to figure out which firm is reading the audience right before earnings arrive.",
      "url": "https://finnhub.io/api/news?id=2029674590d089dbb75fd17ad9c201a246aa296bfd3e76684befed48c695a40f"
    },
    {
      "category": "company",
      "datetime": 1789719201,
      "headline": "Relief Rally: Wall Street Decides a Hawkish Fed It Understands Beats a Fed It Doesn't",
      "id": 142245353,
      "image": "https://www.chartmill.com/images/uploads/THUMBNAILS_CHARTMILL_1000_528_4_fc48c1fc85.webp",
      "related": "WBD",
      "source": "ChartMill",
      "summary": "A day after the Federal Reserve's first rate hike in three years, US stocks rallied as yields eased and the tech names that had been sold hardest this week bounced back.",
      "url": "https://finnhub.io/api/news?id=ba02b2fc907acb035fced53dacc1e5cef6255a6e9bb64f62e530af3ea559ceb8"
    },
    {
      "category": "company",
      "datetime": 1789669680,
      "headline": "Paramount Is One of Today\u2019s Worst S&P 500 Stocks on a Warning Against Mega-Merger",
      "id": 142231723,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WBD",
      "source": "Yahoo",
      "summary": "Paramount Skydance  and  Warner Bros. Discovery  long-awaited merger has been at a standstill.  Barclays analysts led by Kannan Venkateshwar resumed coverage of both stocks, rating Warner Bros. at Equal Weight with a $28 price target and  Paramount  at Underweight with a $8 price target.  Venkateshwar said in a research note Thursday that while the proposed $110 billion merger could increase growth potential for the studios, it could introduce massive financial and operational risks that make the stock hard to value, and \u201ca moving target.\u201d",
      "url": "https://finnhub.io/api/news?id=17e40af79e0bf425478b864dc4fe032714dcd8b6c2fe3d175fbf07010b096274"
    },
    {
      "category": "company",
      "datetime": 1789665391,
      "headline": "Federal Communications Commission Approves Foreign Funding For Paramount Warner Brothers Merger Deal",
      "id": 142256117,
      "image": "",
      "related": "WBD",
      "source": "Benzinga",
      "summary": "https://www.fcc.gov/document/media-bureau-grants-paramount-global-section-310b4-pdr",
      "url": "https://finnhub.io/api/news?id=0200d3632681a07bfeda96abaf4e55a2d3fd22d31575dc8d96ae22615eb273ef"
    },
    {
      "category": "company",
      "datetime": 1789656029,
      "headline": "How Is Warner Bros. Discovery's Stock Performance Compared to Other Entertainment Stocks",
      "id": 142233450,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WBD",
      "source": "Yahoo",
      "summary": "Warner Bros. Discovery has rallied other entertainment stocks, yet analysts remain skeptical about the stock\u2019s outlook.",
      "url": "https://finnhub.io/api/news?id=e87feaecfa908ae89ee946aa190070bb58340688f02bf1b94367710e9e85bb7f"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 16.80454,
    "13WeekPriceReturnDaily": 4.6217,
    "26WeekPriceReturnDaily": 2.3332,
    "3MonthADReturnStd": 18.885332,
    "3MonthAverageTradingVolume": 20.899,
    "52WeekHigh": 30,
    "52WeekHighDate": "2025-12-12",
    "52WeekLow": 17.08,
    "52WeekLowDate": "2025-10-10",
    "52WeekPriceReturnDaily": 53.8082,
    "5DayPriceReturnDaily": -0.461,
    "assetTurnoverAnnual": 0.3726,
    "assetTurnoverTTM": 0.3651,
    "beta": 1.6468972,
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
    "currentEv/freeCashFlowAnnual": 32.0771,
    "currentEv/freeCashFlowTTM": 45.4377,
    "currentRatioAnnual": 1.0565,
    "currentRatioQuarterly": 0.7767,
    "dividendIndicatedAnnual": 0,
    "dividendPerShareTTM": null,
    "ebitdPerShareAnnual": 3.7024,
    "ebitdPerShareTTM": 1.4728,
    "ebitdaCagr5Y": 19.91,
    "ebitdaInterimCagr5Y": 3.37,
    "enterpriseValue": 99054.12,
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
    "evEbitdaTTM": 26.8294,
    "evRevenueTTM": 2.7427,
    "focfCagr5Y": 5.73,
    "grossMargin5Y": 46.05,
    "grossMarginAnnual": 44,
    "grossMarginTTM": 47.67,
    "longTermDebt/equityAnnual": 0.9028,
    "longTermDebt/equityQuarterly": 0.9297,
    "marketCapitalization": 70400.12,
    "monthToDatePriceReturnDaily": -1.6123,
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
    "pb": 2.1439,
    "pbAnnual": 1.9886,
    "pbQuarterly": 2.0355,
    "pcfShareAnnual": 16.3001,
    "pcfShareTTM": 20.5668,
    "peAnnual": 96.8365,
    "peBasicExclExtraTTM": null,
    "peExclExtraTTM": null,
    "peInclExtraTTM": null,
    "peNormalizedAnnual": 96.8365,
    "peTTM": null,
    "pfcfShareAnnual": 22.798,
    "pfcfShareTTM": 26.5061,
    "pretaxMargin5Y": -9.73,
    "pretaxMarginAnnual": 4.39,
    "pretaxMarginTTM": -10.44,
    "priceRelativeToS&P50013Week": 4.725,
    "priceRelativeToS&P50026Week": -10.8773,
    "priceRelativeToS&P5004Week": 0.3394,
    "priceRelativeToS&P50052Week": 39.5582,
    "priceRelativeToS&P500Ytd": -13.1799,
    "psAnnual": 1.8876,
    "psTTM": 1.9493,
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
    "yearToDatePriceReturnDaily": -2.6024
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

## AMZN
Trading candidate:
```json
{
  "symbol": "AMZN",
  "score": 50.16,
  "direction": "WATCH",
  "sector": "Unknown",
  "components": {
    "market": 50.0,
    "sector": 50.0,
    "relative_strength": 42.657319941997876,
    "vwap": 100.0,
    "trend": 0.0,
    "volume": 31.590819833306465,
    "momentum": 55.2803738317757,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 58.55,
    "extension": 100.0,
    "relative_strength_acceleration": 49.937766727742655,
    "trend_acceleration": 25,
    "compression": 41.29329708003327,
    "volatility_contraction": 79.52814415753298,
    "volume_accumulation": 43.480515488355174,
    "breakout_distance": 0.5398589273753629,
    "support_quality": 69.34231784686921,
    "momentum_improvement": 47.69529403942807,
    "early_setup_score": 38.01,
    "entry_timing_score": 38.01,
    "opportunity_score": 46.51,
    "extended": false,
    "return_5d": -1.18,
    "return_10d": -1.99,
    "return_20d": -2.41,
    "distance_to_breakout": 4.97,
    "atr_extension": -0.54
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
      "datetime": 1789732467,
      "headline": "Rates Could Reach 4.5% On AI Spending, And Semiconductors Get Paid First",
      "id": 142257616,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/2292977505/image_2292977505.jpg?io=getty-c-w1536",
      "related": "AMZN",
      "source": "SeekingAlpha",
      "summary": "iShares Semiconductor ETF and VanEck Semiconductor ETF semiconductor funds remain Buys as AI-driven capex fuels demand. Click for more on SMH and SOXX.",
      "url": "https://finnhub.io/api/news?id=f04479a0d80616a98969ab04c76aeb7c4a6fbb2d9e4ad2bcf5e0391c8be6c99a"
    },
    {
      "category": "company",
      "datetime": 1789729200,
      "headline": "Prysmian and Rio Tinto Announce First Electrical Cables Made with ELYSIS(R) Technology Aluminum Contracted for Installation at Amazon Data Center",
      "id": 142251485,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AMZN",
      "source": "Yahoo",
      "summary": "HIGHLAND HEIGHTS, KY / ACCESS Newswire / September 18, 2026 / , the leading provider of solutions for energy and digital connections based in the Cincinnati, Ohio, metropolitan area, in partnership with Rio Tinto, is pleased to announce a collaboration with Amazon in which electrical cables produced with ELYSIS\u00ae aluminum have been contracted for installation in an Amazon data center near Columbus, Ohio. This represents the first known use of inert-anode-smelted, low-carbon aluminum in a data cen",
      "url": "https://finnhub.io/api/news?id=7202539dbf0c4ab8b8a24e51e97cd98b917c0d25c012a05357b911a1b5205094"
    },
    {
      "category": "company",
      "datetime": 1789728313,
      "headline": "\u2018Big Short\u2019 Investor Michael Burry Blasts Economic \u2018Bubbles\u2019 Enriching the Few at \u2018Obscene Rates\u2019",
      "id": 142252975,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AMZN",
      "source": "Yahoo",
      "summary": "\u201cBig Short\u201d investor Michael Burry criticized the economic \u201cbubbles\u201d that he believes are facilitating a wealth transfer to a select few. In a post on X late Tuesday, he criticized the system for creating such bubbles, which he sees as...",
      "url": "https://finnhub.io/api/news?id=d4bb671d8a603a6881691f4cf6aed2804cd6dc55c11424e9c75811351a589534"
    },
    {
      "category": "company",
      "datetime": 1789725154,
      "headline": "AI Capex Boom Risks 'Massive Capital Destruction' in the US, Warns Veteran Market Strategist: 'You Could Get Some News Item That Suddenly\u2026'",
      "id": 142256118,
      "image": "https://cdn.benzinga.com/files/images/story/2026/09/18/Artificial-Intelligence-Analyzing-Global.jpg?width=2048&height=1536",
      "related": "AMZN",
      "source": "Benzinga",
      "summary": "Jefferies\u2019 Chris Wood warns trillion-dollar AI spending could trigger massive capital destruction as hyperscalers turn to debt.",
      "url": "https://finnhub.io/api/news?id=d9666453f9b9939966f0d0496d4bc9aade63cd9fe56afd16c76da8eef80a98c7"
    },
    {
      "category": "company",
      "datetime": 1789722508,
      "headline": "Generac: Data Center Business Takes Off After Amazon Deal",
      "id": 142254610,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/2286378241/image_2286378241.jpg?io=getty-c-w1536",
      "related": "AMZN",
      "source": "SeekingAlpha",
      "summary": "Generac Holdings' July data center backlog was $1.6 billion and excluded Amazon's delivery expectations. Find out why GNRC stock is a buy.",
      "url": "https://finnhub.io/api/news?id=674a2912ca3a3e7fb372d9d42603708ab223696552dd5cade4d96839896d6842"
    }
  ],
  "polygon_news": [
    {
      "id": "eedb3480bf35f1fb1a0b8ace4e98012cbcf6d2a6e6cf539f6fc985557ee91900",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Home Depot vs. Spotify Technology: Which Consumer Stock Is a Better Buy in 2026?",
      "author": "Sara Appino",
      "published_utc": "2026-09-18T12:05:01Z",
      "article_url": "https://www.fool.com/coverage/better-buy/2026/09/18/home-depot-vs-spotify-technology-which-consumer-stock-is-a-better-buy-in-2026/?source=iedfolrf0000001",
      "tickers": [
        "HD",
        "SPOT",
        "AAPL",
        "AMZN"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F3caa0e2607e9485862b0d89e5f6f6be899ae6c41-1200x800.png%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "The article compares Home Depot and Spotify Technology as investment options for 2026. Home Depot, the dominant home improvement retailer, offers steady returns and a 3.07% dividend yield but faces headwinds from a sluggish housing market. Spotify, the global audio streaming leader, demonstrates faster revenue growth (9.7%), record gross margins (32.7%), and improved profitability, making it the author's preferred choice for long-term investors seeking growth exposure.",
      "keywords": [
        "Home Depot",
        "Spotify Technology",
        "stock comparison",
        "consumer stocks",
        "investment analysis",
        "valuation metrics",
        "revenue growth",
        "housing market",
        "streaming services"
      ],
      "insights": [
        {
          "ticker": "HD",
          "sentiment": "neutral",
          "sentiment_reasoning": "Home Depot is described as a dependable, dominant retailer with a loyal customer base and reliable dividend (3.07% yield). However, it faces headwinds from a sluggish housing market and reduced consumer spending on large-ticket projects. The company shows modest revenue growth (3.2%) and higher leverage (5.1x debt-to-equity), making it less attractive than Spotify for growth-focused investors."
        },
        {
          "ticker": "SPOT",
          "sentiment": "positive",
          "sentiment_reasoning": "Spotify demonstrates strong fundamentals with accelerating revenue growth (9.7%), record gross margins (32.7%), and improved net margins (12.9%). The company crossed 300 million premium subscribers, operates with conservative debt (0.3x debt-to-equity), and generates substantial free cash flow ($3.3 billion). The author explicitly recommends Spotify as the better buy for long-term investors due to its superior growth trajectory and multiple monetization opportunities."
        },
        {
          "ticker": "AAPL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Apple is mentioned as a competitive threat to Spotify in the streaming market, with the ability to bundle music services with other products. No direct investment recommendation or analysis is provided."
        },
        {
          "ticker": "AMZN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Amazon is mentioned as a deep-pocketed competitor to Spotify in the streaming industry. No direct investment recommendation or analysis is provided."
        }
      ]
    },
    {
      "id": "34f54c338ebaa95a835993909c6542bd8a55810c998c60772ae29b581e460ed2",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Buy 3 Neuberger Funds With Diverse Investment Strategies",
      "author": "Na",
      "published_utc": "2026-09-18T10:24:00Z",
      "article_url": "https://www.zacks.com/stock/news/2991741/buy-3-neuberger-funds-with-diverse-investment-strategies?cid=CS-ZC-FT-mutual_fund_commentary-2991741",
      "tickers": [
        "INTC",
        "SCCO",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "AMZN",
        "NVDA",
        "NET",
        "VRT",
        "DDOG"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/articles/main/09/344.jpg",
      "description": "Stock markets showed strong recovery with the Nasdaq positioned to close higher for the week and the S&P 500 following closely behind. The article highlights three Neuberger Berman mutual funds recommended for long-term investment, all with Zacks Rank #1 ratings and strong historical returns.",
      "keywords": [
        "stock market rally",
        "Nasdaq",
        "S&P 500",
        "mutual funds",
        "Neuberger Berman",
        "long-term investment"
      ],
      "insights": [
        {
          "ticker": "INTC",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a top holding (4.2%) in NBPTX fund with no specific performance commentary"
        },
        {
          "ticker": "SCCO",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a top holding (3.5%) in NBPTX fund with no specific performance commentary"
        },
        {
          "ticker": "GOOG",
          "sentiment": "positive",
          "sentiment_reasoning": "Top holding (10.5%) in NBSRX fund which has strong 3-year (23.9%) and 5-year (13.5%) annualized returns"
        },
        {
          "ticker": "GOOGL",
          "sentiment": "positive",
          "sentiment_reasoning": "Top holding (10.5%) in NBSRX fund which has strong 3-year (23.9%) and 5-year (13.5%) annualized returns"
        },
        {
          "ticker": "GOOGM",
          "sentiment": "positive",
          "sentiment_reasoning": "Top holding (10.5%) in NBSRX fund which has strong 3-year (23.9%) and 5-year (13.5%) annualized returns"
        },
        {
          "ticker": "GOOGN",
          "sentiment": "positive",
          "sentiment_reasoning": "Top holding (10.5%) in NBSRX fund which has strong 3-year (23.9%) and 5-year (13.5%) annualized returns"
        },
        {
          "ticker": "AMZN",
          "sentiment": "positive",
          "sentiment_reasoning": "Significant holding (8.6%) in NBSRX fund with strong historical performance metrics"
        },
        {
          "ticker": "NVDA",
          "sentiment": "positive",
          "sentiment_reasoning": "Major holding (8.1%) in NBSRX fund which demonstrates strong 3-year and 5-year returns"
        },
        {
          "ticker": "NET",
          "sentiment": "neutral",
          "sentiment_reasoning": "Top holding (4.9%) in NMGAX mid-cap growth fund with modest 3-year returns (12.1%)"
        },
        {
          "ticker": "VRT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Holding (3.9%) in NMGAX fund with no specific performance commentary"
        },
        {
          "ticker": "DDOG",
          "sentiment": "neutral",
          "sentiment_reasoning": "Holding (3.9%) in NMGAX fund with no specific performance commentary"
        }
      ]
    },
    {
      "id": "3b3ff30eb370e64a8b42c87d52565da0b6e27ee82bdfc8e95a8ebe9f28916d5e",
      "publisher": {
        "name": "GlobeNewswire Inc.",
        "homepage_url": "https://www.globenewswire.com",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/globenewswire.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/globenewswire.ico"
      },
      "title": "Sports Fan Analytics & Trends Study in the United States Examines U.S. Sports Fan Behavior Across 18 Sport Categories",
      "author": "Researchandmarkets.Com",
      "published_utc": "2026-09-18T08:20:00Z",
      "article_url": "https://www.globenewswire.com/news-release/2026/09/18/3364522/28124/en/sports-fan-analytics-trends-study-in-the-united-states-examines-u-s-sports-fan-behavior-across-18-sport-categories.html",
      "tickers": [
        "NKE",
        "KO",
        "AMZN",
        "AAPL"
      ],
      "image_url": "https://ml.globenewswire.com/Resource/Download/908fb457-7f8e-4a08-9081-5565e3dfb3d7",
      "description": "A comprehensive sports fan analytics study based on 6,666 U.S. consumers surveyed in January 2024 examines fandom trends across 18 sports categories, measuring viewership, attendance, social media engagement, sponsorship influence, and mobile consumption. The study identifies major brands and provides insights relevant to advertisers, sponsors, leagues, and media companies seeking to understand evolving fan behavior across streaming, mobile, and social channels.",
      "keywords": [
        "sports fandom",
        "fan behavior analytics",
        "sponsorship influence",
        "mobile consumption",
        "social media engagement",
        "fantasy sports",
        "sports betting",
        "consumer demographics",
        "viewership trends"
      ],
      "insights": [
        {
          "ticker": "NKE",
          "sentiment": "positive",
          "sentiment_reasoning": "Nike is identified as a major brand with significant influence in sports sponsorship and consumer product preferences, indicating strong market presence and relevance in sports fan engagement."
        },
        {
          "ticker": "KO",
          "sentiment": "positive",
          "sentiment_reasoning": "Featured as a key sponsor with established influence in sports marketing and consumer brand preferences among sports fans."
        },
        {
          "ticker": "AMZN",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as a major player in sports media consumption and streaming channels, benefiting from the shift in fan engagement toward digital platforms."
        },
        {
          "ticker": "AAPL",
          "sentiment": "positive",
          "sentiment_reasoning": "Listed among key companies in mobile device consumption patterns, positioning it well for sports fan engagement through mobile and streaming platforms."
        }
      ]
    },
    {
      "id": "2a003bc767d263993d97a04ff6da743be7200ab9cdd24b299687ba19b587b25f",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Why Generac Stock Soared Today",
      "author": "Joe Tenebruso",
      "published_utc": "2026-09-17T23:21:07Z",
      "article_url": "https://www.fool.com/investing/2026/09/17/why-generac-stock-soared-today/?source=iedfolrf0000001",
      "tickers": [
        "GNRC",
        "AMZN"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F887949%2Fgenerator-gettyimages-1511329781-1801x1148-0ad1c34.jpg&w=1200&op=resize",
      "description": "Generac's stock surged 18.34% after announcing an $8 billion long-term supply agreement with Amazon to provide backup power generators for AI data centers. Amazon will receive a warrant to purchase over 1.6 million Generac shares, with initial deliveries projected at $2.4 billion in 2027-2028. The partnership is seen as a major vote of confidence that could lead to additional deals with other cloud computing companies.",
      "keywords": [
        "backup power generators",
        "AI data centers",
        "supply agreement",
        "warrant",
        "cloud computing",
        "stock surge"
      ],
      "insights": [
        {
          "ticker": "GNRC",
          "sentiment": "positive",
          "sentiment_reasoning": "Secured a major $8 billion long-term supply deal with Amazon for AI data center backup power, demonstrating strong market demand and providing significant revenue visibility. The partnership validates product quality and could attract additional customers from other cloud computing giants."
        },
        {
          "ticker": "AMZN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Securing reliable backup power supply for data centers is operationally important but represents a routine business transaction. The warrant investment of ~$340 million is modest relative to Amazon's scale and is a strategic hedge rather than a major financial commitment."
        }
      ]
    },
    {
      "id": "4d178b942e73ff460c1de8301d3ecf8f3003a740b735900480e9440ec552b947",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Generac Lands $2.4 Billion Generator Deal With Amazon",
      "author": "Patrick Sanders",
      "published_utc": "2026-09-17T17:10:07Z",
      "article_url": "https://www.fool.com/investing/2026/09/17/generac-lands-24-billion-generator-deal-with-amazon/?source=iedfolrf0000001",
      "tickers": [
        "GNRC",
        "AMZN",
        "PINS",
        "SNOW",
        "MCO"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F90b7aa76e60efd23e20986247672d77905305e52-1200x800.png%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "Generac signed a long-term agreement with Amazon to supply backup generators for its data centers, with initial deliveries totaling $2.4 billion in 2027-2028 and potential additional purchases reaching $8 billion through 2033. Amazon received a warrant for up to 1.69 million Generac shares. The deal supports Amazon's expanding AI infrastructure needs, with Generac stock surging 20% on the announcement.",
      "keywords": [
        "backup generators",
        "data centers",
        "AI infrastructure",
        "long-term agreement",
        "cloud computing",
        "power supply"
      ],
      "insights": [
        {
          "ticker": "GNRC",
          "sentiment": "positive",
          "sentiment_reasoning": "Major $2.4-8 billion deal with Amazon validates Generac's position as critical AI infrastructure supplier. Stock up 20%, company raising profit margins, and securing long-term revenue through 2033 demonstrates strong growth trajectory in high-demand data center backup power market."
        },
        {
          "ticker": "AMZN",
          "sentiment": "positive",
          "sentiment_reasoning": "Securing reliable backup power for data centers is essential for maintaining AWS market leadership and supporting rapidly growing AI business ($25B+ run rate). Deal demonstrates strategic execution in building out AI infrastructure, though stock only up 2% suggesting market already priced in infrastructure investments."
        },
        {
          "ticker": "PINS",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a customer of Amazon's AI services but no specific details provided about the relationship or impact."
        },
        {
          "ticker": "SNOW",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a customer of Amazon's AI services but no specific details provided about the relationship or impact."
        },
        {
          "ticker": "MCO",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a customer of Amazon's AI services but no specific details provided about the relationship or impact."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 30.04339,
    "13WeekPriceReturnDaily": -0.0244,
    "26WeekPriceReturnDaily": 17.3865,
    "3MonthADReturnStd": 43.372677,
    "3MonthAverageTradingVolume": 44.86953,
    "52WeekHigh": 287.2,
    "52WeekHighDate": "2026-08-03",
    "52WeekLow": 196,
    "52WeekLowDate": "2026-02-17",
    "52WeekPriceReturnDaily": 5.0887,
    "5DayPriceReturnDaily": -2.3542,
    "assetTurnoverAnnual": 0.8764,
    "assetTurnoverTTM": 0.872,
    "beta": 1.5078225,
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
    "currentEv/freeCashFlowAnnual": 362.0083,
    "currentEv/freeCashFlowTTM": 115.2247,
    "currentRatioAnnual": 1.0508,
    "currentRatioQuarterly": 1.0331,
    "dividendIndicatedAnnual": 0,
    "dividendPerShareTTM": null,
    "ebitdPerShareAnnual": 7.4621,
    "ebitdPerShareTTM": 15.5375,
    "ebitdaCagr5Y": 28.12,
    "ebitdaInterimCagr5Y": 24.69,
    "enterpriseValue": 2785653.5,
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
    "evEbitdaTTM": 16.4917,
    "evRevenueTTM": 3.5912,
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
    "marketCapitalization": 2708551.5,
    "monthToDatePriceReturnDaily": -5.3162,
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
    "pb": 4.9102,
    "pbAnnual": 6.0027,
    "pbQuarterly": 4.6479,
    "pcfShareAnnual": 19.4142,
    "pcfShareTTM": 16.7813,
    "peAnnual": 34.8726,
    "peBasicExclExtraTTM": 20.0217,
    "peExclExtraTTM": 20.0217,
    "peInclExtraTTM": 20.0217,
    "peNormalizedAnnual": 34.8726,
    "peTTM": 20.0217,
    "pegTTM": 1.36953,
    "pfcfShareAnnual": 351.9885,
    "pfcfShareTTM": 172.5302,
    "pretaxMargin5Y": 7.57,
    "pretaxMarginAnnual": 13.57,
    "pretaxMarginTTM": 22.62,
    "priceRelativeToS&P50013Week": 0.0789,
    "priceRelativeToS&P50026Week": 4.176,
    "priceRelativeToS&P5004Week": -5.5265,
    "priceRelativeToS&P50052Week": -9.1613,
    "priceRelativeToS&P500Ytd": -4.0183,
    "psAnnual": 3.778,
    "psTTM": 3.4918,
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
    "yearToDatePriceReturnDaily": 6.5592
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

## PFE
Trading candidate:
```json
{
  "symbol": "PFE",
  "score": 48.95,
  "direction": "WATCH",
  "sector": "Healthcare",
  "components": {
    "market": 50.0,
    "sector": 52.85,
    "relative_strength": 47.205946625640436,
    "vwap": 100.0,
    "trend": 0.0,
    "volume": 12.955232586001872,
    "momentum": 53.677500902853005,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 50.17947666925673,
    "trend_acceleration": 25,
    "compression": 56.95557174071379,
    "volatility_contraction": 79.92924773696805,
    "volume_accumulation": 36.54236190813812,
    "breakout_distance": 0.0,
    "support_quality": 100.0,
    "momentum_improvement": 47.97153397258701,
    "early_setup_score": 40.47,
    "entry_timing_score": 40.47,
    "opportunity_score": 46.41,
    "extended": false,
    "return_5d": -0.83,
    "return_10d": -4.69,
    "return_20d": -1.29,
    "distance_to_breakout": 5.7,
    "atr_extension": -1.28
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
      "datetime": 1789723352,
      "headline": "5 Undervalued Oncology Stocks Wall Street Is Overlooking",
      "id": 142254787,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/1630128517/image_1630128517.jpg?io=getty-c-w1536",
      "related": "PFE",
      "source": "SeekingAlpha",
      "summary": "Oncology spending may hit $441B by 2029 as growth slows from generics\u00e2\u0080\u0094see 5 underappreciated cancer stocks with catalysts and upside. Click for the picks.",
      "url": "https://finnhub.io/api/news?id=9e36abb4736760f20f2560d69abeba3d6a402c6a5b6c3ebfc2d1ef95ab93e692"
    },
    {
      "category": "company",
      "datetime": 1789674293,
      "headline": "Sector Update: Healthcare Stocks Higher Late Afternoon",
      "id": 142233375,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "Healthcare stocks rose late Thursday afternoon, with the NYSE Healthcare Index adding 0.8% and the S",
      "url": "https://finnhub.io/api/news?id=f89cf0c26810c8cf0052e32ab1027078a1c19166d78c766418c836337f510874"
    },
    {
      "category": "company",
      "datetime": 1789672646,
      "headline": "Can Volume Keep Covering Eli Lilly's Price Cuts?",
      "id": 142232756,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "Eli Lilly (LLY) grew revenue 48% in Q2 2026, driven by Zepbound and Mounjaro. A more understated metric for investors to watch is pricing. Lilly's U.S. price fell 9% from a year earlier, excluding changes to rebate estimates. So far, volume covers that cut. The risk is the quarter it cannot.",
      "url": "https://finnhub.io/api/news?id=42e646b3db8ab4aab5465720745cba226c0c283d0cc8963fdf0343cf6a133d9f"
    },
    {
      "category": "company",
      "datetime": 1789661847,
      "headline": "How Much Do You Really Need Invested to Replace a $130,000 Salary With Dividends?",
      "id": 142231872,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "The yield you chase to replace a six-figure salary determines far more than how much capital you need. It quietly sets your exposure to leverage, dividend cuts, and an NAV that can quietly bleed out before you notice.",
      "url": "https://finnhub.io/api/news?id=6ac0c701f01255baa3df61a2fbf5b827348717fda92c71734c9a6128fef4c921"
    },
    {
      "category": "company",
      "datetime": 1789647089,
      "headline": "What Happens To AbbVie Stock If SKYRIZI Slows Down?",
      "id": 142223863,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "AbbVie (ABBV) is trading within about one percent of its 52-week high after gaining roughly 24% over the past year, well ahead of the S&P 500. That price rests on two drugs, SKYRIZI above all, growing faster than 20% year over year while the company's older medicines shrink. The biggest risk to the stock makes no noise. It is the chance that this engine slows while the price assumes it cannot.",
      "url": "https://finnhub.io/api/news?id=dc4cbf8b69fbadfb93aa4d383979cd3fcb3a5cf28f9596c1e165bded9540a7e2"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 30.01268,
    "13WeekPriceReturnDaily": 5.6154,
    "26WeekPriceReturnDaily": 2.2338,
    "3MonthADReturnStd": 22.17706,
    "3MonthAverageTradingVolume": 39.36712,
    "52WeekHigh": 29.21,
    "52WeekHighDate": "2026-09-03",
    "52WeekLow": 23.58,
    "52WeekLowDate": "2025-09-25",
    "52WeekPriceReturnDaily": 14.8954,
    "5DayPriceReturnDaily": -0.6872,
    "assetTurnoverAnnual": 0.3006,
    "assetTurnoverTTM": 0.3086,
    "beta": 0.2816522,
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
    "monthToDatePriceReturnDaily": -3.5137,
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
    "priceRelativeToS&P50013Week": 5.7187,
    "priceRelativeToS&P50026Week": -10.9767,
    "priceRelativeToS&P5004Week": -0.8103,
    "priceRelativeToS&P50052Week": 0.6454,
    "priceRelativeToS&P500Ytd": -0.2964,
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
    "yearToDatePriceReturnDaily": 10.2811
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