# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合に対する和集合・積集合・差集合を求めよ。さらに、’se’というbi-gramがXおよびYに含まれるかどうかを調べよ。

text1 = "paraparaparadise"
text2 = "paragraph"

def n_gram(sequence, n):
    return [sequence[i:i+n] for i in range(len(sequence)-n+1)]

X = set(n_gram(text1, 2))
Y = set(n_gram(text2, 2))

print('和集合:', X | Y)
print('積集合:', X & Y)
print('差集合:', X - Y)

print('se' in X)
print('se' in Y)