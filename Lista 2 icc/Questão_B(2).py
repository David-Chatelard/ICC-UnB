p = float(input())
h = float(input())
imc = p/(h**2)

if imc < 18.5:
    print('%.2f'%imc)
    print('Baixo peso')
if 18.5 < imc < 24.9:
    print('%.2f'%imc)
    print('Peso normal')
if 24.9 < imc < 29.9:
    print('%.2f'%imc)
    print('Sobrepeso')
    p2 = 24.9*(h**2)
    p3 = p - p2
    print('%.2f'%p3)
if 29.9 < imc < 34.9:
    print('%.2f'%imc)
    print('Obesidade de grau I')
    p2 = 24.9*(h**2)
    p3 = p - p2
    print('%.2f'%p3)
if 34.9 <  imc < 39.9:
    print('%.2f'%imc)
    print('Obesidade de grau II')
    p2 = 24.9*(h**2)
    p3 = p - p2
    print('%.2f'%p3)
if imc > 39.9:
    print('%.2f'%imc)
    print('Obesidade de grau III')
    p2 = 24.9*(h**2)
    p3 = p - p2
    print('%.2f'%p3)
