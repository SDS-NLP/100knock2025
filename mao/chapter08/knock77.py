"""
knock77:GPUでの学習
問題76のモデル学習をGPU上で実行せよ。
また、学習したモデルの開発セットにおける正解率を求めよ。
"""
#GPUでの実行ができなかったのでGoogle Colaboで実行

import torch
from torch import nn
from torch.utils.data import DataLoader
from knock70 import embedding_matrix
from knock71 import train_data, dev_data
from knock72 import BoWClassifier
from knock75 import collate
from tqdm import tqdm
import pickle

# 保存する対象
objects_to_save = {
    'embedding_matrix': embedding_matrix,
    'train_data': train_data,
    'dev_data': dev_data,
    'model_class': BoWClassifier,
    'collate_fn': collate
}

# 保存先ファイル名
with open('saved_objects.pkl', 'wb') as f:
    pickle.dump(objects_to_save, f)


# --- GPUに転送 ---
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"✅ Using device: {device}")

# --- モデル・損失関数・最適化 ---
model = BoWClassifier(embedding_matrix).to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# --- データローダ ---
train_loader = DataLoader(train_data, batch_size=64, shuffle=True, collate_fn=collate)
dev_loader = DataLoader(dev_data, batch_size=64, shuffle=False, collate_fn=collate)

# --- 学習ループ ---
for epoch in range(1, 6):
    model.train()
    total_loss = 0.0

    for batch in tqdm(train_loader, desc=f"Epoch {epoch}"):
        input_ids = batch['input_ids'].to(device)
        labels = batch['label'].to(device).squeeze()

        optimizer.zero_grad()
        logits = model(input_ids)
        loss = criterion(logits, labels)
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
            input_ids = batch['input_ids'].to(device)
            labels = batch['label'].to(device).squeeze()
            logits = model(input_ids)
            preds = (torch.sigmoid(logits) >= 0.5).float()
            correct += (preds == labels).sum().item()
            total += labels.size(0)

    return correct / total

# --- 開発セット評価 ---
dev_accuracy = evaluate(model, dev_loader)
print(f"✅ 開発セットの正解率: {dev_accuracy:.4f}")
