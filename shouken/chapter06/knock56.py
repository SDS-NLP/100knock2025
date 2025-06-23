import pandas as pd
from gensim.models import KeyedVectors
from scipy.stats import spearmanr

# === 1. Word2Vecモデルの読み込み ===
model_path = "GoogleNews-vectors-negative300.bin.gz"  # パスを適宜変更
print("Loading Word2Vec model...")
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("Model loaded.")

# === 2. WordSim-353の読み込み ===
data_path = "combined.csv"  # 解凍した combined.csv のパスを指定
df = pd.read_csv(data_path)

# === 3. 類似度の計算 ===
human_scores = []
model_scores = []
skipped = 0

for _, row in df.iterrows():
    word1 = row['Word 1'].lower()
    word2 = row['Word 2'].lower()
    human_score = row['Human (mean)']

    try:
        similarity = model.similarity(word1, word2)
        human_scores.append(human_score)
        model_scores.append(similarity)
    except KeyError:
        # 単語が語彙に存在しない場合はスキップ
        skipped += 1
        continue

# === 4. スピアマン相関係数の計算 ===
rho, p_value = spearmanr(human_scores, model_scores)

# === 5. 結果の表示 ===
print(f"スピアマン相関係数: {rho:.4f}")
print(f"語彙外によりスキップされたペア数: {skipped}")
print(f"有効評価ペア数: {len(human_scores)} / {len(df)}")
