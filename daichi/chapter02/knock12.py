
with open('./daichi/chapter02/popular-names.txt') as f:
    lines = f.readlines()
    for line in lines[-10:]:
        print(line.rstrip())