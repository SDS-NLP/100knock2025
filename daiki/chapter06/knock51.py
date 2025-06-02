from gensim.models import KeyedVectors

# モデルのパス
model_path = '/Users/aa/GoogleNews-vectors-negative300.bin'

# モデルの読み込み
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 単語の定義
word1 = 'United_States'
word2 = 'U.S.'

# 類似度を計算
similarity = model.similarity(word1, word2)
print(f"「{word1}」と「{word2}」のコサイン類似度：{similarity:.4f}")

#出力：「United_States」と「U.S.」のコサイン類似度：0.7311