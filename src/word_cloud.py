from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Your existing bigram list
bigrams = [
    [["smart", "glasses"], 4],
    [["lowest", "price"], 3],
    [["motorola", "razr"], 3],
    [["samsung", "galaxy"], 3],
    [["la", "gama"], 3],
    [["pixel", "9"], 3],
    [["9", "pro"], 3],
    [["iphone", "17"], 3],
    [["surface", "pro"], 3],
    [["surface", "laptop"], 3],
    [["pro", "2"], 3],
    [["apple", "’"], 2],
    [["’", "latest"], 2],
    [["one", "ui"], 2],
    [["ui", "8"], 2],
    [["razr", "plus"], 2],
    [["ipad", "air"], 2],
    [["gama", "media"], 2],
    [["all-time", "low"], 2],
    [["17", "air"], 2]
]

# Convert to a frequency dictionary with joined strings
freq_dict = {" ".join(pair): count for pair, count in bigrams}

# Generate and display the word cloud
wc = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(freq_dict)

plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Bigram Word Cloud")
plt.tight_layout()
plt.show()