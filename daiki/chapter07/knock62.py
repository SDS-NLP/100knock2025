import joblib # joblib: モデルやデータをファイルに保存・読み込みするためのライブラリ
from sklearn.feature_extraction import DictVectorizer # 辞書形式（BoWなど）をベクトル形式に変換するためのツール
from sklearn.linear_model import LogisticRegression # scikit-learn のロジスティック回帰モデル
from knock61 import train_examples  # knock61.pyで生成されたデータをインポート

# 特徴とラベルの抽出
X_train_dict = [ex["feature"] for ex in train_examples]
y_train = [int(ex["label"]) for ex in train_examples]

# ベクトル化
vectorizer = DictVectorizer(sparse=False) # 単語の頻度の辞書を「数値のベクトル（行列）」に変換
X_train = vectorizer.fit_transform(X_train_dict) # fit：単語の一覧を登録, transform：実際に数値行列に変換する

# モデル学習
model = LogisticRegression(max_iter=1000) # 収束しやすくするために、最大繰り返し回数を増やしている
model.fit(X_train, y_train) # モデルを学習データで訓練

# モデル保存
joblib.dump((model, vectorizer), "logistic_model.joblib")

print(" ロジスティック回帰モデルの学習完了")
