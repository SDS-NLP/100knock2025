# 分からん

from knock20 import uk_article_txt
import re
import mwparserfromhell

pattern = r"基礎情報 (.*?<references/>)"
base_info = re.findall(pattern, uk_article_txt, flags=re.DOTALL)
base_info = base_info[0]

pattern2 = r"\|(.*?)(?: = | =)(.*?)\n"
items = re.findall(pattern2, base_info)

results = {}

for i in range(len(items)):
  tpl = items[i]
  title = tpl[0]
  content = tpl[1]
  wikicode = mwparserfromhell.parse(content)
  cleaned_text = wikicode.strip_code()
  results[f"{title}"] = cleaned_text

if __name__ == "__main__":
  print(results)