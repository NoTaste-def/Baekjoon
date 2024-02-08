arr = [list(map(int,input().split())) for _ in range(3)]
x = [arr[0][0], arr[1][0], arr[2][0]]
y = [arr[0][1], arr[1][1], arr[2][1]]

for i in range(3):
  if x.count(x[i]) == 1:
    rx = x[i]
  if y.count(y[i]) == 1:
    ry = y[i]
print(rx,ry)