trab = int(input())
lista = []
lista2 = []

for i in range(trab):
    n, t1, t2, t3, t4 = input().split()
    lista.append((n, t1, t2, t3, t4))

pesquisa = input().split()

for b in range(len(lista)):
    for c in range(len(pesquisa)):
        if pesquisa[c] in lista[b][1:]:
            if lista[b] not in lista2:
                print(lista[b][0])
                lista2.append(lista[b])

