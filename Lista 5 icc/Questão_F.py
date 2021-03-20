total = input().lower()
resto = input().lower()
comidas = ''
num_comidas = 0
deixadas = 0

for i in range(len(total)):
    if not total[i] in resto:
        comidas += total[i]

for c in range(len(comidas)):
    if comidas[c] == 'j':
        num_comidas += 1
    elif comidas[c] == 'o':
        num_comidas += 1
    elif comidas[c] == 'h':
        num_comidas += 1
    elif comidas[c] == 'n':
        num_comidas += 1

for b in range(len(resto)):
    if resto[b] == 'j':
        deixadas += 1
    elif resto[b] == 'o':
        deixadas += 1
    elif resto[b] == 'h':
        deixadas += 1
    elif resto[b] == 'n':
        deixadas += 1

print(num_comidas, end = ' ')
print(deixadas)
