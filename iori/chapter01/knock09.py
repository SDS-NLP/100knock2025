import random

text = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
ans = []

for i in text.split():
    if len(i) > 4:
        i = i[0] + ''.join(random.sample(i[1:-1], len(i) - 2)) + i[-1]
    ans.append(i)
    
print(' '.join(ans))