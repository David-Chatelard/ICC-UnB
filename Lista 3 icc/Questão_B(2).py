quant = soma = maior = 0
#tem q ver como definir o maior pra dar certo com numero negativo
#tem q ver como arrumar pro 1 x ser 0
while True:
    x = int(input())
    if x == 0:
        break
    if x >= maior:
        maior = x
    quant += 1
    soma += x
    
media = soma/quant

print(quant)
print(maior)
print('%.2f'%media)

