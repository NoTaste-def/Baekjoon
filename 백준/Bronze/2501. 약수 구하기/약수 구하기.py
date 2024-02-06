n,k = map(int, input().split())
arr = []
for i in range(n):
  if n % (i+1) == 0:
    arr.append(i+1)

if len(arr) >= k:
  print(arr[k-1])
else:
  print(0)