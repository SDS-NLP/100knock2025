from knock75 import collate
from knock70 import embedding_dim, embedding_matrix
from knock71 import df1_data, df2_data
from knock72 import LogisticRegressionClassifier
import torch
import torch.nn as nn

vocab_size = embedding_matrix.shape[0]
embedding_dim = embedding_matrix.shape[1]

# embedding_matrix はすでに Tensor と仮定
embedding_matrix = embedding_matrix.detach().clone().float()  # UserWarningを防ぐ
embedding_layer = nn.Embedding(vocab_size, embedding_dim)
embedding_layer.weight.data.copy_(embedding_matrix)
embedding_layer.weight.requires_grad = True  # 必要なら


#dataloaderに渡す用に取得できる要素を定義
class MyDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, idx):
        return self.data[idx]

    def __len__(self):
        return len(self.data)

#パディングされたミニバッチの入力系列から平均埋め込みベクトルを計算する
def average_embedding_batch(input_ids, embedding_matrix):
    embedded = embedding_layer(input_ids)  # (B, L, D)
    mask = (input_ids != 0).unsqueeze(-1)   # (B, L, 1)
    summed = (embedded * mask).sum(dim=1)   # 長さ方向に合計
    lengths = mask.sum(dim=1)               # 実際の長さ
    return summed / lengths                 # 平均 (B, D)

# 変換
embedding_matrix = torch.tensor(embedding_matrix, dtype=torch.float32)

train_dataset = MyDataset(df1_data)
dev_dataset = MyDataset(df2_data)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=4, shuffle=True, collate_fn=collate)
dev_loader = torch.utils.data.DataLoader(dev_dataset, batch_size=4, shuffle=False, collate_fn=collate)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class MLPClassifier(nn.Module):
    def __init__(self, input_dim, hidden_dims=[128, 64]):
        super().__init__()
        layers = []
        last_dim = input_dim
        for h in hidden_dims:
            layers.append(nn.Linear(last_dim, h))
            layers.append(nn.ReLU())
            last_dim = h
        layers.append(nn.Linear(last_dim, 1))
        self.model = nn.Sequential(*layers)

    def forward(self, x):
        return torch.sigmoid(self.model(x))

model = MLPClassifier(input_dim=embedding_dim, hidden_dims=[256, 128])
model = model.to(device)
embedding_layer = embedding_layer.to(device)

loss_fn = nn.BCELoss()
optimizer = torch.optim.Adam(list(model.parameters()) + list(embedding_layer.parameters()))

# 学習
num_epochs = 20
for epoch in range(num_epochs):
    model.train()
    total_loss = 0
    for batch in train_loader:
        input_ids = batch['input_ids'].to(device)
        labels = batch['label'].to(device)

        optimizer.zero_grad()
        X = average_embedding_batch(input_ids, embedding_layer)
        preds = model(X).squeeze()
        loss = loss_fn(preds, labels.squeeze())
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    print(f"Epoch {epoch+1}: Loss = {total_loss:.4f}")

# 評価
model.eval()
total = correct = 0
with torch.no_grad():
    for batch in dev_loader:
        input_ids = batch['input_ids'].to(device)
        labels = batch['label'].to(device)
        X = average_embedding_batch(input_ids, embedding_layer)
        preds = model(X).squeeze()
        pred_labels = (preds >= 0.5).float()
        correct += (pred_labels == labels.squeeze()).sum().item()
        total += labels.size(0)

print(f"Dev Accuracy: {correct / total:.4f}")
