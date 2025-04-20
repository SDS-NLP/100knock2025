sentence: str = "I am an NLPer"
number: int = int(input("n -> "))
tri_gram: list[str]
bi_gram: list[str]

def n_gram(sequence: str, n: int) -> list[str]:
    result: list[str] = []

    for i in range(len(sequence)-n+1):
        result.append(sequence[i:i+n])

    return result

tri_gram = n_gram(sentence, number)
print(f"tri-gram: {tri_gram}")

words = sentence.split(" ")
bi_gram = n_gram(words, number)
print(f"bi-gram: {bi_gram}")