N = int(input())
L = input().split()
L1 = L[:]
c = 0

for _ in range(5):
    B, D, Q = input().split()
    a = L.index(B)
    for _ in range(int(Q)):
        if D == 'D':
            L[a], L[a+1] = L[a+1], L[a]
            a += 1
        else:
            L[a-1], L[a] = L[a], L[a-1]
            a -= 1
for i in range(N):
    if L[i] != L1[i]:
        c += 1
print(c)
