from knock62 import model, vectorizer
import numpy as np

coefs = model.coef_[0]
coefs = coefs.tolist()

feature_names = vectorizer.get_feature_names_out()

top_idx = np.argsort(coefs)[-20:][::-1]
bottom_idx = np.argsort(coefs)[:20]       

print(" 重みの高い特徴量トップ20:")
for i in top_idx:
    print(f"{feature_names[i]:<15} : {coefs[i]:.4f}")

print("\n 重みの低い特徴量トップ20:")
for i in bottom_idx:
    print(f"{feature_names[i]:<15} : {coefs[i]:.4f}")
