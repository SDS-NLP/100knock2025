from knock61 import train_data, dev_data
from knock62 import model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# データ準備関数
def extract_X_y(data):
    X = [d['feature'] for d in data]
    y = [int(d['label']) for d in data]
    return X, y

# データ抽出
X_train, y_train = extract_X_y(train_data)
X_dev, y_dev = extract_X_y(dev_data)

# 予測
y_pred_train = model.predict(X_train)
y_pred_dev = model.predict(X_dev)

# 評価指標出力関数
def print_metrics(y_true, y_pred, name="データ"):
    print(f"\n{name} の評価:")
    print(f"  正解率 (Accuracy):     {accuracy_score(y_true, y_pred):.4f}")
    print(f"  適合率 (Precision):    {precision_score(y_true, y_pred):.4f}")
    print(f"  再現率 (Recall):       {recall_score(y_true, y_pred):.4f}")
    print(f"  F1スコア (F1-score):   {f1_score(y_true, y_pred):.4f}")

# 結果表示
print_metrics(y_train, y_pred_train, name="学習データ")
print_metrics(y_dev, y_pred_dev, name="検証データ")
