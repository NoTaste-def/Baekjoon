def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
def nck(n, k):
  return factorial(n) // (factorial(k) * factorial(n-k))

n = int(input())
for _ in range(n):
  n, k = map(int, input().split())
  print(nck(k,n))