n = int(input())
arr = []
for _ in range(n):
  a = list(map(int, input().split()))
  arr.append(a)
arr.sort()
for item in arr:
  print(item[0], item[1])
