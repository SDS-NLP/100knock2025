"""
knock36:単語出現頻度
まず第3章の処理内容を参考に、Wikipedia記事からマークアップを除去し、
各記事のテキスト出力せよ。そして、コーパスにおける単語(形態素)の出現頻度を求め、
出現頻度の高い20語とその出現頻度を表示せよ。
"""
import json
import re
from collections import Counter
import fugashi

tagger=fugashi.Tagger() #形態素解析器
counter=Counter()       #出現頻度カウント用
cleaned_texts=[]         #マークアップ除去したテキストを格納

filename="mao/chapter04/jawiki-country.json"
with open(filename,encoding="utf-8") as f:
    for line in f:
        article=json.loads(line)
        title=article.get("title","") #knock38用にtitleも取得
        text=article.get("text", "")

        #マークアップを除去
        text=re.sub(r"\'{2,}", "",text)  # 強調
        text=re.sub(r"\[\[.*?\|(.*?)\]\]", r"\1",text) # [[記事名|表示名]]
        text=re.sub(r"\[\[(.*?)\]\]", r"\1",text)      # [[記事名]]
        text=re.sub(r"\{\{.*?\}\}", "",text)           # テンプレート
        text=re.sub(r"\[http[^\s]+\s?(.*?)\]", r"\1",text)  # 外部リンク
        text=re.sub(r"<.*?>", "",text)                 # HTMLタグ
        text=re.sub(r"\{\{.*?\}\}", "",text)           # {{...}}
        text=re.sub(r"\n", " ",text)

        #knock37用にマークアップ除去後のテキスト保存
        #knock38用にtitleも保存
        cleaned_texts.append((title,text))

        for word in tagger(text):
            if word.surface.isalnum(): #記号など除去
                counter[word.surface]+=1
#結果出力
if __name__=="__main__":
    print("出現頻度上位20位:")
    for word,freq in counter.most_common(20):
        print(f"{word}:{freq}")
