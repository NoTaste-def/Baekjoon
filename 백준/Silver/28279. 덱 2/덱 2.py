from collections import deque
from sys import stdin
input = stdin.readline
n = int(input())
dq = deque([])
for _ in range(n):
  protocol = list(map(int, input().split()))
  if protocol[0] == 1:
    dq.appendleft(protocol[1])
  elif protocol[0] == 2:
    dq.append(protocol[1])
  elif protocol[0] == 3:
    if len(dq) == 0:
      print(-1)
    else:
      print(dq.popleft())
  elif protocol[0] == 4:
    if len(dq) == 0:
      print(-1)
    else:
      print(dq.pop())
  elif protocol[0] == 5:
    print(len(dq))
  elif protocol[0] == 6:
    if len(dq) == 0:
      print(1)
    else:
      print(0)
  elif protocol[0] == 7:
    if len(dq) == 0:
      print(-1)
    else:
      print(dq[0])
  else:
    if len(dq) == 0:
      print(-1)
    else:
      print(dq[-1])
      
    
    