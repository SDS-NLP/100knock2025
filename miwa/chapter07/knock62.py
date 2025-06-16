#62.学習
from knock61 import train_data
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# 特徴ベクトルとラベルの抽出
train_features = [example['feature'] for example in train_data]
train_labels = [example['label'] for example in train_data]

# 辞書→数値ベクトルに変換
vectorizer = DictVectorizer(sparse=True)
X_train = vectorizer.fit_transform(train_features)

# ラベルを数値に変換（必要なら）
label_encoder = LabelEncoder()
y_train = label_encoder.fit_transform(train_labels)

# ロジスティック回帰モデルの学習
clf = LogisticRegression(random_state=123, max_iter=1000)
clf.fit(X_train, y_train)

if __name__ == "__main__":
    print("学習完了")
