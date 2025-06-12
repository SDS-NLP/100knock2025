#58. Ward法によるクラスタリング
from knock50 import model
from knock57 import countries, countries_vec
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

#ward法を指定してクラスタリング
linkage_result = linkage(countries_vec, method='ward')

plt.figure(figsize=(16, 9))
dendrogram(linkage_result, labels=countries)
plt.savefig("dendrogram")