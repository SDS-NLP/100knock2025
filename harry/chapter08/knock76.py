# knock76.py
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from knock71 import load_dataset
from knock72 import BoWClassifier
from knock75 import collate_fn

# -----------------------------
# Hyperparameters
# -----------------------------
BATCH_SIZE = 64
NUM_EPOCHS = 5
LR = 0.01

# -----------------------------
# Load data and embeddings
# -----------------------------
word2id = torch.load("word2id.pt")
embedding_matrix = torch.load("embedding.pt")

train_data = load_dataset("SST-2/train.tsv", word2id)
dev_data = load_dataset("SST-2/dev.tsv", word2id)

# -----------------------------
# Model, Loss, Optimizer
# -----------------------------
model = BoWClassifier(embedding_matrix)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=LR)

# -----------------------------
# DataLoader with collate_fn
# -----------------------------
train_loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True, collate_fn=collate_fn)
dev_loader = DataLoader(dev_data, batch_size=BATCH_SIZE, shuffle=False, collate_fn=collate_fn)

# -----------------------------
# Training Loop
# -----------------------------
model.train()
for epoch in range(NUM_EPOCHS):
    total_loss = 0.0
    for batch in train_loader:
        inputs = batch['input_ids']
        labels = batch['label'].squeeze()

        optimizer.zero_grad()
        outputs = model(inputs).squeeze()
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    print(f"📉 Epoch {epoch+1}: Loss = {total_loss:.4f}")

# -----------------------------
# Evaluation
# -----------------------------
model.eval()
correct = total = 0
with torch.no_grad():
    for batch in dev_loader:
        inputs = batch['input_ids']
        labels = batch['label'].squeeze()
        outputs = model(inputs).squeeze()
        preds = (outputs >= 0.5).float()
        correct += (preds == labels).sum().item()
        total += labels.size(0)

accuracy = correct / total
print(f"✅ 開発セットの正解率: {accuracy:.4f}")