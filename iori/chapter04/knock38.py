import MeCab
import ipadic
from collections import Counter
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# ファイルを読み込む
with open('kokoro.txt', 'r', encoding='utf-8') as f:
    text = f.read()

    # 《》で囲まれた部分を削除
    text = re.sub(r'《.*?》', '', text)

    # 章ごとに分割
    chapters = re.split(r'\n\s*\d+\s*\n', text)  # 空白行、章番号、空白行で分割

# 名詞を抽出する関数
def extract_nouns(text):
    tagger = MeCab.Tagger(ipadic.MECAB_ARGS)
    tagger.parse("")  # バグ回避のための空パース
    node = tagger.parseToNode(text)
    nouns = []
    while node:
        if node.feature.split(',')[0] == '名詞':
            nouns.append(node.surface)
        node = node.next
    return ' '.join(nouns)

# 各章から名詞を抽出
nouns_per_chapter = [extract_nouns(chapter) for chapter in chapters]

# TF-IDF計算
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(nouns_per_chapter)
terms = vectorizer.get_feature_names_out()

# 各章ごとにTF-IDFスコア上位20語を表示
for i, chapter in enumerate(chapters):
    print(f"Chapter {i + 1}")
    tfidf_scores = tfidf_matrix[i].toarray().flatten()
    top_indices = tfidf_scores.argsort()[-20:][::-1]
    for idx in top_indices:
        term = terms[idx]
        tf = nouns_per_chapter[i].split().count(term)
        idf = vectorizer.idf_[idx]
        tfidf = tfidf_scores[idx]
        print(f"{term}: TF={tf}, IDF={idf:.4f}, TF-IDF={tfidf:.4f}")
    print()