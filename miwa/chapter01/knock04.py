text="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words=text.replace("."," ").split()

result={}

for i in range(len(words)):
    
    if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        key=words[i][0]
    else:
        key=words[i][:2]
    result[key]=i+1

print(result)