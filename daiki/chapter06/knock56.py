import pandas as pd
from gensim.models import KeyedVectors
from scipy.stats import spearmanr

# 1. Word2Vec モデルの読み込み
model_path = '/Users/aa/GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 2. 評価データの読み込み（combined.csv）
csv_path = '/Users/aa/100knock2025/daiki/chapter06/wordsim353/combined.csv'
df = pd.read_csv(csv_path)

# 3. 類似度計算とフィルタリング
human_scores = []
word2vec_scores = []


for _, row in df.iterrows():
    w1, w2 = row['Word 1'], row['Word 2']
    human = row['Human (mean)']

    if w1 in model and w2 in model:
        sim = model.similarity(w1, w2)
        human_scores.append(human)
        word2vec_scores.append(sim)
    

# 4. スピアマン相関係数の計算
rho, _ = spearmanr(human_scores, word2vec_scores)
print(f"Spearman's rank correlation: {rho:.4f}")
print(f"使用された単語ペア数: {len(human_scores)}")

#出力結果
"""
Spearman's rank correlation: 0.7000
使用された単語ペア数: 353
"""
