num_brinquedos = int(input())
ordem_original = input().split()
ordem = ordem_original[:]
mudanças = 0

for i in range(5):
    b, d, q = input().split()
    indice = ordem.index(b)
    for c in range(int(q)):
        if d == 'D':
            ordem[indice], ordem[indice+1] = ordem[indice+1], ordem[indice]
            indice += 1
        else:
            ordem[indice-1], ordem[indice] = ordem[indice], ordem[indice-1]
            indice -= 1

for k in range(num_brinquedos):
    if ordem[k] != ordem_original[k]:
        mudanças += 1

print(mudanças)
    
