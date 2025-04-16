def n_gram(n,word):
    ans = []
    for i in range(len(word)-n+1):
        ans.append(word[i:i+n])
    return ans

a = 'paraparaparadise'
b = 'paragraph'

X = set(n_gram(2,a))
Y = set(n_gram(2,b))

print(f"X: {X}")
print(f"Y: {Y}")
print(f"X | Y: {X | Y}")
print(f"X & Y: {X & Y}")
print(f"X - Y: {X - Y}")

def check(x):
    if 'se' in x:
        return True
    else:
        return False
    
print(f"Xにseは含まれているか？: {check(X)}")
print(f"Yにseは含まれているか？: {check(Y)}")