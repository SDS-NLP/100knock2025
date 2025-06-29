import spacy
from spacy import displacy

nlp = spacy.load("ja_core_news_sm")
doc = nlp("メロスは激怒した。")

svg = displacy.render(doc, style="dep", jupyter=False, options={
    "compact": True,
    "bg": "#ffffff",
    "font": "IPAexGothic"
})

# SVG をファイル保存
with open("dep_tree.svg", "w", encoding="utf-8") as f:
    f.write(svg)


