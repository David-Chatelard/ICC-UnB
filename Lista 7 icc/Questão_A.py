num_palavras_criticas = int(input())

palavras_criticas = {}
c = 0

for i in range(num_palavras_criticas):
    palavra_critica, personalidade = input().split()
    palavras_criticas[palavra_critica] = personalidade

frase = input().split()

for palavra in frase:
    if palavra in palavras_criticas:
        print(palavras_criticas[palavra], end = ' ')
    elif palavra not in palavras_criticas:
        c += 1
if c == len(frase):
    print('Tudo bem!')
