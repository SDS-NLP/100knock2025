def n_gram(sequence, n):
    return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]

# 文字列
s1 = "paraparaparadise"
s2 = "paragraph"

# bi-gramの集合（重複を除く）
X = set(n_gram(s1, 2))
Y = set(n_gram(s2, 2))

# 出力
print("X =", X)
print("Y =", Y)

# 和集合
print("X ∪ Y =", X | Y)

# 積集合
print("X ∩ Y =", X & Y)

# 差集合
print("X - Y =", X - Y)

# 'se'の存在確認
print("'se' in X?", 'se' in X)
print("'se' in Y?", 'se' in Y)
