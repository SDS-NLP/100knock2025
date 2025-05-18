file = "/Users/aa/Downloads/popular-names.txt"
N = 10
with open(file, 'r') as r:
    lines = r.readlines()
    print(len(lines))