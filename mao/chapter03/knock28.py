"""
27の処理に加えてmテンプレートの値からMediaWikiマークアップを可能は限り
除去し、国の基本情報を整形せよ
"""
import re
from knock27 import inf_dic3

inf_dic4={}
for key, text in inf_dic3.items():
    # HTMLタグの除去
    text=re.sub(r'<.*?>', '', text)
    # 言語テンプレートの除去（例: {{lang|en|England}} → England）
    text=re.sub(r'\{\{lang\|[^|]+\|([^}]+)\}\}', r'\1', text)
    # その他テンプレートの除去（簡易的に）
    text=re.sub(r'\{\{(?:[^{}]*?\|)*([^{}]*?)\}\}', r'\1', text)
    
    inf_dic4[key] = text

#結果確認
#for k, v in inf_dic4.items():
    #print(f"{k}: {v}")
