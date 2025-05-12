import knock28 
import requests
S = requests.Session()
url = "https://ja.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "format": "json",
    "titles": "File:" + knock28.inf_dic4["国旗画像"],
    "prop": "imageinfo",
    "iiprop": "url"
}

response = S.get(url=url, params=params)
data = response.json()

pages = data['query']['pages']
for page in pages.values():
    image_url = page['imageinfo'][0]['url']
    print(image_url)