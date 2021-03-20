L = []

def maior():
    for _ in range(10):
        x = int(input())
        L.append(x)
    return max(L)

m = maior()

print(m)

if max(L) % L[0] == 0:
    print(L[0])
        
    
    
