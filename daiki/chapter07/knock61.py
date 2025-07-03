import pandas as pd
from collections import Counter
from pathlib import Path
import json

# BoW にする 単語が文章内に何回現れたか
def text_to_bow(sentence: str) -> dict[str, int]:
    # スペース区切りでトークン化し Bag-of-Words へ変換
    tokens = sentence.strip().split()
    return dict(Counter(tokens))

def convert_df(df: pd.DataFrame) -> list[dict]:
    # DataFrame(sentence, label) → BoW 付き辞書リスト
    return [
        {
            "text": sent,
            "label": str(label),
            "feature": text_to_bow(sent),
        }
        for sent, label in zip(df["sentence"], df["label"])
    ]

# ファイルパス 
train_path = Path("SST-2/train.tsv")
dev_path   = Path("SST-2/dev.tsv")

# 読み込み & 変換 
for name, path in [("train", train_path), ("dev", dev_path)]:
    if not path.exists():
        raise FileNotFoundError(f"{path} が見つかりません。実行位置またはパスを確認してください。")

train_df = pd.read_csv(train_path, sep="\t")
dev_df   = pd.read_csv(dev_path,   sep="\t")

train_examples = convert_df(train_df)
dev_examples   = convert_df(dev_df)

# 結果の概要 
print(f"train  : {len(train_examples):,} 件")
print(f"dev    : {len(dev_examples):,} 件\n")

# 目視チェック用
print("最初の学習事例")
print(json.dumps(train_examples[0], ensure_ascii=False, indent=2)) 
# json.dumpsはPythonの辞書やリストなどのデータを JSON形式（整った見た目） の文字列に変換する関数
# インデント（字下げ）をして、見やすい形に整形