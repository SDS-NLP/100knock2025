from knock54 import right_answer, results

n = 0
for i in range(len(results)):
  if results[i][3] == right_answer[i]:
    n += 1

acc = n/len(results)

print(acc)


