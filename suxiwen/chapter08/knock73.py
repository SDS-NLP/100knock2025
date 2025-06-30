import torch
import torch.nn as nn
from tqdm import tqdm

# 前提: 72 問で定義した BagOfWordsModel を利用
class BagOfWordsModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.fc = nn.Linear(embedding_dim, 2)
        
        # 単語埋め込み行列を固定（ファインチューニングなし）
        self.embedding.weight.requires_grad = False  

    def forward(self, input_ids):
        embeds = self.embedding(input_ids)
        avg_embeds = torch.mean(embeds, dim=1)
        return self.fc(avg_embeds)

def train_model(model, train_loader, criterion, optimizer, device):
    model.train()
    total_loss = 0
    progress_bar = tqdm(train_loader, desc="学習中", leave=False)
    
    for batch in progress_bar:
        input_ids = batch['input_ids'].to(device)
        labels = batch['label'].to(device)
        
        optimizer.zero_grad()
        outputs = model(input_ids)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        progress_bar.set_postfix({"Loss": loss.item()})
    
    avg_loss = total_loss / len(train_loader)
    print(f"エポック終了 - 平均損失: {avg_loss:.4f}")
    return avg_loss

# 実行例（ダミーデータ用）
if __name__ == "__main__":
    # モデル・データローダー・損失関数の準備（実際は SST データを使用）
    vocab_size = 100000
    embedding_dim = 300
    model = BagOfWordsModel(vocab_size, embedding_dim).to("cuda")
    
    # ダミーデータローダー（実際は train.tsv から作成）
    class DummyLoader:
        def __iter__(self):
            for _ in range(10):  # ダミーバッチ数
                yield {'input_ids': torch.randint(0, vocab_size, (32, 50)), 
                       'label': torch.randint(0, 2, (32,))}
    
    train_loader = DummyLoader()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    
    # 学習実行（エポック数は適宜調整）
    for epoch in range(3):
        print(f"エポック {epoch+1} 開始")
        train_model(model, train_loader, criterion, optimizer, "cuda")