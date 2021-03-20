t = int(input())
s = 0

for i in range(t):
    a, n = input().split()
    a, n = [int(a), int(n)]
    for c in range(a, a+n):
        s += c
        if c != (a+n)-1:
            print(c, end = ' ')
        else:
            print(c)
            print(s)
            s = 0
        
    
        
        

