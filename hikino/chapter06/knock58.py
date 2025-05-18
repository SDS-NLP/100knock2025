from knock57 import vecs, countries
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt


linkage_result = linkage(vecs, method='ward')

# 5. デンドログラム表示
plt.figure(figsize=(12, 6))
dendrogram(linkage_result, labels=countries, leaf_rotation=90)
plt.title("Hierarchical Clustering of Country Word Vectors (Ward's Method)")
plt.xlabel("Country")
plt.ylabel("Distance")
plt.tight_layout()
plt.savefig("../../../Hierarchical_Clustering.png")
