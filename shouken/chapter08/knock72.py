import torch
import torch.nn as nn

class BoWClassifier(nn.Module):
    def __init__(self, embedding_matrix):
        super().__init__()
        vocab_size, embedding_dim = embedding_matrix.shape

        # 事前学習済み埋め込みを設定
        self.embedding = nn.Embedding.from_pretrained(
            embeddings=torch.tensor(embedding_matrix, dtype=torch.float32),
            freeze=True  # 埋め込みは固定
        )

        # 線形層（ロジスティック回帰）
        self.linear = nn.Linear(embedding_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, input_ids):
        """
        input_ids: (batch_size, seq_len) 形式の LongTensor
        """
        embedded = self.embedding(input_ids)            # (batch_size, seq_len, embed_dim)
        mean_vector = embedded.mean(dim=1)              # 平均プーリング (batch_size, embed_dim)
        logits = self.linear(mean_vector)               # (batch_size, 1)
        probs = self.sigmoid(logits)                    # (batch_size, 1)
        return probs
