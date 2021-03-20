n = int(input())
S = []

for i in range(n):
    x, y = input().split()
    x, y = [int(x), int(y)]
    L = []
    F = []
    if x % 2 != 0:
        for c in range(x, x+(y*2), 2):
            L.append(c)
            F.append(c)
        print(sum(L))
        S.append(sum(F))
    else:
        for b in range(x+1, (x+1)+(y*2), 2):
            L.append(b)
            F.append(b)
        print(sum(L))
        S.append(sum(F))
        
print(max(S))
print(min(S))
f = (max(S)+ min(S))/2
print('%.2f'%f)

        
        
            
