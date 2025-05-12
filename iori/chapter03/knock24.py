import knock20
import re
pattern = '\[\[ファイル:(.*?)(?:\||\])'
result = re.findall(pattern, knock20.UK_text)
print(result)
