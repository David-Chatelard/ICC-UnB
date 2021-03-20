quantidade = soma = 0
L = []
x = int(input())

if x != 0:
    while x != 0:
        quantidade += 1
        soma += x
        L.append(x)
        x = int(input())
    print(quantidade)
    print(max(L))
    print('%.2f'%(soma/(quantidade)))
else:
    print(0)
    print(0)
    print('%.2f'%0)
