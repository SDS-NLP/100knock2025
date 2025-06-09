from gensim.models import KeyedVectors

model_path = 'GoogleNews-vectors-negative300.bin'

# Load the pre-trained word vectors
print("Loading word vectors...")
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("Word vectors loaded.")

# Get the vector for "United States"
word = "United_States"
vector = model[word]
print(f"Vector for '{word}':\n{vector}")