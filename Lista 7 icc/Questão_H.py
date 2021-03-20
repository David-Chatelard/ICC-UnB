num_jogadas = int(input())
lista = []

for _ in range(num_jogadas):
    nome, jogada = input().split()
    jogada = int(jogada)
    lista.append((nome, jogada))

play = lista[-1][1]

while lista[play-1][1] != num_jogadas:
    play = lista[play-1][1]

print(lista[play-1][0])
