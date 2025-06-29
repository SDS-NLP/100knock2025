import pandas as pd

train = pd.read_csv('SST-2/train.tsv', sep='\t')
dev = pd.read_csv('SST-2/dev.tsv', sep='\t')

def text_to_feature(text):
    tokens = text.split()
    feature = {}
    for token in tokens:
        feature[token] = feature.get(token, 0) + 1
    return feature

def convert_to_dict(data):
    result = []
    for _, row in data.iterrows():
        text = row['sentence']
        label = row['label']
        feature = text_to_feature(text)
        result.append({'text': text, 'label': label, 'feature': feature})
    return result

train_data = convert_to_dict(train)
dev_data = convert_to_dict(dev)

if __name__ == "__main__":
    # 出力の確認
    print(train_data[0])