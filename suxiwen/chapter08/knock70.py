import numpy as np
from gensim.models import KeyedVectors

def load_word_embeddings(pretrained_path, max_vocab=100000, embedding_dim=300):
    """
    事前学習済みの単語埋め込みモデルを読み込み、埋め込み行列を作成する
    
    パラメータ:
        pretrained_path: 事前学習済みモデルのパス
        max_vocab: 最大語彙数（メモリ節約のため）
        embedding_dim: 埋め込みベクトルの次元数
    """
    print(f"単語埋め込みモデルを読み込み中: {pretrained_path}")
    word_vectors = KeyedVectors.load_word2vec_format(pretrained_path, binary=True)
    
    # 語彙リストを作成（先頭に<PAD>トークンを追加）
    pad_token = "<PAD>"
    tokens = [pad_token] + list(word_vectors.index_to_key)
    
    # 語彙数を制限する（メモリ不足対策）
    if max_vocab and len(tokens) > max_vocab:
        tokens = tokens[:max_vocab]
    
    vocab_size = len(tokens)
    print(f"語彙サイズ: {vocab_size}，埋め込み次元: {embedding_dim}")
    
    # 埋め込み行列を初期化（0行目は<PAD>用のゼロベクトル）
    embedding_matrix = np.zeros((vocab_size, embedding_dim), dtype=np.float32)
    for i, token in enumerate(tokens[1:], 1):  # インデックス1から開始（0は<PAD>）
        embedding_matrix[i] = word_vectors[token]
    
    # 単語とIDの双方向マッピングを作成
    token_to_id = {token: i for i, token in enumerate(tokens)}
    id_to_token = {i: token for i, token in enumerate(tokens)}
    
    return {
        'embedding_matrix': embedding_matrix,    # 埋め込み行列
        'token_to_id': token_to_id,            # 単語 → ID のマッピング
        'id_to_token': id_to_token,            # ID → 単語のマッピング
        'vocab_size': vocab_size,              # 語彙サイズ
        'pad_id': 0,                           # PADトークンのID
        'pad_token': pad_token                 # PADトークンの文字列
    }

if __name__ == "__main__":
    # 自分のパスに置き換えてください
    pretrained_path = "D:\downloadedge\GoogleNews-vectors-negative300.bin.gz"
    
    # 単語埋め込みを読み込む（語彙数を10万に制限してメモリを節約）
    embedding_data = load_word_embeddings(
        pretrained_path,
        max_vocab=100000,
        embedding_dim=300
    )
    
    # 結果を検証する
    print("\n--- 検証結果 ---")
    print(f"埋め込み行列の形状: {embedding_data['embedding_matrix'].shape}")
    print(f"<PAD>トークンのID: {embedding_data['pad_id']}，ベクトル: {embedding_data['embedding_matrix'][0][:5]}")
    print(f"単語'apple'のID: {embedding_data['token_to_id'].get('apple', '見つかりません')}")
    print(f"ID=100に対応する単語: {embedding_data['id_to_token'].get(100, '未定義')}")