F = int(input())
Filosofos = {}
Lutas = {}

for i in range(F):
    IdFilo, Nome = input().split()
    Filosofos[IdFilo] = Nome

while True:
    Luta = input().split()
    if 'FINISHHIM' in Luta:
        break
    Filosofos[Luta[0]] = Filosofos[Luta[-1]]
    if Filosofos[Luta[-1]] not in Lutas:
        Lutas[Filosofos[Luta[-1]]] = 1
    else:
        Lutas[Filosofos[Luta[-1]]] += 1

print(Lutas[Filosofos[Luta[-1]]])
