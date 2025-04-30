import json
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import bigrams
from collections import Counter

# Load the JSON file
with open("data/raw/news_headlines.json", "r") as file:
    data = json.load(file)

# Preview the headlines
articles = data.get("articles", [])
for i, article in enumerate(articles[:5]):  # Show first 5 headlines
    print(f"{i+1}. {article['title']}")

# Download NLTK resources (run once)
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')

# Extract headlines
articles = data.get("articles", [])
headlines = [article["title"] for article in articles if "title" in article]

# Preprocessing function
def clean_and_tokenise(text):
    stop_words = set(stopwords.words("english"))
    punctuations = set(string.punctuation)
    
    # Lowercase the text
    text = text.lower()
    # Tokenise into words
    tokens = word_tokenize(text)
    # Remove stopwords and punctuation
    tokens = [word for word in tokens if word not in stop_words and word not in punctuations]
    
    return tokens

# Clean and tokenise headlines
processed_headlines = [clean_and_tokenise(headline) for headline in headlines]

# Save the cleaned data. We don't need the file, but it's good to have it available to learn.
with open("data/processed/processed_headlines.json", "w") as file:
    json.dump(processed_headlines, file, indent=4)

print("Cleaned and tokenised data saved to data/processed/processed_headlines.json!")

# Generate bigrams for all tokenised headlines
all_bigrams = []
for tokens in processed_headlines:
    bigram_list = list(bigrams(tokens))
    all_bigrams.extend(bigram_list)

# Count bigram frequencies
bigram_counts = Counter(all_bigrams)

# Save bigram frequencies
with open("data/processed/bigram_counts.json", "w") as file:
    json.dump(bigram_counts.most_common(20), file, indent=4)

print("Top 20 bigrams saved to data/processed/bigram_counts.json!") 