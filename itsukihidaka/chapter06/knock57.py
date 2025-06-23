# 国名に関する単語ベクトルを抽出し、k-meansクラスタリングをクラスタ数k=5として実行せよ。

from gensim.models import KeyedVectors
import pandas as pd
import numpy as np

# GoogleNewsの単語ベクトルを読み込む
model = KeyedVectors.load_word2vec_format(
    '/Users/itsukihidaka/Downloads/GoogleNews-vectors-negative300.bin.gz',
    binary=True
)

# 国名に関する単語リストを作成
with open('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter06/countries.txt', 'r') as f:
    countries = []
    for line in f:
        countries.append(line.strip())

# 国名に関する単語ベクトルを抽出（モデルに存在するもののみ）
country_vecs = []
valid_countries = []
for country in countries:
    if country in model:
        country_vecs.append(model[country])
        valid_countries.append(country)


# k-meansクラスタリングを実行
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5, random_state=42)
cluster_labels = kmeans.fit_predict(country_vecs)

# 結果をDataFrameにまとめる
result_df = pd.DataFrame({
    'country': valid_countries,
    'cluster': cluster_labels
})


print("\n=== クラスタごとの国名 ===")
for i in range(5):
    cluster_countries = result_df[result_df['cluster'] == i]['country'].tolist()
    print(f"クラスタ {i}: {cluster_countries}")

# クラスタの統計情報
print(f"\n=== クラスタの統計情報 ===")
cluster_counts = result_df['cluster'].value_counts().sort_index()
print(cluster_counts)

