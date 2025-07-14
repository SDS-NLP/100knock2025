from collections import Counter
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from knock61 import text_to_bow
from knock63 import train_labels, train_dicts

vectorizer= DictVectorizer()
def bow_predict(text):
    # テキストをBag-of-Wordsに変換
    bow = text_to_bow(text)
    # ベクトル化
    X_train = vectorizer.fit_transform(train_dicts)
    X = vectorizer.transform([bow])
    # 予測
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train, train_labels)
    pred = clf.predict(X)
    return pred
print(bow_predict("the worst movie I've ever seen"))