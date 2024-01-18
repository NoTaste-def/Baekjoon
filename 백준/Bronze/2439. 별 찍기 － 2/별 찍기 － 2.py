n = int(input())

for i in range(n, 0, -1):
  for _ in range(0, i-1):
    print(' ', end='')
  for _ in range(0, n-i+1):
    print('*', end='')
  print('')