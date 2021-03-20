def concat(S1, S2):
    if not S1:
        return S2
    else:
        return S1[0:1] + concat(S1[1:], S2)


def rev(S1):
    if not S1:
        return S1
    else:
        return concat(rev(S1[1:]), S1[0:1])


def prefix(S1, S2):
    if not S1:
        return True
    elif S1[0:1] == S2[0:1]:
        return prefix(S1[1:], S2[1:])
    else:
        return False
    





s1 = input()
s2 = input()

print(concat(s1, s2))
print(rev(s1))
print(prefix(s1, s2))
