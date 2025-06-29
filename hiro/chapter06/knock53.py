import os
from gensim.models import KeyedVectors

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'GoogleNews-vectors-negative300.bin')

model = KeyedVectors.load_word2vec_format(
    model_path,
    binary=True
)

similar_words = model.most_similar(
    positive=['Spain', 'Athens'],
    negative=['Madrid'],
    topn=10
)

if __name__ == "__main__":
    for i, (word, similarity) in enumerate(similar_words, 1):
        print(f"No.{i:2}   {word:20} : {similarity}")