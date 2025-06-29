from gensim.models import KeyedVectors

# 学習済みモデルの読み込み
model_path = "GoogleNews-vectors-negative300.bin.gz"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 類似語トップ10の取得
similar_words = model.most_similar("United_States", topn=10)

# 出力
for word, score in similar_words:
    print(f"{word}: {score:.4f}")
