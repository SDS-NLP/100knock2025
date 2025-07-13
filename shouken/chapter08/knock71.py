import pandas as pd
import torch
from knock70 import word_to_id

# ファイルパス
train_file = "train.tsv"
dev_file = "dev.tsv"

# テキストをID列に変換する関数
def text_to_id_sequence(text, word_to_id):
    tokens = text.split()  # スペース区切りでBoW的にトークン化
    ids = [word_to_id[token] for token in tokens if token in word_to_id]
    return ids

# データ読み込みと前処理
def process_sst_dataset(file_path):
    df = pd.read_csv(file_path, sep='\t')
    examples = []
    for _, row in df.iterrows():
        text = row['sentence']
        label = float(row['label'])  # 0 or 1
        input_ids = text_to_id_sequence(text, word_to_id)
        if len(input_ids) == 0:
            continue  # 単語埋め込みに1語も含まれていない → スキップ
        example = {
            'text': text,
            'label': torch.tensor([label], dtype=torch.float32),
            'input_ids': torch.tensor(input_ids, dtype=torch.long)
        }
        examples.append(example)
    return examples

# 実行
train_dataset = process_sst_dataset(train_file)
dev_dataset = process_sst_dataset(dev_file)

# 確認表示（先頭3件）
for ex in train_dataset[:3]:
    print(ex)