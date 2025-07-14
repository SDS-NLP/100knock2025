import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.nn.utils.rnn import pad_sequence
from knock72 import train_data, dev_data
from knock70 import token_to_id, id_to_token, embedding_matrix

# --------------- Dataset & DataLoader 準備 ----------------
class SSTDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data  # list of dict {'input_ids':Tensor, 'label':Tensor, ...}

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        return item['input_ids'], item['label']

def collate_fn(batch):
    # batch: list of tuples (input_ids, label)
    input_ids_list, labels = zip(*batch)
    # パディング: 0 (<PAD>) で埋める
    padded = pad_sequence(input_ids_list, batch_first=True, padding_value=0)
    labels = torch.stack(labels, dim=0)
    return padded, labels

# DataLoader 作成
train_dataset = SSTDataset(train_data)
dev_dataset   = SSTDataset(dev_data)
train_loader  = DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=collate_fn)
dev_loader    = DataLoader(dev_dataset,   batch_size=64, shuffle=False, collate_fn=collate_fn)


# --------------- モデル定義 ----------------
class SentimentModel(nn.Module):
    def __init__(self, embedding_matrix):
        super().__init__()
        num_embeddings, embedding_dim = embedding_matrix.shape
        # 事前学習埋め込みの読み込み・固定
        self.embedding = nn.Embedding.from_pretrained(
            torch.tensor(embedding_matrix),  # numpy -> Tensor
            freeze=True
        )
        # ロジスティック回帰
        self.linear = nn.Linear(embedding_dim, 1)

    def forward(self, input_ids):
        # input_ids: [B, L]
        embeds = self.embedding(input_ids)       # [B, L, D]
        avg    = embeds.mean(dim=1)              # [B, D]
        logits = self.linear(avg).squeeze(1)     # [B]
        probs  = torch.sigmoid(logits)           # [B]
        return probs

# モデル・オプティマイザ・損失関数
model = SentimentModel(embedding_matrix)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

optimizer = optim.Adam(model.linear.parameters(), lr=1e-3)
criterion = nn.BCELoss()


# --------------- 学習ループ ----------------
num_epochs = 5
for epoch in range(1, num_epochs+1):
    model.train()
    total_loss = 0.0
    for batch_idx, (input_ids, labels) in enumerate(train_loader, 1):
        input_ids = input_ids.to(device)
        labels    = labels.to(device).float().squeeze(1)  # [B]

        optimizer.zero_grad()
        outputs = model(input_ids)                      # [B]
        loss    = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        if batch_idx % 100 == 0:
            avg_loss = total_loss / batch_idx
            print(f'Epoch {epoch} | Batch {batch_idx}/{len(train_loader)} | Loss: {avg_loss:.4f}')

    # エポックごとの平均損失
    epoch_loss = total_loss / len(train_loader)
    print(f'=== Epoch {epoch} finished. Average Loss: {epoch_loss:.4f} ===')

    # --------------- 開発セットで評価 ----------------
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for input_ids, labels in dev_loader:
            input_ids = input_ids.to(device)
            labels    = labels.to(device).float().squeeze(1)
            probs     = model(input_ids)
            preds     = (probs >= 0.5).float()
            correct  += (preds == labels).sum().item()
            total    += labels.size(0)
    acc = correct / total
    print(f'--- Dev Accuracy after Epoch {epoch}: {acc*100:.2f}% ---\n')
