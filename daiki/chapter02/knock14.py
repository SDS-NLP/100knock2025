file = "/Users/aa/Downloads/popular-names.txt"
with open(file, 'r') as r:
    for i in range(10):
        line = r.readline()
        first_column = line.split()[0]
        print(first_column)
