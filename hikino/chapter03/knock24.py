from knock20 import article
import re

pattern = r"\[\[ファイル:(.*?)(?:\|)"
files = re.findall(pattern, article)
print(files)