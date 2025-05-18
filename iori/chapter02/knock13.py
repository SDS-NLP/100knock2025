with open('iori/chapter02/popular-names.txt', 'r') as f:
    for i, line in enumerate(f):
        if i >= 10:  
            break
        print(line.replace('\t', ' '), end='')

#head -n 10 iori/chapter02/popular-names.txt | expand -t 1

'''Mary F 7065 1880
Anna F 2604 1880
Emma F 2003 1880
Elizabeth F 1939 1880
Minnie F 1746 1880
Margaret F 1578 1880
Ida F 1472 1880
Alice F 1414 1880
Bertha F 1320 1880
Sarah F 1288 1880'''
