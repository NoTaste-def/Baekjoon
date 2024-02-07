n = int(input())
arr = list(map(int,input().split()))

result = 0

for item in arr:
  cnt = 0
  arr = []
  for i in range(1,item+1):
    if item % i == 0:
      arr.append(i)
      cnt += 1
  if cnt == 2:
    result += 1
print(result)