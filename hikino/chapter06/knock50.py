from gensim.models import KeyedVectors

# モデルの読み込み（バイナリ形式）
model = KeyedVectors.load_word2vec_format(
    r'../../../GoogleNews-vectors-negative300.bin',
    binary=True
)

# 単語ベクトルの取得
vector = model['United_States']  # アンダースコア注意！

if __name__ == "__main__":
  print(vector)
  print("ベクトルの次元数:", len(vector))
