sen = "I am an NLPer"
tri_gram = []
for i in range(len(sen)-2):
  tri = sen[i:i+3]
  tri_gram.append(tri)
print(tri_gram)

sen_sp = sen.split(" ")
bi_gram = []
for i in range(len(sen_sp)-1):
  str1 = sen_sp[i]
  str2 = sen_sp[i+1]
  tpl = (str1, str2)
  bi_gram.append(tpl)
print(bi_gram)