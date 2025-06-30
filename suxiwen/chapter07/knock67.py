from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from knock63 import train_dicts, train_labels, dev_dicts, dev_labels

vectorizer = DictVectorizer()
X_train = vectorizer.fit_transform(train_dicts)
X_dev = vectorizer.transform(dev_dicts)
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, train_labels)

def evaluate_model(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, pos_label='0')
    rec = recall_score(y_true, y_pred, pos_label='0')
    f1 = f1_score(y_true, y_pred, pos_label='0')
    print(f"Accuracy     : {acc:.4f}")
    print(f"Precision    : {prec:.4f}")
    print(f"Recall       : {rec:.4f}")
    print(f"F1 Score     : {f1:.4f}")

dev_pred = clf.predict(X_dev)
train_pred = clf.predict(X_train)
evaluate_model(train_labels, train_pred)
dev_pred = clf.predict(X_dev)
print("検証データの評価指標：")
evaluate_model(dev_labels, dev_pred)