"""
knock64: 条件付き確率
学習したロジスティック回帰モデルを用い、
検証データの先頭の事例を各ラベル（ポジネガ）に分類するときの条件付き確率を求めよ。
"""
from knock61 import dev_bow
from knock62 import model, vectorizer

#検証データ先頭取得
feature=dev_bow[0]['feature']
text=dev_bow[0]['text']
true_label=int(dev_bow[0]['label'])

#特徴ベクトルに変換（リストで渡す）
X_example=vectorizer.transform([feature])

#条件付き確率を算出
probs=model.predict_proba(X_example)[0]  # [P(label=0), P(label=1)]
con_probs=round(probs[0]/probs[1],4)

#結果確認
print("テキスト   :", text)
print("実際のラベル:", true_label)
print("予測確率   :",con_probs) #ネガ/ポジ
