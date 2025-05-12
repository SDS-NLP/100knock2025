#!/usr/bin/env python
# coding: utf-8

# In[ ]:


with open('/Users/niaomuqing/Downloads/popular-names.txt', 'r', encoding='utf-8')  as f:
    lines = f.readlines()

total_lines = len(lines)
N = 10  
lines_per_file = total_lines // N
for i in range(N):
    start = i * lines_per_file
    if i == N - 1:
        end = total_lines
    else:
        end = (i + 1) * lines_per_file

    split_lines = lines[start:end]

#split -l 278 /Users/niaomuqing/Downloads/popular-names.txt popular-names_part_

