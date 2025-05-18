sweets: str = "stressed"
ans: str = ""

for i in range(len(sweets)):
    ans += sweets[len(sweets)-i-1]

print(ans)

# print(sweets[::-1])