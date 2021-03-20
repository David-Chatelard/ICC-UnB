p = float(input())
h = float(input())
imc = p/(h**2)

print('%.2f'%imc)

if imc < 18.5:
    print('Baixo peso')
if 18.5 < imc < 24.9:
    print('Peso normal')
if 24.9 < imc < 29.9:
    print('Sobrepeso')
if 29.9 < imc < 34.9:
    print('Obesidade grau I')
if 34.9 <  imc < 39.9:
    print('Obesidade grau II')
if imc > 39.9:
    print('Obesidade grau III')
if imc > 24.9:
    p2 = 24.9*(h**2)
    p3 = p - p2
    print('%.2f'%p3)
    
