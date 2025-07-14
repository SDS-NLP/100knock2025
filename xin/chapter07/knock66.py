from knock63 import train_labels, train_dicts,dev_dicts,dev_labels
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# ベクトル化
vectorizer = DictVectorizer()
X_train = vectorizer.fit_transform(train_dicts)
X_dev = vectorizer.transform(dev_dicts)

# ロジスティック回帰の学習
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, train_labels)

# 予測
pred_dev = clf.predict(X_dev)

cm=confusion_matrix(dev_labels, pred_dev, labels=['0', '1'])
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Negative', 'Positive'])
fig, ax = plt.subplots()
disp.plot(ax=ax, cmap='Blues')

ax.set_title('Confusion Matrix for Sentiment Analysis')
ax.set_xlabel('Predicted Label')
ax.set_ylabel('True Label')
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(['Negative', 'Positive'])
ax.set_yticklabels(['Negative', 'Positive'])

plt.savefig('confusion_matrix.png')
plt.show()
