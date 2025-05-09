import yfinance as yf
import json
from datetime import datetime, timedelta

today = datetime.today()
start = today - timedelta(days=7) 

# Get 1-minute intraday data for a specific day
ticker = yf.Ticker("NVDA")
df = ticker.history(interval="1m", start=start.strftime('%Y-%m-%d'), end=today.strftime('%Y-%m-%d'))  
df.reset_index(inplace=True)

print(df.head())

# Save to a JSON file
output_file = "data/processed/stock_data_NVDA.json"
with open(output_file, "w") as file:
    json.dump(df.to_dict(orient="records"), file, indent=4, default=str)

print(f"Stock data saved to {output_file}")