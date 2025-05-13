file = "/Users/aa/Downloads/popular-names.txt"
with open(file, "r") as r:
    for i in range(10):
        line = r.readline()
        #タブをスペースに変換
        line = line.replace('\t',' ')
        print(line, end = "")