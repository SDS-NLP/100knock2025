
import random

with open('./daichi/chapter02/popular-names.txt') as f:
    lines = f.readlines()

random.shuffle(lines)

for line in lines:
    print(line.rstrip())
