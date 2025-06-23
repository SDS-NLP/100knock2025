"""
knock74:モデルの評価
問題73で学習したモデルの開発セットにおける正解率を求めよ。
"""
import torch
from torch.utils.data import DataLoader
from torch.nn.utils.rnn import pad_sequence
from knock71 import dev_data
from knock73 import model,collate_fn

# --- 評価用データローダ（knock73と同様のcollate） ---

dev_loader = DataLoader(dev_data, batch_size=64, collate_fn=collate_fn)

# --- 評価ループ ---
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.eval()  # 評価モード
model.to(device)

correct = 0
total = 0

with torch.no_grad():
    for input_ids, labels in dev_loader:
        input_ids, labels = input_ids.to(device), labels.to(device)
        logits =  model(input_ids)
        preds = (torch.sigmoid(logits) >= 0.5).float()  # 閾値0.5で分類

        correct += (preds == labels).sum().item()
        total += labels.size(0)

accuracy = correct / total
print(f'✅ 開発セットの正解率: {accuracy:.4f} ({correct}/{total})')
