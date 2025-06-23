#56. WordSimilarity-353での評価
from knock50 import model
import pandas as pd 
from scipy.stats import spearmanr

path = "combined.csv"
df = pd.read_csv(path)

#人間の結果とモデルの結果をリストに保存
results=[]
humans=[]
for a,b, human in zip(df.iloc[:,0], df.iloc[:,1], df.iloc[:,2]):
    result = model.similarity(a,b) 
    results.append(result)
    human = float(human)
    humans.append(human)

# スピアマン相関係数を計算
corr, p_value = spearmanr(results, humans)

print(f"スピアマン相関係数: {corr:.4f}")
print(f"p値: {p_value:.4f}")
