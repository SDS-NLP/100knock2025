#!/usr/bin/env python
# coding: utf-8

# In[2]:


from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
from collections import defaultdict
import numpy as np

model_path = "/Users/niaomuqing/100knock2025/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("Word2Vec model loaded.\n")

country_path = "/Users/niaomuqing/100knock2025/countries.txt"
with open(country_path, 'r', encoding='utf-8') as f:
    countries = [line.strip().lower() for line in f if line.strip()]

country_vectors = []
valid_countries = []

for country in countries:
    if country in model:
        country_vectors.append(model[country])
        valid_countries.append(country)

print(f"Found {len(valid_countries)} valid countries out of {len(countries)} total.\n")

kmeans = KMeans(n_clusters=5, random_state=42, n_init='auto')
labels = kmeans.fit_predict(country_vectors)

clusters = defaultdict(list)
for country, label in zip(valid_countries, labels):
    clusters[label].append(country)

print("Clustering result (k=5):")
for cluster_id, members in clusters.items():
    print(f"\nCluster {cluster_id}:")
    print(", ".join(members))

