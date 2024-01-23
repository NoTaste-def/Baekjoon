a = list(map(int, input().split()))
data = [1, 1, 2, 2, 2, 8]
result = []

for i in range(len(a)):
  if a[i] != data[i]:
    result.append((data[i]-a[i]))
  else:
    result.append(0)
print(*result)
