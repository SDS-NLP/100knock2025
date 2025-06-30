import torch
from torch.utils.data import DataLoader
from sklearn.metrics import accuracy_score
from knock71 import train_data, dev_data, embedding_model, word2idx
from knock72 import BoWLogisticRegression, compute_avg_embedding, SSTDataset
import numpy as np
import torch.nn as nn


embedding_dim = embedding_model.vector_size
vocab_size = len(word2idx)
embedding_matrix = np.zeros((vocab_size, embedding_dim), dtype=np.float32)
for word, idx in word2idx.items():
    if word == "<PAD>":
        continue
    embedding_matrix[idx] = embedding_model[word]
embedding_tensor = torch.tensor(embedding_matrix)

def collate(batch):
    batch = sorted(batch, key=lambda x: len(x["input_ids"]), reverse=True)
    input_ids = [item["input_ids"] for item in batch]
    labels = [item["label"] for item in batch]
    max_len = len(input_ids[0])
    padded_ids = [torch.cat([ids, torch.zeros(max_len - len(ids), dtype=torch.long)]) for ids in input_ids]
    return {
        "input_ids": torch.stack(padded_ids),
        "label": torch.stack(labels)
    }

train_loader = DataLoader(SSTDataset(train_data), batch_size=32, shuffle=True, collate_fn=collate)
dev_loader = DataLoader(SSTDataset(dev_data), batch_size=32, shuffle=False, collate_fn=collate)

model = BoWLogisticRegression(embedding_dim=embedding_tensor.shape[1])
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

num_epochs = 10
model.train()
for epoch in range(num_epochs):
    total_loss = 0
    for batch in train_loader:
        input_ids = batch["input_ids"]
        labels = batch["label"].squeeze(1)
        avg_emb = compute_avg_embedding(input_ids, embedding_tensor)
        logits = model(avg_emb)
        loss = criterion(logits, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    print(f"[Epoch {epoch+1}] Loss: {total_loss / len(train_loader):.4f}")

def evaluate(model, dataloader, embedding_tensor):
    model.eval()
    all_preds, all_labels = [], []
    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch["input_ids"]
            labels = batch["label"].squeeze(1)
            avg_emb = compute_avg_embedding(input_ids, embedding_tensor)
            logits = model(avg_emb)
            preds = (torch.sigmoid(logits) > 0.5).long()
            all_preds.extend(preds.tolist())
            all_labels.extend(labels.tolist())
    acc = accuracy_score(all_labels, all_preds)
    print(f"Development Set Accuracy: {acc:.4f}")
    model.train()

evaluate(model, dev_loader, embedding_tensor)