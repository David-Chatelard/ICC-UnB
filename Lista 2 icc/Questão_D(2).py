a, b = input().split()
a, b = [int(a), int(b)]

if b == 0:
    print(a, b, 'errados')
elif b >= a:
    print(a, b, 'ok')
else:
    print(a, b, 'errados')
    
