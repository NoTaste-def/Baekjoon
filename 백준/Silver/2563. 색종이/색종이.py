n = int(input())
paper = [ [0]*100 for _ in range(100)]

for _ in range(n):
  y1, x1 = map(int, input().split())
    
  for i in range(x1, x1+10):
    for j in range(y1, y1+10):
      paper[i][j] = 1
      
result = 0

for k in paper:
  result += sum(k)
print(result)