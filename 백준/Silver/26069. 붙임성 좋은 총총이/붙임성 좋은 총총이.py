from sys import stdin
input = stdin.readline
n = int(input())
dancer = ['ChongChong']
for i in range(n):
  a, b = input().split()
  if a in dancer:
    dancer.append(b)
  elif b in dancer:
    dancer.append(a)
  else:
    continue
print(len(set(dancer)))
