from knock75 import collate
from knock70 import embedding_dim, embedding_matrix
from knock71 import df1_data, df2_data
from knock72 import LogisticRegressionClassifier
import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score


vocab_size = embedding_matrix.shape[0]
embedding_dim = embedding_matrix.shape[1]

embedding_layer = nn.Embedding(vocab_size, embedding_dim)
embedding_layer.weight.data.copy_(embedding_matrix.detach().clone()) 
embedding_layer.weight.requires_grad = True 

class MyDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, idx):
        return self.data[idx]

    def __len__(self):
        return len(self.data)

def average_embedding_batch(input_ids, embedding_layer):
    embedded = embedding_layer(input_ids)           
    mask = (input_ids != 0).unsqueeze(-1)           
    summed = (embedded * mask).sum(dim=1)           
    lengths = mask.sum(dim=1)                       
    return summed / lengths  

train_dataset = MyDataset(df1_data)
dev_dataset = MyDataset(df2_data)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=4, shuffle=True, collate_fn=collate)
dev_loader = torch.utils.data.DataLoader(dev_dataset, batch_size=4, shuffle=False, collate_fn=collate)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(torch.cuda.is_available())  # True なら GPU 使用可能
print(torch.cuda.get_device_name())  # 使用GPU名の確認
model = LogisticRegressionClassifier(embedding_dim).to(device)
embedding_layer = embedding_layer.to(device)
loss_fn = nn.BCELoss()

# 学習ループ
import torch
import torch.nn as nn
from tqdm import tqdm  

loss_fn = nn.BCELoss()
optimizer = torch.optim.Adam(list(model.parameters()) + list(embedding_layer.parameters()))

num_epochs = 5

for epoch in range(num_epochs):
    model.train()
    total_loss = 0

    for batch in tqdm(train_loader, desc=f"Epoch {epoch+1}"):
        input_ids = batch['input_ids'].to(device)
        labels = batch['label'].to(device)

        optimizer.zero_grad()
        X = average_embedding_batch(input_ids, embedding_layer)
        y_pred = model(X)

        loss = loss_fn(y_pred, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1} - Loss: {total_loss:.4f}")

model.eval()
total_loss = 0
all_preds = []
all_labels = []

with torch.no_grad():
    for batch in dev_loader:
        input_ids = batch['input_ids'].to(device)
        labels = batch['label'].to(device)

        X = average_embedding_batch(input_ids, embedding_layer)
        y_pred = model(X)

        loss = loss_fn(y_pred, labels)
        total_loss += loss.item()

        preds = (y_pred > 0.5).float()
        all_preds.append(preds.cpu())
        all_labels.append(labels.cpu())

# 結果集計
all_preds = torch.cat(all_preds)
all_labels = torch.cat(all_labels)
accuracy = accuracy_score(all_labels, all_preds)

print(f"[検証結果] Loss: {total_loss:.4f}, Accuracy: {accuracy:.4f}")
