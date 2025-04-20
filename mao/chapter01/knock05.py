def n_gram(n,str): #与シーケンスからn-gram作る関数
    answer=[]
    for s in range(len(str)-n+1):
        answer.append(str[s:s+n])
    return answer

text="I am an NLPer"

#結果表示
print("tri-gram：",n_gram(3,text.replace(" ","")))  #文字tri-gram
print("bi-gram：",n_gram(2,text.split()))           #単語bi-gram




