import json

# Load bigram frequencies
with open("data/processed/bigram_counts.json", "r") as file:
    bigram_data = json.load(file)

# Define bigrams of interest and thresholds
events = {
    ("chip", "shortage"): "Potential supply chain issues",
    ("price", "rise"): "Bullish sentiment",
    ("demand", "increase"): "Growing demand",
    ("semiconductor", "manufacturing"): "Testing works"
}

# Detect events based on bigram counts
detected_events = []
for bigram, count in bigram_data:
    if tuple(bigram) in events:
        detected_events.append({"bigram": bigram, "count": count, "event": events[tuple(bigram)]})

# Save detected events
with open("data/processed/detected_events.json", "w") as file:
    json.dump(detected_events, file, indent=4)

print("Detected events saved to data/processed/detected_events.json!")

# Flexible event detection based on keywords
keywords = {
    "chip": "Possible chip-related event",
    "price": "Possible price-related event",
    "demand": "Possible demand-related event"
}

detected_events_by_keywords = []
for bigram, count in bigram_data:
    for word in bigram:
        if word in keywords:
            detected_events.append({"bigram": bigram, "count": count, "event": keywords[word]})

