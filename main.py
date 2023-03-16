import nltk
nltk.download('punkt')

# Sample text to tokenize
text = "Machine learning is a field of study that uses algorithms to learn from data and make predictions or decisions without being explicitly programmed."

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Print the tokens
print(tokens)

# Calculate the frequency distribution of words
freq_dist = nltk.FreqDist(tokens)

# Print the most common words
print(freq_dist.most_common(5))
