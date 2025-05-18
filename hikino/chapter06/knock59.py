from knock57 import vecs, countries
from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt

tsne = TSNE(n_components=2, random_state=42, init="random", perplexity=5)
vecs = np.array(vecs)
points_2d = tsne.fit_transform(vecs)


# 5. 可視化（matplotlib）
plt.figure(figsize=(12, 8))
for (x, y), name in zip(points_2d, countries):
    plt.scatter(x, y)
    plt.text(x + 1.0, y + 1.0, name, fontsize=9)
plt.title("t-SNE Visualization of Country Word Vectors")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.tight_layout()
plt.savefig("../../../t-SNE.png")