import pandas as pd
from knock62 import model, vectorizer
from sklearn.metrics import confusion_matrix
from collections import Counter
import re

# テストデータの読み込み
dev = pd.read_csv('SST-2/dev.tsv', sep='\t')

# 特徴量の辞書化
def text_to_feature(text):
    tokens = re.findall(r'\w+|[^\w\s]', text)
    return dict(Counter(tokens))

X_dev = vectorizer.transform([text_to_feature(text) for text in dev['sentence']])
y_dev = dev['label']

# モデルの予測
y_pred = model.predict(X_dev)

# 混同行列の計算
conf_matrix = confusion_matrix(y_dev, y_pred)

print("Confusion Matrix:")
print(conf_matrix)