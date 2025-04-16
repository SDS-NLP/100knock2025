#水平リーベ僕の船
text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
num = [1, 5, 6, 7, 8, 9, 15, 16, 19]
text = text.replace(".", "")
ans = {}
for i,j in enumerate(text.split()):
    if i+1 in num:
        ans[j[0]] = i+1 
    else:
        ans[j[0:2]] = i+1
print(ans)



