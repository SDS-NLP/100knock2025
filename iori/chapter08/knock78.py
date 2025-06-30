import torch
import torch.nn as nn
import pandas as pd
from typing import Dict, List, Set
from gensim.models import KeyedVectors
from torch.utils.data import DataLoader, Dataset

# デバイスの設定
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def load_sst2_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, sep="\t", header=0)


def get_vocabulary(df: pd.DataFrame) -> Set[str]:
    vocabulary = set()
    for text in df["sentence"]:
        vocabulary.update(text.lower().split())
    return vocabulary


class MeanEmbeddingClassifier(nn.Module):
    def __init__(self, embedding_matrix: torch.Tensor):
        super().__init__()
        # 埋め込み行列を更新可能にしてnn.Embeddingとして登録
        num_embeddings, embedding_dim = embedding_matrix.size()
        self.embedding = nn.Embedding(num_embeddings, embedding_dim)
        self.embedding.weight = nn.Parameter(embedding_matrix)
        self.linear = nn.Linear(embedding_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: [batch_size, max_len]
        embs = self.embedding(x)            # [batch_size, max_len, dim]
        mean_embs = torch.mean(embs, dim=1) # [batch_size, dim]
        return self.sigmoid(self.linear(mean_embs))


def load_word_embeddings(model_path: str, vocabulary: Set[str]) -> tuple[Dict[str, int], torch.Tensor]:
    word_to_id = {"<PAD>": 0}
    model = KeyedVectors.load_word2vec_format(model_path, binary=True)
    embs = [torch.zeros(model.vector_size)]
    for w in vocabulary:
        if w in model.key_to_index:
            word_to_id[w] = len(word_to_id)
            embs.append(torch.tensor(model[w]))
    embedding_matrix = torch.stack(embs).to(device)
    return word_to_id, embedding_matrix


def convert_text_to_ids(text: str, word_to_id: Dict[str, int]) -> List[int]:
    return [word_to_id[t] for t in text.lower().split() if t in word_to_id]


def collate(batch: List[Dict]) -> Dict[str, torch.Tensor]:
    max_len = max(len(x['input_ids']) for x in batch)
    bs = len(batch)
    input_tensor = torch.zeros(bs, max_len, dtype=torch.long)
    label_tensor = torch.zeros(bs, 1, dtype=torch.float)
    lengths = [len(x['input_ids']) for x in batch]
    sorted_idx = sorted(range(bs), key=lambda i: lengths[i], reverse=True)
    for i, idx in enumerate(sorted_idx):
        ids = batch[idx]['input_ids']
        input_tensor[i, :len(ids)] = ids
        label_tensor[i] = batch[idx]['label']
    return {'input_ids': input_tensor.to(device), 'label': label_tensor.to(device)}


class SST2Dataset(Dataset):
    def __init__(self, data: List[Dict]):
        self.data = data
    def __len__(self) -> int:
        return len(self.data)
    def __getitem__(self, idx: int) -> Dict:
        return self.data[idx]


def process_sst2_data(file_path: str, word_to_id: Dict[str, int]) -> List[Dict]:
    df = load_sst2_data(file_path)
    processed = []
    for _, row in df.iterrows():
        ids = convert_text_to_ids(row['sentence'], word_to_id)
        if not ids:
            continue
        processed.append({'text': row['sentence'], 'label': torch.tensor([float(row['label'])]), 'input_ids': torch.tensor(ids, dtype=torch.long)})
    return processed


def train_model(model: nn.Module, train_loader: DataLoader, dev_loader: DataLoader, num_epochs: int = 10, lr: float = 0.01):
    criterion = nn.BCELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=lr)
    for epoch in range(num_epochs):
        model.train()
        total_loss = 0
        for batch in train_loader:
            optimizer.zero_grad()
            outputs = model(batch['input_ids'])
            loss = criterion(outputs, batch['label'])
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch+1}/{num_epochs} - Loss: {total_loss/len(train_loader):.4f}")

    # 学習後に開発セットでの評価
    accuracy = evaluate_model(model, dev_loader)
    print(f"開発セットの正解率: {accuracy:.2f}%")


def evaluate_model(model: nn.Module, dev_loader: DataLoader) -> float:
    model.eval()
    correct = total = 0
    with torch.no_grad():
        for batch in dev_loader:
            outputs = model(batch['input_ids'])
            preds = (outputs > 0.5).float()
            total += batch['label'].size(0)
            correct += (preds == batch['label']).sum().item()
    return 100 * correct / total


def main():
    train_df = load_sst2_data("SST-2/train.tsv")
    dev_df = load_sst2_data("SST-2/dev.tsv")
    vocab = get_vocabulary(train_df) | get_vocabulary(dev_df)
    word_to_id, embedding_matrix = load_word_embeddings("GoogleNews-vectors-negative300.bin", vocab)
    train_data = process_sst2_data("SST-2/train.tsv", word_to_id)
    dev_data = process_sst2_data("SST-2/dev.tsv", word_to_id)
    train_loader = DataLoader(SST2Dataset(train_data), batch_size=8, shuffle=True, collate_fn=collate)
    dev_loader   = DataLoader(SST2Dataset(dev_data),   batch_size=8, shuffle=False, collate_fn=collate)
    model = MeanEmbeddingClassifier(embedding_matrix).to(device)
    train_model(model, train_loader, dev_loader)

if __name__ == "__main__":
    main()

'''Epoch 1/10 - Loss: 0.6681
Epoch 2/10 - Loss: 0.6371
Epoch 3/10 - Loss: 0.6103
Epoch 4/10 - Loss: 0.5863
Epoch 5/10 - Loss: 0.5644
Epoch 6/10 - Loss: 0.5446
Epoch 7/10 - Loss: 0.5246
Epoch 8/10 - Loss: 0.5089
Epoch 9/10 - Loss: 0.4941
Epoch 10/10 - Loss: 0.4800
開発セットの正解率: 80.39%'''