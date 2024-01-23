N = int(input())

for i in range(N,0,-1):
  for _ in range(0, i-1):
    print(' ', end='')
  for _ in range(0, 2*(N-i)+1):
    print('*', end='')
  print('')
for i in range(N,0,-1):
  for _ in range(0, N-i+1):
    print(' ', end='')
  for _ in range(0, 2*(i-1)-1):
    print('*', end='')

  print('')