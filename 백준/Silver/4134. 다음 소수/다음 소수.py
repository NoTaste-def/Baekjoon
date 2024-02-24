import math
from sys import stdin
input = stdin.readline

def eratos(n):
  if n == 0 or n == 1:
    return False
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True

num = int(input())
for i in range(num):
  n = int(input())
  while True:
    if eratos(n):
      print(n)
      break
    else:
      n += 1