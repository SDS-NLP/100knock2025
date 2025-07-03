#71. データセットの読み込み
import csv
import torch
from knock70 import word2id

def load_sst_dataset(file_path, word2id):
    dataset = []

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)  # ヘッダーをスキップ

        for line in reader:
            if len(line) != 2:
                continue  # 空行・不正行スキップ

            text, label_str = line
            tokens = text.strip().split()
            
            # 単語埋め込み語彙に含まれる単語だけで input_ids を作成
            input_ids = [word2id[word] for word in tokens if word in word2id]

            if len(input_ids) == 0:
                continue  # 空なら除外

            label = torch.tensor([float(label_str)], dtype=torch.float32) #テンソル＝多次元の数値配列（スカラー、ベクトル、行列の総称）　ニューラルネットワークの入出力はすべてテンソルなので、変換する

            dataset.append({
                'text': text,
                'label': label,
                'input_ids': torch.tensor(input_ids, dtype=torch.long)
            })

    print(f"読み込み済み: {file_path}, 有効な事例数: {len(dataset)}")
    return dataset

train_dataset = load_sst_dataset("chapter07/SST-2/train.tsv", word2id)
dev_dataset = load_sst_dataset("chapter07/SST-2/dev.tsv", word2id)

# 1件確認
if __name__ == "__main__":
    print(train_dataset[0])
