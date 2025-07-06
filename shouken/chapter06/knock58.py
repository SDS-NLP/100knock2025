from gensim.models import KeyedVectors
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# === 1. Word2Vecモデルの読み込み ===
model_path = "GoogleNews-vectors-negative300.bin.gz"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# === 2. 国名リストの定義 ===
country_list = [
    'China', 'Japan', 'Germany', 'France', 'Italy', 'Spain', 'Russia',
    'India', 'Pakistan', 'Bangladesh', 'Indonesia', 'Vietnam', 'Thailand',
    'Canada', 'United_States', 'Mexico', 'Brazil', 'Argentina', 'Chile',
    'Egypt', 'South_Africa', 'Nigeria', 'Kenya', 'Turkey', 'Iran', 'Iraq',
    'Australia', 'New_Zealand', 'South_Korea', 'North_Korea', 'Saudi_Arabia',
]

# === 3. ベクトルの抽出 ===
vectors = []
valid_countries = []

for country in country_list:
    if country in model:
        vectors.append(model[country])
        valid_countries.append(country)

# === 4. Ward法クラスタリング ===
linkage_matrix = linkage(vectors, method='ward')

# === 5. デンドログラムの可視化 ===
plt.figure(figsize=(14, 7))
dendrogram(linkage_matrix, labels=valid_countries, leaf_rotation=90)
plt.title("Ward Hierarchical Clustering of Country Vectors")
plt.xlabel("Country")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()
