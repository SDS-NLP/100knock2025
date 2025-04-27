file = "daiki/chapter02/popular-names.txt"
with open(file, 'r') as r:
    lines = r.readlines()
    #３列目を降順でソート
    sorted_lines = sorted(lines, key = lambda item: int(item.split()[2]), reverse = True)
    for line in sorted_lines:
        print(line.strip())
    