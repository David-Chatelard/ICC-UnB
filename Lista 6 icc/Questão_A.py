num_produtos = int(input())
produtos = []

for i in range(num_produtos):
    produto = input()
    produtos.append(produto)

for c in range(len(produtos)):
    if c == 0:
        print(produtos[len(produtos)-1], end = ', ')
    elif 0 < c < (len(produtos)-1):
        print(produtos[len(produtos)-(c+1)], end = ', ')
    else:
        print(produtos[0])
