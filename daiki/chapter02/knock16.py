import random
file = "daiki/chapter02/popular-names.txt"
with open(file, 'r') as r:
    lines = r.readlines()
    random.shuffle(lines)
    #確認
    print(lines[:10])