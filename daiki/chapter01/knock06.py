a = "paraparaparadise"
b = "paragraph"
def word_bigram(word):
    bigrams = []
    for i in range(len(word)-1):
        bigram = word[i:i+2]
        bigrams.append(bigram)
    return bigrams
X = word_bigram(a)
Y = word_bigram(b)
#XとYをprint
print(f"X：{set(X)}")
print(f"Y：{set(Y)}")
#XとYの和集合
ans1 = set(X) | set(Y)
print(f"XとYの和集合：{ans1}")
#XとYの積集合
ans2 = set(X) & set(Y)
print(f"XとYの積集合：{ans2}")
#XとYの差集合
ans3 = set(X) - set(Y)
print(f"XとYの差集合：{ans3}")
if "se" in X:
    print("'se'はXに含まれる。")
else:
    print("'se'はXに含まれない。")
if "se" in Y:
    print("'se'はYに含まれる。")
else:
    print("'se'はYに含まれない。")