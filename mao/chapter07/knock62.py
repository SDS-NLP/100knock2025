"""
knock62: 学習
61で構築した学習データの特徴ベクトルを用いて、
ロジスティック回帰モデルを学習せよ。
"""
from knock61 import train_bow, dev_bow
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer

train_features=[]
train_labels=[]

#特徴ベクトルとラベルを分離
for data in train_bow:
    train_features.append(data['feature'])
    train_labels.append(int(data['label']))

#DictVectorizerでBoW辞書をベクトル化（スパース行列に変換）
#辞書オブジェクトを数値ベクトルに変換
vectorizer=DictVectorizer(sparse=True)
X_train=vectorizer.fit_transform(train_features)  #特徴行列
y_train=train_labels                              #ラベルベクトル

# ロジスティック回帰モデルの学習
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)