import requests

def get_flag_image_url(file_name):
    # MediaWiki APIのURL（日本語版Wikipediaを使用）
    api_url = "https://ja.wikipedia.org/w/api.php"

    # APIのパラメータ設定
    params = {
        "action": "query",
        "format": "json",
        "titles": file_name,  # ファイル名（例：File:Flag of the United Kingdom.svg）
        "prop": "imageinfo",
        "iiprop": "url"  # 画像のURLを取得
    }

    # APIリクエストを送信
    response = requests.get(api_url, params=params)
    data = response.json()

    # 結果からURLを抽出
    pages = data.get("query", {}).get("pages", {})
    for page_id, page_data in pages.items():
        if "imageinfo" in page_data:
            image_url = page_data["imageinfo"][0]["url"]
            return image_url
    return None

# 例としてイギリスの国旗画像を取得
file_name = "File:Flag of the United Kingdom.svg"
image_url = get_flag_image_url(file_name)

if image_url:
    print("画像のURL:", image_url)
else:
    print("画像のURLを取得できませんでした。")
