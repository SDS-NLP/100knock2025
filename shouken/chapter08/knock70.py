import numpy as np
from gensim.models import KeyedVectors

# ファイルパス（同じフォルダにあること）
embedding_file = "GoogleNews-vectors-negative300.bin.gz"

# モデルの読み込み（バイナリ形式）
print("モデルを読み込んでいます...")
model = KeyedVectors.load_word2vec_format(embedding_file, binary=True)
print("読み込み完了")

# パラメータ設定
embedding_dim = model.vector_size
max_vocab = 200000  # 上位N語だけ使用（メモリ節約）

# 埋め込みベクトル・辞書構築
embedding_list = [np.zeros(embedding_dim)]  # ID 0: <PAD>
word_to_id = {}
id_to_word = []

# 語彙とベクトルを追加
for i, word in enumerate(model.index_to_key):
    if i >= max_vocab:
        break
    vec = model[word]
    embedding_list.append(vec)
    word_to_id[word] = len(embedding_list) - 1
    id_to_word.append(word)

# NumPy行列化
embedding_matrix = np.vstack(embedding_list)

# 情報表示
print(f"埋め込み行列の形状: {embedding_matrix.shape}")
print(f"語彙数（<PAD>含まず）: {len(word_to_id)}")

# 例: "great" のベクトル（存在する場合のみ）
if 'great' in word_to_id:
    idx = word_to_id['great']
    print(f"例: 'great' → ID {idx}, ベクトル前5要素: {embedding_matrix[idx][:5]}")
else:
    print("単語 'great' は語彙に含まれていません。")

# 語彙の先頭10個（確認用）
print("語彙リスト上位10語:", list(word_to_id.keys())[:10])
