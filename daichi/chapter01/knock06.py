X = []
Y = []

x = "paraparaparadise"
y = "paragraph"

for i in range(len(x)-1):
    X.append(x[i:i+2])

for i in range(len(y)-1):
    Y.append(y[i:i+2])

X=set(X)
Y=set(Y)

print(X|Y)
print(X&Y)
print(X-Y)

se = {'se'}
print(se <= X)
print(se <= Y)