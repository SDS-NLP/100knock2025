"""
国旗画像のURLを取得する
テンプレートの値からMediaWikiマークアップを可能な限り除去し、
国の基本情報を整形せよ
"""
from knock28 import inf_dic4
import requests

filename =inf_dic4['国旗画像']
params = {
    "action": "query",
    "format": "json",
    "titles": f"File:{filename}",
    "prop": "imageinfo",
    "iiprop": "url"
}

res = requests.get("https://commons.wikimedia.org/w/api.php", params=params)
data = res.json()

#URLを取得
pages = data["query"]["pages"]
for page in pages.values():
    print(page["imageinfo"][0]["url"])

