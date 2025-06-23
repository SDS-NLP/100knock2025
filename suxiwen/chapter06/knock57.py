import gensim.downloader as api
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# --- モデルロード ---
print("Loading model...")
model = api.load("glove-wiki-gigaword-100")
print("Model loaded.")

# --- 国名リスト（必要なら手動で追加可能） ---
countries = [
    "japan", "china", "india", "france", "germany", "italy", "spain", "portugal", "brazil", "argentina",
    "canada", "mexico", "russia", "ukraine", "poland", "sweden", "norway", "denmark", "finland", "netherlands",
    "egypt", "morocco", "south_africa", "nigeria", "kenya", "australia", "new_zealand", "united_states", "united_kingdom",
    "iran", "iraq", "israel", "saudi_arabia", "turkey", "pakistan", "indonesia", "vietnam", "thailand", "philippines"
]

# --- 語彙にある国だけ選別 ---
country_vecs = []
valid_countries = []

for country in countries:
    if country in model:
        country_vecs.append(model[country])
        valid_countries.append(country)

print(f"{len(valid_countries)} か国のベクトルを使用します。")

# --- K-means クラスタリング ---
k = 5
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
labels = kmeans.fit_predict(country_vecs)

# --- クラスタごとの国一覧表示 ---
from collections import defaultdict
clusters = defaultdict(list)
for label, country in zip(labels, valid_countries):
    clusters[label].append(country)

print("\nクラスタ結果：")
for cluster_id, members in clusters.items():
    print(f"\nCluster {cluster_id+1}:")
    print(", ".join(members))

# --- 可視化（PCAで2次元に） ---
pca = PCA(n_components=2)
reduced_vecs = pca.fit_transform(country_vecs)

plt.figure(figsize=(10, 7))
colors = ['red', 'green', 'blue', 'orange', 'purple']
for i in range(k):
    cluster_points = [reduced_vecs[j] for j in range(len(labels)) if labels[j] == i]
    cluster_labels = [valid_countries[j] for j in range(len(labels)) if labels[j] == i]
    xs, ys = zip(*cluster_points)
    plt.scatter(xs, ys, c=colors[i], label=f'Cluster {i+1}')
    for x, y, label in zip(xs, ys, cluster_labels):
        plt.text(x + 0.1, y, label, fontsize=9)

plt.title("Country Word Vectors clustered (k=5)")
plt.legend()
plt.tight_layout()
plt.show()