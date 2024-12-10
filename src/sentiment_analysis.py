from textblob import TextBlob
import json
import re

# Load raw collected data
with open("data/raw/news_headlines.json", "r") as file:
    raw_data = json.load(file)

# Preprocess data for sentiment
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^A-Za-z0-9 .,!?]', '', text)  # Keep letters, numbers, and basic punctuation
    return text.strip()

# Perform sentiment analysis
sentiment_results = []
for article in raw_data.get("articles", []):
    headline = clean_text(article["title"])
    if headline.lower() in {"removed", ""}:  # Skip invalid or empty headlines
        continue
    sentiment = TextBlob(headline).sentiment
    sentiment_results.append({
        "headline": headline,
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity
    })


# Save sentiment results
with open("data/processed/sentiment_results.json", "w") as file:
    json.dump(sentiment_results, file, indent=4)

print("Sentiment analysis results saved to data/processed/sentiment_results.json!")
