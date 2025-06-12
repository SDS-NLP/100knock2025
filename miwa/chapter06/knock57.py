#57. k-meansクラスタリング
from knock50 import model
from sklearn.cluster import KMeans
import numpy as np

# 国名リストのベクトルを作成
countries=[]
countries_vec=[]
with open("countries.txt", "r", encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        if line in model:
            countries.append(line)
            result=model[line]
            countries_vec.append(result)
        else:
            continue
        
if __name__ == "__main__":
    # k-meansクラスタリング
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(countries_vec)
    for i in range(5):
        cluster = np.where(kmeans.labels_ == i)[0]
        print('cluster', i)
        print(', '.join([countries[k] for k in cluster]))

