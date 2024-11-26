import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

# Fetch semiconductor news headlines
url = f"https://newsapi.org/v2/everything?q=NVDA&apiKey={NEWSAPI_KEY}"
# add language=eng 

response = requests.get(url)
data = response.json()

# Save the results
with open("data/raw/news_headlines.json", "w") as file:
    import json
    json.dump(data, file, indent=4)

print("News headlines saved to data/raw/news_headlines.json!")
