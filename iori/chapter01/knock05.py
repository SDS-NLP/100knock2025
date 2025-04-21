#n-gramってなんぞ？→nこずつ単語や文字をセットにしたものらしい
text = 'I am an NLPer'

def n_gram(n,word):
    ans = []
    for i in range(len(word)-n+1):
        ans.append(word[i:i+n])
    return ans

print(n_gram(3,text))
print(n_gram(2,text.split()))