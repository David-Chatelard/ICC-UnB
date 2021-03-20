s = input().lower()
c = 0

for i in range(len(s)):
    if s[i] == 'j':
        c += 1
    elif s[i] == 'o':
        c += 1
    elif s[i] == 'h':
        c += 1
    elif s[i] == 'n':
        c += 1
    
print(c)
