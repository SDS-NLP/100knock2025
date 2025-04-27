#関数cipherを作る
def cipher(s):
    
    a = []
    for ele in s:
        if ele.islower():
            x = ord(ele)
        else:
            x = ele
        a.append(x)
    #連続した文字列で返答
    for ele in a:
        print(ele, end = "")
    #リストで返答
    return a
print(cipher('tokyo2020'))
