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
else:
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    else:
        if a == b == c:
            print('TRIANGULO EQUILATERO')
        else:
            if a == b or b == c or a == c:
                print('TRIANGULO ISOSCELES')
            else:
                print('TRIANGULO ACUTANGULO OU OBTUSANGULO')

    
