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
  "score": 78.6,
  "direction": "LONG",
  "sector": "Technology",
  "components": {
    "market": 50.0,
    "sector": 58.48,
    "relative_strength": 100.0,
    "vwap": 100.0,
    "trend": 100.0,
    "volume": 35.95866325910963,
    "momentum": 81.6473273730264,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 64.96821691992864,
    "trend_acceleration": 85,
    "compression": 36.55147523233787,
    "volatility_contraction": 73.43292816540132,
    "volume_accumulation": 59.131966550254646,
    "breakout_distance": 96.93223856356587,
    "support_quality": 30.16331318235126,
    "momentum_improvement": 64.44781744266788,
    "early_setup_score": 68.32,
    "entry_timing_score": 67.2,
    "opportunity_score": 75.18,
    "extended": false,
    "return_5d": 5.41,
    "return_10d": 2.23,
    "return_20d": 7.2,
    "distance_to_breakout": 0.15,
    "atr_extension": 1.64
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
      "datetime": 1789650726,
      "headline": "Apple iPhone Demand Should Hold Up On Higher Carrier Incentives, BofA Says",
      "id": 142226585,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "BofA\u2019s Wamsi Mohan said the maximum trade-in credit for the iPhone 18 Pro Max has increased to $1,200 from $1,100 for the prior generation.",
      "url": "https://finnhub.io/api/news?id=773c44a3dc1e3a9009d4b2133db121a5286ecaccde473b2515de3b661c269317"
    },
    {
      "category": "company",
      "datetime": 1789647379,
      "headline": "Top strategist thinks the Federal Reserve interest rate hike won't fix this huge earnings risk",
      "id": 142224999,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "Eyes still on memory chips.",
      "url": "https://finnhub.io/api/news?id=f96e7cc7d5570c2bb5bfcbc16e4626fabe35ac458d64001a2c92029563ecec65"
    },
    {
      "category": "company",
      "datetime": 1789646441,
      "headline": "The Same Stock but in 2 Different IRAs: By Retirement, the Tax Bill Is the Only Thing That Changes",
      "id": 142226586,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "The same Apple shares sitting in two different IRAs will compound identically for decades, yet one account hands the IRS a cut of every dollar you withdraw while the other hands you nothing. The wrapper you pick today quietly rewrites your retirement tax bill.",
      "url": "https://finnhub.io/api/news?id=8ea475d682023a50303c04aec5e56fbcf92e37184d6842657a7da50d9f543a1d"
    },
    {
      "category": "company",
      "datetime": 1789646400,
      "headline": "Apple Touts Big Emmy Wins: Will Marketing Do A Big Job?",
      "id": 142226587,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "Premium streamer Apple keeps working under the radar of the big guys - including Netflix, Prime Video, HBO Max and Disney+ - in scoring major awards.",
      "url": "https://finnhub.io/api/news?id=c4166d6c71eac5a4e7a5eb8ce13cd476a78192626a54e7709fde139023d0d64d"
    },
    {
      "category": "company",
      "datetime": 1789645320,
      "headline": "Why Stocks Are Loving the Fed\u2019s Rate Hike Even If Trump Hates It",
      "id": 142225387,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AAPL",
      "source": "Yahoo",
      "summary": "Nvidia looks like a bargain, OpenAI reveals 6 \u2018concerning\u2019 incidents, and more news to start your day.",
      "url": "https://finnhub.io/api/news?id=0d34dbc4d213ca2bd2a7ac310c915208d3dfbb57289073a8acc03b9cc8171987"
    }
  ],
  "polygon_news": [
    {
      "id": "9a0d855334c168e17ce018b176be2dabeeec549addba007b5fb024577c7b3105",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "If You Invest $340 a Month in the Vanguard S&P 500 ETF, Here's What History Says It Could Be Worth in 22 Years",
      "author": "Matt Dilallo",
      "published_utc": "2026-09-17T11:30:01Z",
      "article_url": "https://www.fool.com/investing/2026/09/17/if-you-invest-usd340-a-month-in-the-vanguard-s-and-p-500-etf-here-s-what-history-says-it-could-be-worth-in-22-years/?source=iedfolrf0000001",
      "tickers": [
        "VOO",
        "NVDA",
        "AAPL",
        "MSFT"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2Fee99eea3ecf280dd60a92174ad06e867441d0d1b-2121x1414.jpg%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "Investing $340 monthly in the Vanguard S&P 500 ETF (VOO) could grow to approximately $606,200 over 22 years at its historical 15% average return since 2010, or $306,975 at the S&P 500's longer-term 10% historical average. The article emphasizes that investment returns matter significantly more than the monthly contribution amount, with compounding playing a crucial role in long-term wealth building.",
      "keywords": [
        "S&P 500 ETF",
        "VOO",
        "long-term investing",
        "compound returns",
        "historical returns",
        "index fund",
        "wealth building"
      ],
      "insights": [
        {
          "ticker": "VOO",
          "sentiment": "positive",
          "sentiment_reasoning": "The article presents VOO as a solid long-term investment vehicle with strong historical performance (15% since inception, 10% over 100 years). The analysis demonstrates significant wealth accumulation potential through dollar-cost averaging, and the low expense ratio (0.03%) is favorable. The article positions it as a reasonable bet on U.S. market performance."
        },
        {
          "ticker": "NVDA",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a top holding (8.09%) in VOO's portfolio. The article notes that top holdings are tech/tech-adjacent companies investing in AI, but provides no specific sentiment about Nvidia itself, only contextual information about its position in the fund."
        },
        {
          "ticker": "AAPL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Listed as a top holding (7.04%) in VOO. Mentioned only as part of the fund's composition without specific commentary on the company's prospects."
        },
        {
          "ticker": "MSFT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Included as a top holding (5.70%) in VOO. Referenced only as part of the fund's holdings without independent sentiment analysis."
        }
      ]
    },
    {
      "id": "debc317c12ef7d51ca6bcd209dd3f60d88226e1d9c33c2820d375a74e4e7f881",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "1 AI Stock Poised to Outperform Micron and Sandisk on the Next Infrastructure Surge",
      "author": "Harsh Chauhan",
      "published_utc": "2026-09-17T11:08:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/17/1-ai-stock-poised-to-outperform-micron-and-sandisk/?source=iedfolrf0000001",
      "tickers": [
        "TSM",
        "MU",
        "SNDK",
        "NVDA",
        "ORCL",
        "ORCLpD",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "AAPL"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F886868%2Fdata-center-server.jpg&w=1200&op=resize",
      "description": "Taiwan Semiconductor Manufacturing (TSMC) is positioned to outperform memory chip makers Micron and Sandisk as AI infrastructure spending accelerates. With AI accelerator revenue expected to grow at 60%+ CAGR through 2029 and the company controlling 72.5% of the foundry market, TSMC trades at a discount valuation of 20x forward earnings. Analysts project the stock could reach $850 by 2028, more than doubling from current levels.",
      "keywords": [
        "AI infrastructure spending",
        "semiconductor foundry",
        "AI accelerators",
        "memory chips",
        "hyperscaler demand",
        "valuation discount",
        "earnings growth"
      ],
      "insights": [
        {
          "ticker": "TSM",
          "sentiment": "positive",
          "sentiment_reasoning": "TSMC is highlighted as the primary investment opportunity with strong AI accelerator growth (60%+ CAGR), market dominance (72.5% foundry share), pricing power, and attractive valuation (20x forward earnings vs. 24.5x Nasdaq-100). Price target of $850 by 2028 implies significant upside."
        },
        {
          "ticker": "MU",
          "sentiment": "neutral",
          "sentiment_reasoning": "While benefiting from AI data center spending, Micron faces investor rotation concerns due to potential memory oversupply and already impressive margins. Presented as a less attractive alternative compared to TSMC."
        },
        {
          "ticker": "SNDK",
          "sentiment": "neutral",
          "sentiment_reasoning": "Similar to Micron, Sandisk has benefited from AI infrastructure spending but faces headwinds from investor rotation, oversupply concerns, and margin pressures. Outperformed TSMC year-to-date but considered less favorable going forward."
        },
        {
          "ticker": "NVDA",
          "sentiment": "positive",
          "sentiment_reasoning": "Mentioned as a major TSMC customer with significant AI infrastructure capex expectations ($800 billion from top five hyperscalers in 2026), supporting strong demand for TSMC's foundry services."
        },
        {
          "ticker": "ORCL",
          "sentiment": "positive",
          "sentiment_reasoning": "Cited as evidence of massive AI infrastructure backlogs with $664 billion in contractual backlog, supporting the thesis for sustained AI infrastructure spending."
        },
        {
          "ticker": "ORCLpD",
          "sentiment": "positive",
          "sentiment_reasoning": "Cited as evidence of massive AI infrastructure backlogs with $664 billion in contractual backlog, supporting the thesis for sustained AI infrastructure spending."
        },
        {
          "ticker": "GOOG",
          "sentiment": "positive",
          "sentiment_reasoning": "Google Cloud's $514 billion backlog demonstrates strong AI infrastructure demand, supporting the overall thesis for continued AI spending and TSMC's growth prospects."
        },
        {
          "ticker": "GOOGL",
          "sentiment": "positive",
          "sentiment_reasoning": "Google Cloud's $514 billion backlog demonstrates strong AI infrastructure demand, supporting the overall thesis for continued AI spending and TSMC's growth prospects."
        },
        {
          "ticker": "GOOGM",
          "sentiment": "positive",
          "sentiment_reasoning": "Google Cloud's $514 billion backlog demonstrates strong AI infrastructure demand, supporting the overall thesis for continued AI spending and TSMC's growth prospects."
        },
        {
          "ticker": "GOOGN",
          "sentiment": "positive",
          "sentiment_reasoning": "Google Cloud's $514 billion backlog demonstrates strong AI infrastructure demand, supporting the overall thesis for continued AI spending and TSMC's growth prospects."
        },
        {
          "ticker": "AAPL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a TSMC customer that could benefit from smartphone market rebound in 2028, providing secondary growth opportunity for TSMC."
        }
      ]
    },
    {
      "id": "be6bdc4ae8495ff133cdb151b7bcb79c344810fb2f5d1eb73b4c51e6d28c8005",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Greg Abel Has 75% of Berkshire Hathaway's Portfolio Invested in Just 8 Stocks. Is the 1 That's Lagging Behind the S&P 500 the Best Buy Now?",
      "author": "Daniel Foelber",
      "published_utc": "2026-09-17T10:30:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/17/greg-abel-berkshire-hathaway-american-express/?source=iedfolrf0000001",
      "tickers": [
        "BRK.A",
        "BRK.B",
        "AXP",
        "AAPL",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "KO",
        "MCO",
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
        "CVX",
        "OXY",
        "OXY.WS",
        "V",
        "MA"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F887380%2Fa-person-smiles-while-holding-a-credit-card-and-sitting-in-front-of-a-laptop-computer.jpg&w=1200&op=resize",
      "description": "Under new CEO Greg Abel, Berkshire Hathaway has concentrated 75% of its $365.2 billion equity portfolio into 8 stocks. American Express is the only one lagging the S&P 500 over the past year due to margin compression from high cardholder rewards and marketing expenses. Despite these headwinds, the article argues American Express offers compelling value at 19.7x trailing earnings for long-term investors who believe in its business model.",
      "keywords": [
        "Berkshire Hathaway",
        "Greg Abel",
        "portfolio concentration",
        "American Express",
        "margin compression",
        "cardholder rewards",
        "valuation"
      ],
      "insights": [
        {
          "ticker": "BRK.A",
          "sentiment": "neutral",
          "sentiment_reasoning": "Article discusses portfolio strategy under new CEO without expressing strong positive or negative outlook on the company itself."
        },
        {
          "ticker": "BRK.B",
          "sentiment": "neutral",
          "sentiment_reasoning": "Article discusses portfolio strategy under new CEO without expressing strong positive or negative outlook on the company itself."
        },
        {
          "ticker": "AXP",
          "sentiment": "positive",
          "sentiment_reasoning": "Despite underperformance vs S&P 500, article highlights strong fundamentals (double-digit revenue/EPS growth, record spending levels, raised guidance), attractive valuation at 19.7x earnings, and positions it as 'arguably the best buy' among Berkshire's top holdings despite margin pressure concerns."
        },
        {
          "ticker": "AAPL",
          "sentiment": "positive",
          "sentiment_reasoning": "Listed as a top-5 holding identified by Abel as a company Berkshire expects to compound for decades; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "GOOG",
          "sentiment": "positive",
          "sentiment_reasoning": "Catapulted to top-five holding under Abel; identified as a company expected to compound for decades; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "GOOGL",
          "sentiment": "positive",
          "sentiment_reasoning": "Catapulted to top-five holding under Abel; identified as a company expected to compound for decades; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "GOOGM",
          "sentiment": "positive",
          "sentiment_reasoning": "Catapulted to top-five holding under Abel; identified as a company expected to compound for decades; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "GOOGN",
          "sentiment": "positive",
          "sentiment_reasoning": "Catapulted to top-five holding under Abel; identified as a company expected to compound for decades; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "KO",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as a company Berkshire expects to compound for decades; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "MCO",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as a company Berkshire expects to compound for decades; part of concentrated portfolio strategy."
        },
        {
          "ticker": "BAC",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpB",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpE",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpM",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpN",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpO",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpP",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpQ",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpS",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BMLpG",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BMLpH",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BMLpJ",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BMLpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "MERpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "CVX",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "OXY",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "OXY.WS",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "V",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as comparison to American Express; noted as pure-play payment processor with different business model and lower vulnerability to economic downturns."
        },
        {
          "ticker": "MA",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as comparison to American Express; noted as pure-play payment processor with different business model and lower vulnerability to economic downturns."
        }
      ]
    },
    {
      "id": "16c7ac28cd0e5b27d4df94d0889c193a7f717897ae13627fbd9b2741635414c2",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Nvidia Has Returned $46 Billion to Shareholders This Year, and Another Major Dividend Hike Could Be Coming",
      "author": "Stefon Walters",
      "published_utc": "2026-09-17T06:05:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/17/nvidia-has-returned-46-billion-to-shareholders-thi/?source=iedfolrf0000001",
      "tickers": [
        "NVDA",
        "MSFT",
        "AAPL"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F886829%2Fnvda.png&w=1200&op=resize",
      "description": "Nvidia, the world's most valuable company with a $5.1 trillion market cap, has returned $46 billion to shareholders through dividends and buybacks in the first half of its fiscal year. The chipmaker boosted its quarterly dividend from $0.01 to $0.25 per share in June and sits on $99.4 billion in cash, positioning it for potential further dividend increases as its AI-driven business continues to generate unprecedented profits.",
      "keywords": [
        "Nvidia",
        "shareholder returns",
        "dividend hike",
        "stock buybacks",
        "AI boom",
        "cash reserves",
        "market cap"
      ],
      "insights": [
        {
          "ticker": "NVDA",
          "sentiment": "positive",
          "sentiment_reasoning": "Nvidia is experiencing unprecedented business growth driven by AI demand, has returned $46 billion to shareholders, increased its dividend 2,400%, maintains $99.4 billion in cash reserves, and is positioned for continued shareholder rewards and reinvestment in its growing business."
        },
        {
          "ticker": "MSFT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Microsoft is mentioned as a comparable mature tech company with reliable and growing dividend payouts, but no specific news or performance metrics are discussed in the article."
        },
        {
          "ticker": "AAPL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Apple is mentioned as a comparable mature tech company with reliable and growing dividend payouts, but no specific news or performance metrics are discussed in the article."
        }
      ]
    },
    {
      "id": "eb1523da74abdc0bcb9d2b4f9d2a3c329b34c9355a87dc20007984ffc0337d2b",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "I've Analyzed Hundreds of Stocks in 7 Years. Here's My Step-by-Step System for Researching Any Company Before Buying.",
      "author": "Alex Carchidi",
      "published_utc": "2026-09-16T19:37:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/16/my-step-by-step-system-for-researching-stocks/?source=iedfolrf0000001",
      "tickers": [
        "AAPL",
        "COST"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F885945%2Ftwo-investors-look-at-figures.jpg&w=1200&op=resize",
      "description": "An experienced analyst shares a seven-step stock research methodology developed over years of analyzing hundreds of companies. The process includes comparing returns to the S&P 500, analyzing financial reports, mapping business models, evaluating competitive advantages, assessing macro trends, reviewing leadership, conducting risk analysis, and determining valuation. The author uses Apple and Costco as examples of companies that meet their investment criteria.",
      "keywords": [
        "stock research methodology",
        "fundamental analysis",
        "competitive advantage",
        "financial metrics",
        "valuation analysis",
        "risk assessment",
        "investment strategy"
      ],
      "insights": [
        {
          "ticker": "AAPL",
          "sentiment": "positive",
          "sentiment_reasoning": "Highlighted as a longtime favorite holding that has outperformed the S&P 500 over five years. Praised for strong brand power, integrated ecosystem, customer retention capabilities, and leadership quality with CEO John Ternus demonstrating proven execution history."
        },
        {
          "ticker": "COST",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as a longtime favorite investment that has outperformed the S&P 500. Commended for its unique business model where membership fees provide significant operating income insulation, and CEO Ron Vachris exemplifies the desired leadership profile with deep organizational experience."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 45.66396,
    "13WeekPriceReturnDaily": 13.8117,
    "26WeekPriceReturnDaily": 27.0427,
    "3MonthADReturnStd": 31.401579,
    "3MonthAverageTradingVolume": 52.29406,
    "52WeekHigh": 344.5699,
    "52WeekHighDate": "2026-07-29",
    "52WeekLow": 235.03,
    "52WeekLowDate": "2025-09-15",
    "52WeekPriceReturnDaily": 39.9831,
    "5DayPriceReturnDaily": 5.0739,
    "assetTurnoverAnnual": 1.1584,
    "assetTurnoverTTM": 1.2508,
    "beta": 1.0863714,
    "bookValuePerShareAnnual": 4.991,
    "bookValuePerShareQuarterly": 7.3599,
    "bookValueShareGrowth5Y": 5.34,
    "capexCagr5Y": 11.71,
    "cashFlowPerShareAnnual": 6.6855,
    "cashFlowPerShareQuarterly": 9.3561,
    "cashFlowPerShareTTM": 6.86253,
    "cashPerSharePerShareAnnual": 3.7024,
    "cashPerSharePerShareQuarterly": 4.2713,
    "currentDividendYieldTTM": 0.3234,
    "currentEv/freeCashFlowAnnual": 49.4136,
    "currentEv/freeCashFlowTTM": 35.7062,
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
    "enterpriseValue": 4880435.5,
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
    "evEbitdaTTM": 29.0573,
    "evRevenueTTM": 10.4546,
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
    "marketCapitalization": 4835635.5,
    "monthToDatePriceReturnDaily": 4.5731,
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
    "pb": 44.9743,
    "pbAnnual": 50.978,
    "pbQuarterly": 38.486,
    "pcfShareAnnual": 43.3759,
    "pcfShareTTM": 32.9574,
    "peAnnual": 43.1715,
    "peBasicExclExtraTTM": 37.5059,
    "peExclExtraAnnual": 30.96975,
    "peExclExtraTTM": 37.5059,
    "peInclExtraTTM": 37.5059,
    "peNormalizedAnnual": 43.1715,
    "peTTM": 37.5059,
    "pegTTM": 2.93443,
    "pfcfShareAnnual": 48.96,
    "pfcfShareTTM": 35.3785,
    "pretaxMargin5Y": 30.64,
    "pretaxMarginAnnual": 31.89,
    "pretaxMarginTTM": 33.4,
    "priceRelativeToS&P50013Week": 11.7032,
    "priceRelativeToS&P50026Week": 15.0574,
    "priceRelativeToS&P5004Week": 8.1843,
    "priceRelativeToS&P50052Week": 25.385,
    "priceRelativeToS&P500Ytd": 10.8116,
    "psAnnual": 11.6196,
    "psTTM": 10.3586,
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
    "yearToDatePriceReturnDaily": 21.8789
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

## SPCX
Trading candidate:
```json
{
  "symbol": "SPCX",
  "score": 79.84,
  "direction": "LONG",
  "sector": "Communication Services",
  "components": {
    "market": 50.0,
    "sector": 89.15,
    "relative_strength": 84.71969131610736,
    "vwap": 86.21457632162728,
    "trend": 100.0,
    "volume": 100.0,
    "momentum": 69.21846404121194,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 63.88897563500018,
    "relative_strength_acceleration": 55.714302778110614,
    "trend_acceleration": 85,
    "compression": 0.0,
    "volatility_contraction": 49.4959820541216,
    "volume_accumulation": 48.094345521631546,
    "breakout_distance": 66.60703637447848,
    "support_quality": 0.0,
    "momentum_improvement": 53.871915566304416,
    "early_setup_score": 50.59,
    "entry_timing_score": 50.59,
    "opportunity_score": 71.06,
    "extended": false,
    "return_5d": 2.3,
    "return_10d": 6.12,
    "return_20d": 5.35,
    "distance_to_breakout": 1.67,
    "atr_extension": 1.15
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
      "datetime": 1789647466,
      "headline": "Stock Market Today: Dow Rises In Fed Aftermath; Generac, Nebius, Bloom, SpaceX Are Early Movers (Live Coverage)",
      "id": 142223710,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SPCX",
      "source": "Yahoo",
      "summary": "Futures rebounded with the Nasdaq and S&P 500 eyeing key support. Generac, Nebius, Bloom Energy, SpaceX were early winners.",
      "url": "https://finnhub.io/api/news?id=49d60463dfc18365c2ea7869c2b6ad825c2821bac2c6dfa5a649333d40193d1c"
    },
    {
      "category": "company",
      "datetime": 1789639211,
      "headline": "SpaceX Is Worth $2 Trillion. Why Does Its Stock Swing Like a Small-Cap?",
      "id": 142226806,
      "image": "https://cdn.benzinga.com/files/images/story/2026/09/17/SpaceX-starships-in-launch-position-at-t.jpg?width=2048&height=1536",
      "related": "SPCX",
      "source": "Benzinga",
      "summary": "SpaceX is worth about $2 trillion, but its shares swing roughly 4.5% a day as a small float and heavy retail trading drive volatility.",
      "url": "https://finnhub.io/api/news?id=c199e2b30aa58bc7ada83ad306812fac546f8f9535dc1cbc79d70f3c0a0dc088"
    },
    {
      "category": "company",
      "datetime": 1789636921,
      "headline": "SpaceX CFO: New Compute Deal Puts Company Closer to $100B ARR Goal",
      "id": 142219074,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SPCX",
      "source": "Yahoo",
      "summary": "The company is closer to achieving its audacious goal than investors might think.",
      "url": "https://finnhub.io/api/news?id=74bbab340fc98ccb2f842112980dd25763a4acd371a2d207d4eee8f51dc9a95b"
    },
    {
      "category": "company",
      "datetime": 1789635600,
      "headline": "SpaceX: Great Business At A Dangerous Price",
      "id": 142224482,
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/2254175142/image_2254175142.jpg?io=getty-c-w1536",
      "related": "SPCX",
      "source": "SeekingAlpha",
      "summary": "Space Exploration Technologies surged post-IPO but retraced, now trading 41% above August lows after positive earnings. Read more on SPCX stock here.",
      "url": "https://finnhub.io/api/news?id=af878c50aa1d7c3752abd5c3aa53209e5108fd770ed42354942b2d5e37b41474"
    },
    {
      "category": "company",
      "datetime": 1789634055,
      "headline": "Nasdaq, S&P 500 Futures Rebound After Fed Rate Hike: NVDA, NBIS, SNAP, SPCX, BE, GNRC Stocks In Focus",
      "id": 142216070,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SPCX",
      "source": "Yahoo",
      "summary": "Retail sentiment on SPY and QQQ remained \u2018bearish\u2019, even as futures recovered.",
      "url": "https://finnhub.io/api/news?id=2e03ad0be88e69667d38883382e98ef7254b0fa9459b6efa93c492f0c06496af"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 81.90819,
    "13WeekPriceReturnDaily": -10.8481,
    "3MonthAverageTradingVolume": 109.96881,
    "52WeekHigh": 225.64,
    "52WeekHighDate": "2026-06-16",
    "52WeekLow": 104.83,
    "52WeekLowDate": "2026-08-03",
    "5DayPriceReturnDaily": -2.7516,
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
    "monthToDatePriceReturnDaily": -0.1392,
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
    "priceRelativeToS&P50013Week": -12.9566,
    "priceRelativeToS&P5004Week": 1.4154,
    "priceRelativeToS&P500Ytd": -12.9566,
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
    "yearToDatePriceReturnDaily": -10.8481
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
  "score": 54.25,
  "direction": "LONG",
  "sector": "Healthcare",
  "components": {
    "market": 50.0,
    "sector": 57.42,
    "relative_strength": 56.406117564303486,
    "vwap": 100.0,
    "trend": 0.0,
    "volume": 45.851273424621766,
    "momentum": 53.609931630082784,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 47.76285480163495,
    "trend_acceleration": 25,
    "compression": 32.76332545024562,
    "volatility_contraction": 79.82276046674808,
    "volume_accumulation": 38.24222880598188,
    "breakout_distance": 0.0,
    "support_quality": 100.0,
    "momentum_improvement": 44.78454645033223,
    "early_setup_score": 35.15,
    "entry_timing_score": 35.15,
    "opportunity_score": 48.52,
    "extended": false,
    "return_5d": -1.1,
    "return_10d": -3.78,
    "return_20d": 0.83,
    "distance_to_breakout": 5.6,
    "atr_extension": -1.33
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
      "datetime": 1789647089,
      "headline": "What Happens To AbbVie Stock If SKYRIZI Slows Down?",
      "id": 142223863,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "AbbVie (ABBV) is trading within about one percent of its 52-week high after gaining roughly 24% over the past year, well ahead of the S&P 500. That price rests on two drugs, SKYRIZI above all, growing faster than 20% year over year while the company's older medicines shrink. The biggest risk to the stock makes no noise. It is the chance that this engine slows while the price assumes it cannot.",
      "url": "https://finnhub.io/api/news?id=dc4cbf8b69fbadfb93aa4d383979cd3fcb3a5cf28f9596c1e165bded9540a7e2"
    },
    {
      "category": "company",
      "datetime": 1789635840,
      "headline": "Pfizer's Dividend Faces Big Questions. Here Are 3 Reasons It Should Survive.",
      "id": 142218024,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "Income investors shouldn't be too worried about the pharma giant cutting its dividend.",
      "url": "https://finnhub.io/api/news?id=4a98cedf38ba362ccff6860b92bd7f421418b327db5748c1d7dcf283a569ded0"
    },
    {
      "category": "company",
      "datetime": 1789624500,
      "headline": "Tarja Stenvall Appointed Chief Executive Officer of Bavarian Nordic",
      "id": 142209009,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "COPENHAGEN, Denmark, September 17, 2026 \u2013 Bavarian Nordic A/S (OMX: BAVA) today announced that Tarja Stenvall has been appointed President and Chief Executive Officer, effective October 15, 2026, succeeding Paul Chaplin whose departure was announced earlier this year. Tarja Stenvall is a global healthcare executive with over 20 years of leadership experience from Sanofi, AstraZeneca, and Pfizer, combining deep commercial expertise with a proven track record of building and transforming businesse",
      "url": "https://finnhub.io/api/news?id=4398563e87cc9458d32900e8f4a439bd26acea5cc90c586bb27fa9699f5d328b"
    },
    {
      "category": "company",
      "datetime": 1789618814,
      "headline": "Vaxcyte (PCVX) Brings In Pharma Veterans As Its Big Test Nears",
      "id": 142207570,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "On September 3, Vaxcyte (NASDAQ:PCVX) announced two new C-suite hires and moved up the date for its most important looming catalyst. The company said it now expects topline safety, tolerability and immunogenicity data from the VAX-31 adult Phase 3 OPUS-1 trial by the end of October, narrowing guidance that had previously pointed only to sometime [\u2026]",
      "url": "https://finnhub.io/api/news?id=5b3c5121d8320cbfcd073762c33b74f9dd5c2d54b069c2ed8300acf7f21f9914"
    },
    {
      "category": "company",
      "datetime": 1789589528,
      "headline": "Is Pfizer's New Business Big Enough To Carry The Old One?",
      "id": 142201180,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PFE",
      "source": "Yahoo",
      "summary": "Pfizer (PFE) trades at about 95% of its 52-week high. The business that has to justify that price, the medicines it has launched and acquired, is still only about a fifth of the company. The stock returned roughly 24% over the past year against about 17% for the S&P 500, so investors have so far given the handoff the benefit of the doubt. It is a large bet on a small slice.",
      "url": "https://finnhub.io/api/news?id=f18ff60a19b03a3e4eb745f510ed74b65c961a3130cc840808d3eb4280fba88d"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 31.6574,
    "13WeekPriceReturnDaily": 5.1126,
    "26WeekPriceReturnDaily": 0.9158,
    "3MonthADReturnStd": 22.162418,
    "3MonthAverageTradingVolume": 39.6149,
    "52WeekHigh": 29.21,
    "52WeekHighDate": "2026-09-03",
    "52WeekLow": 23.58,
    "52WeekLowDate": "2025-09-25",
    "52WeekPriceReturnDaily": 14.9353,
    "5DayPriceReturnDaily": -0.8279,
    "assetTurnoverAnnual": 0.3006,
    "assetTurnoverTTM": 0.3086,
    "beta": 0.28045806,
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
    "monthToDatePriceReturnDaily": -3.1975,
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
    "priceRelativeToS&P50013Week": 3.0041,
    "priceRelativeToS&P50026Week": -11.0695,
    "priceRelativeToS&P5004Week": 2.4117,
    "priceRelativeToS&P50052Week": 0.3372,
    "priceRelativeToS&P500Ytd": -0.4247,
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
    "yearToDatePriceReturnDaily": 10.6426
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

## KHC
Trading candidate:
```json
{
  "symbol": "KHC",
  "score": 51.78,
  "direction": "LONG",
  "sector": "Consumer Staples",
  "components": {
    "market": 50.0,
    "sector": 57.02,
    "relative_strength": 61.107760384821525,
    "vwap": 80.51415003974432,
    "trend": 0.0,
    "volume": 42.89046462206459,
    "momentum": 50.787527930124,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 54.22537495825774,
    "trend_acceleration": 25,
    "compression": 3.6602628918099356,
    "volatility_contraction": 69.47566084067601,
    "volume_accumulation": 88.37980961614596,
    "breakout_distance": 0.0,
    "support_quality": 82.20424671385233,
    "momentum_improvement": 52.17028377218684,
    "early_setup_score": 34.97,
    "entry_timing_score": 34.97,
    "opportunity_score": 46.74,
    "extended": false,
    "return_5d": 0.45,
    "return_10d": -4.43,
    "return_20d": -0.38,
    "distance_to_breakout": 6.25,
    "atr_extension": -0.74
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
      "datetime": 1789650261,
      "headline": "RBC bullish on Kraft Heinz, sees return to growth in 2027",
      "id": 142224735,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "KHC",
      "source": "Yahoo",
      "summary": "Investing.com -- RBC Capital Markets initiated coverage of Kraft Heinz at Outperform with a $32 price target in a note Thursday, arguing the packaged food maker is on the cusp of a return to growth that the market is underestimating.",
      "url": "https://finnhub.io/api/news?id=0c7e81625ad05745c29cd473a4165da7582672e8fc8532883049c7803f1d0634"
    },
    {
      "category": "company",
      "datetime": 1789647017,
      "headline": "3 Value Stocks We Find Risky",
      "id": 142224421,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "KHC",
      "source": "Yahoo",
      "summary": "The low valuation multiples for value stocks provide a margin of safety that growth stocks rarely offer. However, the challenge lies in determining whether these cheap assets are genuinely undervalued or simply on sale due to their potentially deteriorating business models.",
      "url": "https://finnhub.io/api/news?id=aecb580acfb96224e22c1ae1fc55a9bb03f4f59be09324dd408b7610d592d4ad"
    },
    {
      "category": "company",
      "datetime": 1789639440,
      "headline": "Berkshire Hathaway Has 30.6% of Its Portfolio in These 2 Magnificent AI Stocks. Here's Why That's a Signal Worth Watching.",
      "id": 142219094,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "KHC",
      "source": "Yahoo",
      "summary": "Berkshire Hathaway is known for holding stable, boring stocks, but it still has significant exposure to AI companies.",
      "url": "https://finnhub.io/api/news?id=222e030a3db11caecf31a5dfe277cef8888464a4c2ad1f759b288d16647af643"
    },
    {
      "category": "company",
      "datetime": 1789636314,
      "headline": "RBC Capital Initiates Coverage On Kraft Heinz with Outperform Rating, Announces Price Target of $32",
      "id": 142226796,
      "image": "",
      "related": "KHC",
      "source": "Benzinga",
      "summary": "RBC Capital  analyst Nik Modi   initiates coverage on Kraft Heinz (NYSE:KHC) with a Outperform rating and announces Price Target of $32.",
      "url": "https://finnhub.io/api/news?id=b9c50d28e309e2ff05cda65030195b2f22e7870f232ee9b4db92da8602024890"
    },
    {
      "category": "company",
      "datetime": 1789578194,
      "headline": "Two Beaten-Down Food Stocks Pay 6.5% Yields. Which Dividend Is Safer?",
      "id": 142198477,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "KHC",
      "source": "Yahoo",
      "summary": "Both General Mills and Kraft Heinz offer nearly identical 6.5% yields at beaten-down valuations, but one of them already cut its dividend once and just wrote down billions in brand value for the second year running. Picking the wrong one could leave your retirement income short.",
      "url": "https://finnhub.io/api/news?id=3636782d30661f3e52a7c467f4cd813f2bdd1b75716e0ebdebc0b454521e3610"
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
    "currentDividendYieldTTM": 6.4654,
    "currentEv/freeCashFlowAnnual": 12.5396,
    "currentEv/freeCashFlowTTM": 12.0302,
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
    "enterpriseValue": 45907.422,
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
    "evEbitdaTTM": 18.1812,
    "evRevenueTTM": 1.8437,
    "focfCagr5Y": -3.31,
    "forwardPE": 12.67104,
    "grossMargin5Y": 33.25,
    "grossMarginAnnual": 33.32,
    "grossMarginTTM": 33.45,
    "inventoryTurnoverAnnual": 5.0839,
    "inventoryTurnoverTTM": 4.8207,
    "longTermDebt/equityAnnual": 0.4604,
    "longTermDebt/equityQuarterly": 0.4893,
    "marketCapitalization": 29325.422,
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
    "pb": 0.8145,
    "pbAnnual": 0.6889,
    "pbQuarterly": 0.7966,
    "pcfShareAnnual": 6.5723,
    "pcfShareTTM": 6.3461,
    "peAnnual": null,
    "peBasicExclExtraTTM": null,
    "peExclExtraAnnual": 18.26107,
    "peExclExtraTTM": null,
    "peInclExtraTTM": null,
    "peNormalizedAnnual": null,
    "peTTM": null,
    "pfcfShareAnnual": 8.0102,
    "pfcfShareTTM": 7.6849,
    "pretaxMargin5Y": 2.58,
    "pretaxMarginAnnual": -21.83,
    "pretaxMarginTTM": -14.71,
    "priceRelativeToS&P50013Week": -0.7145,
    "priceRelativeToS&P50026Week": -5.1141,
    "priceRelativeToS&P5004Week": 0.9482,
    "priceRelativeToS&P50052Week": -18.1096,
    "priceRelativeToS&P500Ytd": -9.0879,
    "psAnnual": 1.1757,
    "psTTM": 1.1777,
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

## AMZN
Trading candidate:
```json
{
  "symbol": "AMZN",
  "score": 49.42,
  "direction": "WATCH",
  "sector": "Unknown",
  "components": {
    "market": 50.0,
    "sector": 50.0,
    "relative_strength": 34.19032484599755,
    "vwap": 96.51841055977955,
    "trend": 0.0,
    "volume": 55.88717413301669,
    "momentum": 49.84924424017908,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 47.97748005379342,
    "trend_acceleration": 25,
    "compression": 36.87548274320095,
    "volatility_contraction": 76.32830602870037,
    "volume_accumulation": 58.16947419598827,
    "breakout_distance": 0.0,
    "support_quality": 100.0,
    "momentum_improvement": 45.029832452799056,
    "early_setup_score": 37.67,
    "entry_timing_score": 37.67,
    "opportunity_score": 45.9,
    "extended": false,
    "return_5d": -2.54,
    "return_10d": -3.49,
    "return_20d": -5.18,
    "distance_to_breakout": 8.29,
    "atr_extension": -2.3
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
      "datetime": 1789644650,
      "headline": "Oracle\u2019s 2026 Cratering: This Pro Is Sure It Will Nearly Triple in the Next 12 Months",
      "id": 142223379,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AMZN",
      "source": "Yahoo",
      "summary": "Oracle just delivered a blowout quarter and its shares cratered anyway, but a handful of Wall Street analysts are calling the selloff the opportunity of the year with a price target that would nearly triple your money.",
      "url": "https://finnhub.io/api/news?id=dc2c9634a3fbc2361efb918f0b73df9baa621d16810dd0b656b6962b52f05918"
    },
    {
      "category": "company",
      "datetime": 1789644385,
      "headline": "Generac Gets $100 Target Hike From Canaccord \u2014 Amazon Deal Could Unlock Up To $8B In Orders, Says Analyst",
      "id": 142223375,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AMZN",
      "source": "Yahoo",
      "summary": "According to TheFly, Canaccord sees the Amazon agreement as a multi-year data center opportunity for Generac with $2.4 billion of initial deliveries expected through 2028.",
      "url": "https://finnhub.io/api/news?id=ea0eee0beb2a3c2f8ce81ea63019c3b744fd098b413cccef55caff0591e1bace"
    },
    {
      "category": "company",
      "datetime": 1789644001,
      "headline": "22.4% of Billionaire Bill Ackman\u2019s Pershing Square Capital Management Is Invested in These 2 Artificial Intelligence (AI) Stocks",
      "id": 142223376,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AMZN",
      "source": "Yahoo",
      "summary": "These AI stocks can be excellent core holdings for a well-diversified portfolio.",
      "url": "https://finnhub.io/api/news?id=6ed92433bdbd002888e13442151331b71c65ef947c8c5c9ac960f5f188a0efb5"
    },
    {
      "category": "company",
      "datetime": 1789643760,
      "headline": "Generac Stock Surges 35% on Amazon Data Center Deal. Why It\u2019s a Game-Changer.",
      "id": 142223128,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AMZN",
      "source": "Yahoo",
      "summary": "The backup power company disclosed a long-term deal to provide Amazon generators for its data centers.",
      "url": "https://finnhub.io/api/news?id=84897bf1bae338c87456a9ecff87679c12046ca66a5e7248ecbd5e894716a234"
    },
    {
      "category": "company",
      "datetime": 1789641924,
      "headline": "Why Is Snap Stock Trading Higher on Thursday?",
      "id": 142223380,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "AMZN",
      "source": "Yahoo",
      "summary": "Snap Inc. (NYSE:SNAP) shares rose about 3% in Thursday premarket trading after new enterprise partnerships expanded the use cases for its SPECS augmented reality glasses. The stock also benefited from a risk-on backdrop, with S&P 500 futures up about 0.9%. SNAP had gained more than 4% in after-hours trading on Wednesday. Salesforce, AWS And Nvidia Expand SPECS Push Snap announced partnerships with Salesforce Inc. (NYSE:CRM), Nvidia Corp. (NASDAQ:NVDA) and Amazon.com Inc.\u2019s (NASDAQ:AMZN) Amazon W",
      "url": "https://finnhub.io/api/news?id=a41403a36f9d3c2b8b1d1c79e23429e580ce283652f29fcb801d753ff8d3ece6"
    }
  ],
  "polygon_news": [
    {
      "id": "61ce2421c6f489b62b4e3899e7ac171a6b2246b86d6089dc25c5f13a80d4c10f",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Billionaire Stanley Druckenmiller Dumped Broadcom and 11X'd His Fund's Stake in This Trillion-Dollar Dual-Industry Leader",
      "author": "Sean Williams",
      "published_utc": "2026-09-17T10:06:01Z",
      "article_url": "https://www.fool.com/investing/2026/09/17/billionaire-stanley-druckenmiller-dumped-broadcom-11x-fund-stake-in-trillion-dollar-dual-industry-leader/?source=iedfolrf0000001",
      "tickers": [
        "AVGO",
        "AMZN",
        "WMT"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F915c589a25edd71e373914033cad5320c095c41f-1280x853.jpg%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "Billionaire investor Stanley Druckenmiller exited his entire position in Broadcom during Q2 2026, likely taking profits after a 50%+ gain in just months. Simultaneously, he massively increased his Amazon stake by 1,083%, betting on the company's high-margin AWS cloud business which is experiencing 37% sales growth driven by AI adoption. Druckenmiller's moves suggest caution on near-term AI hype while favoring Amazon's valuation and long-term growth potential.",
      "keywords": [
        "Stanley Druckenmiller",
        "Form 13F",
        "AI bubble",
        "profit-taking",
        "cloud infrastructure",
        "valuation",
        "trillion-dollar stocks"
      ],
      "insights": [
        {
          "ticker": "AVGO",
          "sentiment": "negative",
          "sentiment_reasoning": "Druckenmiller completely exited his 195,955 share position after a 50%+ gain in one quarter. While profit-taking is cited, the article suggests deeper concerns about AI being overhyped in the near term and the potential for an AI bubble to burst, making near-term AI-focused investments risky."
        },
        {
          "ticker": "AMZN",
          "sentiment": "positive",
          "sentiment_reasoning": "Druckenmiller increased his stake by 1,083%, signaling strong conviction. AWS's 37% sales growth driven by AI, high margins, and Amazon's historically cheap valuation of 11x projected 2027 cash flow (versus historical 23-37x range) make it an attractive value play in the AI space with lower downside risk."
        },
        {
          "ticker": "WMT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as a comparison point to Amazon's e-commerce dominance (40% vs Walmart's much smaller share). No investment activity or sentiment from Druckenmiller is indicated."
        }
      ]
    },
    {
      "id": "2dd77f1e6137ef949b39e6b55405a10b8a709d814dfd6b83d4c05eb8dfaf07a1",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Salesforce vs. Figma: Evaluating the Better High-Growth Software Stock to Buy in 2026",
      "author": "Robert Izquierdo",
      "published_utc": "2026-09-16T19:36:17Z",
      "article_url": "https://www.fool.com/coverage/better-buy/2026/09/16/salesforce-vs-figma-evaluating-the-better-high-growth-software-stock-to-buy-in-2026/?source=iedfolrf0000001",
      "tickers": [
        "CRM",
        "FIG",
        "ADBE",
        "MSFT",
        "AMZN"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2Fbf1840c3c19f65b476307d856544619881ecb92d-1200x800.png%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "The article compares Salesforce and Figma as investment options in 2026. Salesforce, the dominant CRM leader, offers proven profitability with $41.5B revenue, 18% net margins, and $14.4B free cash flow, trading at a reasonable 23.3x P/E ratio. Figma, a rapidly growing design platform, shows 41% revenue growth but remains unprofitable with a negative 118.4% net margin and trades at a premium 66.2x forward P/E. The author recommends Salesforce as the better investment due to its financial stability, competitive moat through AI capabilities, and reasonable valuation, despite acknowledging Figma's impressive growth trajectory.",
      "keywords": [
        "CRM software",
        "cloud-based applications",
        "design platform",
        "AI integration",
        "SaaS stocks",
        "enterprise software",
        "profitability vs growth",
        "valuation comparison"
      ],
      "insights": [
        {
          "ticker": "CRM",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong financial fundamentals with $41.5B revenue, 18% net margins, $14.4B free cash flow, conservative debt levels, and reasonable 23.3x P/E valuation. Leadership position in CRM with competitive AI advantages through Koa platform and 27 years of data depth. Stock has rebounded strongly and is positioned well for AI-driven workplace automation."
        },
        {
          "ticker": "FIG",
          "sentiment": "neutral",
          "sentiment_reasoning": "Impressive 41% revenue growth and strong gross margins (79.14%) demonstrate market traction and transition to enterprise platform. However, company remains unprofitable with $1.3B net loss, negative 118.4% net margin, and extremely high 66.2x forward P/E valuation. Faces competition from Adobe and risks from automated design tools. Growth is compelling but valuation and profitability concerns warrant caution."
        },
        {
          "ticker": "ADBE",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive threat to Figma with bundled software solutions that may be more cost-effective for enterprise customers. Also noted as a competitive rival to Salesforce in the broader software market. No specific financial analysis provided."
        },
        {
          "ticker": "MSFT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Identified as a competitive threat to Salesforce in cloud platform services that could potentially displace market share. No specific analysis or recommendation provided."
        },
        {
          "ticker": "AMZN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as Figma's platform hosting provider, representing a dependency risk. No specific investment analysis provided."
        }
      ]
    },
    {
      "id": "e52ada18ab5c0f155acdaf95f5aff7a16b94241673d08042b0507ecb8f581cdf",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Apple Is Considering Something It Hasn't Done in 15 Years. Here's What Investors Need to Know.",
      "author": "Patrick Sanders",
      "published_utc": "2026-09-16T17:39:50Z",
      "article_url": "https://www.fool.com/investing/2026/09/16/apple-is-considering-something-it-hasnt-done-in-15-years-heres-what-investors-need-to-know/?source=iedfolrf0000001",
      "tickers": [
        "AAPL",
        "NVDA",
        "MSFT",
        "AMZN",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "META",
        "TSLA"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2Fa0e0ec9642a44babaf5b98453f1e9c442cfa3488-2122x1412.jpg%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "Apple is reportedly considering developing its own AI servers in partnership with Nvidia, marking the company's first enterprise server venture since 2011. The proposed servers would combine Apple's M8 Ultra chips with Nvidia's NVLink Fusion technology for AI inference. If approved, the product wouldn't be available until 2029. This represents a potential strategic shift under new CEO John Ternus, as Apple has historically focused on consumer devices rather than infrastructure investments like its peers in the Magnificent Seven.",
      "keywords": [
        "AI servers",
        "custom silicon",
        "enterprise hardware",
        "NVLink technology",
        "AI infrastructure",
        "M8 Ultra chips",
        "CEO transition"
      ],
      "insights": [
        {
          "ticker": "AAPL",
          "sentiment": "positive",
          "sentiment_reasoning": "Apple is exploring strategic expansion into AI server infrastructure, leveraging its strong financial position ($136.7B free cash flow) and custom chip capabilities. This represents potential new revenue streams and positions the company to compete in enterprise AI markets, though the long timeline (2029) and speculative nature warrant cautious optimism."
        },
        {
          "ticker": "NVDA",
          "sentiment": "positive",
          "sentiment_reasoning": "Nvidia's NVLink Fusion technology is being considered as the preferred solution for Apple's proposed servers, validating its advanced chip-to-chip connectivity capabilities. A partnership with Apple would expand Nvidia's enterprise reach and demonstrate the superiority of its technology in high-performance computing applications."
        },
        {
          "ticker": "MSFT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as part of the Magnificent Seven group investing heavily in AI infrastructure. No direct impact from Apple's initiative, though increased competition in enterprise AI infrastructure is implied."
        },
        {
          "ticker": "AMZN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as part of the Magnificent Seven group investing heavily in AI infrastructure. No direct impact from Apple's initiative, though increased competition in enterprise AI infrastructure is implied."
        },
        {
          "ticker": "GOOG",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as part of the Magnificent Seven group investing heavily in AI infrastructure. No direct impact from Apple's initiative, though increased competition in enterprise AI infrastructure is implied."
        },
        {
          "ticker": "GOOGL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as part of the Magnificent Seven group investing heavily in AI infrastructure. No direct impact from Apple's initiative, though increased competition in enterprise AI infrastructure is implied."
        },
        {
          "ticker": "GOOGM",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as part of the Magnificent Seven group investing heavily in AI infrastructure. No direct impact from Apple's initiative, though increased competition in enterprise AI infrastructure is implied."
        },
        {
          "ticker": "GOOGN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as part of the Magnificent Seven group investing heavily in AI infrastructure. No direct impact from Apple's initiative, though increased competition in enterprise AI infrastructure is implied."
        },
        {
          "ticker": "META",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as part of the Magnificent Seven group investing heavily in AI infrastructure. No direct impact from Apple's initiative, though increased competition in enterprise AI infrastructure is implied."
        },
        {
          "ticker": "TSLA",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as part of the Magnificent Seven group investing heavily in AI infrastructure. No direct impact from Apple's initiative."
        }
      ]
    },
    {
      "id": "c510995ddf5817aa3c100817bdd7e204ffca7da10e8376037cce7281aef80b57",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Constellation Energy vs. Vistra: 2 Very Different Bets on the Same AI Power Boom. Here's Which One I'd Buy.",
      "author": "Leo Sun",
      "published_utc": "2026-09-16T16:25:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/16/constellation-energy-vs-vistra-2-very-different-be/?source=iedfolrf0000001",
      "tickers": [
        "CEG",
        "VST",
        "MSFT",
        "META",
        "AMZN",
        "WMT"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F886286%2Fvisualization-of-an-ai-chip.jpg&w=1200&op=resize",
      "description": "Constellation Energy and Vistra are both capitalizing on AI-driven electricity demand, with stocks up 137% and 330% respectively over three years. Constellation focuses on nuclear power (22 GW capacity), while Vistra is more diversified with natural gas (62% of capacity) and smaller nuclear operations (15%). The analyst recommends Vistra as the better buy due to its lower valuation (9x 2026 EBITDA vs. Constellation's 21x P/E), greater diversification, and stronger exposure to natural gas, which powers most U.S. data centers.",
      "keywords": [
        "AI power boom",
        "electricity demand",
        "data centers",
        "nuclear energy",
        "natural gas",
        "power purchasing agreements",
        "renewable energy",
        "energy storage"
      ],
      "insights": [
        {
          "ticker": "CEG",
          "sentiment": "positive",
          "sentiment_reasoning": "Strong growth catalysts including Microsoft's 20-year PPA for Three Mile Island restart, Meta and Walmart PPAs, Calpine acquisition integration, and capacity upgrades. However, stock valuation at 21x forward earnings is considered expensive relative to growth prospects."
        },
        {
          "ticker": "VST",
          "sentiment": "positive",
          "sentiment_reasoning": "Recommended as the better investment due to more diversified energy portfolio, significant exposure to natural gas (primary data center power source), lower valuation at 9x EBITDA, and strong growth drivers including Meta and Amazon PPAs, Cogentrix acquisition, and Helix Digital Infrastructure joint venture."
        },
        {
          "ticker": "MSFT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a major customer with a 20-year PPA with Constellation Energy for Three Mile Island restart, indicating strong AI infrastructure investment but no direct sentiment on the company itself."
        },
        {
          "ticker": "META",
          "sentiment": "neutral",
          "sentiment_reasoning": "Referenced as a major customer with PPAs from both Constellation and Vistra, demonstrating significant AI data center expansion but no direct company sentiment expressed."
        },
        {
          "ticker": "AMZN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a major customer with massive AI-driven PPAs with Vistra, indicating infrastructure investment but no direct sentiment on the company itself."
        },
        {
          "ticker": "WMT",
          "sentiment": "neutral",
          "sentiment_reasoning": "Referenced as a customer with scaling PPAs with Constellation Energy but no direct sentiment analysis provided."
        }
      ]
    },
    {
      "id": "9a67fadddbc7aee6474a08e070ad5ab8d95260a3da10b9de04bbcf6639fc63f4",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Prediction: $1,000 Invested in Oracle Stock Could Be Worth This Much by 2030",
      "author": "Will Ebiefung",
      "published_utc": "2026-09-16T12:15:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/16/prediction-1000-invested-in-oracle-stock-could-be/?source=iedfolrf0000001",
      "tickers": [
        "ORCL",
        "ORCLpD",
        "NVDA",
        "MU",
        "AMZN"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F887374%2Fgettyimages-1358273775.jpg&w=1200&op=resize",
      "description": "Oracle is positioned to benefit from the generative AI boom through its cloud infrastructure and data center services, particularly via a $300 billion deal with OpenAI. However, the stock has underperformed peers like Nvidia and Micron. The company faces risks from massive capital expenditures ($90-95 billion expected in fiscal 2027), heavy concentration on OpenAI as a client, and uncertainty about long-term profitability. Analysts predict Oracle stock will deliver around 10% annual returns, turning a $1,000 investment into approximately $1,464 by 2030.",
      "keywords": [
        "generative AI",
        "cloud infrastructure",
        "capital expenditures",
        "OpenAI partnership",
        "data centers",
        "stock valuation",
        "AI spending"
      ],
      "insights": [
        {
          "ticker": "ORCL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Oracle has significant AI opportunity through OpenAI deal and cloud infrastructure positioning, but faces substantial risks including massive capex requirements, client concentration risk, and underperformance versus peers. Expected market-average returns suggest balanced risk-reward profile."
        },
        {
          "ticker": "ORCLpD",
          "sentiment": "neutral",
          "sentiment_reasoning": "Oracle has significant AI opportunity through OpenAI deal and cloud infrastructure positioning, but faces substantial risks including massive capex requirements, client concentration risk, and underperformance versus peers. Expected market-average returns suggest balanced risk-reward profile."
        },
        {
          "ticker": "NVDA",
          "sentiment": "positive",
          "sentiment_reasoning": "Nvidia is highlighted as an outperformer with 885% gains over five years, demonstrating strong execution in the AI infrastructure space and serving as a benchmark for successful AI-related investments."
        },
        {
          "ticker": "MU",
          "sentiment": "positive",
          "sentiment_reasoning": "Micron is noted as a strong performer with 1,212% gains over five years, indicating successful capitalization on AI infrastructure demand for data storage and computing power."
        },
        {
          "ticker": "AMZN",
          "sentiment": "positive",
          "sentiment_reasoning": "Amazon is presented as a diversified tech giant with multiple profitable businesses backing its $220 billion AI capex investment, providing more financial stability and risk mitigation than Oracle's concentrated approach."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 29.86454,
    "13WeekPriceReturnDaily": 4.1375,
    "26WeekPriceReturnDaily": 16.8211,
    "3MonthADReturnStd": 43.39806,
    "3MonthAverageTradingVolume": 44.89625,
    "52WeekHigh": 287.2,
    "52WeekHighDate": "2026-08-03",
    "52WeekLow": 196,
    "52WeekLowDate": "2026-02-17",
    "52WeekPriceReturnDaily": 7.3413,
    "5DayPriceReturnDaily": -1.5769,
    "assetTurnoverAnnual": 0.8764,
    "assetTurnoverTTM": 0.872,
    "beta": 1.5063177,
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
    "currentEv/freeCashFlowAnnual": 357.0461,
    "currentEv/freeCashFlowTTM": 115.2247,
    "currentRatioAnnual": 1.0508,
    "currentRatioQuarterly": 1.0331,
    "dividendIndicatedAnnual": 0,
    "dividendPerShareTTM": null,
    "ebitdPerShareAnnual": 7.4621,
    "ebitdPerShareTTM": 15.5375,
    "ebitdaCagr5Y": 28.12,
    "ebitdaInterimCagr5Y": 24.69,
    "enterpriseValue": 2747469.8,
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
    "evEbitdaTTM": 16.2657,
    "evRevenueTTM": 3.542,
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
    "marketCapitalization": 2670367.8,
    "monthToDatePriceReturnDaily": -4.3692,
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
    "pb": 4.841,
    "pbAnnual": 6.0027,
    "pbQuarterly": 4.6479,
    "pcfShareAnnual": 19.1405,
    "pcfShareTTM": 16.5447,
    "peAnnual": 34.3809,
    "peBasicExclExtraTTM": 19.7394,
    "peExclExtraTTM": 19.7394,
    "peInclExtraTTM": 19.7394,
    "peNormalizedAnnual": 34.3809,
    "peTTM": 19.7394,
    "pegTTM": 1.36953,
    "pfcfShareAnnual": 347.0264,
    "pfcfShareTTM": 170.098,
    "pretaxMargin5Y": 7.57,
    "pretaxMarginAnnual": 13.57,
    "pretaxMarginTTM": 22.62,
    "priceRelativeToS&P50013Week": 2.029,
    "priceRelativeToS&P50026Week": 4.8358,
    "priceRelativeToS&P5004Week": -2.9405,
    "priceRelativeToS&P50052Week": -7.2568,
    "priceRelativeToS&P500Ytd": -3.4423,
    "psAnnual": 3.7248,
    "psTTM": 3.4426,
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
    "yearToDatePriceReturnDaily": 7.625
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

## WMT
Trading candidate:
```json
{
  "symbol": "WMT",
  "score": 38.95,
  "direction": "WATCH",
  "sector": "Unknown",
  "components": {
    "market": 50.0,
    "sector": 50.0,
    "relative_strength": 50.93518394317374,
    "vwap": 0.0,
    "trend": 0.0,
    "volume": 40.57990269830475,
    "momentum": 66.23464953712451,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 63.62262382202264,
    "trend_acceleration": 55,
    "compression": 62.71974700027901,
    "volatility_contraction": 82.03755132412934,
    "volume_accumulation": 36.04563948274394,
    "breakout_distance": 0.0,
    "support_quality": 54.5158589898614,
    "momentum_improvement": 62.90999675934673,
    "early_setup_score": 51.22,
    "entry_timing_score": 51.22,
    "opportunity_score": 42.63,
    "extended": false,
    "return_5d": 1.56,
    "return_10d": 1.49,
    "return_20d": -6.68,
    "distance_to_breakout": 7.15,
    "atr_extension": 0.76
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
      "datetime": 1789642800,
      "headline": "Corporate DEI pullback has real consequences: Colin Kaepernick",
      "id": 142223775,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WMT",
      "source": "Yahoo",
      "summary": "Former NFL star Colin Kaepernick chats with Yahoo Finance Executive Editor Brian Sozzi about how companies putting profitability and political pressure ahead of equal opportunity risk losing consumers and market share.",
      "url": "https://finnhub.io/api/news?id=e912e14074dce2506c3f700e4f9e8f2810170e8a1afaa35565a309e683203486"
    },
    {
      "category": "company",
      "datetime": 1789639200,
      "headline": "5 Wealth-Building Stocks to Buy With an Inheritance, So You Have Something to Leave Your Kids, Too",
      "id": 142223777,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WMT",
      "source": "Yahoo",
      "summary": "With $124 trillion set to move in the Great Wealth Transfer, these wealth-building stocks can help you leave something behind for your kids.",
      "url": "https://finnhub.io/api/news?id=437e9d4adaeff009193aee00caf8c844c18b27050c61cbcd0f1a1193c1dd7a0a"
    },
    {
      "category": "company",
      "datetime": 1789639200,
      "headline": "Colin Kaepernick exposes the truth behind his NFL blacklist",
      "id": 142223776,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WMT",
      "source": "Yahoo",
      "summary": "Former NFL star Colin Kaepernick sits down with Yahoo Finance Executive Editor Brian Sozzi to reveal the shocking reality behind his NFL fallout, navigating FBI-investigated threats, and why he still wakes up at 4 a.m. to train for a comeback.",
      "url": "https://finnhub.io/api/news?id=5f6c9ad4de7d4af875428d01d5eb883b0f515d801b4f9a935dcb62210f788b6f"
    },
    {
      "category": "company",
      "datetime": 1789604252,
      "headline": "Walmart (WMT) Could Be 31% Undervalued Following Its Marketplace And Advertising Push",
      "id": 142202269,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WMT",
      "source": "Yahoo",
      "summary": "ADT Blu\u2019s DIY security kits arriving on Walmart (WMT) Marketplace put connected home squarely into the retailer\u2019s higher value mix. Investors now have a fresh data point on Walmart\u2019s marketplace and fee income ambitions. Walmart\u2019s short-term share price has cooled, with the stock down 6% over 30 days and 8% over 90 days. This comes even as recent moves in marketplace, advertising, health partnerships and fast delivery build on a 3-year total shareholder return of about 2x and a 5-year total...",
      "url": "https://finnhub.io/api/news?id=5993cb391a8531696f9b18e07abacb8f6145f7f3e4401673d171a7f0a9017fd8"
    },
    {
      "category": "company",
      "datetime": 1789602771,
      "headline": "What Has Home Depot Stopped Telling You About Where Its Goods Come From?",
      "id": 142202282,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "WMT",
      "source": "Yahoo",
      "summary": "Home Depot (HD) stock has lost about a quarter of its value over the past year, while the S&P 500 gained close to 17%. Where the goods on its shelves come from used to be something management explained at length. Now you mostly hear how fast they arrive.",
      "url": "https://finnhub.io/api/news?id=7db065353067f2401e1567db112c19c1b4a833b3f158bbe1fe04c1d8a4fe5b3c"
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
    "10DayAverageTradingVolume": 20.8908,
    "13WeekPriceReturnDaily": -10.6989,
    "26WeekPriceReturnDaily": -12.4706,
    "3MonthADReturnStd": 28.18052,
    "3MonthAverageTradingVolume": 24.18467,
    "52WeekHigh": 135.16,
    "52WeekHighDate": "2026-05-19",
    "52WeekLow": 98.88,
    "52WeekLowDate": "2025-11-14",
    "52WeekPriceReturnDaily": 4.2434,
    "5DayPriceReturnDaily": 2.1355,
    "assetTurnoverAnnual": 2.5052,
    "assetTurnoverTTM": 2.5443,
    "beta": 0.55896974,
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
    "monthToDatePriceReturnDaily": 3.0705,
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
    "priceRelativeToS&P50013Week": -12.8074,
    "priceRelativeToS&P50026Week": -24.4559,
    "priceRelativeToS&P5004Week": -4.8611,
    "priceRelativeToS&P50052Week": -10.3547,
    "priceRelativeToS&P500Ytd": -14.0473,
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
    "yearToDatePriceReturnDaily": -2.98
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

## BAC
Trading candidate:
```json
{
  "symbol": "BAC",
  "score": 45.38,
  "direction": "AVOID",
  "sector": "Financials",
  "components": {
    "market": 50.0,
    "sector": 62.62,
    "relative_strength": 0.0,
    "vwap": 100.0,
    "trend": 0.0,
    "volume": 84.41739718407874,
    "momentum": 29.343647818805337,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 34.16968191434732,
    "trend_acceleration": 25,
    "compression": 0.0,
    "volatility_contraction": 72.22318189670064,
    "volume_accumulation": 70.96334984593113,
    "breakout_distance": 0.0,
    "support_quality": 100.0,
    "momentum_improvement": 29.249491722003516,
    "early_setup_score": 27.62,
    "entry_timing_score": 27.62,
    "opportunity_score": 40.05,
    "extended": false,
    "return_5d": -7.66,
    "return_10d": -6.64,
    "return_20d": -9.91,
    "distance_to_breakout": 10.99,
    "atr_extension": -2.95
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
      "datetime": 1789642980,
      "headline": "Bank of America stock slides after CEO's troubling message",
      "id": 142223336,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "BAC",
      "source": "Yahoo",
      "summary": "Brian Moynihan told an investor conference that revenue in a key area is slowing.",
      "url": "https://finnhub.io/api/news?id=14a973ffe66a41f7f41a13614c2f5032872fedd1d8b32c10054561961d252a2f"
    },
    {
      "category": "company",
      "datetime": 1789639200,
      "headline": "Utility bills are rising faster than inflation, BofA says. Expect higher prices long-term.",
      "id": 142220189,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "BAC",
      "source": "Yahoo",
      "summary": "Utility bills grew faster than overall inflation over the summer, a Bank of America report found, as summer heat, modernization of the US power grid, and the data center build-out contribute to higher costs.",
      "url": "https://finnhub.io/api/news?id=b2805bde427843e40f050adca8f6aa124ec882b7d5c2925835501ea93f4d92a2"
    },
    {
      "category": "company",
      "datetime": 1789632769,
      "headline": "'Mastercard Inks Deal as Payment Giants Brace for New Era of AI Shopping' - Wall Street Journal",
      "id": 142226440,
      "image": "",
      "related": "BAC",
      "source": "Benzinga",
      "summary": "https://www.wsj.com/tech/ai/mastercard-inks-deal-as-payment-giants-brace-for-new-era-of-ai-shopping-eb22da8b",
      "url": "https://finnhub.io/api/news?id=02d5ce65324ce9fd4a9ef997e1f9c8ef2bd3c0f64a92ef28b9eb39856e1a70f7"
    },
    {
      "category": "company",
      "datetime": 1789610580,
      "headline": "Bank of America sees 60% upside in Everpure stock",
      "id": 142207078,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "BAC",
      "source": "Yahoo",
      "summary": "Bank of America sees a much larger storage opportunity ahead as Everpure expands its foothold with hyperscale data-center customers.",
      "url": "https://finnhub.io/api/news?id=d5bac320ad616f49d53a351529f9e87758d557d7ecd347f9145e3b0ff8a14e28"
    },
    {
      "category": "company",
      "datetime": 1789600392,
      "headline": "Bank Of America (BAC) Stock May Be 36% Undervalued After Fee Warning",
      "id": 142200958,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "BAC",
      "source": "Yahoo",
      "summary": "Bank of America has delivered a powerful multiyear run, yet the recent pullback has investors asking whether the current share price is still backed by the returns it earns on its capital. With fresh headlines on interest rates, digital assets, and fee income, the question now is how much of that return profile is already built into the valuation. Over the past 3 years the stock has gained about 117.9%, which puts a lot of weight on whether the bank's underlying return on capital can justify...",
      "url": "https://finnhub.io/api/news?id=181a9b436a62edf1478eafe4e95b1488535f85afde3aab0bc126031286a6bb37"
    }
  ],
  "polygon_news": [
    {
      "id": "be6bdc4ae8495ff133cdb151b7bcb79c344810fb2f5d1eb73b4c51e6d28c8005",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Greg Abel Has 75% of Berkshire Hathaway's Portfolio Invested in Just 8 Stocks. Is the 1 That's Lagging Behind the S&P 500 the Best Buy Now?",
      "author": "Daniel Foelber",
      "published_utc": "2026-09-17T10:30:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/17/greg-abel-berkshire-hathaway-american-express/?source=iedfolrf0000001",
      "tickers": [
        "BRK.A",
        "BRK.B",
        "AXP",
        "AAPL",
        "GOOG",
        "GOOGL",
        "GOOGM",
        "GOOGN",
        "KO",
        "MCO",
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
        "CVX",
        "OXY",
        "OXY.WS",
        "V",
        "MA"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F887380%2Fa-person-smiles-while-holding-a-credit-card-and-sitting-in-front-of-a-laptop-computer.jpg&w=1200&op=resize",
      "description": "Under new CEO Greg Abel, Berkshire Hathaway has concentrated 75% of its $365.2 billion equity portfolio into 8 stocks. American Express is the only one lagging the S&P 500 over the past year due to margin compression from high cardholder rewards and marketing expenses. Despite these headwinds, the article argues American Express offers compelling value at 19.7x trailing earnings for long-term investors who believe in its business model.",
      "keywords": [
        "Berkshire Hathaway",
        "Greg Abel",
        "portfolio concentration",
        "American Express",
        "margin compression",
        "cardholder rewards",
        "valuation"
      ],
      "insights": [
        {
          "ticker": "BRK.A",
          "sentiment": "neutral",
          "sentiment_reasoning": "Article discusses portfolio strategy under new CEO without expressing strong positive or negative outlook on the company itself."
        },
        {
          "ticker": "BRK.B",
          "sentiment": "neutral",
          "sentiment_reasoning": "Article discusses portfolio strategy under new CEO without expressing strong positive or negative outlook on the company itself."
        },
        {
          "ticker": "AXP",
          "sentiment": "positive",
          "sentiment_reasoning": "Despite underperformance vs S&P 500, article highlights strong fundamentals (double-digit revenue/EPS growth, record spending levels, raised guidance), attractive valuation at 19.7x earnings, and positions it as 'arguably the best buy' among Berkshire's top holdings despite margin pressure concerns."
        },
        {
          "ticker": "AAPL",
          "sentiment": "positive",
          "sentiment_reasoning": "Listed as a top-5 holding identified by Abel as a company Berkshire expects to compound for decades; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "GOOG",
          "sentiment": "positive",
          "sentiment_reasoning": "Catapulted to top-five holding under Abel; identified as a company expected to compound for decades; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "GOOGL",
          "sentiment": "positive",
          "sentiment_reasoning": "Catapulted to top-five holding under Abel; identified as a company expected to compound for decades; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "GOOGM",
          "sentiment": "positive",
          "sentiment_reasoning": "Catapulted to top-five holding under Abel; identified as a company expected to compound for decades; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "GOOGN",
          "sentiment": "positive",
          "sentiment_reasoning": "Catapulted to top-five holding under Abel; identified as a company expected to compound for decades; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "KO",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as a company Berkshire expects to compound for decades; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "MCO",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as a company Berkshire expects to compound for decades; part of concentrated portfolio strategy."
        },
        {
          "ticker": "BAC",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpB",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpE",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpM",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpN",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpO",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpP",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpQ",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BACpS",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BMLpG",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BMLpH",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BMLpJ",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "BMLpL",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "MERpK",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "CVX",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "OXY",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "OXY.WS",
          "sentiment": "positive",
          "sentiment_reasoning": "Core holding representing 75% of portfolio; has outperformed S&P 500 in the past year."
        },
        {
          "ticker": "V",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as comparison to American Express; noted as pure-play payment processor with different business model and lower vulnerability to economic downturns."
        },
        {
          "ticker": "MA",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as comparison to American Express; noted as pure-play payment processor with different business model and lower vulnerability to economic downturns."
        }
      ]
    },
    {
      "id": "488d864e9010ef2e45f2ef0d341d8f9f529ca9fa02ec59ea59c9cb32264f9a36",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "JPMorgan Chase Stock Is Beating Nu This Year, but Only One of Them Had Positive Free Cash Flow Last Year",
      "author": "Sarah Sidlow",
      "published_utc": "2026-09-16T12:21:01Z",
      "article_url": "https://www.fool.com/coverage/better-buy/2026/09/16/jpmorgan-chase-stock-is-beating-nu-this-year-but-only-one-of-them-had-positive-free-cash-flow-last-year/?source=iedfolrf0000001",
      "tickers": [
        "AMJB",
        "JPM",
        "JPMpC",
        "JPMpD",
        "JPMpJ",
        "JPMpK",
        "JPMpL",
        "JPMpM",
        "VYLD",
        "NU",
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
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F3caa0e2607e9485862b0d89e5f6f6be899ae6c41-1200x800.png%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "JPMorgan Chase and Nu Holdings represent two contrasting investment approaches in the financial sector. JPMorgan offers stability with $182.4B in revenue and a $937B market cap, but reported negative free cash flow of -$147.8B in FY 2025. Nu, a Latin American fintech disruptor, generated $16.3B in revenue with 45% year-over-year growth and positive free cash flow of $3.5B, though it carries higher valuation multiples and emerging market risks. The choice depends on investor preference for established stability versus high-growth potential.",
      "keywords": [
        "JPMorgan Chase",
        "Nu Holdings",
        "fintech",
        "free cash flow",
        "Latin America",
        "digital banking",
        "valuation comparison",
        "financial stocks"
      ],
      "insights": [
        {
          "ticker": "AMJB",
          "sentiment": "neutral",
          "sentiment_reasoning": "JPMorgan demonstrates strong fundamentals with massive scale, $182.4B revenue, and $57B net income, but faces headwinds from negative free cash flow (-$147.8B), declining net margins (20.4% vs 21.6%), and challenges adapting to technological disruption. Valued cheaper at 15.10 P/E, it offers stability and dividends but limited growth prospects."
        },
        {
          "ticker": "JPM",
          "sentiment": "neutral",
          "sentiment_reasoning": "JPMorgan demonstrates strong fundamentals with massive scale, $182.4B revenue, and $57B net income, but faces headwinds from negative free cash flow (-$147.8B), declining net margins (20.4% vs 21.6%), and challenges adapting to technological disruption. Valued cheaper at 15.10 P/E, it offers stability and dividends but limited growth prospects."
        },
        {
          "ticker": "JPMpC",
          "sentiment": "neutral",
          "sentiment_reasoning": "JPMorgan demonstrates strong fundamentals with massive scale, $182.4B revenue, and $57B net income, but faces headwinds from negative free cash flow (-$147.8B), declining net margins (20.4% vs 21.6%), and challenges adapting to technological disruption. Valued cheaper at 15.10 P/E, it offers stability and dividends but limited growth prospects."
        },
        {
          "ticker": "JPMpD",
          "sentiment": "neutral",
          "sentiment_reasoning": "JPMorgan demonstrates strong fundamentals with massive scale, $182.4B revenue, and $57B net income, but faces headwinds from negative free cash flow (-$147.8B), declining net margins (20.4% vs 21.6%), and challenges adapting to technological disruption. Valued cheaper at 15.10 P/E, it offers stability and dividends but limited growth prospects."
        },
        {
          "ticker": "JPMpJ",
          "sentiment": "neutral",
          "sentiment_reasoning": "JPMorgan demonstrates strong fundamentals with massive scale, $182.4B revenue, and $57B net income, but faces headwinds from negative free cash flow (-$147.8B), declining net margins (20.4% vs 21.6%), and challenges adapting to technological disruption. Valued cheaper at 15.10 P/E, it offers stability and dividends but limited growth prospects."
        },
        {
          "ticker": "JPMpK",
          "sentiment": "neutral",
          "sentiment_reasoning": "JPMorgan demonstrates strong fundamentals with massive scale, $182.4B revenue, and $57B net income, but faces headwinds from negative free cash flow (-$147.8B), declining net margins (20.4% vs 21.6%), and challenges adapting to technological disruption. Valued cheaper at 15.10 P/E, it offers stability and dividends but limited growth prospects."
        },
        {
          "ticker": "JPMpL",
          "sentiment": "neutral",
          "sentiment_reasoning": "JPMorgan demonstrates strong fundamentals with massive scale, $182.4B revenue, and $57B net income, but faces headwinds from negative free cash flow (-$147.8B), declining net margins (20.4% vs 21.6%), and challenges adapting to technological disruption. Valued cheaper at 15.10 P/E, it offers stability and dividends but limited growth prospects."
        },
        {
          "ticker": "JPMpM",
          "sentiment": "neutral",
          "sentiment_reasoning": "JPMorgan demonstrates strong fundamentals with massive scale, $182.4B revenue, and $57B net income, but faces headwinds from negative free cash flow (-$147.8B), declining net margins (20.4% vs 21.6%), and challenges adapting to technological disruption. Valued cheaper at 15.10 P/E, it offers stability and dividends but limited growth prospects."
        },
        {
          "ticker": "VYLD",
          "sentiment": "neutral",
          "sentiment_reasoning": "JPMorgan demonstrates strong fundamentals with massive scale, $182.4B revenue, and $57B net income, but faces headwinds from negative free cash flow (-$147.8B), declining net margins (20.4% vs 21.6%), and challenges adapting to technological disruption. Valued cheaper at 15.10 P/E, it offers stability and dividends but limited growth prospects."
        },
        {
          "ticker": "NU",
          "sentiment": "positive",
          "sentiment_reasoning": "Nu demonstrates exceptional growth with 45% revenue increase to $16.3B, positive free cash flow of $3.5B, expanding customer base to 139M globally, and improving net margins (18.1% vs 17.8%). Strong cash generation while reinvesting in growth, plus first-mover advantage in underbanked Latin American markets, outweigh emerging market regulatory risks and higher valuation multiples."
        },
        {
          "ticker": "BAC",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "BACpB",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "BACpE",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "BACpK",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "BACpL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "BACpM",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "BACpN",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "BACpO",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "BACpP",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "BACpQ",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "BACpS",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "BMLpG",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "BMLpH",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "BMLpJ",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "BMLpL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        },
        {
          "ticker": "MERpK",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned as a competitive peer to JPMorgan in the traditional banking sector. No specific financial data provided, but referenced as a major competitor in the established financial landscape."
        }
      ]
    },
    {
      "id": "02630d3106c4ac69f951d6cf0bc175eb8238cfe6ab3c7ceb64d28f6940b95be4",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Prediction: Warren Buffett's Successor, Greg Abel, Will Dispose of One of Berkshire Hathaway's Largest Holdings",
      "author": "Sean Williams",
      "published_utc": "2026-09-16T09:06:01Z",
      "article_url": "https://www.fool.com/investing/2026/09/16/prediction-warren-buffett-successor-greg-abel-will-dispose-one-of-berkshire-hathaway-largest-holdings/?source=iedfolrf0000001",
      "tickers": [
        "BRK.A",
        "BRK.B",
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
        "KO",
        "AXP",
        "OXY",
        "OXY.WS",
        "AAPL",
        "MCO"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fcdn.content.foolcdn.com%2Fimages%2F1umn9qeh%2Fproduction%2F3067bb9afe420729bf75ef0b6fed3a0ab059dd8b-2048x1365.jpg%3Fw%3D800%26q%3D75%26fit%3Dmax%26auto%3Dformat&w=1200&op=resize",
      "description": "Greg Abel, who took over as CEO of Berkshire Hathaway on December 31, is expected to continue selling the company's Bank of America stake. Berkshire has already sold 549.5 million BofA shares (53% of its position) since June 2024, driven by the bank's valuation reaching a 59% premium to book value and reduced interest rate sensitivity following the Fed's rate cuts.",
      "keywords": [
        "Berkshire Hathaway",
        "Greg Abel",
        "Bank of America",
        "portfolio divestment",
        "valuation",
        "interest rates",
        "succession"
      ],
      "insights": [
        {
          "ticker": "BRK.A",
          "sentiment": "neutral",
          "sentiment_reasoning": "Leadership transition is proceeding smoothly with Abel maintaining similar investment philosophy to Buffett, though actively reshaping the portfolio."
        },
        {
          "ticker": "BRK.B",
          "sentiment": "neutral",
          "sentiment_reasoning": "Leadership transition is proceeding smoothly with Abel maintaining similar investment philosophy to Buffett, though actively reshaping the portfolio."
        },
        {
          "ticker": "BAC",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "BACpB",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "BACpE",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "BACpK",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "BACpL",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "BACpM",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "BACpN",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "BACpO",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "BACpP",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "BACpQ",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "BACpS",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "BMLpG",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "BMLpH",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "BMLpJ",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "BMLpL",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "MERpK",
          "sentiment": "negative",
          "sentiment_reasoning": "Facing significant selling pressure from Berkshire due to premium valuation (59% above book value), reduced interest rate sensitivity from Fed rate cuts, and exclusion from Berkshire's 'indefinite holdings' list, signaling likely full exit."
        },
        {
          "ticker": "KO",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified as an 'indefinite' core holding by Buffett, indicating long-term confidence and commitment to the position."
        },
        {
          "ticker": "AXP",
          "sentiment": "positive",
          "sentiment_reasoning": "Listed as an 'indefinite' core holding by Buffett, demonstrating strong conviction in the company's long-term value."
        },
        {
          "ticker": "OXY",
          "sentiment": "positive",
          "sentiment_reasoning": "Designated as an 'indefinite' holding by Buffett, reflecting confidence in its long-term prospects."
        },
        {
          "ticker": "OXY.WS",
          "sentiment": "positive",
          "sentiment_reasoning": "Designated as an 'indefinite' holding by Buffett, reflecting confidence in its long-term prospects."
        },
        {
          "ticker": "AAPL",
          "sentiment": "positive",
          "sentiment_reasoning": "Identified by Abel as a holding that can 'compound over decades,' indicating strong conviction in its long-term growth potential."
        },
        {
          "ticker": "MCO",
          "sentiment": "positive",
          "sentiment_reasoning": "Highlighted by Abel as a multi-decade compounder, suggesting confidence in sustained value creation."
        }
      ]
    },
    {
      "id": "a9a2e9841f5c70792297f2b008730621e7490c73e2ab7e725707ebe25f2444d0",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "If Zero Rates Are Gone for Good, What Is a Checking Account Worth to a Bank?",
      "author": "Reuben Gregg Brewer",
      "published_utc": "2026-09-16T02:15:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/15/if-zero-rates-are-gone-for-good-what-is-a-checking/?source=iedfolrf0000001",
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
        "AGNC",
        "AGNCL",
        "AGNCM",
        "AGNCN",
        "AGNCO",
        "AGNCP",
        "AGNCZ"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F886630%2F23_04_26-a-pile-of-papers-with-percentages-and-one-on-top-of-the-pile-with-a-question-mark-_mf-dload.jpg&w=1200&op=resize",
      "description": "As interest rates rise, checking accounts become increasingly valuable to banks like Bank of America because they represent the lowest-cost source of capital available. Unlike mortgage REITs that are subject to market rates, banks have control over deposit rates and can maintain profitable spreads between borrowing and lending costs. The stickiness of customer relationships and switching costs further enhance the value of checking accounts in a higher-rate environment.",
      "keywords": [
        "checking accounts",
        "deposit base",
        "interest rates",
        "cost of capital",
        "banking model",
        "mortgage REITs",
        "customer relationships",
        "spread management"
      ],
      "insights": [
        {
          "ticker": "BAC",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "BACpB",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "BACpE",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "BACpK",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "BACpL",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "BACpM",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "BACpN",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "BACpO",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "BACpP",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "BACpQ",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "BACpS",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "BMLpG",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "BMLpH",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "BMLpJ",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "BMLpL",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "MERpK",
          "sentiment": "positive",
          "sentiment_reasoning": "The article highlights Bank of America's competitive advantages in a rising-rate environment, including control over deposit rates, a large deposit base ($957B), brand strength, and customer stickiness. These factors position the bank to maintain profitable spreads and benefit from higher rates better than mortgage REITs."
        },
        {
          "ticker": "AGNC",
          "sentiment": "negative",
          "sentiment_reasoning": "The article uses AGNC as a contrasting example to illustrate the disadvantages of mortgage REITs in rising-rate environments. Unlike banks, mREITs have little control over their cost of capital, face pressure from declining security values, and are more subject to market rate fluctuations, making them less advantaged than traditional banks."
        },
        {
          "ticker": "AGNCL",
          "sentiment": "negative",
          "sentiment_reasoning": "The article uses AGNC as a contrasting example to illustrate the disadvantages of mortgage REITs in rising-rate environments. Unlike banks, mREITs have little control over their cost of capital, face pressure from declining security values, and are more subject to market rate fluctuations, making them less advantaged than traditional banks."
        },
        {
          "ticker": "AGNCM",
          "sentiment": "negative",
          "sentiment_reasoning": "The article uses AGNC as a contrasting example to illustrate the disadvantages of mortgage REITs in rising-rate environments. Unlike banks, mREITs have little control over their cost of capital, face pressure from declining security values, and are more subject to market rate fluctuations, making them less advantaged than traditional banks."
        },
        {
          "ticker": "AGNCN",
          "sentiment": "negative",
          "sentiment_reasoning": "The article uses AGNC as a contrasting example to illustrate the disadvantages of mortgage REITs in rising-rate environments. Unlike banks, mREITs have little control over their cost of capital, face pressure from declining security values, and are more subject to market rate fluctuations, making them less advantaged than traditional banks."
        },
        {
          "ticker": "AGNCO",
          "sentiment": "negative",
          "sentiment_reasoning": "The article uses AGNC as a contrasting example to illustrate the disadvantages of mortgage REITs in rising-rate environments. Unlike banks, mREITs have little control over their cost of capital, face pressure from declining security values, and are more subject to market rate fluctuations, making them less advantaged than traditional banks."
        },
        {
          "ticker": "AGNCP",
          "sentiment": "negative",
          "sentiment_reasoning": "The article uses AGNC as a contrasting example to illustrate the disadvantages of mortgage REITs in rising-rate environments. Unlike banks, mREITs have little control over their cost of capital, face pressure from declining security values, and are more subject to market rate fluctuations, making them less advantaged than traditional banks."
        },
        {
          "ticker": "AGNCZ",
          "sentiment": "negative",
          "sentiment_reasoning": "The article uses AGNC as a contrasting example to illustrate the disadvantages of mortgage REITs in rising-rate environments. Unlike banks, mREITs have little control over their cost of capital, face pressure from declining security values, and are more subject to market rate fluctuations, making them less advantaged than traditional banks."
        }
      ]
    },
    {
      "id": "1991f40f64c1b6f246eb169cb09cb0a2ee571683f85bc41790f0476847fe8cac",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Is Bank of America Stock a Buy, Sell, or Hold After a 25% Run Off Its 52-Week Low?",
      "author": "Reuben Gregg Brewer",
      "published_utc": "2026-09-15T23:15:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/15/is-bank-of-america-stock-a-buy-sell-or-hold-after/?source=iedfolrf0000001",
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
        "VYLD"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F886646%2F23_02_20-a-list-set-up-for-showing-the-pros-and-cons-or-disadvantages-and-advantages-of-an-investment-_mf-dload.jpg&w=1200&op=resize",
      "description": "Bank of America stock has rallied 25% from its 52-week low and now appears overvalued compared to its peers. While the bank remains well-run with a 2% dividend yield, its valuation metrics (P/S, P/E, P/B ratios) have risen above five-year averages. Long-term investors may hold, but value and dividend investors should consider the elevated pricing and look elsewhere.",
      "keywords": [
        "Bank of America",
        "stock valuation",
        "dividend yield",
        "banking sector",
        "price rally",
        "investment decision"
      ],
      "insights": [
        {
          "ticker": "BAC",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "BACpB",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "BACpE",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "BACpK",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "BACpL",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "BACpM",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "BACpN",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "BACpO",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "BACpP",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "BACpQ",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "BACpS",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "BMLpG",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "BMLpH",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "BMLpJ",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "BMLpL",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "MERpK",
          "sentiment": "neutral",
          "sentiment_reasoning": "The article presents a balanced view: BAC is a well-run, large financial institution with strong fundamentals and above-market dividend yield (2%), making it attractive for long-term holders. However, after a 25% rally, valuation metrics have stretched above historical averages, making it less attractive for value investors or new buyers. The recommendation depends on investment style and entry point."
        },
        {
          "ticker": "AMJB",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as context\u2014it is the only larger bank than Bank of America. No specific analysis or recommendation is provided regarding JPMorgan Chase."
        },
        {
          "ticker": "JPM",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as context\u2014it is the only larger bank than Bank of America. No specific analysis or recommendation is provided regarding JPMorgan Chase."
        },
        {
          "ticker": "JPMpC",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as context\u2014it is the only larger bank than Bank of America. No specific analysis or recommendation is provided regarding JPMorgan Chase."
        },
        {
          "ticker": "JPMpD",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as context\u2014it is the only larger bank than Bank of America. No specific analysis or recommendation is provided regarding JPMorgan Chase."
        },
        {
          "ticker": "JPMpJ",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as context\u2014it is the only larger bank than Bank of America. No specific analysis or recommendation is provided regarding JPMorgan Chase."
        },
        {
          "ticker": "JPMpK",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as context\u2014it is the only larger bank than Bank of America. No specific analysis or recommendation is provided regarding JPMorgan Chase."
        },
        {
          "ticker": "JPMpL",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as context\u2014it is the only larger bank than Bank of America. No specific analysis or recommendation is provided regarding JPMorgan Chase."
        },
        {
          "ticker": "JPMpM",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as context\u2014it is the only larger bank than Bank of America. No specific analysis or recommendation is provided regarding JPMorgan Chase."
        },
        {
          "ticker": "VYLD",
          "sentiment": "neutral",
          "sentiment_reasoning": "Mentioned only as context\u2014it is the only larger bank than Bank of America. No specific analysis or recommendation is provided regarding JPMorgan Chase."
        }
      ]
    }
  ],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 34.8274,
    "13WeekPriceReturnDaily": 6.2478,
    "26WeekPriceReturnDaily": 22.6711,
    "3MonthADReturnStd": 20.3805,
    "3MonthAverageTradingVolume": 34.48827,
    "52WeekHigh": 65.225,
    "52WeekHighDate": "2026-08-17",
    "52WeekLow": 46.12,
    "52WeekLowDate": "2026-03-19",
    "52WeekPriceReturnDaily": 17.6517,
    "5DayPriceReturnDaily": -5.0263,
    "beta": 1.2010372,
    "bookValuePerShareAnnual": 42.0443,
    "bookValuePerShareQuarterly": 42.9033,
    "bookValueShareGrowth5Y": 5.91,
    "capexCagr5Y": null,
    "cashFlowPerShareAnnual": 1.7488,
    "cashFlowPerShareQuarterly": 13.4999,
    "cashFlowPerShareTTM": 3.81224,
    "cashPerSharePerShareAnnual": 28.78697,
    "cashPerSharePerShareQuarterly": 44.39103,
    "currentDividendYieldTTM": 2.4123,
    "currentEv/freeCashFlowAnnual": 90.1403,
    "currentEv/freeCashFlowTTM": 12.0004,
    "dividendGrowthRate5Y": 7.86,
    "dividendIndicatedAnnual": 1.28,
    "dividendPerShareAnnual": 1.2903,
    "dividendPerShareTTM": 1.3514,
    "dividendYieldIndicatedAnnual": 3.22906,
    "ebitdPerShareTTM": 9.51473,
    "ebitdaCagr5Y": 3.48988,
    "ebitdaInterimCagr5Y": 10.41612,
    "enterpriseValue": 1136940.16,
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
    "forwardPE": 12.500704379067992,
    "longTermDebt/equityAnnual": 0.9103,
    "longTermDebt/equityQuarterly": 1.1288,
    "marketCapitalization": 404880.16,
    "monthToDatePriceReturnDaily": -3.907,
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
    "pb": 1.3447,
    "pbAnnual": 1.3245,
    "pbQuarterly": 1.3281,
    "pcfShareAnnual": 32.1002,
    "pcfShareTTM": 4.2735,
    "peAnnual": 13.2708,
    "peBasicExclExtraTTM": 12.0303,
    "peExclExtraAnnual": 9.33382,
    "peExclExtraTTM": 12.0303,
    "peInclExtraTTM": 12.0303,
    "peNormalizedAnnual": 13.2708,
    "peTTM": 12.0303,
    "pegTTM": 0.9209,
    "pfcfShareAnnual": 32.1002,
    "pfcfShareTTM": 3.4403,
    "pretaxMargin5Y": 33.47932,
    "pretaxMarginAnnual": 32.61611,
    "pretaxMarginTTM": 32.73721,
    "priceRelativeToS&P50013Week": 4.1393,
    "priceRelativeToS&P50026Week": 10.6858,
    "priceRelativeToS&P5004Week": -6.0222,
    "priceRelativeToS&P50052Week": 3.0536,
    "priceRelativeToS&P500Ytd": -2.8491,
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
    "yearToDatePriceReturnDaily": 8.2182
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

## SMCI
Trading candidate:
```json
{
  "symbol": "SMCI",
  "score": 45.89,
  "direction": "WATCH",
  "sector": "Technology",
  "components": {
    "market": 50.0,
    "sector": 58.48,
    "relative_strength": 29.65339576146276,
    "vwap": 100.0,
    "trend": 0.0,
    "volume": 40.978788401531226,
    "momentum": 38.82564563792877,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 68.22243607368716,
    "relative_strength_acceleration": 35.09693206792707,
    "trend_acceleration": 25,
    "compression": 0.0,
    "volatility_contraction": 35.461364032792574,
    "volume_accumulation": 30.45912218566316,
    "breakout_distance": 0.0,
    "support_quality": 53.737620404287114,
    "momentum_improvement": 30.309206183237514,
    "early_setup_score": 20.13,
    "entry_timing_score": 20.13,
    "opportunity_score": 38.16,
    "extended": false,
    "return_5d": -5.29,
    "return_10d": 0.39,
    "return_20d": -1.48,
    "distance_to_breakout": 9.24,
    "atr_extension": -0.36
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
      "datetime": 1789592208,
      "headline": "Super Micro stock slips as investors look past massive growth estimates",
      "id": 142202738,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SMCI",
      "source": "Yahoo",
      "summary": "The AI server maker is trading at a discount even as Wall Street expects another huge jump in revenue.",
      "url": "https://finnhub.io/api/news?id=5d427586797e79854db2ab9eeb3b3029bc6038da556cc1ebbe3397bc11fe73e3"
    },
    {
      "category": "company",
      "datetime": 1789576237,
      "headline": "SMCI Has Something Nvidia Doesn\u2019t. Here\u2019s Why That Matters",
      "id": 142198478,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SMCI",
      "source": "Yahoo",
      "summary": "Nvidia designs the chips, but Supermicro builds something around them that Nvidia simply cannot sell you, and that distinction may be exactly what the market keeps getting wrong about SMCI.",
      "url": "https://finnhub.io/api/news?id=f313eed3ca74cfc7b1abbf004288261f2c8f50c35a49d38dc13d420253ea3ef0"
    },
    {
      "category": "company",
      "datetime": 1789569099,
      "headline": "Dell Rises 5% Despite Fresh Silver Lake Share Sale Filings; Super Micro Climbs 3%, Hewlett Packard Enterprise Ticks Up",
      "id": 142197184,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "SMCI",
      "source": "Yahoo",
      "summary": "Silver Lake just filed to sell more Dell shares into a session where the stock is surging, and the server complex is moving like the sponsor notices do not matter at all. Here is why buyers are ignoring the overhang and what the Fed could do to that confidence by afternoon.",
      "url": "https://finnhub.io/api/news?id=b591a854adf9ba58fece7eeb7c6a31abe5067ac589d1e9e6439904027e77510f"
    },
    {
      "category": "company",
      "datetime": 1789559584,
      "headline": "Super Micro Rebounds 3% After This Week's AI Infrastructure Selloff",
      "id": 142225301,
      "image": "https://cdn.benzinga.com/files/images/story/2026/09/16/Super-Micro-Computer-SMCI.jpg?width=2048&height=1536",
      "related": "SMCI",
      "source": "Benzinga",
      "summary": "Super Micro Computer stock surges nearly 3% premarket as investors return to AI server hardware makers following an earlier sector-wide sell-off.",
      "url": "https://finnhub.io/api/news?id=faa5ee74a3e95ba80a879369aab65d145fe7f94e5ba303876d9a2bf7fc7556f8"
    },
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
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 36.16716,
    "13WeekPriceReturnDaily": 17.0059,
    "26WeekPriceReturnDaily": 12.1107,
    "3MonthADReturnStd": 95.652435,
    "3MonthAverageTradingVolume": 52.1399,
    "52WeekHigh": 58.78,
    "52WeekHighDate": "2025-10-09",
    "52WeekLow": 19.48,
    "52WeekLowDate": "2026-03-23",
    "52WeekPriceReturnDaily": -21.4632,
    "5DayPriceReturnDaily": -8.4511,
    "assetTurnoverAnnual": 1.3045,
    "assetTurnoverTTM": 1.6313,
    "beta": 2.2036307,
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
    "monthToDatePriceReturnDaily": -4.3991,
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
    "priceRelativeToS&P50013Week": 14.8974,
    "priceRelativeToS&P50026Week": 0.1254,
    "priceRelativeToS&P5004Week": -3.4206,
    "priceRelativeToS&P50052Week": -36.0613,
    "priceRelativeToS&P500Ytd": 10.6956,
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
    "yearToDatePriceReturnDaily": 21.7629
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

## NKE
Trading candidate:
```json
{
  "symbol": "NKE",
  "score": 30.31,
  "direction": "AVOID",
  "sector": "Consumer Discretionary",
  "components": {
    "market": 50.0,
    "sector": 58.8,
    "relative_strength": 12.507641081668861,
    "vwap": 0.0,
    "trend": 0.0,
    "volume": 50.50678955201698,
    "momentum": 33.40471092077091,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 47.107969389585236,
    "trend_acceleration": 25,
    "compression": 1.8151354370287862,
    "volatility_contraction": 74.79554793154344,
    "volume_accumulation": 39.842914531033585,
    "breakout_distance": 0.0,
    "support_quality": 100.0,
    "momentum_improvement": 44.036105979418274,
    "early_setup_score": 28.45,
    "entry_timing_score": 28.45,
    "opportunity_score": 29.75,
    "extended": false,
    "return_5d": -4.15,
    "return_10d": -6.16,
    "return_20d": -10.63,
    "distance_to_breakout": 14.62,
    "atr_extension": -3.54
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
      "datetime": 1789644097,
      "headline": "Bernard Arnault's Son Takes a Nike Board Seat: Why Should NFT Holders Care?",
      "id": 142222820,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NKE",
      "source": "Yahoo",
      "summary": "Alexandre Arnault joins Nike's board with a CryptoPunk in hand, nine months after the brand dumped its NFT studio.",
      "url": "https://finnhub.io/api/news?id=1441fae353427b4220df8758061d05b29108dbc261fdb37ba128e7bec7b6a356"
    },
    {
      "category": "company",
      "datetime": 1789643700,
      "headline": "Mark Cuban says 'I've gotten beat' after investing $20M in 85 Shark Tank startups. What you can learn from his mistakes",
      "id": 142222821,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NKE",
      "source": "Yahoo",
      "summary": "There was already blood in the water.",
      "url": "https://finnhub.io/api/news?id=2dad0bdc24aa527b3b60354c65e5bd9af07bf5d46f5559426fe896bc2e2d0937"
    },
    {
      "category": "company",
      "datetime": 1789643640,
      "headline": "Nike Is Now the Highest-Yielding Stock in the Dow After Falling 79% From Its 2021 High. Is Nike an Obvious Value Stock to Buy Now?",
      "id": 142222822,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "NKE",
      "source": "Yahoo",
      "summary": "Nike looks cheap, but the turnaround still needs proving.",
      "url": "https://finnhub.io/api/news?id=b6ff0991b48fbe2c63492d07e3bbe3c771baa8f6e346dcb036f5e104c3a4b09e"
    },
    {
      "category": "company",
      "datetime": 1789639034,
      "headline": "UBS Maintains Neutral on Nike, Lowers Price Target to $42",
      "id": 142227593,
      "image": "",
      "related": "NKE",
      "source": "Benzinga",
      "summary": "UBS  analyst Jay Sole   maintains Nike (NYSE:NKE) with a Neutral and lowers the price target from $48 to $42.",
      "url": "https://finnhub.io/api/news?id=3a305fd9fcf6bd6bd8535e887f010166b467f77344af505d0ff0d329790ba0c4"
    },
    {
      "category": "company",
      "datetime": 1789620856,
      "headline": "Bill Ackman Says Nike \u2018Needs Help\u2019 as Alexandre Arnault Joins Board: \u2018Great Development\u2019",
      "id": 142227317,
      "image": "https://cdn.benzinga.com/files/images/story/2026/09/17/Nike-Q2-Earnings-Slip.jpg?width=2048&height=1536",
      "related": "NKE",
      "source": "Benzinga",
      "summary": "Bill Ackman said Nike&#39;s decision to add LVMH&#39;s Alexandre Arnault to its board was a &#39;great development&#39; for the struggling company.",
      "url": "https://finnhub.io/api/news?id=3c1269579d209b9855ae31125aa91c169bc1e357919fa5f2ebc18738e49f40b8"
    }
  ],
  "polygon_news": [
    {
      "id": "7e056850db19c21c8bd99b68509e00adfae5f4194e5aaebc5ba2f0fc621aa201",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "2 Top Stocks That Can Double in 5 Years",
      "author": "John Ballard",
      "published_utc": "2026-09-17T08:10:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/17/2-top-stocks-that-can-double-in-5-years/?source=iedfolrf0000001",
      "tickers": [
        "NFLX",
        "ONON",
        "NKE"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F887400%2Fstock-chart-moving-up-making-money.jpg&w=1200&op=resize",
      "description": "Netflix and On Holding are identified as two stocks with potential to double in five years. Netflix trades at reasonable valuations with only 7% penetration of a $670 billion addressable market and expects 13-14% revenue growth in 2026. On Holding, a footwear brand gaining share against Nike, maintains strong profitability with 65% gross margins and expects low-20% sales growth, trading at 16x forward earnings with 24% expected earnings growth.",
      "keywords": [
        "stock doubling potential",
        "Netflix",
        "On Holding",
        "earnings growth",
        "market penetration",
        "valuation",
        "footwear brand",
        "revenue growth"
      ],
      "insights": [
        {
          "ticker": "NFLX",
          "sentiment": "positive",
          "sentiment_reasoning": "Netflix is highlighted as having significant growth potential with low market penetration (less than 45% of addressable market), expected 13-14% revenue growth in 2026, 21% consensus earnings growth, and reasonable forward P/E valuation around 20x. The company demonstrates solid acquisition, retention, and pricing trends."
        },
        {
          "ticker": "ONON",
          "sentiment": "positive",
          "sentiment_reasoning": "On Holding is presented as a strong investment opportunity with disciplined brand-building strategy, gaining market share against Nike, improving gross margins (65.4% in Q2 2026), expected low-20% sales growth, and attractive 16x forward earnings valuation with 24% annualized earnings growth expectations."
        },
        {
          "ticker": "NKE",
          "sentiment": "negative",
          "sentiment_reasoning": "Nike is mentioned as struggling to find growth and facing inventory and discounting issues that weigh on financial performance, contrasting negatively with On Holding's market share gains and disciplined approach."
        }
      ]
    },
    {
      "id": "5f04d77a3aa88962f93bc316d93e01a9262dab25ee4467e5ad030dabff80a168",
      "publisher": {
        "name": "Zacks Investment Research",
        "homepage_url": "https://www.zacks.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/zacks.png",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/zacks.ico"
      },
      "title": "Nike (NKE) Registers a Bigger Fall Than the Market: Important Facts to Note",
      "author": "Zacks.Com",
      "published_utc": "2026-09-16T21:45:05Z",
      "article_url": "https://www.zacks.com/stock/news/2990938/nike-nke-registers-a-bigger-fall-than-the-market-important-facts-to-note?cid=CS-ZC-FT-fundamental_analysis|yseop_template_6-2990938",
      "tickers": [
        "NKE"
      ],
      "image_url": "https://staticx-tuner.zacks.com/images/default_article_images/default76.jpg",
      "description": "Nike stock fell 1.21% on September 16, 2026, underperforming the S&P 500's 0.45% decline. The company has depreciated 9.59% over the past month. Upcoming Q1 earnings (October 1) are expected to show a 10.2% EPS decline year-over-year to $0.44, with revenue projected at $11.43 billion, down 2.51%. Nike holds a Zacks Rank of #4 (Sell) and trades at a Forward P/E of 21.47, above its industry average of 13.64.",
      "keywords": [
        "Nike stock decline",
        "earnings forecast",
        "underperformance",
        "Zacks Rank",
        "valuation premium",
        "consumer discretionary"
      ],
      "insights": [
        {
          "ticker": "NKE",
          "sentiment": "negative",
          "sentiment_reasoning": "Nike is experiencing significant underperformance relative to the broader market, with a 9.59% monthly decline versus the S&P 500's 2.43% loss. Upcoming earnings are expected to show declining EPS (-10.2%) and revenue (-2.51%) year-over-year. The stock carries a Zacks Rank #4 (Sell) rating, trades at a valuation premium to its industry, and analyst consensus estimates have declined 0.53% over the past month, indicating weakening confidence in the company's near-term performance."
        }
      ]
    },
    {
      "id": "b4b48854b0a9240b87616950e975ed011ba0eddbc4253d70f6e99f470bc1f778",
      "publisher": {
        "name": "The Motley Fool",
        "homepage_url": "https://www.fool.com/",
        "logo_url": "https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg",
        "favicon_url": "https://s3.polygon.io/public/assets/news/favicons/themotleyfool.ico"
      },
      "title": "Nike Is Down 79%. Is It Finally the Ultimate Dividend Stock to Buy and Never Sell?",
      "author": "Keith Noonan",
      "published_utc": "2026-09-16T14:15:00Z",
      "article_url": "https://www.fool.com/investing/2026/09/16/nike-is-down-79-is-it-finally-the-ultimate-dividen/?source=iedfolrf0000001",
      "tickers": [
        "NKE"
      ],
      "image_url": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F887269%2Fstacks-of-gold-copy.jpg&w=1200&op=resize",
      "description": "Nike's stock has declined 79% from its peak, pushing its dividend yield to a record 4.5%, making it potentially attractive for income investors. However, the company faces significant challenges including failed growth strategies, declining revenue in Greater China due to competition from domestic brands, and unintended consequences from its direct-to-consumer sales focus that weakened retail partnerships. While Nike maintains solid financials and a 24-year dividend growth streak, the company faces execution risks and the possibility of dividend cuts if earnings continue to decline.",
      "keywords": [
        "dividend yield",
        "stock decline",
        "Greater China revenue",
        "direct-to-consumer strategy",
        "dividend growth",
        "execution risk",
        "retail partnerships"
      ],
      "insights": [
        {
          "ticker": "NKE",
          "sentiment": "neutral",
          "sentiment_reasoning": "Nike presents a mixed investment case. While the elevated 4.5% dividend yield and solid balance sheet ($9B cash vs $11B debt) offer appeal to income investors, significant operational challenges including 11% YoY revenue decline in Greater China, loss of market share to domestic competitors, and weakened retail relationships create substantial execution risks. The company's depressed earnings and potential for dividend cuts offset the attractiveness of the current yield, warranting a cautious neutral stance rather than a clear buy or sell recommendation."
        }
      ]
    },
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
    }
  ],
  "earnings": [
    {
      "symbol": "NKE",
      "date": "2026-12-16",
      "hour": "",
      "quarter": 2,
      "year": 2027,
      "epsEstimate": 0.5388,
      "epsActual": null,
      "revenueEstimate": 11997610553,
      "revenueActual": null
    }
  ],
  "fundamentals": {
    "10DayAverageTradingVolume": 27.61008,
    "13WeekPriceReturnDaily": -19.3857,
    "26WeekPriceReturnDaily": -34.9731,
    "3MonthADReturnStd": 31.885578,
    "3MonthAverageTradingVolume": 24.66102,
    "52WeekHigh": 76.97,
    "52WeekHighDate": "2025-10-02",
    "52WeekLow": 36.17,
    "52WeekLowDate": "2026-09-15",
    "52WeekPriceReturnDaily": -50.4039,
    "5DayPriceReturnDaily": -3.0254,
    "assetTurnoverAnnual": 1.208,
    "assetTurnoverTTM": 1.2324,
    "beta": 1.0616423,
    "bookValuePerShareAnnual": 10.0379,
    "bookValuePerShareQuarterly": 10.0379,
    "bookValueShareGrowth5Y": 4.41,
    "capexCagr5Y": -0.32,
    "cashFlowPerShareAnnual": 1.4748,
    "cashFlowPerShareQuarterly": 1.4748,
    "cashFlowPerShareTTM": 3.82458,
    "cashPerSharePerShareAnnual": 6.0957,
    "cashPerSharePerShareQuarterly": 6.0957,
    "currentDividendYieldTTM": 4.5347,
    "currentEv/freeCashFlowAnnual": 24.4774,
    "currentEv/freeCashFlowTTM": 24.4774,
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
    "enterpriseValue": 53458.586,
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
    "evEbitdaTTM": 11.7647,
    "evRevenueTTM": 1.1522,
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
    "marketCapitalization": 53079.586,
    "monthToDatePriceReturnDaily": -7.2709,
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
    "pb": 3.5708,
    "pbAnnual": 4.5757,
    "pbQuarterly": 4.5757,
    "pcfShareAnnual": 18.5075,
    "pcfShareTTM": 18.5075,
    "peAnnual": 17.0784,
    "peBasicExclExtraTTM": 17.0784,
    "peExclExtraAnnual": 33.32807,
    "peExclExtraTTM": 17.0784,
    "peInclExtraTTM": 17.0784,
    "peNormalizedAnnual": 17.0784,
    "peTTM": 17.0784,
    "pegTTM": 2.44825,
    "pfcfShareAnnual": 24.3038,
    "pfcfShareTTM": 24.3038,
    "pretaxMargin5Y": 11.24,
    "pretaxMarginAnnual": 8.41,
    "pretaxMarginTTM": 8.41,
    "priceRelativeToS&P50013Week": -21.4942,
    "priceRelativeToS&P50026Week": -46.9584,
    "priceRelativeToS&P5004Week": -8.2748,
    "priceRelativeToS&P50052Week": -65.002,
    "priceRelativeToS&P500Ytd": -54.2159,
    "psAnnual": 1.144,
    "psTTM": 1.144,
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
    "yearToDatePriceReturnDaily": -43.1486
  },
  "source_status": {
    "local_research": true,
    "local_news": true,
    "local_sec_filings": true,
    "finnhub_news": true,
    "polygon_news": true,
    "earnings": true,
    "fundamentals": true
  }
}
```

## PCG
Trading candidate:
```json
{
  "symbol": "PCG",
  "score": 24.06,
  "direction": "AVOID",
  "sector": "Utilities",
  "components": {
    "market": 50.0,
    "sector": 54.37,
    "relative_strength": 0.0,
    "vwap": 0.0,
    "trend": 0.0,
    "volume": 16.67107111128682,
    "momentum": 30.923970432946142,
    "volatility": 50.0,
    "options": 50.0,
    "premarket": 50.0,
    "extension": 100.0,
    "relative_strength_acceleration": 53.2268914596339,
    "trend_acceleration": 25,
    "compression": 0.0,
    "volatility_contraction": 26.99839486356342,
    "volume_accumulation": 43.67002764041829,
    "breakout_distance": 0.0,
    "support_quality": 85.76779026217233,
    "momentum_improvement": 51.0291597737596,
    "early_setup_score": 25.26,
    "entry_timing_score": 25.26,
    "opportunity_score": 24.42,
    "extended": false,
    "return_5d": -6.02,
    "return_10d": -5.05,
    "return_20d": -25.11,
    "distance_to_breakout": 37.53,
    "atr_extension": -2.55
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
      "datetime": 1789649100,
      "headline": "Itron Unveils Itron Inspire 2026 Lineup Focused on Proven Approaches to Utility Challenges",
      "id": 142226939,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PCG",
      "source": "Yahoo",
      "summary": "Opening General Session to Feature Leaders from Host Utility CenterPoint Energy and Pacific Gas & Electric, Duquesne Light Company, San Antonio Water System and Spire EnergyLIBERTY LAKE, Wash., Sept. 17, 2026 (GLOBE NEWSWIRE) -- Itron, Inc. (NASDAQ: ITRI), the infrastructure provider for modern energy and water management, revealed the speaker lineup for its premier customer-focused event, Itron Inspire 2026. The event will take place in Houston, TX, Oct. 16-21, 2026, with CenterPoint Energy ser",
      "url": "https://finnhub.io/api/news?id=0c44f6d2cdb1fe9ed69f8293ce167a7df3361eda330a4e34d93028eb741fc13b"
    },
    {
      "category": "company",
      "datetime": 1789525113,
      "headline": "Is PG&E Stock Cheap, Or Just Waiting On California?",
      "id": 142174579,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PCG",
      "source": "Yahoo",
      "summary": "PG&E (PCG) has lost about 13% over the past twelve months while the S&P 500 gained 17%. The California utility now trades at 9.5 times earnings against an S&P 500 median of 22.9, the kind of gap value buyers hunt for. So what has the market marked down: the utility, or the state it operates in.",
      "url": "https://finnhub.io/api/news?id=d443b2fbae594302beb5d64b44ef69df66fe07b2e3929cca42bb7d9f14f9850d"
    },
    {
      "category": "company",
      "datetime": 1789490101,
      "headline": "Discover which S&P500 stocks are making waves on Tuesday.",
      "id": 142164766,
      "image": "https://www.chartmill.com/images/uploads/CM_Top_Movers_Small_free_2b4ff2fc22.webp",
      "related": "PCG",
      "source": "ChartMill",
      "summary": "Curious about the S&P500 stocks that are in motion on Tuesday? Join us as we explore the top movers within the S&P500 index during today's session.",
      "url": "https://finnhub.io/api/news?id=23931929989dd5bdd640d3c96eb27ee2ac994dff22b15bbefaedb838e51d0aff"
    },
    {
      "category": "company",
      "datetime": 1789486802,
      "headline": "PCG vs. WEC: Which Stock Is the Better Value Option?",
      "id": 142166214,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PCG",
      "source": "Yahoo",
      "summary": "PCG vs. WEC: Which Stock Is the Better Value Option?",
      "url": "https://finnhub.io/api/news?id=5bc6f789b1549b22634f242f9ea0df3836cfacd993b04e0f0828c193f0f5aad9"
    },
    {
      "category": "company",
      "datetime": 1789479605,
      "headline": "Should Value Investors Buy PG&E (PCG) Stock?",
      "id": 142162227,
      "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
      "related": "PCG",
      "source": "Yahoo",
      "summary": "Here at Zacks, our focus is on the proven Zacks Rank system, which emphasizes earnings estimates and estimate revisions to find great stocks. Nevertheless, we are always paying attention to the latest value, growth, and momentum trends to underscore strong picks.",
      "url": "https://finnhub.io/api/news?id=d431b1eaa7b2ea8daca03214b9f1f8426aacb9f8ccbf5cfaa293133a742d28e8"
    }
  ],
  "polygon_news": [],
  "earnings": [],
  "fundamentals": {
    "10DayAverageTradingVolume": 63.5485,
    "13WeekPriceReturnDaily": -22.4189,
    "26WeekPriceReturnDaily": -27.5083,
    "3MonthADReturnStd": 53.427658,
    "3MonthAverageTradingVolume": 28.07761,
    "52WeekHigh": 19.16,
    "52WeekHighDate": "2026-03-02",
    "52WeekLow": 12.59,
    "52WeekLowDate": "2026-09-02",
    "52WeekPriceReturnDaily": -14.2764,
    "5DayPriceReturnDaily": -7.3291,
    "assetTurnoverAnnual": 0.1761,
    "assetTurnoverTTM": 0.1823,
    "beta": 0.19172178,
    "bookValuePerShareAnnual": 14.8048,
    "bookValuePerShareQuarterly": 15.393,
    "bookValueShareGrowth5Y": 6.95,
    "capexCagr5Y": 8.92,
    "cashFlowPerShareAnnual": -1.3972,
    "cashFlowPerShareQuarterly": -1.9356,
    "cashFlowPerShareTTM": 2.65106,
    "cashPerSharePerShareAnnual": 0.3244,
    "cashPerSharePerShareQuarterly": 0.4413,
    "currentDividendYieldTTM": 1.4523,
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
    "enterpriseValue": 92647.598,
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
    "evEbitdaTTM": 9.3982,
    "evRevenueTTM": 3.5858,
    "focfCagr5Y": null,
    "forwardPE": 10.22545,
    "forwardPEG": 1.09951,
    "grossMarginTTM": 35.88346,
    "inventoryTurnoverAnnual": 4.5317,
    "inventoryTurnoverTTM": 4.9445,
    "longTermDebt/equityAnnual": 1.7636,
    "longTermDebt/equityQuarterly": 1.822,
    "marketCapitalization": 29401.598,
    "monthToDatePriceReturnDaily": -0.9043,
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
    "pb": 0.8673,
    "pbAnnual": 1.0854,
    "pbQuarterly": 1.0926,
    "pcfShareAnnual": 3.3733,
    "pcfShareTTM": 3.6089,
    "peAnnual": 10.8774,
    "peBasicExclExtraTTM": 9.2867,
    "peExclExtraAnnual": 21.34363,
    "peExclExtraTTM": 9.2867,
    "peInclExtraTTM": 9.2867,
    "peNormalizedAnnual": 10.8774,
    "peTTM": 9.2867,
    "pegTTM": 1.39517,
    "pfcfShareAnnual": 87.5048,
    "pfcfShareTTM": 39.7857,
    "pretaxMargin5Y": 5.57,
    "pretaxMarginAnnual": 9.72,
    "pretaxMarginTTM": 10.68,
    "priceRelativeToS&P50013Week": -24.5274,
    "priceRelativeToS&P50026Week": -39.4936,
    "priceRelativeToS&P5004Week": -24.8957,
    "priceRelativeToS&P50052Week": -28.8745,
    "priceRelativeToS&P500Ytd": -29.2378,
    "psAnnual": 1.1791,
    "psTTM": 1.138,
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
    "yearToDatePriceReturnDaily": -18.1705
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