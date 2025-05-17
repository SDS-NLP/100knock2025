import random

text=str(input())
words=text.split() #単語に分割する

word=""
shuffle_list=[]    #shuffle用
answer=""          #答え格納

random.seed(0)
for i in range(len(words)):
    if len(words[i])>4:     #4文字以上のものは単語の順序並び替える
        word=words[i][1:-1]  #先頭と末尾消去
        shuffle_list=list(word)
        random.shuffle(shuffle_list)  #リスト型に変換しシャッフル
        answer+=words[i][0]+''.join(shuffle_list)+words[i][-1]+" "
    else:                    #4文字以下のものはそのまま
        answer+=words[i]
        answer+=" "

print(answer)



"""
andom.seed(0)
for i in range(len(words)):
    if len(words[i])>=5:     #4文字以上のものは単語の順序並び替える
        word=words[i][1:-1]  #先頭と末尾消去
        shuffle_list=list(word)
        random.shuffle(shuffle_list)  #リスト型に変換しシャッフル
        answer+=''.join(shuffle_list)
        answer+=" "
    else:                    #4文字以下のものはそのまま
        answer+=words[i]
        answer+=" "

print(answer)
"""