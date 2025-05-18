from knock20 import uk_article_txt
from knock25 import inf_dic
import re

inf_dic_no_markup = {}

for key, text in inf_dic.items():
  inf_dic_no_markup[key] = re.sub(r'(\\\'){2,5}' , '', text)

print(inf_dic_no_markup)

"""
r は生文字列（raw string）を示します。これにより、バックスラッシュ（\）がエスケープされずにそのまま扱われます。
\\\' は、バックスラッシュとシングルクォートの組み合わせを表します。具体的には、\\ はバックスラッシュを表し、\' はシングルクォートを表します。
( ... ) はキャプチャグループを作成します。この部分に一致した文字列は後で参照することができますが、ここでは特に参照する必要はありません。
{2,5} は、直前のパターン（この場合は \\\'）が2回から5回繰り返されることを意味します。つまり、2つから5つのバックスラッシュとシングルクォートの組み合わせに一致します。
"""