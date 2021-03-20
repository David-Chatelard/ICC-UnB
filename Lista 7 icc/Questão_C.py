num_problemas = int(input())

tupla = ()

dificuldades = []

for i in range(num_problemas):
    problema, solucao, dificuldade = input().split()
    dificuldade = int(dificuldade)
    tupla += problema, solucao, dificuldade
    

for c in range(2, len(tupla), 3):
    dificuldades.append(tupla[c])

dificuldades = sorted(dificuldades, reverse = True)

for b in dificuldades:
    print(tupla[tupla.index(b)-1], end = '')
    
    
        
        
        
