A = float(input())
B = float(input())
C = float(input())

if B >= A and B >= C:
    A,B = B,A
elif C >= A and C >= B:
    C,A = A,C
    
if A >= (B + C):
    print('NAO FORMA TRIANGULO')
    
elif (A**2) == ((B**2) + (C**2)):
    print('TRIANGULO RETANGULO')
    
elif A == B == C:
    print(' TRIANGULO EQUILATERO')
    
elif (A == B) or (A == C) or (A == C):
    print('TRIANGULO ISOSCELES')
    
else:
    print('TRIANGULO ACUTANGULO OU OBTUSANGULO')
    
