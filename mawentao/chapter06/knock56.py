#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv # CSVファイルを読み込むために使う
from scipy.stats import spearmanr # スピアマンの順位相関係数を計算するために使う
from gensim.models import KeyedVectors #

# モデルのパスを指定
model_path = "/Users/niaomuqing/100knock2025/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True) #ファイルがバイナリ形式（.bin）、テキスト形式（.txt）ではない。Flaseは.txt
print("Model loaded.") 

# データのパスを指定
ws353_path = "/Users/niaomuqing/100knock2025/wordsim353/combined.csv"

# リストの初期化
human_scores = []
model_scores = []
oov_count = 0

# CSVファイルを読み込み、単語間の類似度を計算する
with open(ws353_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # 1行目（列名）を読み飛ばす。
    for word1, word2, score in reader: # 各行に対して、word1, word2, score を読み込む
        word1, word2 = word1.lower(), word2.lower() # 単語をすべて小文字に変換（モデルの語彙が小文字で格納されているため）
        if word1 in model and word2 in model: 
            sim = model.similarity(word1, word2) # 2語がどちらもモデルの語彙にあるかどうかを確認
            human_scores.append(float(score)) # 元々はstrですので
            model_scores.append(sim)
        else:
            oov_count += 1

# スピアマン相関係数の計算
result, _ = spearmanr(human_scores, model_scores) 
print(f"\nSpearman's rank correlation: {result}")
print(f"OOV (out-of-vocabulary) pairs skipped: {oov_count}")

