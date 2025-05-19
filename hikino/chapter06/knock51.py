from knock50 import model
import numpy as np

word1 = "United_States"
word2 = "U.S."

v1 = model[word1]
v2 = model[word2]
sim = np.dot(v1, v2)/(np.sqrt(np.sum(np.abs(v1**2)))*np.sqrt(np.sum(np.abs(v2**2))))

similarity = model.similarity(word1, word2)

print(f"Cosine similarity between '{word1}' and '{word2}': {similarity:.4f}")
print(sim)

