# import numpy as np
n, m = map(int, input().split())
bascket = [0 for _ in range(0, n)]
# bascket.xeros(1, n)

for _ in range(0,m):
  i, j, k = map(int,input().split())
  for index in range(i-1,j):
    bascket[index] = k

print(*bascket)
