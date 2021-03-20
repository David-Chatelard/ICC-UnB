frase = input().split('. ')

for i in range(len(frase)):
    if i != len(frase) - 1:
        print(frase[i].capitalize(), end = '. ')
    else:
        print(frase[i].capitalize())
