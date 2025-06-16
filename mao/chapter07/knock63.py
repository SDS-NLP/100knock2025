"""
knock63: 予測
学習したロジスティック回帰モデルを用い、
検証データの先頭の事例のラベル（ポジネガ）を予測せよ。
また、予測されたラベルが検証データで付与されていたラベルと一致しているか、確認せよ。
"""
from knock61 import dev_bow
from knock62 import model, vectorizer  

#検証データの最初の事例
feature=dev_bow[0]['feature']
true_label=int(dev_bow[0]['label'])

#特徴ベクトルに変換（単体なのでリスト化）
X_example=vectorizer.transform([feature])

#ラベル予測 リスト形式なので一応番号指定
predicted_label=model.predict(X_example)[0] 

#結果確認
print("テキスト:", dev_bow[0]['text'])
print("正解   :", true_label)
print("予測結果:", predicted_label)