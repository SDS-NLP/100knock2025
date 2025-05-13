import random

with open('iori/chapter02/popular-names.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

random.shuffle(lines)
for line in lines:
    print(line, end='')  

# #shuf iori/chapter02/popular-names.txt

'''Susan   F       31515   1964
Helen   F       23221   1914
Justin  M       31492   1987
Edward  M       2398    1906
John    M       9342    1908
Jason   M       52680   1976
Anna    F       15228   1916
Stephanie       F       15774   1975
'''