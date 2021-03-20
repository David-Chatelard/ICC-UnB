import math
x1, y1 = input().split()
x2, y2 = input().split()
x1, y1, x2, y2 = [float(x1), float(y1), float(x2), float(y2)]
z = complex(input())
a = z.real
bj = z.imag
dpq = math.sqrt((x1-x2)**2+(y1-y2)**2)
modz = math.sqrt(a**2+(bj)**2)
print('%.4f'%dpq)
print('%.4f'%modz)

