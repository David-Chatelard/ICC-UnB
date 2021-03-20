n, m = input().split()
n, m = [int(n), int(m)]

aux1 = n
aux2 = m
if n > m:
    while True:
        r = n % m
        if r == 0:
            break
        n = m
        m = r
    print(m)
elif m > n:
    while True:
        r = m % n
        if r == 0:
            break
        m = n
        n = r
    print(n)
else:
    print(n)
        
        
        
