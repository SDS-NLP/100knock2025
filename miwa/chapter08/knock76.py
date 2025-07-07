#76. ミニバッチ学習
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from knock70 import E
from knock71 import train_dataset, dev_dataset
from knock75 import collate

class SSTBoWDataset(Dataset):
    def __init__(self, loaded_dataset):
        self.data = loaded_dataset

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return  {
            "input_ids": torch.tensor(self.data[idx]["input_ids"], dtype=torch.long),
            "label": torch.tensor([self.data[idx]["label"]], dtype=torch.float)
        }

class BoWLogisticRegression(nn.Module):
    def __init__(self, embedding_dim):
        super().__init__()
        self.linear = nn.Linear(embedding_dim, 1)

    def forward(self, x):
        return torch.sigmoid(self.linear(x)).squeeze(1)

def train_model(model, train_loader, dev_loader, embedding_matrix, epochs=5, lr=1e-3):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    optimizer = optim.Adam(model.parameters(), lr=lr)
    criterion = nn.BCELoss()

    for epoch in range(1, epochs + 1):
        model.train()
        total_loss = 0

        for batch in train_loader:
            input_ids = batch["input_ids"].to(device)  
            labels = batch["label"].to(device).squeeze(1)

            # 埋め込み → 平均（BoW）
            emb = embedding_matrix[input_ids] 
            emb_mean = emb.mean(dim=1) 

            optimizer.zero_grad()
            preds = model(emb_mean)
            loss = criterion(preds, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        acc = evaluate(model, dev_loader, embedding_matrix, device)
        print(f"Epoch {epoch}: Loss={total_loss:.4f}, Dev Accuracy={acc:.4f}")

def evaluate(model, data_loader, embedding_matrix, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for batch in data_loader:
            input_ids = batch["input_ids"].to(device)
            labels = batch["label"].to(device).squeeze(1)

            emb = embedding_matrix[input_ids]  
            emb_mean = emb.mean(dim=1)    

            preds = model(emb_mean)
            predicted = (preds >= 0.5).float()
            correct += (predicted == labels).sum().item()
            total += labels.size(0)
    return correct / total

# 事前に読み込んだものを前提
# E: numpy配列 → 埋め込み行列
# word2id: 単語→ID辞書

if __name__ == "__main__":

    embedding_matrix = torch.tensor(E, dtype=torch.float32)
    embedding_matrix.requires_grad = False
    train_dataset = SSTBoWDataset(train_dataset)
    dev_dataset = SSTBoWDataset(dev_dataset)

    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=collate)
    dev_loader = DataLoader(dev_dataset, batch_size=32, collate_fn=collate)

    model = BoWLogisticRegression(embedding_dim=embedding_matrix.size(1))
    train_model(model, train_loader, dev_loader, embedding_matrix, epochs=10, lr=1e-3)

