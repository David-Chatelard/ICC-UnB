def correctChar(char):
    if char.lower() in 'aeiou ':
        return char
    return 'p'



frase = input()
resposta = ''

for i in range(len(frase)):
    resposta += correctChar(frase[i])

print(resposta)
