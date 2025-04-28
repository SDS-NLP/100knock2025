
count = 0
with open('./daichi/chapter02/popular-names.txt') as f:
    for line in f:
        count += 1

print(count)

# wc -l daichi/chapter02/popular-names.txt
# 2780