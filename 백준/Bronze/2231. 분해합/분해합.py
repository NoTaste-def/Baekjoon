n = int(input())

for i in range(1, n+1):
  sum_of = sum(map(int,str(i)))
  result = sum_of + i
  if(result == n):
    print(i)
    break
  if(i==n):
    print(0)