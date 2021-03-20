valor_inicial = int(input())
cedula_100 = valor_inicial//100
valor_pos100 = valor_inicial%100
cedula_50 = valor_pos100//50
valor_pos50 = valor_pos100%50
cedula_20 = valor_pos50//20
valor_pos20 = valor_pos50%20
cedula_10 = valor_pos20//10
valor_pos10 = valor_pos20%10
cedula_5 = valor_pos10//5
valor_pos5 = valor_pos10%5
cedula_2 = valor_pos5//2
valor_pos2 = valor_pos5%2
cedula_1 = valor_pos2//1
print(valor_inicial)
print(cedula_100, 'nota(s) de R$ 100,00')
print(cedula_50, 'nota(s) de R$ 50,00')
print(cedula_20, 'nota(s) de R$ 20,00')
print(cedula_10, 'nota(s) de R$ 10,00')
print(cedula_5, 'nota(s) de R$ 5,00')
print(cedula_2, 'nota(s) de R$ 2,00')
print(cedula_1, 'nota(s) de R$ 1,00')

      
