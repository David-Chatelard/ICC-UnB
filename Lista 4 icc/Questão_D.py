def soma(a):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        return a + soma(a-2) 


n = int(input())
if n >= 2 or n <0:
        
    if n % 2 != 0:
        n -= 1
        
    n -= 2

    s = soma(n)

    print(s)
else:
    print(0)
