import torch
from datasets import load_dataset
import gensim.downloader as api

# 1. 単語埋め込みの読み込み（例：GloVe 100次元）
embedding_model = api.load("glove-wiki-gigaword-100")

# 辞書構築（0は<PAD>用に予約）
word2idx = {"<PAD>": 0}
for i, word in enumerate(embedding_model.key_to_index, start=1):
    word2idx[word] = i

# 2. SST-2の訓練・検証データの読み込み
dataset = load_dataset("glue", "sst2")
train_data_raw = dataset["train"]
dev_data_raw = dataset["validation"]

# 3. テキストをトークンID列に変換し、辞書形式で出力
def convert_example(example):
    text = example["sentence"]
    label = float(example["label"])
    tokens = text.lower().split()
    input_ids = [word2idx[word] for word in tokens if word in word2idx]
    
    # 全トークンが語彙外の場合、Noneを返す（後で除去）
    if len(input_ids) == 0:
        return None
    
    return {
        "text": text,
        "label": torch.tensor([label], dtype=torch.float32),
        "input_ids": torch.tensor(input_ids, dtype=torch.long)
    }

# 4. 無効な例（None）を除去
train_data = list(filter(None, map(convert_example, train_data_raw)))
dev_data = list(filter(None, map(convert_example, dev_data_raw)))

print(f"Train examples: {len(train_data)}, Dev examples: {len(dev_data)}")
print(train_data[0])
