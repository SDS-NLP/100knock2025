#この暗号化で小文字アルファベットが反転する

text = 'Highway to the danger zone'

def cipher(text):
    ans = ''
    for i in text:
        if i.islower():
            ans += chr(219 - ord(i))
        else:
            ans += i
    return ans

print(cipher(text))
print(cipher(cipher(text)))