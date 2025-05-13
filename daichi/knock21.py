import knock20
import re
pattern = "\[\[Category:.*?\]\]"
category = re.findall(pattern, knock20.uk_text)
print(category)