"""
内部リンクの除去
26の処理に加えて、テンプレートの値からMediaWikiの内部リンクマークアップ
を除去し、テキストに変換せよ
"""
import re
from knock26 import inf_dic2

inf_dic3={}
for key, text in inf_dic2.items():
  inf_dic3[key]=re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', text)

#結果確認
#for k, v in inf_dic3.items():
    #print(f"{k}: {v}")