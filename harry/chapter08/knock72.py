# 72. Bag of wordsモデルの構築
# 単語埋め込みの平均ベクトルでテキストの特徴ベクトルを表現し、
# 重みベクトルとの内積でポジティブ及びネガティブを分類するニューラルネットワーク（ロジスティック回帰モデル）を設計せよ。

# knock72.py
import torch
import torch.nn as nn

class BoWClassifier(nn.Module):
    def __init__(self, embedding_matrix):
        super().__init__()
        vocab_size, emb_dim = embedding_matrix.size()
        
        # 埋め込み層（学習しない）
        self.embedding = nn.Embedding.from_pretrained(embedding_matrix, freeze=True, padding_idx=0)
        
        # 線形層（ロジスティック回帰）
        self.fc = nn.Linear(emb_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, input_ids):
        """
        input_ids: (batch_size, seq_len)
        出力: (batch_size, 1) ロジット
        """
        embedded = self.embedding(input_ids)                # (batch_size, seq_len, emb_dim)
        mask = (input_ids != 0).unsqueeze(-1).float()        # PADマスク: (batch_size, seq_len, 1)
        summed = torch.sum(embedded * mask, dim=1)           # (batch_size, emb_dim)
        lengths = torch.sum(mask, dim=1) + 1e-9              # avoid division by zero
        averaged = summed / lengths                          # (batch_size, emb_dim)
        out = self.fc(averaged)                              # (batch_size, 1)
        return self.sigmoid(out)                             # (batch_size, 1)

# -----------------------------
# 平均ベクトルを返すユーティリティ関数（単一インスタンス用）
# -----------------------------
def make_bow_vector(input_ids, embedding_matrix):
    """
    input_ids: 1次元のトークンIDテンソル
    embedding_matrix: (vocab_size, emb_dim) のtorch.Tensor

    出力: (emb_dim,) の平均ベクトル
    """
    if len(input_ids) == 0:
        return torch.zeros(embedding_matrix.size(1))
    vecs = embedding_matrix[input_ids]
    return vecs.mean(dim=0)

# -----------------------------
# テスト
# -----------------------------
if __name__ == "__main__":
    embedding = torch.load("embedding.pt")  # (vocab_size, emb_dim)
    model = BoWClassifier(embedding)

    # 仮のinput_ids（例: バッチサイズ2、長さ5）
    dummy_input = torch.tensor([[4, 10, 15, 0, 0], [5, 20, 30, 40, 50]])
    output = model(dummy_input)
    print("🧪 出力:", output)
