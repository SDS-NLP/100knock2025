#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from gensim.models import KeyedVectors

model_path = "/Users/niaomuqing/100knock2025/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

country_path = "/Users/niaomuqing/100knock2025/countries.txt"
with open(country_path, 'r', encoding='utf-8') as f:
    countries = [line.strip().lower() for line in f if line.strip()]

country_vectors = []
valid_countries = []

for country in countries:
    if country in model:
        country_vectors.append(model[country])
        valid_countries.append(country)

Z = linkage(country_vectors, method='ward')

plt.figure(figsize=(12, 6)) 
dendrogram(Z, labels=valid_countries, leaf_rotation=90)
plt.title("Hierarchical Clustering of Countries (Ward method)")
plt.xlabel("Country")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()

