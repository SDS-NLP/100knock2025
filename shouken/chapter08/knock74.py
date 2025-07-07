import torch
from torch.utils.data import DataLoader
from knock72 import BoWClassifier
from knock73 import embedding_matrix  # 学習済みのモデルと同じ重み
from knock71 import dev_dataset       # 入力: text, label, input_ids 含む辞書
import torch.nn.functional as F

# 評価用データセット
class SSTDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        return item['input_ids'], item['label']

def collate_batch(batch):
    input_ids_list, labels = zip(*batch)
    padded = torch.nn.utils.rnn.pad_sequence(input_ids_list, batch_first=True, padding_value=0)
    labels = torch.stack(labels)
    return padded, labels

# DataLoader
dev_loader = DataLoader(
    dataset=SSTDataset(dev_dataset),
    batch_size=32,
    shuffle=False,
    collate_fn=collate_batch
)

# デバイス設定
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# モデル再構築（学習済みモデルと同一）
model = BoWClassifier(embedding_matrix).to(device)
model.load_state_dict(torch.load("bow_model.pt"))  # 73で保存していれば
model.eval()

# 評価ループ
correct = 0
total = 0

with torch.no_grad():
    for input_ids, labels in dev_loader:
        input_ids, labels = input_ids.to(device), labels.to(device)
        outputs = model(input_ids)
        preds = (outputs >= 0.5).float()
        correct += (preds == labels).sum().item()
        total += labels.size(0)

accuracy = correct / total
print(f"開発セットの正解率: {accuracy:.4f}")
