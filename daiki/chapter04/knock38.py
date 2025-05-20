import MeCab
import sklearn
#名詞のみを取り出す関数を作成
def extrct_nouns(text):
    tagger = MeCab.Tagger()#MeCab の解析器オブジェクトを生成
    node = tagger.parseToNode(text)#入力テキストを解析し、形態素解析結果を双方向リスト（ノード）として取得
    words = []
    while node:
        features = node.feature.split(',')#品詞情報（feature）をカンマで分割してリスト化
        if features[0] == '名詞':#features[0]は品詞情報
            words.append(node.surface)#ノードの表層形（surface）をリストに追加
        node = node.next
    return words

from sklearn.feature_extraction.text import TfidfVectorizer#文書集合から TF-IDF を計算するためのクラスをインポート
import numpy as np
import pandas as pd
with open("/Users/aa/100knock2025/daiki/chapter04/kokoro.txt", "r", encoding = "utf-8") as f:
    text = f.read()

#読み込んだテキストを「。」で分割し、各要素の前後の空白を取り除いた上で空文字列を除外し、文ごとのリストを作る
documents = [line.strip() for line in text.split("。") if line.strip()]

# 名詞のみからなる文書のリストを作る
noun_docs = [" ".join(extrct_nouns(doc)) for doc in documents] 

# TF-IDFベクトライザを定義して学習
vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")  # スペース区切りの単語をキャプチャ
X = vectorizer.fit_transform(noun_docs)#fit_transform は fit（学習）＋transform（変換）をまとめたもの 
                                       #fit: 語彙（語彙リスト）を学習
                                       #transform: 各文書をベクトルに変換

# 単語一覧
terms = vectorizer.get_feature_names_out()#ベクトライザが学習した語彙リスト（特徴量名）を NumPy 配列 terms に取得

# TF, IDF, TF-IDF を取得
tf = X.sum(axis=0).A1  # 各単語の出現頻度（全体での合計）。TF（Term Frequency）として、行列 X の各列（単語）を文全体で合計し、A1 で一次元配列に変換して tf に格納
idf = vectorizer.idf_  # 各単語のIDF値
tfidf = tf * idf       # 各単語のTF-IDFスコア

# pandasでデータフレームにまとめる
df = pd.DataFrame({
    "term": terms,
    "TF": tf,
    "IDF": idf,
    "TF-IDF": tfidf
})

# TF-IDFのスコアで降順に並べて上位20語を表示
top20 = df.sort_values("TF-IDF", ascending=False).head(20)
print(top20)
