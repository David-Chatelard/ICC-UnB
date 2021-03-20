lista1 = list(input().split())
lista1 = list(map(lambda x: x.lower(), lista1))
ordem = sorted(lista1)
if lista1 == ordem:
    print('B')
else:
    print('A')
