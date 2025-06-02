from gensim.models import KeyedVectors

model_path = 'GoogleNews-vectors-negative300.bin'

# Load the pre-trained word vectors
print("Loading word vectors...")
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("Word vectors loaded.")

analogy_file = 'questions-words.txt'  

# Open the analogy file and process the capital-common-countries section
output_file = 'capital_common_countries_results.txt'
with open(analogy_file, 'r') as f, open(output_file, 'w') as out_f:
    in_section = False
    for line in f:
        line = line.strip()
        if line.startswith(':'):
            in_section = line.lower() == ': capital-common-countries'
            continue

        if in_section:
            words = line.split()
            if all(word in model for word in words):
                # Perform the vector calculation
                result_vector = model[words[1]] - model[words[0]] + model[words[2]]
                # Find the most similar word
                most_similar = model.most_similar([result_vector], topn=1)[0]
                # Write the result to the output file
                out_f.write(f"{line} -> {most_similar[0]} ({most_similar[1]:.4f})\n")