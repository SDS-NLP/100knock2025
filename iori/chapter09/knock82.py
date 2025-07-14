from transformers import BertTokenizer
from transformers import BertForMaskedLM
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

model = BertForMaskedLM.from_pretrained('bert-base-uncased')

# Encode the input text
input_text = "The movie was full of [MASK]."
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Get the index of the [MASK] token
mask_token_index = torch.where(input_ids == tokenizer.mask_token_id)[1]

# Predict the tokens for the [MASK]
with torch.no_grad():
    output = model(input_ids)

# Get the logits for the [MASK] token
mask_token_logits = output.logits[0, mask_token_index, :]

# Get the top 10 tokens and their probabilities
top_10_tokens = torch.topk(mask_token_logits, 10, dim=1)
top_10_ids = top_10_tokens.indices[0].tolist()
top_10_probs = torch.softmax(mask_token_logits, dim=1)[0, top_10_ids].tolist()

# Decode the tokens and print them with their probabilities
for token_id, prob in zip(top_10_ids, top_10_probs):
    token = tokenizer.decode([token_id])
    print(f"{token}: {prob:.4f}")