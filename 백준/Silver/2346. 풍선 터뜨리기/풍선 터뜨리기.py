from collections import deque
from sys import stdin
input = stdin.readline
n = int(input())
dq = deque(enumerate(map(int, input().split())))
result = []
while dq:
  idx, finder = dq.popleft()
  if finder > 0:
    dq.rotate(-finder+1)
  else:
    dq.rotate(-finder)
  result.append(idx+1)
print(*result)