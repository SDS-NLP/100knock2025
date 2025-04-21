
def template(x,y,z):
    print(str(x)+"時の"+str(y)+"は"+str(z))
    #こっちでも
    print(f'{x}時の{y}は{z}')

x=12
y="気温"
z=22.4

template(x,y,z)