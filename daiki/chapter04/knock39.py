import MeCab
import collections
import matplotlib.pyplot as plt 

with open('/Users/aa/100knock2025/daiki/chapter04/kokoro.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()

#MeCabで全単語（表層系）を抽出
tagger = MeCab.Tagger()
node = tagger.parseToNode(text)
words = []
while node:
    surface = node.surface
    if surface:    #空文字列を除外
        words.append(surface)
    node = node.next
#出現頻度をカウント
freq = collections.Counter(words)

#頻度順にソートしてランクと頻度のリストを作成
most_common = freq.most_common() #頻度降順リスト
ranks = list(range(1, len(most_common)+1))
frequencies = [count for i, count in most_common]

#両対数グラフをプロット
plt.figure()
plt.loglog(ranks, frequencies)
plt.xlabel('rank')
plt.ylabel('frequencies')
plt.title("Zipf's law")
plt.grid(True, which = 'both', ls = '--', lw = 0.5)
plt.show()