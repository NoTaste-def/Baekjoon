n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
x=[]
for i in range(n):
  x.append(arr[i][0])

y=[]
for i in range(n):
  y.append(arr[i][1])

x.sort()
y.sort()

rx = x[-1] - x[0]
ry = y[-1] - y[0]

print(rx*ry)