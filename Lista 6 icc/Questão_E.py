tamanho_matriz = int(input())
matriz = []

for c in range(tamanho_matriz):
    matriz.append(c)

for i in range(len(matriz)):
    matriz[i] = input().split()

for a in range(len(matriz)+1):
    for l in range(len(matriz)):
        if a == 0:
            if matriz[len(matriz)-2][l] == 'o':
                if matriz[len(matriz)-1][l] == '.':
                    matriz[len(matriz)-2][l] = '.'
                    matriz[len(matriz)-1][l] = 'o'
        elif a > 2 :
            if matriz[len(matriz)-a][l] == 'o':
                if matriz[len(matriz)-(a-1)][l] == '.':
                    matriz[len(matriz)-a][l] = '.'
                    matriz[len(matriz)-(a-1)][l] = 'o'

for b in range(len(matriz)):
    for k in range(len(matriz)):
        if k == (len(matriz)-1):
            print(matriz[b][k])
        else:
            print(matriz[b][k], end = ' ')
