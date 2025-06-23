from gensim.models import KeyedVectors
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np

# 1. Word2Vecモデル読み込み
model_path = '/Users/aa/GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 2. 国名リスト（前と同じでOK）
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
        print(f"モデルに存在しない国名: {country}")
vectors = np.array(vectors)

# 4. t-SNE で次元圧縮
tsne = TSNE(n_components=2, random_state=42, perplexity=5)
reduced = tsne.fit_transform(vectors)

# 5. 可視化
plt.figure(figsize=(10, 8))
plt.scatter(reduced[:, 0], reduced[:, 1])

for label, x, y in zip(valid_countries, reduced[:, 0], reduced[:, 1]):
    plt.annotate(label, (x, y), fontsize=9)

plt.title("t-SNE Visualization of Country Word Vectors")
plt.tight_layout()
plt.show()
