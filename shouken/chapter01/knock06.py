def ngram(sequence, n):
    result = []
    for i in range(len(sequence) - n + 1):
        result.append(sequence[i:i+n])
    return result

s1 = "paraparaparadise"
s2 = "paragraph"

X = set(ngram(s1, 2))
Y = set(ngram(s2, 2))

union = X | Y        # X ∪ Y
intersection = X & Y   # X ∩ Y
difference = X - Y  # X \ Y

print("X =", X)
print("Y =", Y)
print("和集合 (X ∪ Y):", union)
print("積集合 (X ∩ Y):", intersection)
print("差集合 (X - Y):", difference)

print("'se' in X:", 'se' in X)
print("'se' in Y:", 'se' in Y)