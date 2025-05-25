"""
knock39:Zipfの法則
コーパスにおける単語の出現頻度順位を横軸、その出現頻度を縦軸として、
両対数グラフをプロットせよ。
"""
from knock36 import cleaned_texts
from collections import Counter
import matplotlib.pyplot as plt
import fugashi

tagger=fugashi.Tagger() #形態素解析器
counter=Counter()
freqs=[] #出現頻度格納用
ranks=[] #出現頻度順位格納用

#出現頻度調べる
for _,text in cleaned_texts:
    for word in tagger(text):
        counter[word.surface]+=1

for _,freq in counter.most_common(): #出現頻度リスト作成
    freqs.append(freq)

ranks=list(range(1,len(freqs)+1,1))  #出現頻度順位リスト作成

#両対数グラフを描画
plt.figure(figsize=(14,6))
plt.loglog(ranks,freqs)    #両対数グラフを描画
plt.xlabel("Frequency Rank")
plt.ylabel("Frequency")
plt.title("The low of Zipf")
plt.show()