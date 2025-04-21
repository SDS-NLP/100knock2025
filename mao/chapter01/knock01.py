words="パタトクカシーー"
answer=""

for i in range(len(words)):
    if i%2==1: #偶数番目抽出
        answer+=words[i]
print(answer)
        
