# run_knock.py
# This script ties together knock70, knock71, and knock73 to load embeddings, data, train, and evaluate the sentiment model.

import torch
from torch.utils.data import Dataset, DataLoader
from torch.nn.utils.rnn import pad_sequence

from knock70 import load_pretrained_embeddings
from knock71 import load_data
import knock73


class SSTDataset(Dataset):
    """
    Dataset wrapper for SST data, returning (input_ids, label) tuples.
    """
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        return item['input_ids'], item['label']


def collate_fn(batch):
    """
    batch: list of (input_ids: Tensor, label: Tensor)
    Pads input_ids to the max length in batch using 0 (<PAD>), stacks labels.
    """
    input_ids_list, labels = zip(*batch)
    padded = pad_sequence(input_ids_list, batch_first=True, padding_value=0)
    labels = torch.stack(labels, dim=0)
    return padded, labels


def main():
    # Hyperparameters
    embedding_path = "GoogleNews-vectors-negative300.bin"  # path to pretrained embeddings
    vocab_size = 50000
    batch_size = 32
    lr = 1e-3
    num_epochs = 5

    # 1. Load pretrained embeddings (knock70)
    embedding_matrix, token_to_id, id_to_token = \
        load_pretrained_embeddings(embedding_path, vocab_size)

    # 2. Load SST-2 dataset (knock71)
    train_data = load_data("SST-2/train.tsv", token_to_id)
    dev_data   = load_data("SST-2/dev.tsv",   token_to_id)

    # 3. Wrap data in Dataset
    train_dataset = SSTDataset(train_data)
    dev_dataset   = SSTDataset(dev_data)

    # 4. Prepare DataLoaders
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)
    dev_loader   = DataLoader(dev_dataset,   batch_size=batch_size*2, shuffle=False, collate_fn=collate_fn)

    # 5. Initialize model, optimizer, loss
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = knock73.SentimentModel(embedding_matrix).to(device)
    optimizer = torch.optim.Adam(model.linear.parameters(), lr=lr)
    criterion = torch.nn.BCELoss()

    # 6. Training loop
    for epoch in range(1, num_epochs + 1):
        model.train()
        total_loss = 0.0
        for batch_idx, (input_ids, labels) in enumerate(train_loader, 1):
            input_ids = input_ids.to(device)
            labels    = labels.to(device).float().squeeze(1)

            optimizer.zero_grad()
            outputs = model(input_ids)
            loss    = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            if batch_idx % 100 == 0:
                avg_loss = total_loss / batch_idx
                print(f"Epoch {epoch} | Batch {batch_idx}/{len(train_loader)} | Loss: {avg_loss:.4f}")

        avg_epoch_loss = total_loss / len(train_loader)
        print(f"=== Epoch {epoch} finished. Average Loss: {avg_epoch_loss:.4f} ===")

        # 7. Development set evaluation
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
        accuracy = correct / total * 100
        print(f"--- Dev Accuracy after Epoch {epoch}: {accuracy:.2f}% ---\n")


if __name__ == "__main__":
    main()
