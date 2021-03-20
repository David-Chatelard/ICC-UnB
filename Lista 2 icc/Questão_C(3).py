x = float(input())
y = float(input())
z = float(input())

if x >= y >= z or x >= z >= y:
    a = x
    b = y
    c = z
if y >= x >= z or y >= z >= x:
    a = y
    b = x
    c = z
if z >= x >= y or z >= y >= x:
    a = z
    b = x
    c = y

if a >= (b+c):
    print('NAO FORMA TRIANGULO')
elif a**2 == b**2 + c**2:
    print('TRIANGULO RETANGULO')
elif a == b == c:
    print('TRIANGULO EQUILATERO')
elif a == b:
    print('TRIANGULO ISOSCELES')
elif b == c:
    print('TRIANGULO ISOSCELES')
elif a == c:
    print('TRIANGULO ISOSCELES')
else:
    print('TRIANGULO ACUTANGULO OU OBTUSANGULO')
    
