# ファイル名: bow_vectorizer.py
# 保存場所: chapter07/bow_vectorizer.py
# 目的: SST-2データをBoW特徴ベクトルに変換し、辞書形式で保存する

import os
import csv
import pickle       # データ保存・読み込みに使用
from collections import Counter


def load_and_vectorize(filepath):
    """
    指定されたTSVファイルからデータを読み込み、
    各文をBag of Words（BoW）特徴ベクトルに変換する

    Parameters:
        filepath (str): データファイルへのパス（例: SST-2/train.tsv）

    Returns:
        list: 各行を辞書形式にしたデータのリスト
              例: {'text': ..., 'label': ..., 'feature': {...}}
    """
    examples = []

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')

        for row in reader:
            text = row['sentence']
            label = row['label']
            tokens = text.split()
            bow = Counter(tokens)

            example = {
                'text': text,
                'label': label,
                'feature': dict(bow)
            }

            examples.append(example)

    return examples


def save_as_pickle(data, filepath):
    """
    データをpickle形式で保存する

    Parameters:
        data (object): 保存したいPythonオブジェクト（listやdictなど）
        filepath (str): 保存先ファイルのパス（.pkl）
    """
    with open(filepath, 'wb') as f:
        pickle.dump(data, f)
    print(f"✅ 保存完了: {filepath}")


def main():
    # ベースパスとファイルパスの準備
    base_dir = os.path.dirname(__file__)
    sst_dir = os.path.join(base_dir, 'SST-2')
    output_dir = os.path.join(base_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)  # 出力用ディレクトリがなければ作成

    train_file = os.path.join(sst_dir, 'train.tsv')
    dev_file = os.path.join(sst_dir, 'dev.tsv')

    # 特徴ベクトルの構築
    train_data = load_and_vectorize(train_file)
    dev_data = load_and_vectorize(dev_file)

    # pickle形式で保存（再利用用）
    save_as_pickle(train_data, os.path.join(output_dir, 'train_bow.pkl'))
    save_as_pickle(dev_data, os.path.join(output_dir, 'dev_bow.pkl'))

    # 学習データの最初の事例を確認
    print('\n🔍 学習データの最初の事例:')
    first = train_data[0]
    print(f"Text   : {first['text']}")
    print(f"Label  : {first['label']}")
    print(f"Feature: {first['feature']}")


if __name__ == '__main__':
    main()
