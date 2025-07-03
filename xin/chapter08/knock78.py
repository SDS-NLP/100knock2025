import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from sklearn.metrics import accuracy_score
from knock72 import SSTDataset, collate_fn, embedding_matrix, train_data
from knock74 import dev_loader, evaluate
from knock75 import compute_avg_embedding
from knock76 import MLPClassifier

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 1. 学習可能な埋め込み層を作成
embedding_tensor = nn.Embedding.from_pretrained(
    torch.tensor(embedding_matrix), freeze=False
).to(device)

# 2. データローダー
train_loader = DataLoader(SSTDataset(train_data), batch_size=32, shuffle=True, collate_fn=collate_fn)

# 3. モデル構築
model = MLPClassifier(embedding_dim=embedding_tensor.embedding_dim).to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(list(model.parameters()) + list(embedding_tensor.parameters()), lr=1e-3)

# 4. 学習
num_epochs = 10
model.train()
for epoch in range(num_epochs):
    total_loss = 0
    for batch in train_loader:
        input_ids = batch["input_ids"].to(device)
        labels = batch["label"].squeeze(1).to(device)

        avg_emb = compute_avg_embedding(input_ids, embedding_tensor)
        logits = model(avg_emb)
        loss = criterion(logits, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
    print(f"[Epoch {epoch+1}] Loss: {total_loss / len(train_loader):.4f}")

# 5. 評価
evaluate(model.eval(), dev_loader, embedding_tensor)