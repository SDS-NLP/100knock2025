import pandas as pd

# ファイルパスの設定
train_path = "SST-2/train.tsv"
dev_path = "SST-2/dev.tsv"

# データの読み込み
train_df = pd.read_csv(train_path, sep="\t")
dev_df = pd.read_csv(dev_path, sep="\t") #sep="\t" はタブ区切りのデータを読み込むことを指定している

# ラベルのカウント
train_counts = train_df['label'].value_counts() #DataFrame内の列 label にある各ラベル（感情）の頻度（件数）を数えるために、value_counts() メソッドを使っている
dev_counts = dev_df['label'].value_counts()

print("Trainデータのラベル分布:")
print(train_counts)

print("\nDevデータのラベル分布:")
print(dev_counts)
