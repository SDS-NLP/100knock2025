import spacy
from spacy import displacy


nlp = spacy.load("ja_ginza")
doc = nlp("メロスは激怒した。")

displacy.serve(doc, style="dep", port=5000)
