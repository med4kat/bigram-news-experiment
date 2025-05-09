import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load API key from .env file
load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

# Fetch semiconductor news headlines
# url = f"https://newsapi.org/v2/everything?q=NVDA&q=AMD&q=INTC&q=QCOM&q=TSM&from=2024-11-27&to=2024-11-30&sortBy=popularity&apiKey={NEWSAPI_KEY}"
# add language=eng 

# Fetch news headlines from the last 24 hours AI chip, GPU manufacturing, tech innovation, processor technology:
today = datetime.today().strftime('%Y-%m-%d')
a_year_ago = datetime.today().replace(year=datetime.today().year-1).strftime('%Y-%m-%d')
a_month_ago = datetime.today().replace(month=datetime.today().month-1).strftime('%Y-%m-%d')
a_week_ago = datetime.today().replace(day=datetime.today().day-7).strftime('%Y-%m-%d')
a_day_ago = datetime.today().replace(day=datetime.today().day-1).strftime('%Y-%m-%d')
url = f"https://newsapi.org/v2/everything?q=AI+chip&q=GPU+manufacturing&q=tech+innovation&q=processor+technology&from={a_week_ago}&to={today}&sortBy=popularity&apiKey={NEWSAPI_KEY}"

response = requests.get(url)
data = response.json()

# Save the results
with open("data/raw/news_headlines.json", "w") as file:
    import json
    json.dump(data, file, indent=4)

print("News headlines saved to data/raw/news_headlines.json!")
