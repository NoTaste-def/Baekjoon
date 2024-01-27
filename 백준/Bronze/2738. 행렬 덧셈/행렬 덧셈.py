n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

for row in range(n):
  for col in range(m):
    print(a[row][col] + b[row][col], end=' ')
  print()