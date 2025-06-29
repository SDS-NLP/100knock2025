from knock70 import token2id
import pandas as pd
import torch

df1 = pd.read_csv("../../../SST-2/train.tsv", sep="\t")
df2 = pd.read_csv("../../../SST-2/dev.tsv", sep="\t")

def convert_token_into_id(text, token2id):
    tokens = text.strip().split()
    input_ids = [token2id[token] for token in tokens if token in token2id]
    return input_ids if input_ids else None  # 空のときはNoneで除外対象に

def make_dict(df, token2id):
  processed_train = []
  for _, row in df.iterrows():
    text = row['sentence']
    label = float(row['label'])
    input_ids = convert_token_into_id(text, token2id)
    if input_ids is None:
        continue
    processed_train.append({
        'text': text,
        'label': torch.tensor([label], dtype=torch.float32),
        'input_ids': torch.tensor(input_ids, dtype=torch.long)
    })
  return processed_train

df1_data = make_dict(df1, token2id)
df2_data = make_dict(df2, token2id)

if __name__ == "__main__":
    print(df1_data[:5])
    print(df2_data[:5])