N = 10 #今回は最初の１０行u
file = "daiki/chapter02/popular-names.txt"
with open(file, 'r') as r:
    for i in range(N):
        line = r.readline()
        if not line:#行が終われば終了
            break
        print(line.strip())#余分な空白を除去
#headコマンド head -n 10 daiki/chapter02/popular-names.txt
"""Mary    F       7065    1880
Anna    F       2604    1880
Emma    F       2003    1880
Elizabeth       F       19391880
Minnie  F       1746    1880
Margaret        F       15781880
Ida     F       1472    1880
Alice   F       1414    1880
Bertha  F       1320    1880
Sarah   F       1288    1880"""