#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#08. 暗号文
def cipher(text):
    result = ''
    for c in text:
        if c.islower():
            result += chr(219 - ord(c))
        else:
            result += c
    print(result)

