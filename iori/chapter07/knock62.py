from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from knock61 import train_data, dev_data 

# 特徴量のベクトル化
vectorizer = DictVectorizer(sparse=False)
X_train = vectorizer.fit_transform([data['feature'] for data in train_data])
X_dev = vectorizer.transform([data['feature'] for data in dev_data])

# ラベルの抽出
y_train = [data['label'] for data in train_data]
y_dev = [data['label'] for data in dev_data]

# ロジスティック回帰モデルの学習
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


