"""
knock70:単語埋め込みの読み込み
事前学習済み単語埋め込みを活用し、の単語埋め込み行列を作成せよ。

ここで、は単語埋め込みの語彙数、は単語埋め込みの次元数である。
ただし、単語埋め込み行列の先頭の行ベクトルは、将来的に
パディング（<PAD>）トークンの埋め込みベクトルとして用いたいので、
ゼロベクトルとして予約せよ。
ゆえに、の2行目以降に事前学習済み単語埋め込みを読み込むことになる。

もし、Google Newsデータセットの学習済み単語ベクトル
（300万単語・フレーズ、300次元）を全て読み込んだ場合、になるはずである
（ただ、300万単語の中には、殆ど用いられない稀な単語も含まれるので、
語彙を削減した方がメモリの節約になる）。

また、単語埋め込み行列の構築と同時に、単語埋め込み行列の各行のインデックス番号
（トークンID）と、単語（トークン）への双方向の対応付けを保持せよ。
"""
import numpy as np
from gensim.models import KeyedVectors

# 事前学習済みの単語ベクトルの読み込み（GoogleNewsの300次元word2vec）
# ファイルパスは実際の環境に応じて変更
w2v_path = 'mao/chapter08/GoogleNews-vectors-negative300.bin'
w2v = KeyedVectors.load_word2vec_format(w2v_path, binary=True)

# 語彙数と次元数
vocab_size = len(w2v.key_to_index) + 1  # +1 は <PAD> 用
embedding_dim = w2v.vector_size         # 通常は 300

# 埋め込み行列の初期化：先頭をゼロベクトルに（<PAD> 用）
embedding_matrix = np.zeros((vocab_size, embedding_dim))

# 単語 ↔ トークンID 辞書の初期化
word2id = {'<PAD>': 0}
id2word = {0: '<PAD>'}

# 2行目以降に事前学習済みベクトルを格納
for idx, word in enumerate(w2v.key_to_index.keys(), start=1):
    embedding_matrix[idx] = w2v[word]
    word2id[word] = idx
    id2word[idx] = word
