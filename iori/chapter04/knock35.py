import spacy
from spacy import displacy

text = "メロスは激怒した。"

nlp = spacy.load("ja_ginza")
doc = nlp(text)

# SVG形式でレンダリング
svg = displacy.render(doc, style="dep", options={"compact": True, "color": "blue", "bg": "#ffffff"})

# SVGファイルとして保存
with open("dependency.svg", "w", encoding="utf-8") as f:
    f.write(svg)


