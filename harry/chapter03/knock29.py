import json
import requests
import subprocess

# 1. JSONファイルを読み込み
with open('cleaned_infobox.json', 'r', encoding='utf-8') as f:
    infobox_dict = json.load(f)

# 2. 国旗画像のファイル名を取得
flag_filename = infobox_dict.get("国旗画像")

# 3. 画像URLを取得する関数
def get_flag_image_url(filename):
    endpoint = "https://ja.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": f"File:{filename}",
        "iiprop": "url"
    }
    response = requests.get(endpoint, params=params)
    data = response.json()

    pages = data.get('query', {}).get('pages', {})
    for page in pages.values():
        imageinfo = page.get('imageinfo')
        if imageinfo:
            return imageinfo[0]['url']
    return None

# 4. Windows の既定ブラウザで開く関数
def open_in_windows_browser(url):
    subprocess.run(['cmd.exe', '/c', 'start', '', url])

# 5. 画像URLの取得と表示
if flag_filename:
    url = get_flag_image_url(flag_filename)
    if url:
        print(f"🏳️ 国旗画像のURL: {url}")
        open_in_windows_browser(url) 
    else:
        print("❌ 国旗画像のURLを取得できませんでした。")
else:
    print("⚠️ '国旗画像' のフィールドが見つかりませんでした。")
