text="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
extract_first=[1,5,6,7,8,9,15,16,19] #先頭１文字を抜き出すkey list
words=text.split() #単語に分割
answer={}

for i in range(len(words)):
    if i+1 in extract_first:     #先頭１文字を抜き出す
        answer[i+1]=words[i][0]
    else:                        #先頭２文字を抜き出す
        answer[i+1]=words[i][0:2]
#結果確認
print(answer)


