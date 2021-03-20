m, d = input().split()
m, d = [int(m), int(d)]

if 1 <= m <= 12 and 1 <= d <= 7:
    if m <= 7 and m % 2 != 0 or m >= 8 and m % 2 == 0:
        if d == 6 or d == 7:
            print(6)
        else:
            print(5)
    if 3 < m < 7 and m % 2 == 0 or m > 8 and m % 2 != 0:
        if d == 7:
            print(6)
        else:
            print(5)
    if m == 2:
        if d == 1:
            print(4)
        else:
            print(5)
            
        
        
    
        
            
