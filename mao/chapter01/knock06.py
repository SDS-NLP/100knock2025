strings_x="paraparaparadise"
strings_y="paragraph"

bi_gram_x=[]      #xのbi_gram格納
bi_gram_y=[]      #yのbi_gram格納
x_or_y=[]         #xとyの和集合
x_and_y=[]        #xとyの積集合
x_minus_y=[]      #xとyの差集合

for i in range(len(strings_x)-1): #xのbi_gram作成
    if strings_x[i:i+2] not in bi_gram_x:
        bi_gram_x.append(strings_x[i:i+2])

for j in range(len(strings_y)-1): #yのbi_gram作成
    if strings_y[j:j+2] not in bi_gram_y:
        bi_gram_y.append(strings_y[j:j+2])

for k in range(len(bi_gram_x)):
    #積集合求める
    if bi_gram_x[k] in bi_gram_y:
        x_and_y.append(bi_gram_x[k])
    #差集合求める
    if bi_gram_x[k] not in bi_gram_y:
        x_minus_y.append(bi_gram_x[k])

#和集合求める
x_or_y=bi_gram_y+x_minus_y

#結果表示
print("xのbi_gram：",bi_gram_x)
print("yのbi_gram：",bi_gram_y)
print()
print("和集合：",x_or_y)
print("積集合：",x_and_y)
print("差集合：",x_minus_y)
print("se in x：","se" in bi_gram_x) #seがxに含まれるか
print("se in y：","se" in bi_gram_y) #seがyに含まれるか
