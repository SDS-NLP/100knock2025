# 問題76のモデル学習をGPU上で実行せよ。また、学習したモデルの開発セットにおける正解率を求めよ。

from knock70 import E, word_to_index, index_to_word
from knock71 import train_data, dev_data
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

# GPU利用可能性のチェック
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'使用デバイス: {device}')

class WordEmbeddingDataset(Dataset):
    """単語ID列とラベルのみを返すデータセットクラス"""
    def __init__(self, data):
        self.input_ids = [torch.LongTensor(item['input_ids']) for item in data]
        self.labels = [item['label'][0].item() for item in data]

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.labels[idx]

def collate_fn(batch):
    input_ids, labels = zip(*batch)
    input_ids = torch.nn.utils.rnn.pad_sequence(input_ids, batch_first=True, padding_value=0)
    labels = torch.FloatTensor(labels)
    return input_ids, labels

class FineTuneEmbeddingClassifier(nn.Module):
    def __init__(self, embedding_matrix: torch.Tensor):
        super().__init__()
        # freeze=False でファインチューニング可能
        self.embedding = nn.Embedding.from_pretrained(embedding_matrix, freeze=False)
        self.linear = nn.Linear(embedding_matrix.size(1), 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        # input_ids: [batch_size, seq_len]
        embeds = self.embedding(input_ids)  # [batch_size, seq_len, emb_dim]
        mean_embeds = embeds.mean(dim=1)   # パディングも含めて平均
        return self.sigmoid(self.linear(mean_embeds))

def create_data_loaders(train_data, dev_data, batch_size=32):
    train_dataset = WordEmbeddingDataset(train_data)
    dev_dataset = WordEmbeddingDataset(dev_data)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)
    dev_loader = DataLoader(dev_dataset, batch_size=batch_size, shuffle=False, collate_fn=collate_fn)
    return train_loader, dev_loader

def train_model(model, train_loader, dev_loader, num_epochs=100, lr=0.01):
    criterion = nn.BCELoss()
    optimizer = optim.SGD(model.parameters(), lr=lr)
    for epoch in range(num_epochs):
        model.train()
        total_loss = 0
        for batch_X, batch_y in train_loader:
            batch_X = batch_X.to(device)
            batch_y = batch_y.to(device)
            optimizer.zero_grad()
            outputs = model(batch_X).squeeze()
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
            batch_X = batch_X.to(device)
            batch_y = batch_y.to(device)
            outputs = model(batch_X).squeeze()
            predictions = (outputs >= 0.5).float()
            correct += (predictions == batch_y).sum().item()
            total += batch_y.size(0)
    accuracy = correct / total
    print(f'開発データでの精度: {accuracy:.4f}')
    return accuracy

def main():
    train_loader, dev_loader = create_data_loaders(train_data, dev_data)
    vocab_size = len(E)
    embedding_dim = len(E[0])
    print(f"語彙数: {vocab_size}, 埋め込み次元数: {embedding_dim}")
    model = FineTuneEmbeddingClassifier(torch.FloatTensor(E)).to(device)
    train_model(model, train_loader, dev_loader)
    accuracy = evaluate_model(model, dev_loader)
    return model, accuracy

if __name__ == "__main__":
    model, accuracy = main()




