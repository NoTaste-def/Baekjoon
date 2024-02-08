n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = []
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if arr[i] + arr[j] + arr[k] > m:
        continue
      else:
        result.append(arr[i] + arr[j] + arr[k])
result.sort(reverse=True)
print(result[0])