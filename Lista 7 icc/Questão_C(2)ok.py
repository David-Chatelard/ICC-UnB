n = int(input())
L = []

for _ in range(n):
    p, s, d = input().split()
    L.append((p, s, int(d)))

Lordem = sorted(L, key = lambda x: x[2], reverse = True)

for i in range(n):
    print(Lordem[i][1], end = '')
