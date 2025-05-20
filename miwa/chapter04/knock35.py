#係り受け木
import spacy
from spacy import displacy

# GiNZAのモデルを読み込む
nlp = spacy.load("ja_ginza")

# 対象の文
text = "メロスは激怒した。"
doc = nlp(text)

# 描画
displacy.serve(doc, style="dep", options={"compact": True, "font": "Noto Sans JP"})
