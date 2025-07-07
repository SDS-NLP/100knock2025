#73. モデルの学習
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from knock70 import E
from knock71 import train_dataset, dev_dataset

class SSTBoWDataset(Dataset):
    def __init__(self, loaded_dataset, embedding_matrix):
        self.data = []

        for example in loaded_dataset:
            input_ids = example["input_ids"]
            emb_vec = embedding_matrix[input_ids].mean(dim=0)
            self.data.append((emb_vec, example["label"]))

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
train_dataset = SSTBoWDataset(train_dataset, embedding_matrix)
dev_dataset = SSTBoWDataset(dev_dataset, embedding_matrix)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
dev_loader = DataLoader(dev_dataset, batch_size=32)

model = BoWLogisticRegression(embedding_dim=embedding_matrix.size(1))

if __name__ == "__main__":
    train_model(model, train_loader, dev_loader, epochs=10, lr=1e-3)
