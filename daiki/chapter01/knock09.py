import random
def shuffle_word(word):
    word_list = list(word)
    middle = word_list[1:-1]
    random.shuffle(middle)
    new_word_list = [word_list[0]] + middle + [word_list[-1]]
    return "".join(new_word_list)

s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
a = list(s.split())
b = []
for i in range(len(a)):
    if len(a[i]) <= 4:
        b.append(a[i])
    else:
         b.append(shuffle_word(a[i]))

ans = " ".join(b)
print(ans)
