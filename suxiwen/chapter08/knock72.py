import torch
import torch.nn as nn
import numpy as np

class BagOfWordsModel(nn.Module):
    """単語埋め込みの平均を用いたBag-of-Wordsモデル（ロジスティック回帰）"""
    def __init__(self, vocab_size, embedding_dim):
        """
        モデルの初期化
        
        Args:
            vocab_size: 語彙サイズ
            embedding_dim: 単語埋め込みの次元数
        """
        super(BagOfWordsModel, self).__init__()
        # 単語IDを埋め込みベクトルに変換する層
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        # 分類器（ロジスティック回帰）
        self.fc = nn.Linear(embedding_dim, 2)  # 2クラス分類（肯定/否定）

    def forward(self, input_ids):
        """
        順伝播計算
        
        Args:
            input_ids: 入力の単語ID列 [batch_size, seq_length]
            
        Returns:
            logits: 分類スコア [batch_size, 2]
        """
        # 単語IDを埋め込みベクトルに変換
        embeds = self.embedding(input_ids)  # [batch_size, seq_length, embedding_dim]
        
        # 文内の全単語の埋め込みを平均して文ベクトルを作成
        # Bag-of-Wordsの考え方（順序無視で単語の集合として扱う）
        avg_embeds = torch.mean(embeds, dim=1)  # [batch_size, embedding_dim]
        
        # 分類器に入力
        logits = self.fc(avg_embeds)  # [batch_size, 2]
        
        return logits

# モデルのインスタンス化と学習の例
def train_example():
    # パラメータ設定（前のステップで作成した語彙と合わせる）
    vocab_size = 100000  # 語彙サイズ
    embedding_dim = 300   # Google Newsの埋め込み次元
    
    # モデルの作成
    model = BagOfWordsModel(vocab_size, embedding_dim)
    
    # 損失関数とオプティマイザ
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    # ダミーデータでの学習例
    batch_size = 32
    seq_length = 50
    
    # ダミーの入力データ（単語ID列）
    dummy_input_ids = torch.randint(0, vocab_size, (batch_size, seq_length))
    
    # ダミーのラベル（0:否定的, 1:肯定的）
    dummy_labels = torch.randint(0, 2, (batch_size,))
    
    # 訓練ステップ
    optimizer.zero_grad()  # 勾配の初期化
    outputs = model(dummy_input_ids)  # 順伝播
    loss = criterion(outputs, dummy_labels)  # 損失計算
    loss.backward()  # 逆伝播
    optimizer.step()  # パラメータ更新
    
    print(f"損失値: {loss.item():.4f}")
    print("Bag-of-Wordsモデルの訓練例が完了しました。")
    
    return model

# モデルの保存例
def save_model(model, path="bow_model.pt"):
    """モデルを保存する"""
    torch.save(model.state_dict(), path)
    print(f"モデルが{path}に保存されました。")

# メイン実行
if __name__ == "__main__":
    model = train_example()
    save_model(model)