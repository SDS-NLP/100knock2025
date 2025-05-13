str1 = "paraparaparadise"
str2 = "paragraph"

def bi_gram(strs):
  s = set()
  for i in range(len(strs)-1):
    str1 = strs[i]
    str2 = strs[i+1]
    tpl = (str1, str2)
    s.add(tpl)
  return s
bi1 = bi_gram(str1)
bi2 = bi_gram(str2)
print(bi1 | bi2)
print(bi1 & bi2)
print(bi1 - bi2)