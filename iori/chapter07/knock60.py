import pandas as pd

train = pd.read_csv('SST-2/train.tsv', sep='\t')
dev = pd.read_csv('SST-2/dev.tsv', sep='\t')

# 正しい列名を使用
print(train['label'].value_counts()) 
print(dev['label'].value_counts())   