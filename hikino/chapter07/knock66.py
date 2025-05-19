from knock62 import model, X_dev, y_dev
from knock61 import df1
import numpy as np

y_pred = model.predict(X_dev)
y_ans = df1.loc[:, "label"]
y_pred = y_pred.tolist()
y_ans = y_ans.to_list()

n1 = 0
n2 = 0
n3 = 0
n4 = 0
for i in range(len(y_pred)):
    pred = y_pred[i]
    ans = y_ans[i]
    if pred == 0 and ans ==0:
        n1 += 1
    elif pred == 0 and ans ==1:
        n2 += 1
    elif pred == 1 and ans ==0:
        n3 += 1
    else:
        n4 += 1


result = np.array([[n1, n2],
                  [n3, n4]])
print(result)