def pares(a):
    if a == 2:
        print(a)
        return
    elif a == 0:
        return
    else:
        print(a)
        return pares(a-2)

n = int(input())
if n == 0 or n == 1:
    n = 0
elif n % 2 != 0:
    n -= 1

pares(n)
