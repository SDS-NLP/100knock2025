from knock71 import df1_data, df2_data
from knock70 import token2id, embedding_dim, embedding_matrix
import torch
import torch.nn as nn


def average_embedding(input_ids, embedding_matrix):
    return embedding_matrix[input_ids].mean(dim=0)

X_train = torch.stack([average_embedding(s['input_ids'], embedding_matrix) for s in df1_data])
y_train = torch.stack([s['label'] for s in df1_data])

X_dev = torch.stack([average_embedding(s['input_ids'], embedding_matrix) for s in df2_data])
y_dev = torch.stack([s['label'] for s in df2_data])

class LogisticRegressionClassifier(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.linear = nn.Linear(input_dim, 1)  # 重みベクトルとバイアスを持つ

    def forward(self, x):
        return torch.sigmoid(self.linear(x))  # 確率として出力

model = LogisticRegressionClassifier(embedding_dim)