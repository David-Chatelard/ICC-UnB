import statistics
quant = soma = 0
L = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        L.append(x)
        quant += 1
        soma += x

print(quant)
print(max(L))
print('%.2f'%statistics.mean(L))

