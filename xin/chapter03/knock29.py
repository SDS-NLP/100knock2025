import requests
from knock20 import uk_data
from knock25 import extract_template
from knock26 import remove_emphasis
from knock27 import remove_internal_links
from knock28 import remove_markup

# Wikipedia本文を取得
uk_text = uk_data()

# 基礎情報を抽出・整形
info_dict = extract_template(uk_text)
info_dict = remove_emphasis(info_dict)
info_dict = remove_internal_links(info_dict)
info_dict = remove_markup(info_dict)

# 国旗画像ファイル名を取得
flag_filename = info_dict.get('国旗画像')
if not flag_filename:
    print("国旗画像が見つかりません")
    exit()

title = "File:" + flag_filename

# Wikipedia APIで画像情報を取得
url = "https://commons.wikimedia.org/w/api.php"
params = {
    'action': 'query',
    'titles': title,
    'prop': 'imageinfo',
    'iiprop': 'url',
    'format': 'json'
}

response = requests.get(url, params=params)
data = response.json()

# URLを取り出して表示
pages = data.get('query', {}).get('pages', {})
for page in pages.values():
    if 'imageinfo' in page:
        print(page['imageinfo'][0]['url'])
    else:
        print("画像情報が見つかりません")
