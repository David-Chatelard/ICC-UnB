frase = input().split('. ')
resposta = ''

for i in range(len(frase)):
    resposta = frase[i].capitalize()
    if i != len(frase) - 1:
        print(resposta, end = '. ')
    else:
        print(resposta)
