#66. 混同行列の作成
from knock61 import dev_data
from knock62 import clf, vectorizer, label_encoder
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# dev_data の特徴ベクトルとラベルを抽出
dev_features = [example['feature'] for example in dev_data]
dev_labels = [example['label'] for example in dev_data]

# 特徴ベクトルに変換（DictVectorizerで整形）
X_dev = vectorizer.transform(dev_features)

# ラベルを数値に変換
y_true = label_encoder.transform(dev_labels)

# モデルによる予測
y_pred = clf.predict(X_dev)

# 混同行列を計算
cm = confusion_matrix(y_true, y_pred)

# 結果を表示
print("混同行列:")
print(cm)

# グラフで可視化
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=label_encoder.classes_)
disp.plot(cmap='Blues')
plt.title("Confusion Matrix")
plt.savefig("Confusion_Matrix")
