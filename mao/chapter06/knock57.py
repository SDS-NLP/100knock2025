"""
knock57:k-meansクラスタリング
国名に関する単語ベクトルを抽出し、k-meansクラスタリングをクラスタ数k=5として
実行せよ。
"""
import pandas as pd
import numpy as np
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# 1. モデルの読み込み
model_path = 'mao/chapter06/GoogleNews-vectors-negative300.bin'  # あなたの環境に合わせて修正
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 2. 国名リストの定義（例：一部）
countries = np.loadtxt("mao/chapter06/countries.txt", dtype=str)

# 3. 存在する国のベクトルを抽出
country_vecs = []
valid_countries = []

for country in countries:
    if country in model:
        country_vecs.append(model[country])
        valid_countries.append(country)

# 4. KMeansクラスタリング（k=5）
k = 5
kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
labels = kmeans.fit_predict(country_vecs)

# 5. クラスタリング結果の表示
print("\nクラスタリング結果:")
for i in range(k):
    print(f"\nCluster {i+1}:")
    for country, label in zip(valid_countries, labels):
        if label == i:
            print(f" - {country}")

# 6. 可視化（PCAで2次元に圧縮）
pca = PCA(n_components=2)
vecs_2d = pca.fit_transform(country_vecs)

plt.figure(figsize=(10, 6))
for i in range(len(valid_countries)):
    plt.scatter(vecs_2d[i][0], vecs_2d[i][1], c=f'C{labels[i]}', label=f'Cluster {labels[i]}' if i == 0 else "")
    plt.text(vecs_2d[i][0]+0.1, vecs_2d[i][1]+0.1, valid_countries[i], fontsize=9)

plt.title("K-means clustering of country vectors (k=5)")
plt.grid(True)
plt.show()