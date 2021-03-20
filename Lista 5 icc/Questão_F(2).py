frase = input().lower()
sobras = input().lower()
pc = ''
d = ''

for letras in frase:
    if letras in 'john':
        pc += letras

for let in sobras:
    if let in 'john':
        d += let

c = (len(pc)-len(d))

print(c, len(d))

