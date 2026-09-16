# OpenClaw Candidate Research Handoff

Review each candidate using the supplied trading data and evidence packet. Do not place orders. Return only JSON in this format:

```json
{"research":[{"symbol":"MSFT","research_score":0,"conviction":"Low","catalysts":[],"risks":[],"summary":""}]}
```

Use a 0-100 research score. Do not invent facts or infer fundamentals from technical data. Treat missing data as uncertainty, name the missing source in risks, and use only dated/source-labelled news, earnings, filings, or fundamentals. Keep Python's technical score authoritative; this research score is a 30% adjustment.

## KHC
Trading candidate:
```json
{
  "symbol": "KHC",
  "score": 48.93,
  "direction": "WATCH",
  "sector": "Consumer Staples",
  "components": {
    "market": 50.0,
    "sector": 52.54,
    "relative_strength": 58.159020865899315,
    "vwap": 84.0648181448806,
    "trend": 0.0,
    "volume": 15.455551175716648,
    "momentum": 53.25005078204353,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 53.19004549700487,
    "trend_acceleration": 25,
    "compression": 4.009671569615193,
    "volatility_contraction": 69.65545033246022,
    "volume_accumulation": 84.68392003198637,
    "breakout_distance": 0.0,
    "support_quality": 78.64195043320568,
    "momentum_improvement": 53.270195826362624,
    "early_setup_score": 34.54,
    "entry_timing_score": 34.54,
    "opportunity_score": 44.61,
    "extended": false,
    "return_5d": 0.81,
    "return_10d": -4.08,
    "return_20d": -0.02,
    "distance_to_breakout": 5.86,
    "atr_extension": -0.6
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
      "datetime": 1789556400,
      "headline": "Capri Sun Tests Its Biggest Pouch Yet \u2013 and Fans Could Help Make it Permanent",
      "id": 142194241,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "KHC",
      "source": "Yahoo",
      "summary": "CHICAGO, September 16, 2026--Capri Sun is saying goodbye to summer in a BIG way! As generations of Capri Sun fans have grown up, one request has only gotten louder: bigger pouches. In recent years, nearly 80% of fan requests ask for a bigger size.1 Now, just in time for one last supersized sip of summer, Capri Sun is answering the call and putting that demand to the test with the Capri Sun Big Pouch \u2014 the biggest Capri Sun pouch ever tested, standing nearly nine inches tall, twice as wide and no",
      "url": "https://finnhub.io/api/news?id=4e0c2cc75ebe80631a87a8e260a3a1ed24e08633f898d39d8aa57e9bbeedadf5"
    },
    {
      "category": "company",
      "datetime": 1789478817,
      "headline": "Philadelphia cream cheese launches 3 new flavors in 2026",
      "id": 142162298,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "KHC",
      "source": "Yahoo",
      "summary": "Kraft Heinz is increasing spending on the Philadelphia brand by 63% this year as part of a $700 million push to revive its portfolio",
      "url": "https://finnhub.io/api/news?id=6c4be2da96a7e9e6ea8f013e7b4419ba29875038a616764bca1f91ddfb194a3c"
    },
    {
      "category": "company",
      "datetime": 1789470000,
      "headline": "Philadelphia Turns Up the Heat with its First-Ever Sweet Heat Cream Cheese in the United States in Partnership with Mike's Hot Honey\u00ae",
      "id": 142160601,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "KHC",
      "source": "Yahoo",
      "summary": "PITTSBURGH & CHICAGO, September 15, 2026--As temperatures cool off, Philadelphia is turning up the heat on a familiar favorite with the introduction of Philadelphia Mike\u2019s Hot Honey Whipped Cream Cheese. In a collaboration with America's original and leading hot honey brand, the craveable new spread swirls the iconic sweet heat of Mike\u2019s Hot Honey into Philadelphia\u2019s light and fluffy whipped cream cheese, bringing a little kick to everything from bagels and charcuterie boards to pizza. Available",
      "url": "https://finnhub.io/api/news?id=76032007497f8f950d14b77848bafc529a3c083570b36f2bb81096ab7c0d26b3"
    },
    {
      "category": "company",
      "datetime": 1789467015,
      "headline": "Kraft Heinz (KHC) Stock Looks Reasonable Following Oscar Mayer Fix Effort",
      "id": 142160602,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "KHC",
      "source": "Yahoo",
      "summary": "Kraft Heinz has been working through a mix of pressures on its core brands and shoppers' budgets, while the share price has drifted rather than surged. That combination puts a sharp focus on whether the current US$24.27 price is adequately backed by the packaged food giant's sales base. Over the past 3 years the stock has fallen about 14%, which puts the spotlight on whether the business now generates enough revenue to support even this lower share price. Management is trying to repair sales...",
      "url": "https://finnhub.io/api/news?id=c56c29ebad74bf07b74b8ba76d57fa73a9e2ce310bbdb4f0bfbd9500d3c39e23"
    },
    {
      "category": "company",
      "datetime": 1789452001,
      "headline": "Kraft Heinz bets on more flavors for Philadelphia cream cheese as it looks to revive brands",
      "id": 142165195,
      "image": "https://image.cnbcfm.com/api/v1/image/108362556-1789404347324-Philadelphia_Fall_Flavors_Image.jpg?v=1789416588&w=1920&h=1080",
      "related": "KHC",
      "source": "CNBC",
      "summary": "Philadelphia will release more cream cheese flavors as part of Kraft Heinz's turnaround.",
      "url": "https://finnhub.io/api/news?id=d1835f9be091d2ab28fb0b10b81740bb409246ab3d3c67b1c867eb3ba5a3b353"
    }
  ],
  "polygon_news": [
    {
      "id": "c613430c23c5e30703b7f3a3eaa76bdc47e0ac97e8b4266e4d4bd36f21645274",
      "publisher": {
        "name": "GlobeNewswire Inc.",
        "homepage_url": "https://www.globenewswire.com",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/globenewswire.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/globenewswire.ico"
      },
      "title": "Baby Food & Infant Formula Market Size to Reach USD 74.30 Billion by 2035 | Report by SNS Insider",
      "author": "Sns Insider",
      "published_utc": "2026-09-04T22:30:00Z",
      "article_url": "https://www.globenewswire.com/news-release/2026/09/04/3356839/0/en/baby-food-infant-formula-market-size-to-reach-usd-74-30-billion-by-2035-report-by-sns-insider.html",
      "tickers": [
        "ABT",
        "NSRGY",
        "DANOY",
        "KHC"
      ],
      "image_url": "https://ml.globenewswire.com/Resource/Download/d6272c2e-d204-41b8-b545-a6e2e24f85c2",
      "description": "The global Baby Food and Infant Formula Market was valued at USD 40.37 billion in 2025 and is projected to reach USD 74.30 billion by 2035, growing at a CAGR of 6.29%. Growth is driven by urbanization, increasing parental health consciousness, demand for organic/premium products, and e-commerce expansion. However, recent product recalls by major manufacturers highlight safety concerns in the industry.",
      "keywords": [
        "baby food market",
        "infant formula",
        "market growth",
        "organic products",
        "e-commerce distribution",
        "product recalls",
        "Asia Pacific",
        "North America"
      ],
      "insights": [
        {
          "ticker": "ABT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as a leading market player with no specific negative or positive developments mentioned in the article."
        },
        {
          "ticker": "NSRGY",
          "sentiment": "negative",
          "sentiment_reasoning": "Company initiated a mass infant formula recall across Europe, Asia, and South America in 2026 due to cereulide toxin contamination, which poses significant reputational and financial risks."
        },
        {
          "ticker": "DANOY",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as a leading market player with no specific developments mentioned in the article."
        },
        {
          "ticker": "KHC",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as a leading market player with no specific developments mentioned in the article."
        }
      ]
    },
    {
      "id": "0e27613ee60ad4212e660ec02d1d3629346b298119e9859e41f1aa684e49e731",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Kraft Heinz (KHC) Up 1.8% Since Last Earnings Report: Can It Continue?",
      "author": "Zacks.Com",
      "published_utc": "2026-09-04T15:30:27Z",
      "article_url": "https://www.zacks.com/stock/news/2985284/kraft-heinz-khc-up-1-8-since-last-earnings-report-can-it-continue?cid=CS-ZC-FT-realtime_blog-2985284",
      "tickers": [
        "KHC",
        "CHEF"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default172.jpg",
      "description": "Kraft Heinz beat Q2 2026 earnings estimates with adjusted EPS of 56 cents versus consensus of 53 cents, but organic sales fell 1.3% year-over-year. The company raised its 2026 organic sales guidance to a decline of 0.5-2% from prior guidance of 1.5-3.5%, though adjusted operating income guidance worsened to a 16-18% decline. Estimates have trended downward since the earnings release, and the stock carries a Zacks Rank #3 (Hold) with an expected in-line return.",
      "keywords": [
        "earnings report",
        "organic sales decline",
        "guidance raised",
        "volume/mix headwinds",
        "pricing actions",
        "Zacks Rank Hold",
        "estimate revisions downward"
      ],
      "insights": [
        {
          "ticker": "KHC",
          "sentiment": "negative",
          "sentiment_reasoning": "While the company beat EPS estimates and raised organic sales guidance, adjusted earnings fell 18.8% YoY, organic sales declined 1.3%, and adjusted operating income guidance was lowered to a 16-18% decline. Post-earnings, consensus estimates have shifted downward by 8.25%, and the stock received a Zacks Rank #3 (Hold) with expectations for in-line returns. Volume/mix pressures and inflationary headwinds outweighed pricing benefits."
        },
        {
          "ticker": "CHEF",
          "sentiment": "positive",
          "sentiment_reasoning": "The company reported strong results with revenues up 12.9% YoY and EPS of $0.78 versus $0.52 a year ago. Consensus estimates have increased 11.7% over the last 30 days, and the stock carries a Zacks Rank #1 (Strong Buy) with a VGM Score of B. The stock has gained 4.7% over the past month, outperforming Kraft Heinz."
        }
      ]
    },
    {
      "id": "cb031be9f79315f1aafeabfffcc76146d814794b6f5989049fd03742e75a2449",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Better Consumer Staples ETF: the iShares IYK vs. First Trust's Food and Beverage-Focused FTXG",
      "author": "Robert Izquierdo",
      "published_utc": "2026-08-29T21:30:46Z",
      "article_url": "https://www.fool.com/coverage/etfs/2026/08/29/better-consumer-staples-etf-the-ishares-iyk-vs-first-trust-s-food-and-beverage-focused-ftxg/?source=iedfolrf0000001",
      "tickers": [
        "IYK",
        "FTXG",
        "KO",
        "PG",
        "PM",
        "KHC"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F7669db1dbfa6e097df450be5b22faf5d854bd54d-1401x1251.png%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "The iShares U.S. Consumer Staples ETF (IYK) emerges as the superior choice compared to First Trust Nasdaq Food & Beverage ETF (FTXG) for most investors seeking defensive equity exposure. IYK offers broader sector diversification across consumer staples, healthcare, and basic materials with a lower 0.38% expense ratio, larger asset base ($1.4B), and stronger five-year returns ($1,364 vs $1,063 on $1,000 invested). FTXG provides a narrower food and beverage focus that may appeal only to investors seeking specialized sector exposure.",
      "keywords": [
        "consumer staples ETF",
        "defensive investing",
        "ETF comparison",
        "dividend yield",
        "expense ratio",
        "portfolio diversification"
      ],
      "insights": [
        {
          "ticker": "IYK",
          "sentiment": "positive",
          "sentiment_reasoning": "IYK is recommended as the better buy due to lower expense ratio (0.38%), significantly larger AUM ($1.4B) providing better liquidity, superior 5-year returns, lower maximum drawdown (15% vs 21.7%), and broader diversification across 53 holdings in consumer staples, healthcare, and basic materials."
        },
        {
          "ticker": "FTXG",
          "sentiment": "neutral",
          "sentiment_reasoning": "FTXG is presented as a viable alternative only for investors specifically seeking targeted food and beverage exposure. While it has a higher expense ratio (0.6%), smaller AUM ($18.7M), and weaker performance, its factor-weighted methodology focusing on gross income and cash flow metrics may appeal to specialized investors."
        },
        {
          "ticker": "KO",
          "sentiment": "neutral",
          "sentiment_reasoning": "Coca-Cola is mentioned as a major holding in both ETFs (13.39% in IYK, 8.98% in FTXG), indicating its significance in consumer staples portfolios, but no specific sentiment is expressed about the company itself."
        },
        {
          "ticker": "PG",
          "sentiment": "neutral",
          "sentiment_reasoning": "P&G is noted as the second-largest holding in IYK at 12.70%, reflecting its importance in the consumer staples sector, but no specific company sentiment is provided."
        },
        {
          "ticker": "PM",
          "sentiment": "neutral",
          "sentiment_reasoning": "PM is mentioned as a significant IYK holding at 11.40% and is recommended by The Motley Fool, but the article focuses on ETF comparison rather than individual stock sentiment."
        },
        {
          "ticker": "KHC",
          "sentiment": "neutral",
          "sentiment_reasoning": "Kraft Heinz is noted as a top holding in FTXG at 8.40% and is recommended by The Motley Fool, but no specific sentiment is expressed in the article's analysis."
        }
      ]
    },
    {
      "id": "67b3b6974cf98adfc12a3b11167c97336d92ea9345ba26d547fa1107cfd1eb5b",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "VDC vs. FTXG: Which Defensive ETF Is the Better Buy?",
      "author": "Andy Gould",
      "published_utc": "2026-07-28T10:28:52Z",
      "article_url": "https://www.fool.com/coverage/etfs/2026/07/28/vdc-vs-ftxg-which-defensive-etf-is-the-better-buy/?source=iedfolrf0000001",
      "tickers": [
        "VDC",
        "FTXG",
        "WMT",
        "COST",
        "PG",
        "KO",
        "KHC"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F7669db1dbfa6e097df450be5b22faf5d854bd54d-1401x1251.png%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "Vanguard's VDC and First Trust's FTXG are both defensive ETFs investing in consumer staples, but with different approaches. VDC offers broader diversification across 103 stocks with a lower 0.09% expense ratio and stronger 5-year returns, while FTXG concentrates on 30 food and beverage companies with a higher 2.59% dividend yield but higher 0.60% expense ratio. For most long-term investors, VDC is the more straightforward choice due to lower costs and better diversification.",
      "keywords": [
        "defensive ETF",
        "consumer staples",
        "expense ratio",
        "dividend yield",
        "diversification",
        "food and beverage"
      ],
      "insights": [
        {
          "ticker": "VDC",
          "sentiment": "positive",
          "sentiment_reasoning": "VDC is recommended as the better choice for most investors due to significantly lower expense ratio (0.09% vs 0.60%), broader diversification with 103 holdings, stronger 1-year (5.73% vs 3.23%) and 5-year returns, and lower volatility (beta 0.54 vs 0.48)."
        },
        {
          "ticker": "FTXG",
          "sentiment": "neutral",
          "sentiment_reasoning": "FTXG offers a higher dividend yield (2.59% vs 2.13%) and provides concentrated exposure to food and beverage trends, but underperforms VDC in returns, carries higher expenses, and has greater concentration risk with only 30 holdings. Suitable only for investors with specific views on the food and beverage sector."
        },
        {
          "ticker": "WMT",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as a major holding in VDC (14.0%) and described as a familiar retail name benefiting from steady foot traffic and everyday spending."
        },
        {
          "ticker": "COST",
          "sentiment": "positive",
          "sentiment_reasoning": "Second-largest holding in VDC (11.4%) and noted as a retail giant benefiting from steady foot traffic and everyday spending patterns."
        },
        {
          "ticker": "PG",
          "sentiment": "positive",
          "sentiment_reasoning": "Third-largest holding in VDC (8.7%), representing a major consumer staples company in the diversified portfolio."
        },
        {
          "ticker": "KO",
          "sentiment": "neutral",
          "sentiment_reasoning": "Major holding in FTXG (8.5%), but subject to food and beverage industry headwinds including shifting consumer tastes toward healthier options."
        },
        {
          "ticker": "KHC",
          "sentiment": "neutral",
          "sentiment_reasoning": "Significant FTXG holding (8.2%), but exposed to packaged food industry challenges including input costs and shifting consumer preferences toward healthier snacking."
        }
      ]
    },
    {
      "id": "84a932617780d00eca1e4dd95af905ebe2d6b6c3088762857dba169cd91b64c1",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Warren Buffett Backed This Consumer Brand for 38 Years. Here's Why Greg Abel Will Keep Holding.",
      "author": "Patrick Sanders",
      "published_utc": "2026-07-22T09:05:00Z",
      "article_url": "https://www.fool.com/investing/2026/07/22/warren-buffett-backed-this-consumer-brand-for-38-y/?source=iedfolrf0000001",
      "tickers": [
        "KO",
        "BRK.A",
        "BRK.B",
        "AXP",
        "KHC"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F878815%2Fbuffett21-tmf-2.png&w=1200&op=resize",
      "description": "Berkshire Hathaway's 38-year investment in Coca-Cola continues to be exceptionally lucrative, generating $816 million in annual dividends on a $1.299 billion cost basis. With a 2.6% dividend yield and 65 consecutive years of dividend increases, the investment returns over 60% of its original cost annually, making it an easy hold for new CEO Greg Abel.",
      "keywords": [
        "Coca-Cola",
        "Berkshire Hathaway",
        "dividend growth",
        "Warren Buffett",
        "Greg Abel",
        "long-term investing",
        "consumer brands"
      ],
      "insights": [
        {
          "ticker": "KO",
          "sentiment": "positive",
          "sentiment_reasoning": "Exceptional dividend yield of 2.6%, 65 consecutive years of dividend increases (Dividend King status), strong global revenue growth (12% in Q1), diversified product portfolio, and generates $816 million annually for Berkshire on minimal cost basis."
        },
        {
          "ticker": "BRK.A",
          "sentiment": "positive",
          "sentiment_reasoning": "Demonstrates shrewd long-term investment strategy with highly profitable holdings. The Coca-Cola investment alone provides substantial passive income, validating Buffett's investment philosophy that will continue under Abel's leadership."
        },
        {
          "ticker": "BRK.B",
          "sentiment": "positive",
          "sentiment_reasoning": "Demonstrates shrewd long-term investment strategy with highly profitable holdings. The Coca-Cola investment alone provides substantial passive income, validating Buffett's investment philosophy that will continue under Abel's leadership."
        },
        {
          "ticker": "AXP",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as part of Berkshire's portfolio of time-tested consumer companies, but no specific performance data or analysis provided in the article."
        },
        {
          "ticker": "KHC",
          "sentiment": "neutral",
          "sentiment_reasoning": "Referenced as another mature consumer company in Berkshire's portfolio, but receives no detailed analysis or performance commentary."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 30.59417,
    "13WeekPriceReturnDaily": 1.394,
    "26WeekPriceReturnDaily": 6.8712,
    "3MonthADReturnStd": 32.838715,
    "3MonthAverageTradingVolume": 16.14463,
    "52WeekHigh": 28.09,
    "52WeekHighDate": "2026-07-29",
    "52WeekLow": 21.035,
    "52WeekLowDate": "2026-03-24",
    "52WeekPriceReturnDaily": -3.5115,
    "5DayPriceReturnDaily": 0.4876,
    "assetTurnoverAnnual": 0.305,
    "assetTurnoverTTM": 0.3126,
    "beta": 0.12698637,
    "bookValuePerShareAnnual": 35.1892,
    "bookValuePerShareQuarterly": 30.3592,
    "bookValueShareGrowth5Y": -2.99,
    "capexCagr5Y": 6.09,
    "cashFlowPerShareAnnual": 3.0921,
    "cashFlowPerShareQuarterly": 3.2175,
    "cashFlowPerShareTTM": 3.18607,
    "cashPerSharePerShareAnnual": 3.1039,
    "cashPerSharePerShareQuarterly": 2.2605,
    "currentDividendYieldTTM": 6.5879,
    "currentEv/freeCashFlowAnnual": 12.3906,
    "currentEv/freeCashFlowTTM": 11.8873,
    "currentRatioAnnual": 1.1537,
    "currentRatioQuarterly": 1.0614,
    "dividendGrowthRate5Y": -0.08,
    "dividendIndicatedAnnual": 1.6,
    "dividendPerShareAnnual": 1.5956,
    "dividendPerShareTTM": 1.6,
    "dividendYieldIndicatedAnnual": 4.57928,
    "ebitdPerShareAnnual": -3.1533,
    "ebitdPerShareTTM": -1.8668,
    "ebitdaCagr5Y": null,
    "ebitdaInterimCagr5Y": null,
    "enterpriseValue": 45361.943,
    "epsAnnual": -4.925,
    "epsBasicExclExtraItemsAnnual": -4.925,
    "epsBasicExclExtraItemsTTM": -2.8637,
    "epsExclExtraItemsAnnual": -4.925,
    "epsExclExtraItemsTTM": -2.8637,
    "epsGrowth3Y": null,
    "epsGrowth5Y": null,
    "epsGrowthQuarterlyYoy": null,
    "epsGrowthTTMYoy": null,
    "epsInclExtraItemsAnnual": -4.925,
    "epsInclExtraItemsTTM": -2.8637,
    "epsNormalizedAnnual": -4.925,
    "epsTTM": -2.8637,
    "evEbitdaTTM": 17.9651,
    "evRevenueTTM": 1.8218,
    "focfCagr5Y": -3.31,
    "forwardPE": 12.67104,
    "grossMargin5Y": 33.25,
    "grossMarginAnnual": 33.32,
    "grossMarginTTM": 33.45,
    "inventoryTurnoverAnnual": 5.0839,
    "inventoryTurnoverTTM": 4.8207,
    "longTermDebt/equityAnnual": 0.4604,
    "longTermDebt/equityQuarterly": 0.4893,
    "marketCapitalization": 28779.943,
    "monthToDatePriceReturnDaily": -3.6619,
    "netIncomeEmployeeAnnual": -0.167,
    "netIncomeEmployeeTTM": -0.097,
    "netInterestCoverageAnnual": -5.5778,
    "netInterestCoverageTTM": -5.4286,
    "netMarginGrowth5Y": null,
    "netProfitMargin5Y": 2.14,
    "netProfitMarginAnnual": -23.44,
    "netProfitMarginTTM": -13.64,
    "operatingMargin5Y": 6.35,
    "operatingMarginAnnual": -18.89,
    "operatingMarginTTM": -12.92,
    "payoutRatioAnnual": 70.37,
    "payoutRatioTTM": 68.85,
    "pb": 0.7993,
    "pbAnnual": 0.6889,
    "pbQuarterly": 0.7966,
    "pcfShareAnnual": 6.45,
    "pcfShareTTM": 6.2281,
    "peAnnual": null,
    "peBasicExclExtraTTM": null,
    "peExclExtraAnnual": 18.26107,
    "peExclExtraTTM": null,
    "peInclExtraTTM": null,
    "peNormalizedAnnual": null,
    "peTTM": null,
    "pfcfShareAnnual": 7.8612,
    "pfcfShareTTM": 7.5419,
    "pretaxMargin5Y": 2.58,
    "pretaxMarginAnnual": -21.83,
    "pretaxMarginTTM": -14.71,
    "priceRelativeToS&P50013Week": -0.7145,
    "priceRelativeToS&P50026Week": -5.1141,
    "priceRelativeToS&P5004Week": 0.9482,
    "priceRelativeToS&P50052Week": -18.1096,
    "priceRelativeToS&P500Ytd": -9.0879,
    "psAnnual": 1.1539,
    "psTTM": 1.1558,
    "ptbvAnnual": 6.9416,
    "ptbvQuarterly": 7.8932,
    "quickRatioAnnual": 0.7597,
    "quickRatioQuarterly": 0.6513,
    "receivablesTurnoverAnnual": 11.3347,
    "receivablesTurnoverTTM": 10.7559,
    "revenueEmployeeAnnual": 0.7126,
    "revenueEmployeeTTM": 0.7114,
    "revenueGrowth3Y": -1.98,
    "revenueGrowth5Y": -0.97,
    "revenueGrowthQuarterlyYoy": -1.42,
    "revenueGrowthTTMYoy": -1.62,
    "revenuePerShareAnnual": 21.0126,
    "revenuePerShareTTM": 20.9949,
    "revenueShareGrowth5Y": -0.29,
    "roa5Y": 0.56,
    "roaRfy": -7.1499999999999995,
    "roaTTM": -4.26,
    "roe5Y": 0.84,
    "roeRfy": -14.030000000000001,
    "roeTTM": -8.44,
    "roi5Y": 0.73,
    "roiAnnual": -9.3,
    "roiTTM": -5.58,
    "tangibleBookValuePerShareAnnual": 3.4924,
    "tangibleBookValuePerShareQuarterly": 3.0641,
    "tbvCagr5Y": 3.77,
    "totalDebt/totalEquityAnnual": 0.5093,
    "totalDebt/totalEquityQuarterly": 0.5277,
    "yearToDatePriceReturnDaily": 1.9794
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