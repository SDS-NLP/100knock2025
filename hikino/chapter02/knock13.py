with open("../../../popular-names.txt", "r") as f:
  lines = f.readlines()
  for i in range(10):
    txt = lines[i]
    txt = txt.replace("/t", " ")
    print(txt)

#sed "s/\t/ /g" ../../../popular-names.txt
#実行結果
# Mary F 7065 1880
# Anna F 2604 1880
# Emma F 2003 1880
# Elizabeth F 1939 1880
# Minnie F 1746 1880
# Margaret F 1578 1880
# Ida F 1472 1880
# Alice F 1414 1880
# Bertha F 1320 1880
# Sarah F 1288 1880
