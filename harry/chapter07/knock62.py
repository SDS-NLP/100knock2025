# 62. 学習
# 61で構築した学習データの特徴ベクトルを用いて、ロジスティック回帰モデルを学習せよ。
# 目的: BoW特徴ベクトルを使ってロジスティック回帰モデルを訓練する

import os
import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_data(pkl_path):
    """
    pickleファイルからデータを読み込む
    """
    with open(pkl_path, 'rb') as f:
        return pickle.load(f)

def extract_features_and_labels(data):
    """
    BoW特徴とラベルをリストに分けて取り出す

    Returns:
        X: list of feature dicts
        y: list of labels (int)
    """
    X = [ex['feature'] for ex in data]
    y = [int(ex['label']) for ex in data]
    return X, y

def main():
    # ファイルのパスを指定
    base_dir = os.path.dirname(__file__)
    input_dir = os.path.join(base_dir, 'output')
    train_path = os.path.join(input_dir, 'train_bow.pkl')

    # データを読み込む
    train_data = load_data(train_path)

    # 特徴とラベルを抽出
    X_train_dicts, y_train = extract_features_and_labels(train_data)

    # Dict形式 → 数値ベクトルに変換（ベクトル化）
    vectorizer = DictVectorizer(sparse=True)  # sparse=FalseにするとNumPyの配列になる
    # これは DictVectorizer のデフォルト設定でもあり、不要なゼロをメモリに展開しない「疎行列（sparse matrix）」形式で保持するので、メモリ使用量が大幅に削減されます。
    X_train = vectorizer.fit_transform(X_train_dicts)

    # ロジスティック回帰モデルを学習
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # 訓練データで予測＆評価
    y_pred = model.predict(X_train)
    acc = accuracy_score(y_train, y_pred)

    print(f'✅ ロジスティック回帰モデルを訓練しました')
    print(f'🎯 訓練データの正解率: {acc:.4f}')

    # モデルとベクトライザーも保存しておく（後の予測や検証に使える）
    with open(os.path.join(input_dir, 'logreg_model.pkl'), 'wb') as f:
        pickle.dump(model, f)
    with open(os.path.join(input_dir, 'vectorizer.pkl'), 'wb') as f:
        pickle.dump(vectorizer, f)
    print('📦 モデルとベクトライザーを保存しました')

if __name__ == '__main__':
    main()
