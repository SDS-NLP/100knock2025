def n_gram(sentence, W_or_L, n):
    if W_or_L == "W":
        sentence = sentence.split(" ")
    result = []
    for i in range(len(sentence)-n+1):
        result.append(sentence[i:i+n])
    return(result)

a = "I am an NLPer"
print(n_gram(a, "L", 3))
print(n_gram(a, "W", 2))


    
