import pandas as pd

# データセットの読み込み
df_train = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter07/SST-2/train.tsv', sep='\t')
df_dev = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter07/SST-2/dev.tsv', sep='\t')

# labelの0,1の個数をカウント
print('---trainデータのlabelの0,1の個数---')
print(df_train['label'].value_counts())

print('---devデータのlabelの0,1の個数---')
print(df_dev['label'].value_counts())
