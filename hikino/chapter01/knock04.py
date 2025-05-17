sen = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
dict_result = {}
one_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
sen_sp = sen.split(" ")
for i in range(len(sen_sp)):
  if i + 1 in one_list:
    key = sen_sp[i][0]
    dict_result[key] = i + 1
  else:
    key = sen_sp[i][0] + sen_sp[i][1]
    dict_result[key] = i + 1
print(dict_result)