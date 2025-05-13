#12.末尾のＮ行を出力

path="popular-names.txt"

n=10
with open(path, "r", encoding="utf-8") as f:
    lines=f.readlines()

for line in lines[-n:]:
    print(line.strip())

### unixコマンド ###
# tail popular-names.txt
 
### 実行結果 ###
# Liam    M       19837   2018
# Noah    M       18267   2018
# William M       14516   2018
# James   M       13525   2018
# Oliver  M       13389   2018
# Benjamin        M       13381   2018
# Elijah  M       12886   2018
# Lucas   M       12585   2018
# Mason   M       12435   2018
# Logan   M       12352   2018