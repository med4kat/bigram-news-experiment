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

# Calculate average sentiment
if sentiment_results:
    avg_polarity = sum(item["polarity"] for item in sentiment_results) / len(sentiment_results)
    avg_subjectivity = sum(item["subjectivity"] for item in sentiment_results) / len(sentiment_results)

    print(f"Average Polarity: {avg_polarity:.2f}")
    print(f"Average Subjectivity: {avg_subjectivity:.2f}")
else:
    print("No sentiment results available.")

# Filter sentiment results for a specific company (e.g., NVIDIA)
company_name = "nvidia"  # Change this to your chosen company
filtered_results = [
    result for result in sentiment_results if company_name in result["headline"].lower()
]

# Save the filtered results
with open(f"data/processed/{company_name}_sentiment_results.json", "w") as file:
    json.dump(filtered_results, file, indent=4)

print(f"Sentiment results for {company_name} saved to data/processed/{company_name}_sentiment_results.json!")
