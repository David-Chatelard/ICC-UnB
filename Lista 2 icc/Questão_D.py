a, b = input().split()
a, b = [int(a), int(b)]

if 0 <= a <= 100 and 0 <= b <= 100 :
    if a > b :
        print(a, b, 'errados')
    else:
        print(a, b, 'ok')
    #if b == 0:
        #print(a, b, 'errados')
        #ver se os comentarios acima sao necessarios pq tem no enunciado fala q o ghost sobe pleo menos 1, mas tambem pede para 0 <= a, b <= 100, ai se eu n botar os comentarios acima 0 0 daria ok, mas eu acho que era pra dar errados, mas eu n tenho ctz to confuso, espera sair o corretor da lista 2 e testa pra ver qual fica certo
        
        
    
        
