from sys import stdin
input = stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

def gcd(a,b):
  while b>0:
    a,b = b, a%b
  return a

tmp = 0
result = []
a = 0
b = 0
for i in range(n):
  result.append( arr[i][0]*arr[i][1] // gcd(arr[i][0], arr[i][1]) )

for item in result:
  print(item)
  