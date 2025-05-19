"""
knock38:TF・IDF
日本に関する記事における名詞のTF・IDFスコアを求め、
TF・IDFスコア上位20語とそのTF,IDF,TF・IDFを表示せよ
"""
#####以下sklearn使用####
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

filename = "mao/chapter04/jawiki-country.json"
documents = []

with open(filename, encoding="utf-8") as f:
    for line in f:
        article = json.loads(line)
        documents.append(article.get("text", ""))

vectorizer=TfidfVectorizer()
tfidf_matrix=vectorizer.fit_transform(documents)

#単語一覧
terms=vectorizer.get_feature_names_out()

#文書×単語のTF-IDF行列(SciPyの疎行列)
print(tfidf_matrix.shape) #(文書数、単語数)

#文書0の上位単語表示
doc_index = 0
row = tfidf_matrix[doc_index].toarray().flatten()
top_indices = np.argsort(row)[::-1][:20]

print("文書0のTF-IDF上位語:")
for i in top_indices:
    print(f"{terms[i]}: {row[i]:.4f}")

"""
rom knock36 import cleaned_texts,nouns_list
import fugashi
from collections import Counter
import numpy as np

japan_article=[]
counter_japan_noun=Counter()
tagger=fugashi.Tagger()

for title,word in nouns_list: #titleが日本のもの抽出

    if title=="日本":
        counter_japan_noun.append(())   


#全文書数
N=len(cleaned_texts)

#各文書ごとの単語リスト

for text i
#文書dにおける単語の出現回数

#

###TFスコア計算
#文書dにおける単語の出現回数
#文書d中の総単語数
tf_score=counter_japan_noun/len

#IDFスコア計算
#全文書数
#単語を含む文書数
idf_score=np.log(len(cleand_text)/len)

#TF-IDFスコア計算:ある文書においてその単語がどれほど重要かを表す
tf_idf_score=tf_score*idf_score

#結果出力
print(f"TFスコア:{tf_score}")
print(f"IDFスコア:{idf_score}")
print(f"TF-IDFスコア:{tf_idf_score}")
"""
print(np.__version__)
#numpyとsklearnの互換性が低い、numpyが最近最新になったばかり
#numpyを最新版からダウングレードしたらいけた