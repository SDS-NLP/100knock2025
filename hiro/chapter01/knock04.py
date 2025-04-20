sentence: str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
index: list[int] = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans: dict[str,int] = {}

words: list[str] = sentence.split(" ")

for i, word in enumerate(words):
    if i+1 in index:
        ans[words[i][0]] = i + 1
    else:
        ans[words[i][0:2]] = i + 1

print(ans)