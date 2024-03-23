from sys import stdin
input = stdin.readline
while True:
  cnt = 0
  sen = input().rstrip()
  if sen == '#':
    break
  for a in sen:
    if a in 'aeiouAEIOU':
      cnt += 1
  print(cnt)