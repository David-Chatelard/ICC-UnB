n = int(input())
x = int(input())

while x != n:
    if x > n:
        print('O número correto é menor.')
    if x < n:
        print('O número correto é maior.')
    x = int(input())
print('Parabéns! Você acertou.')
    
