import sys
sys.setrecursionlimit(2147483647)
x, y = input().split()
x, y = [int(x), int(y)]
previo = {}

def fack(x, y):
    if not (x, y) in previo:
        if x == 0:
            return y + 1
        elif y == 0:
            previo [(x, y)] = fack(x-1, 1)
        else:
            previo[(x, y)] = fack(x-1, fack(x, y-1))
    return previo[x, y]

print(fack(x, y))
        
                                  
