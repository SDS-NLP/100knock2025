# 63. 予測
# 学習したロジスティック回帰モデルを用い、検証データの先頭の事例のラベル（ポジネガ）を予測せよ。また、予測されたラベルが検証データで付与されていたラベルと一致しているか、確認せよ。
# 目的: 検証データの先頭5件をロジスティック回帰モデルで予測し、正解と比較

import os
import pickle

def load_pickle(filepath):
    """
    pickleファイルを読み込むユーティリティ関数
    """
    with open(filepath, 'rb') as f:
        return pickle.load(f)

def main():
    # パスの設定
    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, 'output')

    # モデル・ベクトライザー・検証データを読み込み
    model = load_pickle(os.path.join(output_dir, 'logreg_model.pkl'))
    vectorizer = load_pickle(os.path.join(output_dir, 'vectorizer.pkl'))
    dev_data = load_pickle(os.path.join(output_dir, 'dev_bow.pkl'))

    # 先頭5件を取り出す（最大でもlen(dev_data)件に制限）
    top5_data = dev_data[:5]

    for i, example in enumerate(top5_data):
        text = example['text']
        true_label = int(example['label'])
        feature_dict = example['feature']

        # BoW特徴ベクトルに変換（1件だけでもリストで包む必要あり）
        X = vectorizer.transform([feature_dict])
        pred_label = model.predict(X)[0]

        # 結果を表示
        print(f"\n📝 事例 {i+1}")
        print("Text   :", text)
        print("予測ラベル :", pred_label)
        print("正解ラベル :", true_label)
        if pred_label == true_label:
            print("🎯 一致しました（正解）")
        else:
            print("❌ 不一致でした（不正解）")

if __name__ == '__main__':
    main()
