word_1: str = "paraparaparadise"
word_2: str = "paragraph"
number: int = int(input("n -> "))
tri_gram: list[str]
bi_gram: list[str]

def n_gram(sequence: str, n: int) -> list[str]:
    result: list[str] = []

    for i in range(len(sequence)-n+1):
        result.append(sequence[i:i+n])

    return result

set_1 = set(n_gram(word_1, number))
set_2 = set(n_gram(word_2, number))

union = set_1 | set_2
intersection = set_1 & set_2
difference = set_1 - set_2

print(f"和集合: {union}")
print(f"積集合: {intersection}")
print(f"差集合: {difference}")

print(f"seはXに含まれる： {"se" in set_1}")
print(f"seはYに含まれる： {"se" in set_2}")