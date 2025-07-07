# word2id を定義
from gensim.models import KeyedVectors

model_path = "/Users/aa/Downloads/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

word2id = {"<PAD>": 0}
for i, word in enumerate(model.key_to_index, start=1):
    word2id[word] = i


import torch

def load_sst_data(tsv_path, word2id):
    dataset = []
    with open(tsv_path, encoding="utf-8") as f:
        next(f)  # ヘッダーをスキップ
        for line in f:
            try:
                text, label = line.strip().split("\t")
                tokens = text.split()  # 単語分割（空白区切り）
                input_ids = [word2id[token] for token in tokens if token in word2id]
                if not input_ids:
                    continue  # 空のトークン列は除外
                ex = {
                    "text": text,
                    "label": torch.tensor([float(label)]),
                    "input_ids": torch.tensor(input_ids)
                }
                dataset.append(ex)
            except ValueError:
                continue  # 不正な行があればスキップ
    return dataset


# 実行例
train_data = load_sst_data("SST-2/train.tsv", word2id)
dev_data = load_sst_data("SST-2/dev.tsv", word2id)

print(f"train: {len(train_data)}")
print(f"dev: {len(dev_data)}")
print(train_data[0])

#出力
"""
train: 66650
dev: 872
{'text': 'hide new secretions from the parental units ', 'label': tensor([0.]), 'input_ids': tensor([  5785,     66, 113845,     18,     12,  15095,   1594])}
"""