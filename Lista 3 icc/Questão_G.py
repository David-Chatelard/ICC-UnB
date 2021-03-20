n = int(input())

if n == 1:
    print(3)
else:
    for m in range(1, 1001):
        for i in range(2, ((n*m)+1)):
            if ((n*m)+1) % i == 0:
                break
        if ((n*m)+1) % i == 0:
            break
    print(m)
