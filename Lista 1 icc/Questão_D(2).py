import math
x1, y1 = input().split()
x2, y2 = input().split()
a, b = input().split()
x1, y1, x2, y2, a, b = [float(x1), float(y1), float(x2), float(y2), float(a), float(b)]
z = complex(a, b)
dpq = math.sqrt((x1-x2)**2+(y1-y2)**2)
modz = math.sqrt(a**2+b**2)
print('%.4f'%dpq)
print('%.4f'%modz)

