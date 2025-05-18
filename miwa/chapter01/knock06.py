#06.集合
def n_gram(sequence,n):
    answer=[]
    for i in range(len(sequence)-n+1):
        answer.append(sequence[i:i+n])
    return answer

X=set(n_gram("paraparaparadise",2))
Y=set(n_gram("paragraph",2))
#print(X,Y)

#和集合、積集合、差集合
union_XY = X|Y
intersection_XY = X & Y
difference_XY = X - Y

print("和集合:",union_XY)
print("積集合:",intersection_XY)
print("差集合:",difference_XY)

#seが含まれるかどうか
se_in_X = "se" in X
se_in_Y = "se" in Y

print("'se' in X :",se_in_X)
print("'se' in Y :",se_in_Y)