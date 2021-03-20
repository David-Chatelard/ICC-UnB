frase = input()

for i in range(len(frase)):
    if i == 0:
        print(frase[i].upper(), end = '')
        
    elif i >= 1 and frase[i-1] == '.':
        print(frase[i].upper(), end ='')
        
    elif i >= 2 and frase[i-2] == '.' and frase[i-1] == ' ':
        print(frase[i].upper(), end = '')
        
    else:
        print(frase[i], end = '')
        
