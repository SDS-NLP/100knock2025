import torch
from tqdm import tqdm

def evaluate_model(model, dev_loader, device):
    model.eval()
    correct = 0
    total = 0
    progress_bar = tqdm(dev_loader, desc="評価中", leave=False)
    
    with torch.no_grad():
        for batch in progress_bar:
            input_ids = batch['input_ids'].to(device)
            labels = batch['label'].to(device)
            
            outputs = model(input_ids)
            _, predicted = torch.max(outputs.data, 1)
            
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    accuracy = correct / total
    print(f"開発セット正解率: {accuracy * 100:.2f}%")
    return accuracy

# 実行例（ダミーデータ用）
if __name__ == "__main__":
    # 前提: 学習済みモデルと開発セットローダーが準備済み
    class DummyLoader:
        def __iter__(self):
            for _ in range(5):  # ダミーバッチ数
                yield {'input_ids': torch.randint(0, 100000, (32, 50)), 
                       'label': torch.randint(0, 2, (32,))}
    
    # 学習済みモデル（73問のモデルを仮定）
    from bag_of_words import BagOfWordsModel  # 72問のモデルクラスをインポート
    model = BagOfWordsModel(vocab_size=100000, embedding_dim=300).to("cuda")
    model.load_state_dict(torch.load("bow_model.pt"))  # 学習済みパラメータ読み込み
    
    dev_loader = DummyLoader()
    evaluate_model(model, dev_loader, "cuda")