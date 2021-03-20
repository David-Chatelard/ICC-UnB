n = int(input())
p = 0
u = 0
for _ in range(n):
    S = input().lower()
    for i in range(len(S)):
        if S[i] == 'p':
            p += 1
        elif S[i] == 'u':
            u += 1

print(p, end = ' ')
print(u)
