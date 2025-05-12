#28. MediaWikiマークアップの除去
import json
import re
path="jawiki-country.json"

uk_text=None
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        article=json.loads(line)
        if article["title"]=="イギリス":
            uk_text = article["text"]
            break

#基礎情報テンプレート全体を抽出
pattern=r"\{\{基礎情報.*?\n(.*?)\n\}\}" 
result1 = re.findall(pattern, uk_text,re.DOTALL)
#print(result)

#フィールド名と値を抽出
pattern=r"\|(.*?)\s*=\s*(.*?)(?=\n\|)" 
result1[0] += "\n|" #最後の項目の後ろを他の項目と同じにする
result2 = re.findall(pattern, result1[0], re.DOTALL)
information= {}
for i,j in result2:
    information[i] = j

#強調マークアップ除去
for k, v in information.items():
    information[k]=re.sub(r"\'{2,5}", "", v)

#内部リンク除去
#関数を作る
def clean_internal_links(text):
    def replace_link(match):
        link = match.group(1)
        # ファイルやカテゴリは除外
        if link.startswith(("ファイル:", "Category:")):
            return match.group(0)  # 元のまま返す
        # 表示名がある場合はそれだけ使う
        if '|' in link:
            return link.split('|')[-1]
        else:
            return link

    return re.sub(r"\[\[(.*?)\]\]", replace_link, text)

# 適用
for k, v in information.items():
    cleaned = clean_internal_links(v)
    information[k] = cleaned

    pattern = r"\{\{lang\|.*?\|"
    information[k] = re.sub(pattern, "", information[k])

    #<ref>で囲まれている部分を削除
    pattern = r"\<ref.*?\>.*?\<\/ref\>"
    information[k] = re.sub(pattern, "", information[k])

    #<ref><br />単体を削除
    pattern = r"\<ref.*?\>|\<br \/\>|\<\/ref\>"
    information[k] = re.sub(pattern, "", information[k])
    
    #箇条書きに対する処理
    pattern = r"\*{2}"
    information[k] = re.sub(pattern, "\t・", information[k])
    pattern = r"\*{1}"
    information[k] = re.sub(pattern, "・", information[k])

    pattern = r"\{\{center\|"
    information[k] = re.sub(pattern, "", information[k])

    pattern = r"\{\{仮リンク\|.*?\|.{2}\|"
    information[k] = re.sub(pattern, "", information[k])

    pattern = r"\}\}|\{\{"
    information[k] = re.sub(pattern, "", information[k])

    print(f'{k} : {information[k]}')
