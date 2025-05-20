"""
強調マークアップの除去
25の処理時に、テンプレートの値からMediaWikiの強調マークアップ（弱い強調、強調、強い強調のすべて）
を除去してテキストに変換せよ（参考: マークアップ早見表）。
"""
import re
from knock25 import inf_dic

inf_dic2 = {}
for key, text in inf_dic.items():
  inf_dic2[key] = re.sub(r'(\\\'){2,5}' , '', text)

#結果確認
#for k, v in inf_dic2.items():
  #print(f"{k}: {v}")