import numpy as np
from knock62 import X_dev, model

x = X_dev[0]

w = model.coef_[0]            
b = model.intercept_[0]       

z = x.dot(w) + b             
z = z[0]                      

prob_1 = 1 / (1 + np.exp(-z))  
prob_0 = 1 - prob_1           

print(f"ラベル0（ネガティブ）の確率: {prob_0:.4f}")
print(f"ラベル1（ポジティブ）の確率: {prob_1:.4f}")

i = 0
probs = model.predict_proba(X_dev[i])[0]

print(f"ラベル0（ネガティブ）の確率: {probs[0]:.4f}")
print(f"ラベル1（ポジティブ）の確率: {probs[1]:.4f}")