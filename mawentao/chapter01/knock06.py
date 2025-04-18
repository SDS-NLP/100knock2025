#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#06. 集合
strlong = 'paraparaparadise'
strshort = 'paragraph'
def bi_gram(sequence, n):
    return [sequence[i:i + n] for i in range(len(sequence) - n + 1)]

bi_gram_l = bi_gram(strlong,2)
bi_gram_s = bi_gram(strshort,2)


set_long = set(bi_gram_l)
set_short = set(bi_gram_s)

common = set_long & set_short
union = set_long | set_short
diff = set_long - set_short

import re

def find_se(bi_gram):
  for sequence in bi_gram:
    target = re.findall(r'se', sequence)
    if target:
        return True
  else:
    return False

print(bi_gram_l)
print(bi_gram_s)
print(common)
print(union)
print(diff)
print(find_se(bi_gram_l))
print(find_se(bi_gram_s))

