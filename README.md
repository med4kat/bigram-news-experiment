# Bigrams and Disappointment: A Very Short AI Adventure

**Can you predict financial events from news headlines using bigrams and sentiment analysis?**  
Not really — but here's what I tried anyway.

---

## TL;DR

This project was a curious dive into *Statistical Language Models*, sentiment analysis, and market correlation — using real semiconductor news and stock data. It didn’t work. But it was fun, and I learned a lot.

---


## What This Project Does

- Collects **daily semiconductor news** via NewsAPI
- Extracts **bigrams** using NLTK
- Runs **sentiment analysis** using TextBlob
- Attempts to correlate sentiment with **stock price data** from yFinance
- Outputs:
  - Top bigrams
  - Sentiment scores per headline
  - Basic price/sentiment correlation

---

## What I Learned

- **Bigrams** often look like nonsense (`'quarter quarter'`, `'latest latest'`)
- **Sentiment scores** tend to be neutral (most news is factual or clickbait)
- **No strong correlation** between sentiment and daily price change or volume

---

## Structure
```plaintext
.
├── data/
│   ├── raw/               # Raw downloaded data
│   ├── processed/         # Cleaned sentiment & stock results
├── src/
│   ├── news_collection.py
│   ├── bigram_analysis.py
│   ├── sentiment_analysis.py
│   ├── stock_data_collection.py
│   ├── sentiment_vs_stock_analysis.py
├── requirements.txt
└── README.md
```

---

## Example Outputs
### Top Bigrams
```
[  
    [[smart, glasses], 4],
    [[lowest, price], 3],
    [[motorola, razr], 3],
    [[samsung, galaxy], 3],
]
```
### Correlation Matrix

|                | Polarity | Price Change | Volume |
|----------------|----------|---------------|--------|
| **Polarity**   | 1.00     | -0.02         | -0.06  |
| **Price Change** | -0.02  | 1.00          | 0.06   |
| **Volume**     | -0.06    | 0.06          | 1.00   |

---

# Project Requirements

This project requires Python 3 and several common packages for NLP, sentiment analysis, stock data handling, and visualisation.

## Installation Guide

1. **Create a virtual environment** (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2.	**Install required packages manually:**
   
   ```
   pip install nltk textblob yfinance wordcloud pandas matplotlib requests python-dotenv
  ```

  Or create a requirements.txt from your environment:

  ```
  pip freeze > requirements.txt
  ```

  Then install it with:

  ```
  pip install -r requirements.txt
  ```

**Python Packages:**

- **nltk** — For tokenising text and extracting bigrams
- **textblob** — For basic sentiment analysis
- **yfinance** — To fetch stock market data
- **wordcloud** — To visualise most frequent bigrams
- **pandas** — For structured data analysis
- **matplotlib** — (Optional) For plotting or visualisations
- **requests** — To fetch news via API
- **python-dotenv** — To manage API keys securely

# License

MIT — feel free to fork, remix, or make fun of it 😄
