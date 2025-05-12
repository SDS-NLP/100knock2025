import random

sen = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
sen_sp = sen.split(" ")
for i in range(len(sen_sp)):
  strs = sen_sp[i]
  if len(strs) > 4:
    m_str = strs[1:len(strs)-1]
    lst = list(m_str)
    random.shuffle(lst)
    r_str = ''.join(lst)
    new_str = strs[0] + r_str + strs[-1]
    sen_sp[i] = new_str

typo = " ".join(sen_sp)
print(typo)