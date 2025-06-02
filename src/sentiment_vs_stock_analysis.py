import json
import pandas as pd

# Load sentiment results
with open("data/processed/sentiment_results.json", "r") as file:
    sentiment_data = json.load(file)

# Load stock data
with open("data/processed/stock_data.json", "r") as file:
    stock_data = json.load(file)

# Calculate average daily sentiment polarity
sentiment_df = pd.DataFrame(sentiment_data)
sentiment_df["date"] = pd.to_datetime(sentiment_df["timestamp"]).dt.date
# sentiment_df["date"] = pd.to_datetime(sentiment_df["headline"].str.extract(r'(\d{4}-\d{2}-\d{2})')[0])
daily_sentiment = sentiment_df.groupby("date")["polarity"].mean().reset_index()

# Analyze stock data for a specific ticker (e.g., NVDA)
ticker = "NVDA"
stock_df = pd.DataFrame(stock_data)

stock_df["Date"] = pd.to_datetime(stock_df["Datetime"]).dt.date

# Merge sentiment with stock data
merged_data = pd.merge(daily_sentiment, stock_df, left_on="date", right_on="Date")

# Calculate daily price change
merged_data["price_change"] = merged_data["Close"].pct_change() * 100

# Correlation analysis
correlation = merged_data[["polarity", "price_change", "Volume"]].corr()
print("Correlation Matrix:")
print(correlation)

# Save merged data for further exploration
merged_data.to_csv("data/processed/sentiment_stock_correlation.csv", index=False)
print("Merged sentiment and stock data saved to data/processed/sentiment_stock_correlation.csv")
