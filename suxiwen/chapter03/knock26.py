import re

def remove_emphasis(value):
    return re.sub(r"'{2,3}", "", value)

cleaned_data_26 = {k: remove_emphasis(v) for k, v in template_data.items()}
print(cleaned_data_26)