# ニューラルネットワークのアーキテクチャを自由に変更し、モデルを学習せよ。また、学習したモデルの開発セットにおける正解率を求めよ。例えば、テキストの特徴ベクトル（単語埋め込みの平均ベクトル）に対して多層のニューラルネットワークを通したり、畳み込みニューラルネットワーク（CNN; Convolutional Neural Network）や再帰型ニューラルネットワーク（RNN; Recurrent Neural Network）などのモデルの学習に挑戦するとよい。

from knock70 import E, word_to_index, index_to_word
from knock71 import train_data, dev_data
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

class WordEmbeddingSequenceDataset(Dataset):
    """単語埋め込みの系列を使用したデータセットクラス（パディングあり）"""
    def __init__(self, data, embedding_matrix, pad_idx=0, max_len=None):
        self.embedding_matrix = embedding_matrix
        self.pad_idx = pad_idx
        self.max_len = max_len if max_len is not None else self._get_max_len(data)
        self.features, self.labels = self._prepare_data(data)

    def _get_max_len(self, data):
        return max(len(item['input_ids']) for item in data)

    def _prepare_data(self, data):
        features = []
        labels = []
        for item in data:
            ids = item['input_ids']
            if not isinstance(ids, list):
                ids = list(ids)
            padded = ids + [self.pad_idx] * (self.max_len - len(ids))
            word_vectors = [self.embedding_matrix[i] for i in padded]
            features.append(word_vectors)
            labels.append(item['label'][0].item())
        return torch.FloatTensor(features), torch.FloatTensor(labels)

    def __len__(self):
        return len(self.features)

    def __getitem__(self, idx):
        return self.features[idx], self.labels[idx]

def collate_fn_cnn(batch):
    features = torch.stack([item[0] for item in batch])  # (B, L, D)
    features = features.permute(0, 2, 1)  # (B, D, L)
    labels = torch.stack([item[1] for item in batch])
    return features, labels

class CNNTextClassifier(nn.Module):
    def __init__(self, embed_dim, num_classes=1, kernel_size=3, num_filters=100):
        super().__init__()
        self.conv = nn.Conv1d(embed_dim, num_filters, kernel_size, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.AdaptiveMaxPool1d(1)
        self.fc = nn.Linear(num_filters, num_classes)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.conv(x)  # (B, F, L)
        x = self.relu(x)
        x = self.pool(x).squeeze(-1)  # (B, F)
        x = self.fc(x)
        x = self.sigmoid(x).squeeze(-1)
        return x

def create_data_loaders_cnn(train_data, dev_data, embedding_matrix, batch_size=32):
    max_len = max(
        max(len(item['input_ids']) for item in train_data),
        max(len(item['input_ids']) for item in dev_data)
    )
    train_dataset = WordEmbeddingSequenceDataset(train_data, embedding_matrix, max_len=max_len)
    dev_dataset = WordEmbeddingSequenceDataset(dev_data, embedding_matrix, max_len=max_len)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn_cnn)
    dev_loader = DataLoader(dev_dataset, batch_size=batch_size, shuffle=False, collate_fn=collate_fn_cnn)
    return train_loader, dev_loader

def train_model(model, train_loader, dev_loader, num_epochs=1, lr=0.01):
    criterion = nn.BCELoss()
    optimizer = optim.SGD(model.parameters(), lr=lr)
    for epoch in range(num_epochs):
        model.train()
        total_loss = 0
        for batch_X, batch_y in train_loader:
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        if (epoch + 1) % 10 == 0:
            avg_loss = total_loss / len(train_loader)
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss:.4f}')

def evaluate_model(model, dev_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for batch_X, batch_y in dev_loader:
            outputs = model(batch_X)
            predictions = (outputs >= 0.5).float()
            correct += (predictions == batch_y).sum().item()
            total += batch_y.size(0)
    accuracy = correct / total
    print(f'開発データでの精度: {accuracy:.4f}')
    return accuracy

def main():
    train_loader, dev_loader = create_data_loaders_cnn(train_data, dev_data, E)
    sample_batch = next(iter(train_loader))
    input_dim = sample_batch[0].shape[1]
    print(f"CNN入力次元数: {input_dim}")
    model = CNNTextClassifier(embed_dim=input_dim)
    train_model(model, train_loader, dev_loader)
    accuracy = evaluate_model(model, dev_loader)
    return model, accuracy

if __name__ == "__main__":
    model, accuracy = main()




