# ロジスティック回帰モデルを学習するとき、正則化の係数（ハイパーパラメータ）を調整することで、学習時の適合度合いを制御できる。正則化の係数を変化させながらロジスティック回帰モデルを学習し、検証データ上の正解率を求めよ。実験の結果は、正則化パラメータを横軸、正解率を縦軸としたグラフにまとめよ。

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
import matplotlib_fontja

# データセットの読み込み
df_train = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter07/SST-2/train.tsv', sep='\t')
df_dev = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter07/SST-2/dev.tsv', sep='\t')

# ラベルの準備
texts = df_train['sentence'].tolist()
labels = df_train['label'].tolist()

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# 検証データの準備
texts_dev = df_dev['sentence'].tolist()
labels_dev = df_dev['label'].tolist()
X_dev = vectorizer.transform(texts_dev)

# 正則化パラメータCの値を設定（Cが小さいほど正則化が強くなる）
C_values = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
accuracies = []

print("正則化パラメータCを変化させた学習結果:")
print("C\t\t正解率")
print("-" * 20)

# 各正則化パラメータで学習と評価
for C in C_values:
    # ロジスティック回帰モデルの学習（Cパラメータで正則化強度を制御）
    model = LogisticRegression(C=C, random_state=42, max_iter=1000)
    model.fit(X, labels)
    
    # 検証データでの予測
    predictions = model.predict(X_dev)
    
    # 精度の計算
    accuracy = accuracy_score(labels_dev, predictions)
    accuracies.append(accuracy)
    
    print(f"{C}\t\t{accuracy:.3f}")

# グラフの作成
plt.figure(figsize=(10, 6))
plt.plot(C_values, accuracies, 'bo-', linewidth=2, markersize=8)
plt.xscale('log')  # 対数スケールで表示
plt.xlabel('正則化パラメータ C')
plt.ylabel('正解率')
plt.title('正則化パラメータCと正解率の関係')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# 最適なCの値を表示
best_C = C_values[np.argmax(accuracies)]
best_accuracy = max(accuracies)
print(f"\n最適な正則化パラメータ: C = {best_C}")
print(f"最高正解率: {best_accuracy:.3f}")

plt.show()




