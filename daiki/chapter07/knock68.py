import joblib
import pandas as pd

# モデルとベクトライザを読み込み
model, vectorizer = joblib.load("logistic_model.joblib")

# 特徴語（語彙）と重みを取得
feature_names = vectorizer.get_feature_names_out()
weights = model.coef_[0]  # shape: (1, 語彙数)

# DataFrameにまとめてソート
df = pd.DataFrame({
    "feature": feature_names,
    "weight": weights
})

# 重みの高いトップ20
print("重みの高い特徴量 トップ20（ポジ寄り）")
print(df.sort_values(by="weight", ascending=False).head(20))

# 重みの低いトップ20
print("\n重みの低い特徴量 トップ20（ネガ寄り）")
print(df.sort_values(by="weight", ascending=True).head(20))

#出力
"""
重みの高い特徴量 トップ20（ポジ寄り）
           feature    weight
10593   refreshing  3.417448
10675   remarkable  3.405659
9915      powerful  3.211314
6169     hilarious  3.168394
1263     beautiful  2.996458
14622    wonderful  2.963931
10145        prose  2.905816
788      appealing  2.851465
13103     terrific  2.849718
13492        treat  2.791016
4321     enjoyable  2.785668
2180       charmer  2.749920
14212      vividly  2.711300
7627       likable  2.680033
12089        solid  2.647767
2181      charming  2.639948
4802   fascinating  2.624691
5877      half-bad  2.603915
6574    impressive  2.589212
6901    intriguing  2.574548

重みの低い特徴量 トップ20（ネガ寄り）
             feature    weight
7365         lacking -4.329513
7367           lacks -4.065212
14674          worst -3.995111
3543          devoid -3.642725
8216            mess -3.591564
4729         failure -3.554489
12618         stupid -3.332083
1615            bore -3.243641
5021            flat -3.222988
3456      depressing -3.177937
7780           loses -3.159257
14322          waste -3.143172
7361            lack -3.041178
5973          hardly -3.023565
8844            none -3.022456
12321      squanders -3.020871
9829            poor -2.976445
9789       pointless -2.946055
13856  unfortunately -2.936320
7793           lousy -2.916910"""