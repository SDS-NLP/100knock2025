"""
knock35: 係り受け木
「メロスは激怒した。」の係り受け木を可視化せよ。
"""
import spacy
from spacy import displacy

text="メロスは激怒した。"

#GiNZAモデルの読み込み・テキスト解析
nlp=spacy.load("ja_ginza")
doc=nlp(text)

#係り受け木をブラウザで可視化
html = displacy.render(doc, style="dep", options={"compact": True, "font_size": 16})
with open("dependency_tree.html", "w", encoding="utf-8") as f:
    f.write(html)

#htmlをブラウザで開いて係り受け木を確認
print("dependency_tree.html")


