#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ。この関数を用い、”I am an NLPer”という文から文字tri-gram、単語bi-gramを得よ。

text = "I am an NLPer"

def n_gram(sequence, n):
    return [sequence[i:i+n] for i in range(len(sequence)-n+1)]

print('文字tri-gram:', n_gram(text, 3))
print('単語bi-gram:', n_gram(text.split(), 2))