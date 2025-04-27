N = 10
file = "/Users/aa/Downloads/popular-names.txt"
with open(file, 'r') as r:
    for i in range(N):
        line = r.readline()
        if not line:
            break
        print(line.strip())
