
def cipher(text):
    ciphersentence=""
    for c in text:
        if c.islower() == True:
            ciphersentence += chr(219 - ord(c))
        else:
            ciphersentence += c
    return(ciphersentence)

sentence = "I have a pen."
encripted = cipher(sentence)
decripted = cipher(encripted)

print(encripted)
print(decripted)
