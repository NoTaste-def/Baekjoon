# stack (1이면) 오른쪽부터 pop
# queue (0이면) 왼쪽부터 pop
from collections import deque
from sys import stdin
input = stdin.readline
n = int(input())
what = list(input().split())
init = list(input().split())
m = int(input())
push = list(input().split())
dq = deque()
for index, value in enumerate(init):
  if what[index] == '0': # int 안해줬으니 '0'으로.
    dq.appendleft(value)
dq.extend(push)
for i in range(m):
  print(dq[i], end=' ')