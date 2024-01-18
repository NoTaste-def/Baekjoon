arr = []
for _ in range(0,10):
  num = int(input())
  arr.append(num%42)

arr = dict.fromkeys(arr)
arr = list(arr)

print(len(arr))
