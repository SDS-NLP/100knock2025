"""
knock37:名詞の出現頻度
コーパスにおける名詞の出現頻度を求め、
出現頻度の高い20語とその出現頻度を表示せよ
"""
from knock36 import cleaned_texts
import fugashi
from collections import Counter

tagger=fugashi.Tagger() #形態素解析器作成
nouns_list=[]           #名詞のコーパス,knock38用
non_counter=Counter()   #名詞の出現頻度カウント用

for title,text in cleaned_texts:
    for word in tagger(text):
        if word.feature.pos1=="名詞": 
        #数字除外するときは and not word.surface.isdigit():追加
            nouns_list.append((title,word))
            non_counter[word.surface]+=1

if __name__=="__main__":
    print("名詞の出現頻度 上位20位：")
    for word,freq in non_counter.most_common(20):
        print(f"{word}:{freq}")

