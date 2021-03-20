lack ={}

def fack(x, y):
    if (x, y) in lack.keys():
        return lack[(x, y)]
    else:
        if x == 0:
            r = y + 1
        elif x == 1:
            r = y + 2
        elif x == 2:
            r = 2*y + 3
        elif x == 3:
            r = 2**(y + 3) - 3
        elif y == 0:
            r = fack(x-1, 1)
        else:
            r = fack(x-1, fack(x, y-1))
        lack[(x, y)] = r
        return r

x, y = input().split()
x, y = [int(x), int(y)]

print(fack(x, y))

            
