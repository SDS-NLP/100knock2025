file = "daiki/chapter02/popular-names.txt"
with open(file, 'r') as r:
    lines = r.readlines()
    total_lines = len(lines)
    names = []
    #１列目の文字列のリストを作る
    for i in total_lines:
        line = r.readline()
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