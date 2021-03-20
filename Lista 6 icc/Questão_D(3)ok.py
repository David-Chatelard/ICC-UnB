n = int(input())
lista = []
original = []
diferente = 0

brinquedo = input().split()

for v1 in brinquedo:
    lista.append(v1)
    original.append(v1)

for v2 in range(5):
    b, d, q = input().split()
    q = int(q)
    for v3 in range(q):
        x = lista.index(b)
        if d == 'D' and x < len(lista)-1:
            lista[x], lista[x+1] = lista[x+1], lista[x]
        elif d == 'E' and x > 0:
            lista[x], lista [x-1] = lista[x-1], lista[x]

for v4 in range(len(original)):
    if original[v4] != lista[v4]:
        diferente += 1

print(diferente)
            
