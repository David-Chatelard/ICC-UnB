num_fatias, premio = input().split()
num_fatias, premio = [int(num_fatias), int(premio)]
ganhador = ''
L = []

for c in range(num_fatias):
    L.append(c)

for i in range(num_fatias):
    pessoa, fatia = input().split()
    fatia = int(fatia)
    if L[fatia] == premio:
        ganhador = pessoa
    del L[fatia]
        
print(ganhador)

