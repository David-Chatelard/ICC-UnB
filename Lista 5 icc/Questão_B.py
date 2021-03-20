f = input()
f = f.lower()
f = list(f)
p = 'p'

for i in range(len(f)):
    if f[i] in 'bcdfghjklmnpqrstwxyz':
        f[i] = p

f = ''.join(f)
f = f.capitalize()

print(f)
