from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
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

# Perform hierarchical clustering using Ward's method
print("Performing hierarchical clustering...")
linkage_matrix = linkage(country_vectors, method='ward')
print("Clustering completed.")

# Plot the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linkage_matrix, labels=valid_countries, leaf_rotation=90, leaf_font_size=10)
plt.title("Dendrogram of Country Word Vectors")
plt.xlabel("Countries")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()