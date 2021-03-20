n = int(input())

aux = n
for i in range(1, n+1):
   if i == 1:
      fn1 = 1
      fn2 = 1
      fn = 1
   elif i == 2:
      fn = 1
   else:
      fn = fn1 + fn2
      fn2 = fn1 
      fn1 = fn
print(fn, end = ' ')
for c in range(1, n):
   n = n*c
print(n, end = ' ')
aux2 = fn
if aux2 % 2 == 0:
   fn += fn2
   print(fn - aux2)
   
