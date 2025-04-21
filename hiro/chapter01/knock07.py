def variable2sentence(x, y, z) -> str:
    return(str(x) + "時の" + str(y) + "は" + str(z))

x = 12
y = "気温"
z = 22.4

print(variable2sentence(x, y, z))