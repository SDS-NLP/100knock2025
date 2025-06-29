import joblib
from knock61 import dev_examples

# モデルとベクトライザの読み込み
model, vectorizer = joblib.load("logistic_model.joblib")

# devデータの先頭事例
ex = dev_examples[2] # dev_examples から1件を取り出す
x_dict = ex["feature"]

# ベクトル化
x_vec = vectorizer.transform([x_dict]) # BoW辞書を数値のベクトルに変換

# 条件付き確率の予測
probs = model.predict_proba(x_vec)[0] # predict_proba は、各クラス（0と1）の 所属確率（＝条件付き確率） を返す関数

# 出力 
print("条件付き確率")
print(f"テキスト         : {ex['text']}")
print(f"ラベル0 (ネガ)   : {probs[0]:.4f}")
print(f"ラベル1 (ポジ)   : {probs[1]:.4f}")

#出力
"""
テキスト         : allows us to hope that nolan is poised to embark a major career as a commercial yet inventive filmmaker . 
ラベル0 (ネガ)   : 0.0049
ラベル1 (ポジ)   : 0.9951
"""