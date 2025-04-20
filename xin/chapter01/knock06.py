def n_gram(sequence, n):
    """与えられたシーケンスから n-gram を生成する関数"""
    return {sequence[i:i+n] for i in range(len(sequence) - n + 1)}

X = n_gram("paraparaparadise", 2)
Y = n_gram("paragraph", 2)
wa_set = X | Y
seki_set = X & Y
sa_set = X - Y
contains_se_x = "se" in X
contains_se_y = "se" in Y
print("X:", X)
print("Y:", Y)
print("和集合:", wa_set)
print("積集合:", seki_set)
print("差集合:", sa_set)
print("'se' は X に含まれる？", contains_se_x)
print("'se' は Y に含まれる？", contains_se_y)