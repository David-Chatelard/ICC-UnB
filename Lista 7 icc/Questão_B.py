n = int(input())

depita = {}

for i in range(n):
    nome, comida = input().split(' ', 1)
    nome = nome.lower()
    depita[nome] = comida
    

print(len(depita))

ordem = sorted(depita.items(), key = lambda x: x[0])

for c in range(len(depita)):
    print(ordem[c][1])
