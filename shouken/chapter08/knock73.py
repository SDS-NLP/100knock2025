import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from knock72 import BoWClassifier
from knock71 import train_dataset  # text, label, input_ids の list of dict
from knock70 import embedding_matrix

# 設定
batch_size = 32
num_epochs = 5
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Dataset → DataLoader に変換
class SSTDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        return item['input_ids'], item['label']

# collate_fn（可変長の入力をパディングしてバッチ化）
def collate_batch(batch):
    input_ids_list, labels = zip(*batch)
    padded = torch.nn.utils.rnn.pad_sequence(input_ids_list, batch_first=True, padding_value=0)
    labels = torch.stack(labels)
    return padded.to(device), labels.to(device)

train_loader = DataLoader(
    dataset=SSTDataset(train_dataset),
    batch_size=batch_size,
    shuffle=True,
    collate_fn=collate_batch
)

# モデル構築
model = BoWClassifier(embedding_matrix).to(device)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# 学習ループ
for epoch in range(1, num_epochs + 1):
    model.train()
    total_loss = 0
    for batch_inputs, batch_labels in train_loader:
        optimizer.zero_grad()
        outputs = model(batch_inputs)
        loss = criterion(outputs, batch_labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    avg_loss = total_loss / len(train_loader)
    print(f"Epoch {epoch}: 損失 = {avg_loss:.4f}")
