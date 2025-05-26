file = "daiki/chapter02/popular-names.txt"
with open(file, 'r') as r:
    lines = r.readlines()
    names = []
    #１列目の文字列のリストを作る
    for line in lines:
        first_column = line.split()[0]
        names.append(first_column)
    #文字列の種類をカウント
    count = 0
    lst = []
    for name in names:
        if name not in lst:
            count += 1 
            lst.append(name)
    print(count)
#結果　136
#cut -d ' ' -f 1 daiki/chapter02/popular-names.txt | sort | uniq | wc -l

