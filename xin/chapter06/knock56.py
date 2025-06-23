import gensim.downloader as api
import urllib.request
import csv
from scipy.stats import spearmanr
import numpy as np

# --- モデルロード ---
print("Loading embedding model...")
model = api.load("glove-wiki-gigaword-100")
print("Model loaded.")

# --- WordSimilarity-353 データセットのダウンロード ---
url = "https://raw.githubusercontent.com/mfaruqui/eval-word-vectors/master/data/wordsim353/combined.tab"
local_file = "wordsim353_combined.tab"
urllib.request.urlretrieve(url, local_file)
print("Downloaded WordSimilarity-353 dataset.")

# --- データ読み込み ---
human_scores = []
model_scores = []
skipped_pairs = 0

with open(local_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")
    next(reader)  # ヘッダーをスキップ

    for row in reader:
        word1, word2, human_score = row[0].lower(), row[1].lower(), float(row[2])

        if word1 in model and word2 in model:
            vec1, vec2 = model[word1], model[word2]
            similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
            human_scores.append(human_score)
            model_scores.append(similarity)
        else:
            skipped_pairs += 1

# --- スピアマン相関計算 ---
rho, p = spearmanr(human_scores, model_scores)

# --- 結果出力 ---
print(f"\n使用ペア数: {len(human_scores)}")
print(f"スキップされたペア数（語彙になかった）: {skipped_pairs}")
print(f"スピアマン相関係数 (ρ): {rho:.4f}")
print(f"p値: {p:.4g}")