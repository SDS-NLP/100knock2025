words = sentence.split()  # スペースで単語に分割

# 特殊な位置（1-based index）
special_positions = {1, 5, 6, 7, 8, 9, 15, 16, 19}

element_dict = {}
for idx, word in enumerate(words, start=1):  # idxは1から始まる位置
    # 単語から記号（句点など）を除去（末尾の句点のみ想定）
    cleaned_word = word.rstrip('.')  # 例："Fluorine." → "Fluorine"
    
    if idx in special_positions:
        key = cleaned_word[0]  # 先頭1文字
    else:
        key = cleaned_word[:2]  # 先頭2文字
    
    element_dict[idx] = key

print(element_dict)