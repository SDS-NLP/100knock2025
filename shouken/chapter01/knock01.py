t = "パタトクカシーー"
t1 = ""
for i, ch in enumerate(t):
    if i % 2 == 0:
        continue
    else:
        t1 = t1 + ch
print(t1)
