x1, y1, x2, y2, a, b = input().split()
x1, y1, x2, y2, a, b = [float(x1), float(y1), float(x2), float(y2), float(a), float(b)]
p = (x1, y1)
q = (x2, y2)
z = complex(a, b)
dpq = ((x1-x2)**2+(y1-y2)**2)**(1/2)
print('%.4f'%dpq)
modz = (a**2+b**2)**(1/2)
print('%.4f'%modz)

