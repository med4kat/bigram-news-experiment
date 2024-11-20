import json
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json

# Load the JSON file
with open("data/raw/news_headlines.json", "r") as file:
    data = json.load(file)

# Preview the headlines
articles = data.get("articles", [])
for i, article in enumerate(articles[:5]):  # Show first 5 headlines
    print(f"{i+1}. {article['title']}")

# Download NLTK resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Load data from the JSON file
with open("data/raw/news_headlines.json", "r") as file:
    data = json.load(file)

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

# Save the cleaned data
with open("data/processed/processed_headlines.json", "w") as file:
    json.dump(processed_headlines, file, indent=4)

print("Cleaned and tokenised data saved to data/processed/processed_headlines.json!")
