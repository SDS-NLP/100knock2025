from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
import numpy as np

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

# Perform k-means clustering
k = 5
kmeans = KMeans(n_clusters=k, random_state=0)
clusters = kmeans.fit_predict(np.array(country_vectors))

# Print the clustering results
for cluster_id in range(k):
    print(f"Cluster {cluster_id}:")
    for i, country in enumerate(valid_countries):
        if clusters[i] == cluster_id:
            print(f"  {country}")