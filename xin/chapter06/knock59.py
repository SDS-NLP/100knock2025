import gensim.downloader as api
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# --- モデル読み込み ---
print("Loading model...")
model = api.load("glove-wiki-gigaword-100")
print("Model loaded.")

# --- 国名リストの定義 ---
countries = [
    "japan", "china", "india", "france", "germany", "italy", "spain", "portugal", "brazil", "argentina",
    "canada", "mexico", "russia", "ukraine", "poland", "sweden", "norway", "denmark", "finland", "netherlands",
    "egypt", "morocco", "south_africa", "nigeria", "kenya", "australia", "new_zealand", "united_states", "united_kingdom",
    "iran", "iraq", "israel", "saudi_arabia", "turkey", "pakistan", "indonesia", "vietnam", "thailand", "philippines"
]

# --- モデルに含まれる国だけ取得 ---
valid_countries = []
vectors = []

for country in countries:
    if country in model:
        valid_countries.append(country)
        vectors.append(model[country])

print(f"{len(valid_countries)} か国のベクトルを使用します。")

# --- t-SNE による2次元への次元削減 ---
tsne = TSNE(n_components=2, random_state=42, perplexity=5, n_iter=1000)
reduced = tsne.fit_transform(vectors)

# --- 可視化 ---
plt.figure(figsize=(12, 9))
plt.scatter(reduced[:, 0], reduced[:, 1], c='skyblue', edgecolors='black')

# ラベル表示
for i, country in enumerate(valid_countries):
    plt.text(reduced[i, 0] + 0.5, reduced[i, 1] + 0.5, country, fontsize=9)

plt.title("t-SNE による国名の単語ベクトル可視化")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.grid(True)
plt.tight_layout()
plt.savefig("country_vectors_tsne.png", dpi=300)
print("t-SNE プロットを 'country_vectors_tsne.png' に保存しました。")
