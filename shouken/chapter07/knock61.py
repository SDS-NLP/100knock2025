import pandas as pd
from collections import Counter

# ファイルパスの指定
train_file = "train.tsv"
dev_file = "dev.tsv"

# データの読み込み
train_df = pd.read_csv(train_file, sep='\t')
dev_df = pd.read_csv(dev_file, sep='\t')

# BoW変換関数
def convert_to_bow_dict(df):
    result = []
    for _, row in df.iterrows():
        text = row['sentence']
        label = str(row['label'])  # ラベルを文字列として扱う
        tokens = text.split()  # スペースで分割（単純なBoW）
        bow = dict(Counter(tokens))
        result.append({
            'text': text,
            'label': label,
            'feature': bow
        })
    return result

# 各データの変換
train_data = convert_to_bow_dict(train_df)
dev_data = convert_to_bow_dict(dev_df)

# 学習データの最初の1件を目視確認
from pprint import pprint
pprint(train_data[0])
