"""
knock54:アナロジーデータでの実験
単語アナロジーの評価データをダウンロードし、国と首都に関する事例（: capital-common-countriesセクション）
に対して、vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し、
そのベクトルと類似度が最も高い単語と、その類似度を求めよ。
求めた単語と類似度は、各事例と一緒に記録せよ
"""
from gensim.models import KeyedVectors
from tqdm import tqdm
import pandas as pd

# モデルとデータの読み込み
questions_path = "mao/chapter06/questions-words.txt"
model_path = "mao/chapter06/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

results = []
section_list = []

# tqdm で全行に進捗バーを表示
with open(questions_path, encoding="utf-8") as f:
    lines = f.readlines()

section = None
for line in tqdm(lines, desc="Processing analogies"):
    line = line.strip()

    if not line:
        continue  # 空行をスキップ

    if line.startswith(":"):
        section = line[2:].strip()
        continue

    parts = line.split()
    if len(parts) != 4:
        continue  # 異常行をスキップ

    A, B, C, D = parts
    section_list.append(section)

    # アナロジー推論（全セクション対象）
    if all(w in model for w in [A, B, C]):
        try:
            predicted_word, similarity = model.most_similar(
                positive=[B, C], negative=[A], topn=1)[0]
        except KeyError:
            predicted_word, similarity = "N/A", 0.0
    else:
        predicted_word, similarity = "N/A", 0.0

    results.append((A, B, C, D, predicted_word, similarity))

# 結果確認
for row in results[:5]:
    print("\t".join(map(str, row)))

# セクション一覧表示
ia = pd.Series(section_list).unique()
print(ia)

