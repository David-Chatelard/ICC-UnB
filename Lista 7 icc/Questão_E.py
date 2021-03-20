import string
texto = input().lower()
dic = {}
def limpa(texto):
    res = ''
    for i in range(len(texto)):
        if texto[i] not in string.punctuation or texto[i] == '-':
            res += texto[i]
    return res

texto = limpa(texto)
lista = texto.split()

for palavra in lista:
    if palavra not in dic:
        dic[palavra] = 1
    else:
        dic[palavra] += 1

ordem = sorted(dic.items(), key = lambda x: x[0], reverse = True)
ordem2 = sorted(ordem, key = lambda x: -x[1])

for b in range(len(ordem2)):
    print(ordem2[b][0].capitalize(), ordem2[b][1])


