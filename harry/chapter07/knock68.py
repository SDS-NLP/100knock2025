# 68. 特徴量の重みの確認
# 学習したロジスティック回帰モデルの中で、重みの高い特徴量トップ20と、重みの低い特徴量トップ20を確認せよ。

# ファイル名: knock68.py
# 目的: ロジスティック回帰モデルの特徴量の重みを確認（上位・下位20語）

import os
import pickle
import numpy as np

def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def main():
    # パス設定
    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, 'output')

    # モデル・ベクトライザーの読み込み
    model = load_pickle(os.path.join(output_dir, 'logreg_model.pkl'))
    vectorizer = load_pickle(os.path.join(output_dir, 'vectorizer.pkl'))

    # 特徴名と係数の取得
    feature_names = vectorizer.get_feature_names_out()  # 単語のリスト（str）
    weights = model.coef_[0]  # 各特徴語に対応する重み（float）

    # 重みの高い順・低い順にインデックスを取得
    top20_idx = np.argsort(weights)[-20:][::-1]  # 高い → 低い（降順）
    bottom20_idx = np.argsort(weights)[:20]      # 低い → 高い（昇順）

    # 結果表示
    print("🔥 ポジティブに寄与する特徴量トップ20:")
    for i in top20_idx:
        print(f"{feature_names[i]:<15} : {weights[i]:.4f}")

    print("\n❄️ ネガティブに寄与する特徴量トップ20:")
    for i in bottom20_idx:
        print(f"{feature_names[i]:<15} : {weights[i]:.4f}")

if __name__ == '__main__':
    main()
