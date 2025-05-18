#10.行数のカウント

path="popular-names.txt"

with open(path, "r", encoding="utf-8") as f:
    line_count=sum(1 for line in f)
print("行数:", line_count)

### unixコマンド ###
# wc -l popular-names.txt
 
### 実行結果 ###
# 2780 popular-names.txt
