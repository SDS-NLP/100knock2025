import torch
import torch.nn as nn
from knock70 import word2id, E

# 例：埋め込み行列 E (numpy → torch に変換済)
# E.shape = (vocab_size, embedding_dim)
embedding_matrix = torch.tensor(E, dtype=torch.float32)

# テキスト → 単語ID列（例: "great movie" → [123, 456]）
tokens = ["great", "movie"]
input_ids = [word2id[w] for w in tokens if w in word2id]
input_vec = embedding_matrix[input_ids].mean(dim=0)  # 平均埋め込み (d_emb,)

# モデル定義（ロジスティック回帰）
class BoWLogisticRegression(nn.Module):
    def __init__(self, embedding_dim):
        super().__init__()
        self.linear = nn.Linear(embedding_dim, 1)

    def forward(self, x):
        return torch.sigmoid(self.linear(x)).squeeze(1)

# モデルインスタンス
model = BoWLogisticRegression(embedding_dim=embedding_matrix.size(1))

# 動作確認（1件分）
with torch.no_grad():
    output = model(input_vec.unsqueeze(0))  # (1, d_emb)
    print("出力確率:", output.item())
