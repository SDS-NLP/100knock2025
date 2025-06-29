import zipfile
import pandas as pd

zip_path = "/home/tanxin/100knock2025/xin/chapter07/SST-2.zip"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    print(zip_ref.namelist())

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    with zip_ref.open('SST-2/train.tsv') as train_file:
        train_data = pd.read_csv(train_file, sep='\t')
    with zip_ref.open('SST-2/dev.tsv') as dev_file:
        dev_data = pd.read_csv(dev_file, sep='\t')

# ポジティブ・ネガティブのカウント
train_counts = train_data["label"].value_counts()
dev_counts = dev_data["label"].value_counts()

print("Trainデータのカウント:")
print(train_counts)

print("\nDevデータのカウント:")
print(dev_counts)