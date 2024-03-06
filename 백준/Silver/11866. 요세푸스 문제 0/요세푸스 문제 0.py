from collections import deque
from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
dq = deque([i+1 for i in range(n)])
result = []
while True:
  if len(dq) == 0:
    break
  dq.rotate(-(k-1))
  result.append(dq.popleft())
print('<', end='')
print(*result, sep=', ', end='')
print('>')

