n, m = map(int,input().split())
arr = [i+1 for i in range(0,n)]
for _ in range(0,m):
  i, j = map(int, input().split())
  arr[i-1:j] = reversed(arr[i-1:j])
  
print(*arr)

