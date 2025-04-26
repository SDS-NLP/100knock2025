def ngram(sequence, n):
    return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]

# 文字列
X_text = "paraparaparadise"
Y_text = "paragraph"

# bi-gram の集合
X = set(ngram(X_text, 2))
Y = set(ngram(Y_text, 2))

# 和集合
union = X | Y

# 積集合
intersection = X & Y

# 差集合（X - Y）
difference = X - Y

# 'se' を含むか？
contains_se_X = 'se' in X
contains_se_Y = 'se' in Y

# 結果出力
print("X:", X)
print("Y:", Y)
print("和集合 (X ∪ Y):", union)
print("積集合 (X ∩ Y):", intersection)
print("差集合 (X - Y):", difference)
print("'se' in X:", contains_se_X)
print("'se' in Y:", contains_se_Y)
