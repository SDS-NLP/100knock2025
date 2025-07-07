import pandas as pd
from collections import Counter

# ファイルパスの指定
train_file = "train.tsv"
dev_file = "dev.tsv"

# データの読み込み（タブ区切り）
train_df = pd.read_csv(train_file, sep='\t')
dev_df = pd.read_csv(dev_file, sep='\t')

# ラベルのカウント関数
def count_labels(df, name=""):
    label_counts = Counter(df['label'])
    print(f"{name} データ")
    print(f"  ポジティブ (1): {label_counts.get(1, 0)} 件")
    print(f"  ネガティブ (0): {label_counts.get(0, 0)} 件\n")

# 結果の表示
count_labels(train_df, "学習")
count_labels(dev_df, "検証")

