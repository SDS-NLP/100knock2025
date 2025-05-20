import re

def remove_internal_links(value):
    return re.sub(r'\[\[([^|]*?)\|?([^]]*?)\]\]', r'\2' if r'\2' else r'\1', value)

cleaned_data_27 = {k: remove_internal_links(v) for k, v in cleaned_data_26.items()}
print(cleaned_data_27)