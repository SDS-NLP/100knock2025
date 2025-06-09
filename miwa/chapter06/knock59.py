#59. t-SNEによる可視化
from knock50 import model
from knock57 import countries, countries_vec
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

#K-meansクラスタリング
kmeans = KMeans(n_clusters=5)
kmeans.fit(countries_vec)

#t-SNEで次元削減
tsne = TSNE(n_components=2, random_state=64)
X_reduced = tsne.fit_transform(np.array(countries_vec))

#描画
plt.figure(figsize=(10, 10))
for x, country, color in zip(X_reduced, countries, kmeans.labels_):
    plt.text(x[0], x[1], country, color='C{}'.format(color))
plt.xlim([-12, 15])
plt.ylim([-15, 15])
plt.savefig("t-SNE")
