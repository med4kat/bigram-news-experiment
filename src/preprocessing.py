import json

# Load the JSON file
with open("data/raw/news_headlines.json", "r") as file:
    data = json.load(file)

# Preview the headlines
articles = data.get("articles", [])
for i, article in enumerate(articles[:5]):  # Show first 5 headlines
    print(f"{i+1}. {article['title']}")
