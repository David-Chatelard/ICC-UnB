n, m = input().split()
n, m = [int(n), int(m)]

if n == m:
    print(n)
elif n % m == 0:
    print(m)
elif m % n == 0:
    print(n)
elif n > m:
    f = n % m
    print(f)
elif m > n:
    g = m % n
    print(g)
    
