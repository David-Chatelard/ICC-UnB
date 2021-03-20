x = float(input())
y = float(input())
z = float(input())

if x >= y and x >= z:
    a = x
    b = y
    c = z
if y >= x and y >= z:
    a = y
    b = x
    c = z
if z >= x and z >= y:
    a = z
    b = x
    c = y

if a >= (b+c):
    print('NAO FORMA TRIANGULO')
elif a**2 == b**2 + c**2:
    print('TRIANGULO RETANGULO')
elif a == b == c:
    print('TRIANGULO EQUILATERO')
elif a == b or a == c or b == c:
    print('TRIANGULO ISOSCELES')
else:
    print('TRIANGULO ACUTANGULO OU OBTUSANGULO')
    
