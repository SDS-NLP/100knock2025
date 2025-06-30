import pandas as pd
from gensim.models import KeyedVectors

# 事前に作成した単語埋め込み読み込み関数を利用
def load_word_embeddings(pretrained_path, max_vocab=100000, embedding_dim=300):
    print(f"単語埋め込みモデルを読み込み中: {pretrained_path}")
    word_vectors = KeyedVectors.load_word2vec_format(pretrained_path, binary=True)
    
    pad_token = "<PAD>"
    tokens = [pad_token] + list(word_vectors.index_to_key)
    
    if max_vocab and len(tokens) > max_vocab:
        tokens = tokens[:max_vocab]
    
    vocab_size = len(tokens)
    print(f"語彙サイズ: {vocab_size}，埋め込み次元: {embedding_dim}")
    
    embedding_matrix = np.zeros((vocab_size, embedding_dim), dtype=np.float32)
    for i, token in enumerate(tokens[1:], 1):
        embedding_matrix[i] = word_vectors[token]
    
    token_to_id = {token: i for i, token in enumerate(tokens)}
    id_to_token = {i: token for i, token in enumerate(tokens)}
    
    return {
        'embedding_matrix': embedding_matrix,
        'token_to_id': token_to_id,
        'id_to_token': id_to_token,
        'vocab_size': vocab_size,
        'pad_id': 0,
        'pad_token': pad_token
    }

# SSTデータセットの読み込みと前処理
def load_sst_data(file_path, token_to_id):
    """
    SSTデータセットを読み込み、トークンIDに変換する
    
    パラメータ:
        file_path: データセットのパス（train.tsv または dev.tsv）
        token_to_id: 単語→IDのマッピング辞書
    """
    print(f"データセットを読み込み中: {file_path}")
    # TSVファイルを読み込む（ヘッダーがない場合は header=None を指定）
    df = pd.read_csv(file_path, sep='\t')
    
    dataset = []
    for text, label in zip(df['text'], df['label']):
        # テキストを小文字に変換し、トークン化（シンプルなスペース分割）
        tokens = text.lower().split()
        
        # 単語埋め込みの語彙に含まれるトークンのみを抽出
        input_ids = []
        for tok in tokens:
            if tok in token_to_id:
                input_ids.append(token_to_id[tok])
        
        # 空のトークン列の場合はデータセットから除外
        if not input_ids:
            continue
        
        # ラベルを数値に変換（positive→1, negative→0 の例）
        label_tensor = 1 if label == 'positive' else 0
        
        # データを辞書形式で保存
        dataset.append({
            'text': text,
            'label': label_tensor,
            'input_ids': input_ids
        })
    
    return dataset

if __name__ == "__main__":
    # 単語埋め込みモデルのパス（事前にダウンロードしたファイル）
    pretrained_path = "/home/suxiwen/100knock2025/GoogleNews-vectors-negative300.bin"
    
    # 単語埋め込みの読み込み
    embedding_data = load_word_embeddings(pretrained_path, max_vocab=100000)
    token_to_id = embedding_data['token_to_id']
    
    # SSTデータセットの読み込み（train.tsv と dev.tsv のパスを指定）
    train_data = load_sst_data('train.tsv', token_to_id)
    dev_data = load_sst_data('dev.tsv', token_to_id)
    
    # データセットの確認
    print(f"学習データ数: {len(train_data)}")
    print(f"開発データ数: {len(dev_data)}")
    print("最初のデータ例:", train_data[0])