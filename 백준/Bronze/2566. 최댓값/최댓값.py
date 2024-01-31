a = [list(map(int, input().split())) for _ in range(9)]
tmp = a[0][0]
tmpXIndex = 0
tmpYIndex = 0

for i in range(9):
  for j in range(9):
    if tmp < a[i][j]:
      tmp = a[i][j]
      tmpXIndex = i
      tmpYIndex = j

print(tmp)
print(tmpXIndex+1, tmpYIndex+1)