from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from knock61 import df1_dct, df2_dct

X_train_dict = [d['feature'] for d in df2_dct]
y_train = [int(d['label']) for d in df2_dct]

X_dev_dict = [d['feature'] for d in df1_dct]
y_dev = [int(d['label']) for d in df1_dct]

vectorizer = DictVectorizer(sparse=True)
X_train = vectorizer.fit_transform(X_train_dict)
X_dev = vectorizer.transform(X_dev_dict)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

