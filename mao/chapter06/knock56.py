"""
knock56:WordSimilarity-353での評価
The WordSimilarity-353 Test Collectionの評価データをダウンロードし、
単語ベクトルにより計算される類似度のランキングと、
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ。
"""
import pandas as pd
from gensim.models import KeyedVectors
from scipy.stats import spearmanr

# ダウンロードした combined.csv のパスを指定
ws353_path = 'mao/chapter06/wordsim353/combined.csv'
df = pd.read_csv(ws353_path)

# ------------------------------
# 2. Word2Vec モデルのロード
# ------------------------------
# GoogleNews-vectors-negative300.bin.gz をダウンロードして以下にパスを指定
model_path = 'mao/chapter06/GoogleNews-vectors-negative300.bin'
print("Loading Word2Vec model... (this may take a few minutes)")
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("Model loaded.")

# ------------------------------
# 3. 類似度の計算
# ------------------------------
human_scores = []
model_scores = []

for word1, word2, human_score in zip(df['Word 1'], df['Word 2'], df['Human (mean)']):
    # 両単語が語彙に存在するかチェック
    if word1 in model and word2 in model:
        sim = model.similarity(word1, word2)
        model_scores.append(sim)
        human_scores.append(human_score)
    else:
        # 単語がモデルに含まれていない場合はスキップ
        continue

# ------------------------------
# 4. スピアマン相関係数の計算
# ------------------------------
correlation, p_value = spearmanr(human_scores, model_scores)

print(f"\nスピアマン相関係数: {correlation:.4f}")
print(f"p値: {p_value:.4e}")
