from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# Sentences
sentences = [
    "The movie was full of fun.",
    "The movie was full of excitement.",
    "The movie was full of crap.",
    "The movie was full of rubbish."
]

# Load pre-trained model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Get embeddings
embeddings = []
for sentence in sentences:
    inputs = tokenizer(sentence, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    # Take the mean of the last hidden state
    embeddings.append(outputs.last_hidden_state.mean(dim=1).squeeze().numpy())

# Compute cosine similarity
for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        similarity = cosine_similarity([embeddings[i]], [embeddings[j]])[0][0]
        print(f"Cosine similarity between '{sentences[i]}' and '{sentences[j]}': {similarity:.4f}")