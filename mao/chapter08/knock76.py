"""
knock76:ミニバッチ学習
問題75のパディングの処理を活用して、ミニバッチでモデルを学習せよ。
また、学習したモデルの開発セットにおける正解率を求めよ。
"""
import torch
from torch import nn
from torch.utils.data import DataLoader
from knock70 import embedding_matrix
from knock71 import train_data, dev_data
from knock72 import BoWClassifier
from knock75 import collate  # ここが新しい
from tqdm import tqdm

# --- モデル・学習設定 ---
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = BoWClassifier(embedding_matrix).to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# --- データローダ ---
train_loader = DataLoader(train_data, batch_size=64, shuffle=True, collate_fn=collate)
dev_loader = DataLoader(dev_data, batch_size=64, shuffle=False, collate_fn=collate)

# --- 学習ループ ---
for epoch in range(1, 20):
    model.train()
    total_loss = 0

    for batch in tqdm(train_loader, desc=f"Epoch {epoch}"):
        input_ids, labels = batch['input_ids'].to(device), batch['label'].to(device)

        optimizer.zero_grad()
        logits = model(input_ids)
        loss = criterion(logits, labels.squeeze())
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(train_loader)
    print(f"▶️ Epoch {epoch} - Training Loss: {avg_loss:.4f}")

# --- 評価関数 ---
def evaluate(model, dataloader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for batch in dataloader:
            input_ids, labels = batch['input_ids'].to(device), batch['label'].to(device)
            logits = model(input_ids)
            preds = (torch.sigmoid(logits) >= 0.5).float()
            correct += (preds == labels.squeeze()).sum().item()
            total += labels.size(0)
    return correct / total

# --- 開発セットでの正解率評価 ---
dev_acc = evaluate(model, dev_loader)
print(f"✅ 開発セットの正解率: {dev_acc:.4f}") #開発セットの正解率: 0.7890
