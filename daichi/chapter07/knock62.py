from sklearn.linear_model import LogisticRegression # ロジスティック回帰モデルを使用
from sklearn.feature_extraction import DictVectorizer # BoW 辞書をベクトル化するためのツール
from knock61 import df1_dct, df2_dct # knock61.pyから学習用のデータとテスト用のデータをインポート

X_train_dict = [d['feature'] for d in df2_dct] # 学習用の BoW 辞書をリスト化（特徴量）
y_train = [int(d['label']) for d in df2_dct] # ラベル（0 or 1）を整数として取り出す（教師データ）

X_dev_dict = [d['feature'] for d in df1_dct] # 検証用の BoW 辞書をリスト化
y_dev = [int(d['label']) for d in df1_dct] # 検証用ラベルも整数で抽出(0 or 1)

vectorizer = DictVectorizer(sparse=True) 
X_train = vectorizer.fit_transform(X_train_dict) # 学習データをベクトル化
X_dev = vectorizer.transform(X_dev_dict) # 検証データを同じベクトル化器で変換

model = LogisticRegression(max_iter=1000) # モデルを初期化（max_iter=1000 は収束しないエラー回避）
model.fit(X_train, y_train) #fit() により、X_train と y_train を使って分類器を訓練
