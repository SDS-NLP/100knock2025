def cipher(s):
    return ''.join([chr(219 - ord(c)) if c.islower() else c for c in s])


message = "Hello, World!"
print("暗号化後:", cipher(message)) 
print("復号化後:", cipher(cipher(message)))  