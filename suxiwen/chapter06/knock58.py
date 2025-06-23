import gensim.downloader as api
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist

# --- 単語ベクトルモデルのロード ---
print("Loading model...")
model = api.load("glove-wiki-gigaword-100")
print("Model loaded.")

# --- 国名リスト（自由に追加・削除可能） ---
countries = [
    "japan", "china", "india", "france", "germany", "italy", "spain", "portugal", "brazil", "argentina",
    "canada", "mexico", "russia", "ukraine", "poland", "sweden", "norway", "denmark", "finland", "netherlands",
    "egypt", "morocco", "south_africa", "nigeria", "kenya", "australia", "new_zealand", "united_states", "united_kingdom",
    "iran", "iraq", "israel", "saudi_arabia", "turkey", "pakistan", "indonesia", "vietnam", "thailand", "philippines"
]

# --- モデルに存在する国のみを抽出 ---
valid_countries = []
vectors = []

for country in countries:
    if country in model:
        valid_countries.append(country)
        vectors.append(model[country])

print(f"{len(valid_countries)} か国がクラスタリング対象です。")

# --- 階層クラスタリング（Ward法） ---
vectors = np.array(vectors)
linked = linkage(vectors, method='ward')

# --- デンドログラムの可視化 ---
plt.figure(figsize=(14, 8))
dendrogram(linked, labels=valid_countries, leaf_rotation=90, leaf_font_size=10)
plt.title("Hierarchical Clustering of Country Word Vectors (Ward method)")
plt.tight_layout()
plt.savefig("country_dendrogram.png", dpi=300, bbox_inches="tight")
print("Dendrogram saved as 'country_dendrogram.png'.")