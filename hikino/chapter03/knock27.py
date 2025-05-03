from knock20 import article
import re
import mwparserfromhell

pattern = r"基礎情報 (.*?<references/>)"
base_info = re.findall(pattern, article, flags=re.DOTALL)
base_info = base_info[0]

pattern2 = r"\|(.*?)(?: = | =)(.*?)\n"
items = re.findall(pattern2, base_info)

results = {}

for title, content in items:
    content = re.sub(r"'{2,5}", "", content)

    wikicode = mwparserfromhell.parse(content)
    for link in wikicode.filter_wikilinks():
        parts = str(link).split("|")
        if len(parts) >= 3:
          replacement = parts[-1].rstrip("]]")
        elif "|" in str(link):
            replacement = str(link.text)
        else:
            replacement = str(link.title)
        wikicode.replace(link, replacement)

    results[title.strip()] = str(wikicode).strip()

print(results)