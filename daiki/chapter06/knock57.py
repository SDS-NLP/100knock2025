from gensim.models import KeyedVectors
from sklearn.cluster import KMeans

# 1. Word2Vecモデル読み込み（GoogleNews）
model_path = '/Users/aa/GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 2. 国名リストの定義（例：20ヶ国）
countries = [
    'Japan', 'China', 'Korea', 'India', 'Vietnam',
    'Germany', 'France', 'Italy', 'Spain', 'Poland',
    'Canada', 'Brazil', 'Mexico', 'Argentina', 'Chile',
    'Russia', 'Ukraine', 'Turkey', 'Egypt', 'Nigeria'
]

# 3. ベクトル抽出
vectors = []
valid_countries = []

for country in countries:
    if country in model:
        vectors.append(model[country])
        valid_countries.append(country)
    else:
        print(f"モデルに存在しない国名スキップ: {country}")

# 4. k-meansクラスタリング実行（k=5）
k = 5
kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
labels = kmeans.fit_predict(vectors)

# 5. 結果出力
print("\n=== クラスタリング結果 ===")
for country, label in zip(valid_countries, labels):
    print(f"{country:<10} → Cluster {label}")

#出力結果
"""
=== クラスタリング結果 ===
Japan      → Cluster 2
China      → Cluster 2
Korea      → Cluster 2
India      → Cluster 2
Vietnam    → Cluster 2
Germany    → Cluster 0
France     → Cluster 0
Italy      → Cluster 0
Spain      → Cluster 0
Poland     → Cluster 1
Canada     → Cluster 2
Brazil     → Cluster 3
Mexico     → Cluster 3
Argentina  → Cluster 3
Chile      → Cluster 3
Russia     → Cluster 1
Ukraine    → Cluster 1
Turkey     → Cluster 1
Egypt      → Cluster 2
Nigeria    → Cluster 4
"""