import math
from sys import stdin
input = stdin.readline
def Eratos(n):
  if n == 0 or n == 1:
    return False
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True

m,n = map(int, input().split())

for i in range(m,n+1):
  if Eratos(i):
    print(i)