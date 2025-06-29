from gensim.models import KeyedVectors
from sklearn.cluster import KMeans

# Word2Vecモデルの読み込み
model_path = "GoogleNews-vectors-negative300.bin.gz"
print("Loading Word2Vec model...")
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("Model loaded.")

# 対象の国名リスト
countries = [
    'China', 'Japan', 'Germany', 'France', 'Italy', 'Spain', 'Russia',
    'India', 'Pakistan', 'Bangladesh', 'Indonesia', 'Vietnam', 'Thailand',
    'Canada', 'United_States', 'Mexico', 'Brazil', 'Argentina', 'Chile',
    'Egypt', 'South_Africa', 'Nigeria', 'Kenya', 'Turkey', 'Iran', 'Iraq',
    'Australia', 'New_Zealand', 'South_Korea', 'North_Korea', 'Saudi_Arabia',
]

# モデルに含まれる国のベクトルを取得
country_vectors = []
country_names = []

for country in countries:
    if country in model:
        country_vectors.append(model[country])
        country_names.append(country)

print(f"{len(country_names)} countries found in the model vocabulary.")

# KMeansクラスタリング
num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
labels = kmeans.fit_predict(country_vectors)

# クラスタごとに国をまとめて表示
clusters = [[] for _ in range(num_clusters)]
for country, label in zip(country_names, labels):
    clusters[label].append(country)

for i, cluster in enumerate(clusters):
    print(f"\n--- Cluster {i + 1} ---")
    for country in cluster:
        print(f"- {country}")
