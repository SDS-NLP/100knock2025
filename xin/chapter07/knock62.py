from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from knock61 import bow_train_data, bow_dev_data
# 特徴とラベルを抽出
train_dicts = [d['feature'] for d in bow_train_data]
train_labels = [d['label'] for d in bow_train_data]
dev_dicts = [d['feature'] for d in bow_dev_data]
dev_labels = [d['label'] for d in bow_dev_data]

# ベクトル化
vectorizer = DictVectorizer()
X_train = vectorizer.fit_transform(train_dicts)
X_dev = vectorizer.transform(dev_dicts)

# ロジスティック回帰の学習
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, train_labels)