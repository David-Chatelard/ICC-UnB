a, b = input().split()
a, b = [int(a), int(b)]

if b == 0:
    print(a, b, 'errados')
elif a == b-1:
    print(a, b, 'ok')
elif a == b:
    print(a, b, 'ok')
else:
    print(a, b, 'errados')
