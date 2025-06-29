#67. 精度の計測
from knock61 import dev_data, train_data
from knock62 import clf, vectorizer, label_encoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_model(X, y_true, dataset_name=""):
    y_pred = clf.predict(X)
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average='binary')
    rec = recall_score(y_true, y_pred, average='binary')
    f1 = f1_score(y_true, y_pred, average='binary')

    print(f"{dataset_name}の評価結果：")
    print(f"正解率(Accuracy)：{acc:.4f}")
    print(f"適合率(Precision)：{prec:.4f}")
    print(f"再現率(Recall)：{rec:.4f}")
    print(f"F1スコア: {f1:.4f}")

    return 

# 学習データ
train_features = [ex['feature'] for ex in train_data]
train_labels = [ex['label'] for ex in train_data]
X_train = vectorizer.transform(train_features)
y_train = label_encoder.transform(train_labels)

evaluate_model(X_train, y_train, dataset_name="学習データ")

# 検証データ
dev_features = [ex['feature'] for ex in dev_data]
dev_labels = [ex['label'] for ex in dev_data]
X_dev = vectorizer.transform(dev_features)
y_dev = label_encoder.transform(dev_labels)

evaluate_model(X_dev, y_dev, dataset_name="検証データ")
