from transformers import BertTokenizer
from transformers import BertForMaskedLM
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

model = BertForMaskedLM.from_pretrained('bert-base-uncased')

text = "The movie was full of [MASK]."
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
    predictions = outputs.logits

mask_token_index = (inputs.input_ids == tokenizer.mask_token_id).nonzero(as_tuple=True)[1]
mask_token_logits = predictions[0, mask_token_index, :]
top_token = torch.argmax(mask_token_logits, dim=1)

predicted_token = tokenizer.decode(top_token)
print(f"The most suitable token for [MASK] is: {predicted_token}")