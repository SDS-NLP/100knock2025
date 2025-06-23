"""
knock72:Bag of words モデルの構築
単語埋め込みの平均ベクトルでテキストの特徴ベクトルを表現し、
重みベクトルとの内積でポジティブ及びネガティブを分類するニューラルネットワーク
（ロジスティック回帰モデル）を設計せよ。
"""
import torch
import torch.nn as nn
import torch.nn.functional as F

class BoWClassifier(nn.Module):
    def __init__(self, embedding_matrix):
        super().__init__()
        vocab_size, embedding_dim = embedding_matrix.shape
        
        # 単語埋め込み層：事前学習済みの重みを固定（凍結）
        self.embedding = nn.Embedding.from_pretrained(
            torch.tensor(embedding_matrix, dtype=torch.float32),
            freeze=True
        )
        
        # 線形層（出力1次元 → sigmoidで2値分類）
        self.linear = nn.Linear(embedding_dim, 1)

    def forward(self, input_ids):
        """
        input_ids: (batch_size, seq_len)
        return: (batch_size, 1)
        """
        # (batch_size, seq_len, embedding_dim)
        embeds = self.embedding(input_ids)
        
        # パディング対策なしの平均（必要あればマスク処理を加えてください）
        mean_vec = embeds.mean(dim=1)  # (batch_size, embedding_dim)
        
        logits = self.linear(mean_vec)  # (batch_size, 1)
        return logits.squeeze(1)        # (batch_size,)
