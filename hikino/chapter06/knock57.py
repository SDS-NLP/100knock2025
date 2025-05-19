from knock50 import model
import difflib
from sklearn.cluster import KMeans
import numpy as np

countries = []
vecs = []

with open("../../../countries.txt", mode = "r") as f:
    for line in f:
        line = line.strip()
        if line in model:
            countries.append(line)
        else:
            candidates = difflib.get_close_matches(line.replace(" ", "_"), model.key_to_index.keys(), n=1, cutoff=0.6)
            candidates = candidates[0]
            countries.append(candidates)

for country in countries:
    vec = model[country]
    vecs.append(vec)

k = 5
kmeans = KMeans(n_clusters=k, random_state=42)
labels = kmeans.fit_predict(vecs)

# 5. 結果表示
if __name__ == "__main__":
  for i in range(k):
      print(f"\n[Cluster {i}]")
      for country, label in zip(countries, labels):
          if label == i:
              print(country)
