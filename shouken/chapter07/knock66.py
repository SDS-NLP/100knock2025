from knock61 import dev_data
from knock62 import model
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# 特徴とラベルの抽出
X_dev = [d['feature'] for d in dev_data]
y_true = [int(d['label']) for d in dev_data]

# 予測
y_pred = model.predict(X_dev)

# 混同行列の計算
cm = confusion_matrix(y_true, y_pred, labels=[0, 1])

# 表示
print("混同行列（行：正解ラベル，列：予測ラベル）")
print(cm)

# オプション：図として可視化（必要なら）
try:
    import matplotlib.pyplot as plt
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Negative (0)", "Positive (1)"])
    disp.plot(cmap="Blues")
    plt.title("Confusion Matrix")
    plt.show()
except ImportError:
    print("matplotlib が未インストールのため図は表示できません。")
