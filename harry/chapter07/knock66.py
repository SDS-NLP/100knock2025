# 66. 混同行列の作成
# 学習したロジスティック回帰モデルの検証データにおける混同行列（confusion matrix）を求めよ。

# ファイル名: knock66.py
# 目的: 検証データに対する混同行列を表示する

import os
import pickle
from sklearn.metrics import confusion_matrix, classification_report

def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def extract_features_and_labels(data):
    X = [ex['feature'] for ex in data]
    y = [int(ex['label']) for ex in data]
    return X, y

def main():
    # パス設定
    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, 'output')

    # モデル・ベクトライザー・検証データ読み込み
    model = load_pickle(os.path.join(output_dir, 'logreg_model.pkl'))
    vectorizer = load_pickle(os.path.join(output_dir, 'vectorizer.pkl'))
    dev_data = load_pickle(os.path.join(output_dir, 'dev_bow.pkl'))

    # 特徴とラベルの抽出
    X_dev_dicts, y_true = extract_features_and_labels(dev_data)
    X_dev = vectorizer.transform(X_dev_dicts)

    # 予測
    y_pred = model.predict(X_dev)

    # 混同行列の表示
    print("🔍 混同行列:")
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    print("行：実際のラベル / 列：予測ラベル")
    print(cm)

    # 精度・再現率・F1などもあわせて表示（任意）
    print("\n📊 分類レポート:")
    print(classification_report(y_true, y_pred, target_names=["ネガティブ", "ポジティブ"]))

if __name__ == '__main__':
    main()
