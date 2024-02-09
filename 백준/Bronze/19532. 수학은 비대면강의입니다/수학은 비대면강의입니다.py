a,b,c,d,e,f = map(int,input().split())

X = 0
Y = 0

for x in range(-999,1000):
  for y in range(-999, 1000):
    if a*x+b*y == c and d*x+e*y == f:
      X = x
      Y = y
      break
print(X,Y)