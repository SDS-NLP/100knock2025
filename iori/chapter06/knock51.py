from gensim.models import KeyedVectors

model_path = 'GoogleNews-vectors-negative300.bin'

# Load the pre-trained word vectors
print("Loading word vectors...")
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("Word vectors loaded.")

# Words to compare
word1 = "United_States"
word2 = "U.S."

# Calculate cosine similarity
similarity = model.similarity(word1, word2)
print(f"Cosine similarity between '{word1}' and '{word2}': {similarity}")
