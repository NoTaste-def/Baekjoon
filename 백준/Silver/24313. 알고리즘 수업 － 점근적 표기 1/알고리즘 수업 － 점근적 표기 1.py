a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

fn = a1*n0 + a0
gn = n0*c
if fn <= gn and a1 <= c:
  print(1)
else:
  print(0)