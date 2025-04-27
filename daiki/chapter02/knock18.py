file = "daiki/chapter02/popular-names.txt"
with open(file, 'r') as r:
    lines = r.readlines()
    names = []
    for line in lines:
        first_column = line.split()[0]
        names.append(first_column)
    dct = {}
    for name in names:
        if name in dct:
            dct[name] += 1
        else:
            dct[name] = 1 
    sorted_dct = dict(sorted(dct.items(), key = lambda item: item[1], reverse = True))
    for key, value in sorted_dct.items():
        print(key, value)
#cut -d ' ' -f 1 daiki/chapter02/popular-names.txt | sort | uniq -c | sort -nr | awk '{print $2, $1}'


