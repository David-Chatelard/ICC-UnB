x = int(input())
y = int(input())

def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1
    
r = compare(x, y)

if r == 1:
    print('x e maior que y')
elif r == 0:
    print('x e igual a y')
else:
    print('x e menor que y')
