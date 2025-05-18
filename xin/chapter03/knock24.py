import json
import gzip
import re
from knock20 import uk_data
pattern=r"(?:File|ファイル):(.+?)\|"
media_files=re.findall(pattern,uk_data())
print("\n".join(media_files))
