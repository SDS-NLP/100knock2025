# 単語埋め込みの平均ベクトルでテキストの特徴ベクトルを表現し、重みベクトルとの内積でポジティブ及びネガティブを分類するニューラルネットワーク（ロジスティック回帰モデル）を設計せよ。

from knock70 import E, word_to_index, index_to_word
from knock71 import train_data, dev_data
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

class WordEmbeddingDataset(Dataset):
    """単語埋め込みの平均ベクトルを使用したデータセットクラス"""
    
    def __init__(self, data, embedding_matrix):
        self.embedding_matrix = embedding_matrix
        self.features, self.labels = self._prepare_data(data)
    
    def _prepare_data(self, data):
        """データの前処理：単語埋め込みの平均ベクトルを計算"""
        features = []
        labels = []
        
        for item in data:
            # 各単語の埋め込みベクトルを取得
            word_vectors = [self.embedding_matrix[id] for id in item['input_ids']]
            # 平均ベクトルを計算
            mean_vector = np.mean(word_vectors, axis=0)
            features.append(mean_vector)
            labels.append(item['label'][0].item())
        
        return torch.FloatTensor(features), torch.FloatTensor(labels)
    
    def __len__(self):
        return len(self.features)
    
    def __getitem__(self, idx):
        return self.features[idx], self.labels[idx]

class LogisticRegression(nn.Module):
    """ロジスティック回帰モデル（単層ニューラルネットワーク）"""
    
    def __init__(self, input_dim):
        super(LogisticRegression, self).__init__()
        self.linear = nn.Linear(input_dim, 1)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        return self.sigmoid(self.linear(x))

def create_data_loaders(train_data, dev_data, embedding_matrix, batch_size=32):
    """データローダーを作成する関数"""
    # データセットを作成
    train_dataset = WordEmbeddingDataset(train_data, embedding_matrix)
    dev_dataset = WordEmbeddingDataset(dev_data, embedding_matrix)
    
    # データローダーを作成
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    dev_loader = DataLoader(dev_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, dev_loader

def train_model(model, train_loader, dev_loader, num_epochs=100, lr=0.01):
    """モデルの学習を行う関数"""
    criterion = nn.BCELoss()
    optimizer = optim.SGD(model.parameters(), lr=lr)
    
    for epoch in range(num_epochs):
        # 学習モード
        model.train()
        total_loss = 0
        
        for batch_X, batch_y in train_loader:
            optimizer.zero_grad()
            
            # 順伝播
            outputs = model(batch_X).squeeze()
            loss = criterion(outputs, batch_y)
            
            # 逆伝播
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        # 10エポックごとに損失を表示
        if (epoch + 1) % 10 == 0:
            avg_loss = total_loss / len(train_loader)
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss:.4f}')

def evaluate_model(model, dev_loader):
    """モデルの評価を行う関数"""
    model.eval()
    correct = 0
    total = 0
    
    with torch.no_grad():
        for batch_X, batch_y in dev_loader:
            outputs = model(batch_X).squeeze()
            predictions = (outputs >= 0.5).float()
            correct += (predictions == batch_y).sum().item()
            total += batch_y.size(0)
    
    accuracy = correct / total
    print(f'開発データでの精度: {accuracy:.4f}')
    return accuracy

def main():
    """メイン処理"""
    # データローダーを作成
    train_loader, dev_loader = create_data_loaders(train_data, dev_data, E)
    
    # 入力次元数を取得（最初のバッチから）
    sample_batch = next(iter(train_loader))
    input_dim = sample_batch[0].shape[1]
    print(f"入力次元数: {input_dim}")
    
    # モデルを初期化
    model = LogisticRegression(input_dim)
    
    return model

if __name__ == "__main__":
    model = main()




