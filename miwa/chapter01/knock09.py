#09.Typoglycemia

import random

def typoglycemia(text):
    words=text.replace(",","").split()
    result=[]
    for word in words:
        if len(word) > 4:
            first=word[0]
            last=word[-1]
            middle=list(word[1:-1])
            random.shuffle(middle)
            shuffled_word = first + ''.join(middle) + last
            result.append(shuffled_word)
        else:
            result.append(word)
    return " ".join(result)

str1="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(str1))          
