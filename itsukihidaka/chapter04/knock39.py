# コーパスにおける単語の出現頻度順位を横軸、その出現頻度を縦軸として、両対数グラフをプロットせよ。
from knock36 import texts
import MeCab
import matplotlib.pyplot as plt
import japanize_matplotlib

mecab = MeCab.Tagger('-Ochasen')

numcount = {}

for text in texts:
    node = mecab.parseToNode(text)
    while node:
        if node.surface not in numcount:
            numcount[node.surface] = 0
        numcount[node.surface] += 1
        node = node.next

# 出現頻度順にソート
sorted_numcount = sorted(numcount.items(), key=lambda x: x[1], reverse=True)

# 順位と出現頻度のリストを作成
ranks = list(range(1, len(sorted_numcount) + 1))
frequencies = [count for word, count in sorted_numcount]

# 両対数グラフのプロット
plt.figure(figsize=(8, 6))
plt.loglog(ranks, frequencies, marker='.', linestyle='None')
plt.xlabel('出現頻度順位')
plt.ylabel('出現頻度')
plt.title('Zipfの法則')
plt.grid(True)
plt.show()

