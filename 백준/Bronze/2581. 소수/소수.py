m = int(input())
n = int(input())

result = []
for num in range(m, n+1):
  cnt = 0
  for j in range(1, num+1):
    if(num % j == 0):
      cnt += 1
  if(cnt == 2):
    result.append(num)
    
if(len(result) == 0):
  print(-1)
else:
  result.sort
  print(sum(result))
  print(result[0])
