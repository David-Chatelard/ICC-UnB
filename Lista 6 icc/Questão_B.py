num_convidados = int(input())
convidados = []

for i in range(num_convidados):
    convidado = input()
    convidados.append(convidado)

if 'André' in convidados:
    print('Cuidado!')
else:
    print('Seguro!')
