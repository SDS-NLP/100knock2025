from gensim.models import KeyedVectors
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# 1. Word2Vecモデルの読み込み
model_path = '/Users/aa/GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 2. 国名リスト
countries = [
    'Japan', 'China', 'Korea', 'India', 'Vietnam',
    'Germany', 'France', 'Italy', 'Spain', 'Poland',
    'Canada', 'Brazil', 'Mexico', 'Argentina', 'Chile',
    'Russia', 'Ukraine', 'Turkey', 'Egypt', 'Nigeria'
]

# 3. 国名ベクトルの抽出
vectors = []
valid_countries = []

for country in countries:
    if country in model:
        vectors.append(model[country])
        valid_countries.append(country)
    else:
        print(f"'{country}' はモデルに存在しません")

# 4. Ward法による階層クラスタリング
Z = linkage(vectors, method='ward')

# 5. デンドログラム描画
plt.figure(figsize=(10, 6))
dendrogram(Z, labels=valid_countries, leaf_rotation=90)
plt.title("Ward Hierarchical Clustering of Country Vectors")
plt.tight_layout()
plt.show()
