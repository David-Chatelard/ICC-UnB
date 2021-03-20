num_produtos = int(input())
produtos = []

for i in range(num_produtos):
    produto = input()
    produtos.append(produto)

ordem = ', '.join(produtos[::-1])

print(ordem)
