def quadr(a):
    if a == 0 or a == 1:
        return
    else:
        print(a,'^',2, sep = '', end = ' ')
        print('=', end = ' ')
        print((a)**2)
        return quadr(a-2)



n = int(input())

if n != 1:
    if n % 2 != 0:
        n -= 1

while n != 0:
    quadr(n)
    n = int(input())
    if n != 1:
        if n % 2 != 0:
            n -= 1
        
