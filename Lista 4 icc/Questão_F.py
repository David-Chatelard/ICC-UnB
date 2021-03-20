def mdc(a, b):
    if a == 0 or b == 0:
        return 0
    elif a % b == 0:
        return b
    else:
        r = a % b
        return mdc(b, r)
    



x, y = input().split()
x, y = [int(x), int(y)]

while x >= 0 and y >= 0:

    if x >= y:
        q = x
        w = y
    else:
        q = y
        w = x
        

    z = mdc(q, w)
    if x == 0 or y == 0:
        print(z)
    else:
        mmc = (x*y)/z

        print('%.0f'%mmc)
    x, y = input().split()
    x, y = [int(x), int(y)]
