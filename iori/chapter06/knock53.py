from gensim.models import KeyedVectors

model_path = 'GoogleNews-vectors-negative300.bin'

# Load the pre-trained word vectors
print("Loading word vectors...")
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("Word vectors loaded.")

vector = model['Spain'] - model['Madrid'] + model['Athens']

# Find the top 10 most similar words to the resulting vector
similar_words = model.similar_by_vector(vector, topn=10)

# Print the results
for word, similarity in similar_words:
    print(f"{word}: {similarity:.4f}")