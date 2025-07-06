# ファイル名: count_labels.py
# 保存場所: chapter07/count_labels.py
# 目的: SST-2フォルダ内のtrain.tsvとdev.tsvにある感情ラベル（0:ネガティブ, 1:ポジティブ）の数をカウントする

import os               # ファイルやフォルダのパスを扱う標準ライブラリ
import csv              # TSV（タブ区切り）ファイルを読み込むためのライブラリ
from collections import Counter  # ラベルの数を簡単に数えるためのライブラリ

def count_labels(filepath):
    """
    指定されたTSVファイルを読み込み、ラベルの数をカウントする関数

    Parameters:
        filepath (str): ファイルのパス（例: SST-2/train.tsv）

    Returns:
        Counter: ラベルごとの出現回数を持つ辞書のようなオブジェクト
    """
    counts = Counter()  # ラベルの数を記録するCounterオブジェクト（自動的に数をカウントしてくれる）
    
    # ファイルをUTF-8で開いて読み込む
    with open(filepath, 'r', encoding='utf-8') as f:
        # タブ区切りで読み込む（TSVファイルのため）
        reader = csv.DictReader(f, delimiter='\t')
        
        # 1行ずつ処理
        for row in reader:
            label = row['label']  # "label"列の値（0 または 1）を取り出す
            counts[label] += 1    # そのラベルのカウントを1つ増やす

    return counts


def main():
    """
    メインの処理を行う関数。
    SST-2フォルダ内のtrain.tsvとdev.tsvを読み込み、ラベルごとの件数を表示する。
    """
    # このスクリプトファイル（count_labels.py）があるディレクトリを基準にして、
    # SST-2フォルダへのパスを作成
    base_dir = os.path.join(os.path.dirname(__file__), 'SST-2')

    # 処理したいファイル名をリストで指定
    files = ['train.tsv', 'dev.tsv']

    # それぞれのファイルについてラベルをカウントし、結果を表示
    for filename in files:
        path = os.path.join(base_dir, filename)   # SST-2フォルダ内のファイルへの完全なパスを作成
        label_counts = count_labels(path)         # ラベルをカウントする関数を呼び出す
        
        # 結果を表示（ネガティブ: 0, ポジティブ: 1）
        print(f'--- {filename} ---')
        print(f"Negative (0): {label_counts.get('0', 0)} 件")
        print(f"Positive (1): {label_counts.get('1', 0)} 件")
        print()


# Pythonスクリプトとして実行された場合のみ、main()を実行する
# 他のスクリプトから読み込まれた場合は実行されない
if __name__ == '__main__':
    main()
