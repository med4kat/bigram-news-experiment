import yfinance as yf
import json
from datetime import datetime, timedelta

# List of tickers for companies to tract, for the first time try NVDA only
tickers = ["NVDA"]

# Fetch historical data
def fetch_stock_data(ticker, date="2024-12-18"):
    stock = yf.Ticker(ticker)
    start_date = datetime.strptime(date, '%Y-%m-%d')
    end_date = start_date + timedelta(days=1) # Add one day to include full day range
    data = stock.history(start=start_date, end=end_date)
    # Convert datetime index to a column for easier processing
    data.reset_index(inplace=True)
    return data

nvda_data = fetch_stock_data("NVDA", date='2024-12-17')
print(nvda_data)

