def create_bigram(s):
    return [s[i:i + 2] for i in range(len(s) - 1)]

str_x = "paraparaparadise"
str_y = "paragraph"


X = set(create_bigram(str_x))
Y = set(create_bigram(str_y))


union_xy = X | Y 
intersection_xy = X & Y  
difference_xy = X - Y  


se_in_x ='se' in X
se_in_y ='se' in Y


print("X と Y の和集合:", union_xy)
print("X と Y の積集合:", intersection_xy)
print("X と Y の差集合:", difference_xy)
print("'se' が X に含まれるか:", se_in_x)
print("'se' が Y に含まれるか:", se_in_y)