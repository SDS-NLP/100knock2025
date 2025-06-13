import numpy as np
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
from sklearn.manifold import TSNE

# === 1. Word2Vecモデルの読み込み ===
model_path = "GoogleNews-vectors-negative300.bin.gz"  # モデルのパスを適宜修正
print("Loading Word2Vec model...")
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("Model loaded.")

# === 2. 国名リスト ===
country_list = [
    'China', 'Japan', 'Germany', 'France', 'Italy', 'Spain', 'Russia',
    'India', 'Pakistan', 'Bangladesh', 'Indonesia', 'Vietnam', 'Thailand',
    'Canada', 'United_States', 'Mexico', 'Brazil', 'Argentina', 'Chile',
    'Egypt', 'South_Africa', 'Nigeria', 'Kenya', 'Turkey', 'Iran', 'Iraq',
    'Australia', 'New_Zealand', 'South_Korea', 'North_Korea', 'Saudi_Arabia',
]

# === 3. 単語ベクトルの取得 ===
vectors = []
valid_countries = []

for country in country_list:
    if country in model:
        vectors.append(model[country])
        valid_countries.append(country)
    else:
        print(f"Skip: {country} (not in vocabulary)")

# NumPy配列に変換（t-SNE用）
vectors = np.array(vectors)

# === 4. t-SNEで次元圧縮 ===
tsne = TSNE(n_components=2, random_state=42, perplexity=5, max_iter=1000)
reduced = tsne.fit_transform(vectors)

# === 5. 結果のプロット ===
plt.figure(figsize=(12, 8))
for (x, y), name in zip(reduced, valid_countries):
    plt.scatter(x, y)
    plt.annotate(name, (x + 1, y + 1), fontsize=9)  # 少しずらして表示

plt.title("t-SNE Visualization of Country Word Vectors")
plt.tight_layout()
plt.savefig("tsne_countries.png")  # ← グラフを保存
print("プロット画像を 'tsne_countries.png' に保存しました。")
