#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from gensim.models import KeyedVectors
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
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

country_vectors_np = np.array(country_vectors)

tsne = TSNE(n_components=2, random_state=42, perplexity=30, init='pca', learning_rate='auto')
embeddings_2d = tsne.fit_transform(country_vectors_np)

plt.figure(figsize=(12, 8))
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], alpha=0.7)

for i, country in enumerate(valid_countries):
    plt.annotate(country, (embeddings_2d[i, 0], embeddings_2d[i, 1]), fontsize=9)

plt.title("t-SNE Visualization of Country Word Vectors")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.tight_layout()
plt.show()

