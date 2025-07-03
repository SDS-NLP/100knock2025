#!/usr/bin/env python
# coding: utf-8

# In[2]:


import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from gensim.models import KeyedVectors
import numpy as np
import csv
from collections import Counter
from sklearn.metrics import accuracy_score

w2v_path = "/Users/niaomuqing/100knock2025/GoogleNews-vectors-negative300.bin" 
print("Loading Word2Vec model...")
try:
    if 'w2v_model_loaded' not in globals(): 
        w2v = KeyedVectors.load_word2vec_format(w2v_path, binary=True)
        globals()['w2v_model_loaded'] = w2v
    else:
        w2v = globals()['w2v_model_loaded']
    print("Loaded!")
except Exception as e:
    print(f"Error loading Word2Vec model: {e}")
    print("Please ensure 'GoogleNews-vectors-negative300.bin' is in the correct path and accessible.")
    exit()

def convert_w2v_to_embedding_matrix(w2v_model, max_vocab=100000): 
    word2id = {'<PAD>': 0}
    vectors = [np.zeros(w2v_model.vector_size)]

    for word in w2v_model.index_to_key: 
        if len(word2id) >= max_vocab + 1:
            break
        word2id[word] = len(vectors)
        vectors.append(w2v_model[word])

    embedding_matrix = torch.tensor(np.array(vectors), dtype=torch.float32)
    id2word = {v: k for k, v in word2id.items()}
    return embedding_matrix, word2id, id2word

embedding_matrix, word2id, id2word = convert_w2v_to_embedding_matrix(w2v)
print(f"embedding_matrix 生成成功. 語彙数: {len(word2id)}")

class SST2Dataset(Dataset):
    def __init__(self, data_path, word2id):
        self.data = []
        self.word2id = word2id
        with open(data_path, encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                text = row['sentence']
                label = int(row['label'])
                tokens = text.split()
                input_ids = [self.word2id.get(token, 0) for token in tokens]
                self.data.append({
                    'input_ids': torch.tensor(input_ids, dtype=torch.long),
                    'label': torch.tensor([label], dtype=torch.float32)
                })

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

base_path = "/Users/niaomuqing/100knock2025/SST-2/"
train_path = base_path + "train.tsv"
dev_path = base_path + "dev.tsv"

train_dataset = SST2Dataset(train_path, word2id)
dev_dataset = SST2Dataset(dev_path, word2id)

print(f"訓練データセットのサンプル数: {len(train_dataset)}")
print(f"開発データセットのサンプル数: {len(dev_dataset)}")

def collate_fn(batch):
    lengths = [len(d['input_ids']) for d in batch]
    sorted_batch_tuples = sorted([(length, i, item) for i, (length, item) in enumerate(zip(lengths, batch))], 
                                 key=lambda x: x[0], reverse=True) 

    sorted_lengths = [t[0] for t in sorted_batch_tuples]
    sorted_items = [t[2] for t in sorted_batch_tuples] 

    max_len = sorted_lengths[0]

    padded_input_ids = []
    labels = []
    for item in sorted_items:
        input_ids = item['input_ids']
        label = item['label']

        current_len = len(input_ids)
        padding_needed = max_len - current_len

        padded_ids = torch.cat([input_ids, torch.zeros(padding_needed, dtype=torch.long)])
        padded_input_ids.append(padded_ids)
        labels.append(label)

    final_input_ids_tensor = torch.stack(padded_input_ids)
    final_labels_tensor = torch.stack(labels)

    return {'input_ids': final_input_ids_tensor, 'label': final_labels_tensor}

class BoWLogRegModel(nn.Module):
    def __init__(self, embedding_matrix):
        super().__init__()
        self.emb = nn.Embedding.from_pretrained(embedding_matrix, freeze=False) 
        self.linear = nn.Linear(embedding_matrix.shape[1], 1)

    def forward(self, input_ids):
        emb = self.emb(input_ids)              
        mean_emb = emb.mean(dim=1)             
        logits = self.linear(mean_emb)         
        probs = torch.sigmoid(logits)          
        return probs

if torch.backends.mps.is_available():
    device = torch.device("mps")
    print("使用 Apple Silicon (MPS) GPU。")
elif torch.cuda.is_available(): 
    device = torch.device("cuda")
    print("使用 NVIDIA CUDA GPU。")
else:
    device = torch.device("cpu")
    print("使用 CPU。")

print(f"\n使用デバイス: {device}")

model = BoWLogRegModel(embedding_matrix).to(device)
criterion = nn.BCELoss()
optimizer = optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=0.001)

BATCH_SIZE = 64
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, collate_fn=collate_fn)
dev_loader = DataLoader(dev_dataset, batch_size=BATCH_SIZE, shuffle=False, collate_fn=collate_fn)

EPOCHS = 10

print("\n--- モデル訓練開始 (単語埋め込みファインチューニングあり) ---")
for epoch in range(EPOCHS):
    model.train()
    total_loss = 0.0
    for i, batch in enumerate(train_loader):
        batch_x = batch['input_ids'].to(device)
        batch_y = batch['label'].to(device)

        optimizer.zero_grad()
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"[Epoch {epoch+1}/{EPOCHS}] Loss: {total_loss:.4f}")

print("\n--- モデル評価開始 (開発セット) ---")
model.eval()
all_preds = []
all_labels = []
with torch.no_grad():
    for batch in dev_loader:
        batch_x = batch['input_ids'].to(device)
        batch_y = batch['label'].to(device)

        outputs = model(batch_x)
        preds = (outputs >= 0.5).float()

        all_preds.append(preds.cpu())
        all_labels.append(batch_y.cpu())

final_preds = torch.cat(all_preds).numpy()
final_labels = torch.cat(all_labels).numpy()

acc = accuracy_score(final_labels, final_preds)

print(f"開発セットの正解率（Accuracy）: {acc * 100:.2f}%")

