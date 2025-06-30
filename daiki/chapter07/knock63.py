import joblib
from knock61 import dev_examples  # すでにBoWに変換済み

# モデルとベクトライザの読み込み
model, vectorizer = joblib.load("logistic_model.joblib") # joblib.load でファイルを復元

# devデータの先頭事例
ex = dev_examples[0]
x_dict = ex["feature"]
true_label = int(ex["label"])

# ベクトル化して予測
x_vec = vectorizer.transform([x_dict]) # 辞書を 1行の行列（shape = (1, 語彙数)）に変換
pred_label = model.predict(x_vec)[0] # ロジスティック回帰でラベルを推論

# 結果表示
print("予測結果")
print(f"テキスト       : {ex['text']}")
print(f"正解ラベル     : {true_label}")
print(f"予測ラベル     : {pred_label}")
print("一致しているか : ", "一致" if pred_label == true_label else "不一致")

#出力
"""
予測結果
テキスト       : it 's a charming and often affecting journey . 
正解ラベル     : 1
予測ラベル     : 1
一致しているか :  一致
"""