import knock25
import re
inf_dic2 = {}
for key, text in knock25.infobox.items():
  inf_dic2[key] = re.sub(r'(\\\'){2,5}' , '', text)

print(inf_dic2)