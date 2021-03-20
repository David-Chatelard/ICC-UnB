texto = input()
resposta = ''

for i in range(len(texto)):
    if texto[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        resposta += 'U'
    elif texto[i] in 'qwertyuiopasdfghjklzxcvbnm':
        resposta += 'L'
    elif texto[i] in '0123456789':
        resposta += 'D'
    else:
        resposta += 'W'

print(resposta)
        
