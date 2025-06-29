from gensim.models import KeyedVectors

# 学習済みモデルの読み込み
model_path = "GoogleNews-vectors-negative300.bin.gz"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# コサイン類似度の計算
similarity = model.similarity("United_States", "U.S.")
print(f"United_States と U.S. のコサイン類似度: {similarity}")
