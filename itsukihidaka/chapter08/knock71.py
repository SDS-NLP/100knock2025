from knock70 import E, word_to_index, index_to_word
import pandas as pd
import torch

# データセットの読み込み
df_train = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter07/SST-2/train.tsv', sep='\t')
df_dev = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter07/SST-2/dev.tsv', sep='\t')

# 学習データ
train_texts = df_train['sentence'].tolist()
train_labels = df_train['label'].tolist()

# 検証データ
dev_texts = df_dev['sentence'].tolist()
dev_labels = df_dev['label'].tolist()

def make_data(texts, labels):
    data = []
    for i, text in enumerate(texts):
        dic = {}
        dic['text'] = text
        dic['label'] = torch.tensor([labels[i]])
        input_ids_list = []
        for word in text.split():
            if word in word_to_index:
                input_ids_list.append(word_to_index[word])
        if input_ids_list:
            dic['input_ids'] = torch.tensor(input_ids_list)
        else:
            continue
        dic['input_ids'] = torch.tensor(input_ids_list)
        data.append(dic)
    return data

train_data = make_data(train_texts, train_labels)
dev_data = make_data(dev_texts, dev_labels)

print(train_data[0])
print(dev_data[0])
    






