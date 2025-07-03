import numpy as np
from gensim.models import KeyedVectors

def load_pretrained_embeddings(embedding_path, vocab_size=None):
    # 事前学習済み単語埋め込みを読み込む
    print("Loading pretrained embeddings...")
    word_vectors = KeyedVectors.load_word2vec_format(embedding_path, binary=True)
    
    # 語彙数と次元数を取得
    embedding_dim = word_vectors.vector_size
    if vocab_size is None:
        vocab_size = len(word_vectors.key_to_index) + 1  # +1 for <PAD> token
    
    # 単語埋め込み行列を初期化
    embedding_matrix = np.zeros((vocab_size, embedding_dim), dtype=np.float32)
    
    # トークンIDと単語の対応付けを保持する辞書
    token_to_id = {"<PAD>": 0}
    id_to_token = {0: "<PAD>"}
    
    # 埋め込み行列の2行目以降に事前学習済み単語埋め込みを格納
    for idx, (word, vector) in enumerate(word_vectors.key_to_index.items(), start=1):
        if vocab_size and idx >= vocab_size:
            break
        embedding_matrix[idx] = word_vectors[word]
        token_to_id[word] = idx
        id_to_token[idx] = word
    
    print("Pretrained embeddings loaded successfully.")
    return embedding_matrix, token_to_id, id_to_token

# 使用例
embedding_path = "GoogleNews-vectors-negative300.bin"  # Google Newsデータセットのパス
vocab_size = 50000  # 語彙数を制限する場合（例: 50000語）
embedding_matrix, token_to_id, id_to_token = load_pretrained_embeddings(embedding_path, vocab_size)

# 結果を確認
print("Embedding matrix shape:", embedding_matrix.shape)
print("Number of tokens:", len(token_to_id))