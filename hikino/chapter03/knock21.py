from knock20 import article
import re

pattern = "\[\[Category:.*?\]\]"
category = re.findall(pattern, article)
print(category)