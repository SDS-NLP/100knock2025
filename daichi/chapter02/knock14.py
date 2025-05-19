count = 0

with open('./daichi/chapter02/popular-names.txt') as f:
    while count < 10:
        count += 1
        name = f.readline().rsplit()
        print(name[0])