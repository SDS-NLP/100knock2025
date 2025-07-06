from knock63 import X_train, X_dev, train_labels
from sklearn.linear_model import LogisticRegression
# devデータの先頭のBoW特徴ベクトルを取得
X_dev_first = X_dev[0:1]

# 条件付き確率を求める
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, train_labels)
prob = clf.predict_proba(X_dev_first)

# クラスの順番を取得（['neg', 'pos']など）
classes = clf.classes_

# 結果を表示
for label, p in zip(classes, prob[0]):
    print(f"ラベル: {label}, 条件付き確率: {p:.4f}")