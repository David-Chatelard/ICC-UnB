x = int(input())
y = int(input())

#def compare(x, y): (qual a diferença pra linha de baixo, as duas funcionam)
def compare():
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1
    
r = compare()

if r == 1:
    print('x e maior que y')
elif r == 0:
    print('x e igual a y')
else:
    print('x e menor que y')
