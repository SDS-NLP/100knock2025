car: str = "パタトクカシーー"
ans: str = ""

for i in range(len(car)):
    if not((i+1)%2):
        ans += car[i]

print(ans)