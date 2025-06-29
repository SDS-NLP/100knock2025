from knock75 import collate
from knock70 import embedding_dim, embedding_matrix
from knock71 import df1_data, df2_data
from knock72 import LogisticRegressionClassifier
import torch

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
    embedded = embedding_matrix[input_ids]  # (B, L, D)
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

model = LogisticRegressionClassifier(embedding_dim)
loss_fn = torch.nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters())

# 学習
for epoch in range(20):
    model.train()
    for batch in train_loader:
        X = average_embedding_batch(batch['input_ids'], embedding_matrix)
        y = batch['label']

        optimizer.zero_grad()
        y_pred = model(X)
        loss = loss_fn(y_pred, y)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}: Loss = {loss.item():.4f}")

# 評価（正解率）
model.eval()
correct = total = 0

with torch.no_grad():
    for batch in dev_loader:
        X = average_embedding_batch(batch['input_ids'], embedding_matrix)
        y = batch['label']
        y_pred = (model(X) >= 0.5).float()
        correct += (y_pred == y).sum().item()
        total += y.size(0)

accuracy = correct / total
print(f"Dev Accuracy: {accuracy:.4f}")
