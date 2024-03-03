from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
dq = deque([])
for i in range(n):
  arr = input().split()
  if arr[0] == 'push':
    dq.append(arr[1])
  elif arr[0] == 'pop':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq.popleft())
  elif arr[0] == 'size':
    print(len(dq))
  elif arr[0] == 'front':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq[0])
  elif arr[0] == 'back':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq[-1])
  elif arr[0] == 'empty':
    if len(dq) == 0:
      print(1)
    else:
      print(0)
  