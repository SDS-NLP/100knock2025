def cipher(x):
    ciphersentence = ''
    for i in x:
        if i.islower() == True:
            ciphersentence += chr(219 - ord(i))
        else:
            ciphersentence += i
    return(ciphersentence)

print(cipher('hello world'))
