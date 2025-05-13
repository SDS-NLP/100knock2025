#05.n-gram
def n_gram(sequence,n):
    answer=[]
    for i in range(len(sequence)-n+1):
        answer.append(sequence[i:i+n])
    return answer

str1="I am an NLPer"
#文字tri-gram
tri_gram=n_gram(str1.replace(" ",""),3)
print(tri_gram)

#単語bi-gram
bi_gram=n_gram(str1.split(),2)
print(bi_gram)
    
