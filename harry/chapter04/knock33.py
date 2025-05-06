import CaboCha
import os
import csv

# CaboChaパーサ初期化
cabocha = CaboCha.Parser()

# ファイルパス設定
base_dir = os.path.expanduser("~/100knock/100knock2025/harry/chapter04")
input_file = os.path.join(base_dir, "kokoro_cleaned.txt")
output_file = os.path.join(base_dir, "kokoro_kakari.csv")

# 結果格納用リスト
pairs = []

# 1行ずつ係り受け解析
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        tree = cabocha.parse(line)
        chunks = {}

        for i in range(tree.chunk_size()):
            chunk = tree.chunk(i)
            tokens = []
            for j in range(chunk.token_pos, chunk.token_pos + chunk.token_size):
                token = tree.token(j)
                tokens.append(token.surface)
            chunks[i] = {
                "text": "".join(tokens),
                "link": chunk.link
            }

        for i, chunk in chunks.items():
            dst = chunk["link"]
            if dst != -1:
                src_text = chunk["text"]
                dst_text = chunks[dst]["text"]
                pairs.append([src_text, dst_text])

# CSVファイルに保存
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["係り元", "係り先"])
    writer.writerows(pairs)

print(f"✅ 解析結果を {output_file} に保存しました。")

# import spacy
# import os

# ファイルの読み込み
# base_dir = os.path.expanduser("~/100knock/100knock2025/harry/chapter04")
# text_file = os.path.join(base_dir, "kokoro_short.txt")

# with open(text_file, "r", encoding="utf-8") as f:
#    text = f.read()

# GiNZAの日本語モデルを読み込み
# nlp = spacy.load("ja_ginza")

# 係り受け解析の実行
# doc = nlp(text)

# 結果を表示（係り元\t係り先）
# print("🔗 係り受けペア（表層形ベース）:")
# for sent in doc.sents:
#    for token in sent:
#        if token.i == token.head.i:
#            continue  # ROOTはスキップ
#        print(f"{token.text}\t{token.head.text}")
