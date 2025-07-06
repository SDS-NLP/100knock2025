import pandas as pd
from scipy.stats import spearmanr
from gensim.models import KeyedVectors

# WordSimilarity-353のCSVを読み込み
df = pd.read_csv("wordsim353/combined.csv")
df.columns = ['word1', 'word2', 'human_similarity']

# Word2Vecモデルの読み込み
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

# 類似度の計算とフィルタリング
results = []
for idx, row in df.iterrows():
    w1, w2, human_score = row['word1'], row['word2'], row['human_similarity']
    if w1 in model and w2 in model:
        vector_score = model.similarity(w1, w2)
        results.append((w1, w2, human_score, vector_score))

# 結果をDataFrameにまとめる
results_df = pd.DataFrame(results, columns=["word1", "word2", "human_similarity", "vector_similarity"])

# ランキングを計算（降順で順位付け）
results_df["human_rank"] = results_df["human_similarity"].rank(ascending=False)
results_df["vector_rank"] = results_df["vector_similarity"].rank(ascending=False)

# スピアマン相関係数の計算
rho, pval = spearmanr(results_df["human_rank"], results_df["vector_rank"])

# ランキング付きの結果を表示
pd.set_option('display.max_rows', None)  # 全行表示（必要に応じて）
print(results_df.sort_values("human_rank")[["word1", "word2", "human_similarity", "human_rank", "vector_similarity", "vector_rank"]])

print(f"\nスピアマン相関係数: {rho:.4f}（p値: {pval:.4g}）")
