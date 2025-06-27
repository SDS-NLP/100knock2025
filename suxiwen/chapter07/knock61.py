import zipfile
from collections import Counter

def text_to_bow(text):
    tokens = text.strip().split()
    return dict(Counter(tokens))

def bow(zip_file, inner_path):
    data_points = []
    with zipfile.ZipFile(zip_file) as zf:
        with zf.open(inner_path) as f:
            for i, line in enumerate(f):
                if i == 0:
                    continue  # ヘッダー行スキップ
                fields = line.decode('utf-8').strip().split('\t')
                if len(fields) < 2:
                    continue
                label, text = fields[1], fields[0]
                feature = text_to_bow(text)
                data_points.append({
                    'text': text,
                    'label': label,
                    'feature': feature
                })
    return data_points
bow_train_data=bow("/home/suxiwen/100knock2025/suxiwen/chapter07/SST-2.zip", "SST-2/train.tsv")
bow_dev_data=bow("/home/suxiwen/100knock2025/suxiwen/chapter07/SST-2.zip", "SST-2/dev.tsv")
print(bow_train_data[0])
print(bow_dev_data[0])