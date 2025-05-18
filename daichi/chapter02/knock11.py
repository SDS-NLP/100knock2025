
with open('./daichi/chapter02/popular-names.txt') as f:
    for i in range(10):
        print(f.readline().rstrip())