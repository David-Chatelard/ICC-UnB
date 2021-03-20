x, y = input().split()
x, y = [int(x), int(y)]
previo = {(0,0):1, (0, 1):2}

def fack(x, y):
    if not (x, y) in previo:
        if (x, y) in previo:
            return previo[(x, y)]
        elif x == 0:
            return y + 1
        elif x > 0 and y == 0:
            novoValor = fack(x-1, 1)
            previo[(x, y)] = novoValor
            return previo[(x, y)]
        elif x > 0 and y > 0:
            novovalor = fack(x-1, fack(x, y-1))
            previo[(x, y)] = novovalor
        return previo[(x, y)]

print(fack(x, y))

##def fack(x, y):
##    if x == 0:
##        return y + 1
##    elif x > 0 and y == 0:
##        return fack(x-1, 1)
##    elif x > 0 and y > 0:
##        return fack(x-1, fack(x, y-1))
##
##print(fack(x,y))

