n, s = input().split()
n, s = [int(n), int(s)]
moves = []
towers = {'P1': n, 'P2': 0, 'P3': 0}

def hanoi(n, p1, p2, p3):
    if len(moves) >= s:
        return
    elif n == 1:
        if len(moves) < s:
            movedisk(p1, p3)
    else:
        hanoi(n-1, p1, p3, p2)
        if len(moves) < s:
            movedisk(p1, p3)
        hanoi(n-1, p2, p1, p3)

def movedisk(p1, p3):
    towers[p1] -= 1
    towers[p3] += 1
    moves.append((p1, p3))

hanoi(n, 'P1', 'P2', 'P3')
print(towers['P1'], towers['P2'], towers['P3'])
