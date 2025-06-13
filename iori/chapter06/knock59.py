from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

model_path = 'GoogleNews-vectors-negative300.bin'

# Load the pre-trained word vectors
print("Loading word vectors...")
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("Word vectors loaded.")

# Load country names from the file
with open('countries.txt', 'r') as f:
    countries = [line.strip() for line in f.readlines()]

# Extract word vectors for the countries
country_vectors = []
valid_countries = []
for country in countries:
    if country in model:
        country_vectors.append(model[country])
        valid_countries.append(country)

# Perform t-SNE to reduce dimensionality to 2D
print("Performing t-SNE...")
tsne = TSNE(n_components=2, random_state=42, perplexity=10)
country_vectors_2d = tsne.fit_transform(np.array(country_vectors))
print("t-SNE completed.")

# Plot the 2D representation of country vectors
plt.figure(figsize=(12, 8))
for i, country in enumerate(valid_countries):
    plt.scatter(country_vectors_2d[i, 0], country_vectors_2d[i, 1], marker='o', color='blue')
    plt.text(country_vectors_2d[i, 0] + 0.5, country_vectors_2d[i, 1] + 0.5, country, fontsize=9)
plt.title("t-SNE visualization of country word vectors")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.grid(True)
plt.show()