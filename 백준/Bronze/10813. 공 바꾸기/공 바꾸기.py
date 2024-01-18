n, m = map(int, input().split())
bascket = [i+1 for i in range(0,n)]

for _ in range(0,m):
  i, j = map(int, input().split())
  bascket[i-1], bascket[j-1] = bascket[j-1], bascket[i-1]
  
print(*bascket)