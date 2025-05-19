import requests
import json

def get_flag_url(file_name):
    api_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url&titles=File:{file_name}"
    response = requests.get(api_url)
    data = json.loads(response.text)
    page_id = next(iter(data['query']['pages'].keys()))
    return data['query']['pages'][page_id]['imageinfo'][0]['url']

flag_file = template_data.get('国旗画像', '')
flag_url = get_flag_url(flag_file)
print(flag_url)