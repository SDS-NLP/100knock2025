import torch
from knock76 import MLPClassifier, embedding_tensor, train_loader, dev_loader, compute_avg_embedding, criterion, optimizer
from torch.utils.data import DataLoader
from sklearn.metrics import accuracy_score
import torch.nn as nn
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

model = MLPClassifier(embedding_dim=embedding_tensor.shape[1])
model.to(device)

# embedding_tensor もGPUへ（計算に使うため）
num_epochs = 10
embedding_tensor = embedding_tensor.to(device)
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

def evaluate(model, dataloader, embedding_tensor):
    model.eval()
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch["input_ids"].to(device)
            labels = batch["label"].squeeze(1).to(device)

            avg_emb = compute_avg_embedding(input_ids, embedding_tensor)
            logits = model(avg_emb)
            probs = torch.sigmoid(logits)
            preds = (probs > 0.5).long()

            all_preds.extend(preds.cpu().tolist())  # GPU→CPUに戻す
            all_labels.extend(labels.cpu().tolist())

    acc = accuracy_score(all_labels, all_preds)
    print(f"Development Set Accuracy: {acc:.4f}")
    model.train()
evaluate(model, dev_loader, embedding_tensor)
