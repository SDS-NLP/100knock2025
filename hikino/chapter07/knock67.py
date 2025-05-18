from knock66 import n1, n2, n3, n4

TN = n1
FN = n2
FP = n3
TP = n4

accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F1 = 2 * (precision * recall) / (precision + recall)

print(accuracy, precision, recall, F1)