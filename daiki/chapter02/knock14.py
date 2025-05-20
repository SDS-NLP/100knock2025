file = "daiki/chapter02/popular-names.txt"
with open(file, 'r') as r:
    for i in range(10):
        line = r.readline()
        first_column = line.split()[0]
        print(first_column)
#cutコマンド head -n 10 daiki/chapter02/popular-names.txt | cut -f 1
"""Mary
Anna
Emma
Elizabeth
Minnie
Margaret
Ida
Alice
Bertha
Sarah"""
