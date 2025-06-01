import os
from gensim.models import KeyedVectors

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'GoogleNews-vectors-negative300.bin')

model = KeyedVectors.load_word2vec_format(
    model_path,
    binary=True
)

# 単語ベクトルの取得
vector = model['United_States']

if __name__ == "__main__":
  print(f"単語ベクトル: {vector}")
  print(f"単語ベクトルの次元数: {len(vector)}")