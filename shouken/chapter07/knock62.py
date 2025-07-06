from knock61 import train_data, dev_data
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# 特徴ベクトルとラベルを抽出
X_train_dict = [d['feature'] for d in train_data]
y_train = [int(d['label']) for d in train_data]

X_dev_dict = [d['feature'] for d in dev_data]
y_dev = [int(d['label']) for d in dev_data]

# パイプライン（ベクトル化 → ロジスティック回帰）
model = Pipeline([
    ('vectorizer', DictVectorizer()),
    ('classifier', LogisticRegression(max_iter=1000))
])

# 学習
model.fit(X_train_dict, y_train)

# 精度評価
y_pred = model.predict(X_dev_dict)
accuracy = accuracy_score(y_dev, y_pred)

print(f"検証データの正解率: {accuracy:.4f}")
