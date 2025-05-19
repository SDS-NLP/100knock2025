import json
import requests

def load_uk_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            article = json.loads(line)
            if article.get('title') == 'イギリス':
                return article.get('text')
    return None

def extract_basic_info(text):
    in_template = False
    template_lines = []

    for line in text.split('\n'):
        if line.startswith('{{基礎情報'):
            in_template = True
        elif line.startswith('}}') and in_template:
            break
        if in_template:
            template_lines.append(line)

    info_dict = {}
    for line in template_lines:
        if line.startswith('|'):
            parts = line[1:].split(' = ', 1)
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                info_dict[key] = value

    return info_dict


def get_flag_image_url(file_name):
    endpoint = 'https://commons.wikimedia.org/w/api.php'
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'imageinfo',
        'titles': f'File:{file_name}',
        'iiprop': 'url'
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    pages = data.get('query', {}).get('pages', {})
    for page in pages.values():
        if 'imageinfo' in page:
            return page['imageinfo'][0]['url']

    return None


file_path = 'jawiki-country.json'

article_text = load_uk_article(file_path)
basic_info = extract_basic_info(article_text)

flag_file_name = basic_info['国旗画像']
flag_url = get_flag_image_url(flag_file_name)

if flag_url:
    print(flag_url)
