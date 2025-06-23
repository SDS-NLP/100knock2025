import pandas as pd

# データセットの読み込み
df_train = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter07/SST-2/train.tsv', sep='\t')
df_dev = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter07/SST-2/dev.tsv', sep='\t')

train_list = []
for i in range(len(df_train)):
    train_data = {}
    train_data['text'] = df_train['sentence'][i]
    train_data['label'] = df_train['label'][i]
    BoW = {}
    for word in train_data['text'].split():
        BoW[word] = BoW.get(word, 0) + 1
    train_data['feature'] = BoW
    train_list.append(train_data)

print(train_list[0])

dev_list = []
for i in range(len(df_dev)):
    dev_data = {}
    dev_data['text'] = df_dev['sentence'][i]
    dev_data['label'] = df_dev['label'][i]
    BoW = {}
    for word in dev_data['text'].split():
        BoW[word] = BoW.get(word, 0) + 1
    dev_data['feature'] = BoW
    dev_list.append(dev_data)