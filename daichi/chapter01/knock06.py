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

print(f"和集合：{X|Y}")
print(f"積集合：{X&Y}")
print(f"差集合：{X-Y}")

se = {'se'}

if se in X:
    print("’se’というbi-gramがXに含まれます。")
else:
    print("’se’というbi-gramはXに含まれません。")

if se in Y:
    print("’se’というbi-gramがYに含まれます。")
else:
    print("’se’というbi-gramはYに含まれません。")


