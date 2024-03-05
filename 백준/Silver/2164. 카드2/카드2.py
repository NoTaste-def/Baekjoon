from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
dq = deque([i for i in range(1,n+1)])
while True:
  if len(dq) == 1:
    break
  dq.popleft()
  dq.rotate(-1)
print(dq[0])