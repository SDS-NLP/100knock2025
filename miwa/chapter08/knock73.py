#73. モデルの学習
import csv
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from knock70 import word2id, E

class SSTBoWDataset(Dataset):
    def __init__(self, file_path, word2id, embedding_matrix):
        self.data = []
        self.embedding_matrix = embedding_matrix
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader)  # skip header
            for row in reader:
                if len(row) != 2:
                    continue
                text, label_str = row
                tokens = text.strip().split()
                input_ids = [word2id[w] for w in tokens if w in word2id]
                if not input_ids:
                    continue
                emb_vec = self.embedding_matrix[input_ids].mean(dim=0)  # 平均ベクトル
                label = float(label_str)
                self.data.append((emb_vec, torch.tensor([label], dtype=torch.float32)))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

class BoWLogisticRegression(nn.Module):
    def __init__(self, embedding_dim):
        super().__init__()
        self.linear = nn.Linear(embedding_dim, 1)

    def forward(self, x):
        return torch.sigmoid(self.linear(x)).squeeze(1)

def train_model(model, train_loader, dev_loader, epochs=5, lr=1e-3):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    optimizer = optim.Adam(model.parameters(), lr=lr)
    criterion = nn.BCELoss()

    for epoch in range(1, epochs + 1):
        model.train()
        total_loss = 0
        for x, y in train_loader:
            x, y = x.to(device), y.to(device).squeeze(1)
            optimizer.zero_grad()
            preds = model(x)
            loss = criterion(preds, y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        acc = evaluate(model, dev_loader, device)
        print(f"Epoch {epoch}: Loss={total_loss:.4f}, Dev Accuracy={acc:.4f}")

def evaluate(model, data_loader, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for x, y in data_loader:
            x, y = x.to(device), y.to(device).squeeze(1)
            preds = model(x)
            predicted = (preds >= 0.5).float()
            correct += (predicted == y).sum().item()
            total += y.size(0)
    return correct / total

# 事前に読み込んだものを前提
# E: numpy配列 → 埋め込み行列
# word2id: 単語→ID辞書

embedding_matrix = torch.tensor(E, dtype=torch.float32)
embedding_matrix.requires_grad = False
train_dataset = SSTBoWDataset("chapter07/SST-2/train.tsv", word2id, embedding_matrix)
dev_dataset = SSTBoWDataset("chapter07/SST-2/dev.tsv", word2id, embedding_matrix)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
dev_loader = DataLoader(dev_dataset, batch_size=32)

model = BoWLogisticRegression(embedding_dim=embedding_matrix.size(1))
train_model(model, train_loader, dev_loader, epochs=10, lr=1e-3)
