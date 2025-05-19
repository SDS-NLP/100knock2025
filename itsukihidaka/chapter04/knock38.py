# 日本に関する記事における名詞のTF・IDFスコアを求め、TF・IDFスコア上位20語とそのTF, IDF, TF・IDFを表示せよ。

from knock36 import texts
import MeCab
import math
from collections import defaultdict

mecab = MeCab.Tagger('-Ochasen')

# 各文書における単語の出現回数
doc_word_counts = []
# 各単語が出現する文書数
word_doc_counts = defaultdict(int)

# 各文書の単語出現回数を計算
for text in texts:
    word_count = defaultdict(int)
    node = mecab.parseToNode(text)
    while node:
        if node.feature.split(',')[0] == '名詞':
            word_count[node.surface] += 1
        node = node.next
    
    doc_word_counts.append(word_count)
    
    # 各単語が出現する文書数をカウント
    for word in word_count:
        word_doc_counts[word] += 1

# 文書数
N = len(texts)

# TF-IDFの計算
tfidf_scores = defaultdict(float)
tf_scores = {}
idf_scores = {}

for word in word_doc_counts:
    # IDFの計算
    idf = math.log(N / word_doc_counts[word])
    idf_scores[word] = idf
    
    # 各文書のTFとTF-IDFを計算して合計
    total_tfidf = 0
    total_tf = 0
    
    for doc_idx, word_count in enumerate(doc_word_counts):
        if word in word_count:
            # 文書内の総単語数（名詞）
            total_words = sum(word_count.values())
            # TFの計算
            tf = word_count[word] / total_words if total_words > 0 else 0
            # TF-IDFの計算
            tfidf = tf * idf
            
            total_tfidf += tfidf
            total_tf += tf
    
    # 平均TFとTF-IDFを記録
    tf_scores[word] = total_tf / N
    tfidf_scores[word] = total_tfidf / N

# TF-IDFスコアで単語を降順ソート
sorted_words = sorted(tfidf_scores.items(), key=lambda x: x[1], reverse=True)

# 上位20語を表示
print('TF-IDFスコア上位20語:')
print('順位\t単語\tTF\tIDF\tTF-IDF')
for i, (word, tfidf) in enumerate(sorted_words[:20], 1):
    print(f'{i}\t{word}\t{tf_scores[word]:.6f}\t{idf_scores[word]:.6f}\t{tfidf:.6f}')
