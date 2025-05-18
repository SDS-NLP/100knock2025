car_1: str = "パトカー"
car_2: str = "タクシー"
ans: str = ""

for i in range(len(car_1)):
    ans += car_1[i] + car_2[i]

print(ans)