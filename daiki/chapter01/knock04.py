s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
a = list(s.split())
A = {}
for i in range(len(a)):
    if i == 0 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 14 or i == 15 or i == 18:
        A[a[i][0]] = i+1 
    else:
        A[a[i][:2]] = i+1
print(A)
