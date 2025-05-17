#08.暗号文
def cipher(text):
    result=""
    for c in text:
        if c.islower():
            result += chr(219-ord(c))
        else:
            result += c
    return result

str1="I am an NLPer"
str2=cipher(str1)
str3=cipher(str2)
print("暗号化:",str2)
print("復号化:",str3)