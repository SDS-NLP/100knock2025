import joblib
from knock61 import text_to_bow  # BoW変換関数

text = "the worst movie I've ever seen"

# BoW形式に変換（スペースで区切り→単語カウント）
x_dict = text_to_bow(text)

# 学習済みモデルとベクトライザを読み込み
model, vectorizer = joblib.load("logistic_model.joblib")

# ベクトル化（BoW辞書 → 数値ベクトル）
x_vec = vectorizer.transform([x_dict])

# 予測（ラベルと確率の両方）
pred_label = model.predict(x_vec)[0]
probs = model.predict_proba(x_vec)[0]

# 結果の表示
print("【ポジネガ予測結果】")
print(f"テキスト        : {text}")
print(f"予測ラベル      : {pred_label}（{'ポジティブ' if pred_label == 1 else 'ネガティブ'}）")
print(f"ネガティブ確率  : {probs[0]:.4f}")
print(f"ポジティブ確率  : {probs[1]:.4f}")
