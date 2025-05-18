import random

def Typoglycemia(sentence):
    mylist = sentence.split(' ')
    new_list = list()
    for i in mylist:
        if len(i) <= 4:
            new_list.append(i)
        else:
            temp = i[1:len(x)-1]
            temp = ''.join(random.sample(temp, len(temp)))
            new_list.append(i[0] + temp + i[len(i)-1])
    return ' '.join(map(str, new_list))

x = r"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(Typoglycemia(x))
