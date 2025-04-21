def cipher(s):
    
    a = []
    for ele in s:
        if ele.islower():
            x = ord(ele)
        else:
            x = ele
        a.append(x)
    for ele in a:
        print(ele, end = "")
    return a
print(cipher('tokyo2020'))
