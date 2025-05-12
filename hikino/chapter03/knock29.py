from knock28 import results

image_flag = results["国旗画像"]
print(image_flag)

import requests


S = requests.Session()
URL = "https://ja.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "File:" + image_flag,
    "prop": "imageinfo",
    "iiprop": "url"
}

response = S.get(url=URL, params=PARAMS)
data = response.json()
print(data)

pages = data['query']['pages']
for page in pages.values():
    image_url = page['imageinfo'][0]['url']
    print(image_url)
