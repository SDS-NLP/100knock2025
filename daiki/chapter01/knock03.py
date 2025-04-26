s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
a = list(s.split())
numbers = []
for i in range(len(a)):
    if "," in a[i]:
        numbers.append(len(a[i].strip(",")))
    elif "." in a[i]:
        numbers.append(len(a[i].strip(".")))
    else:
        numbers.append(len(a[i]))
print(numbers)
