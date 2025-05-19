#38. TF・IDF
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# GiNZAの日本語モデルをロード
nlp = spacy.load("ja_ginza")

# 文書ごとに名詞だけを抽出する関数
def extract_nouns(text):
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if token.pos_ in ["NOUN", "PROPN"]])

# コーパス読み込み：文書ごとに分ける（1文書＝1段落、または1行）
with open("kokoro.txt", "r", encoding="utf-8") as f:
    docs = [line.strip() for line in f if line.strip()]

# 各文書から名詞を抽出（文字列として）
noun_docs = [extract_nouns(doc) for doc in docs]

# TF-IDFベクトライザを使って計算
vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
tfidf_matrix = vectorizer.fit_transform(noun_docs)

# 単語リスト取得
terms = vectorizer.get_feature_names_out()

# TF：文書全体の単語の出現回数合計
tf = np.asarray(tfidf_matrix.sum(axis=0)).flatten()

# IDF：scikit-learn内部で保持されている
idf = vectorizer.idf_

# TF-IDFスコア（TF × IDF）
tfidf_scores = tf * idf

# 上位20件のインデックスを取得
top_indices = tfidf_scores.argsort()[::-1][:20]

# 結果を表示
print("語彙\tTF\tIDF\tTF-IDF")
for idx in top_indices:
    print(f"{terms[idx]}\t{tf[idx]:.2f}\t{idf[idx]:.2f}\t{tfidf_scores[idx]:.2f}")
