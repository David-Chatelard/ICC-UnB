num_movimentos = int(input())

plano = []

norte = []
sul = []
leste = []
oeste = []

for i in range(num_movimentos):
    direcao, passos = input().split()
    passos = int(passos)
    dupla = direcao, passos
    plano.append(dupla)

for b in range(len(plano)):
    if plano[b][0] == 'N':
        norte.append(plano[b][1])        
    elif plano[b][0] == 'S':
        sul.append(plano[b][1])        
    elif plano[b][0] == 'L':
        leste.append(plano[b][1])        
    elif plano[b][0] == 'O':
        oeste.append(plano[b][1])

norte = sum(norte)
sul = sum(sul)
leste = sum(leste)
oeste = sum(oeste)

if norte > sul:
    sul = norte - sul
    norte = 0
else:
    norte = sul - norte
    sul = 0

if oeste > leste:
    leste = oeste - leste
    oeste = 0
else:
    oeste = leste - oeste
    leste = 0

print(norte, sul, leste, oeste)
