n = int(input())
x = 0

while x != n:
    x = int(input())
    if x > n:
        print('O número correto é menor.')
    if x < n:
        print('O número correto é maior.')
print('Parabéns! Você acertou.')
    
