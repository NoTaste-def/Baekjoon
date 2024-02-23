def gcd(a,b):
  while b>0:
    a,b = b, a%b
  return a

from sys import stdin
input = stdin.readline
n = int(input())
parameter = int(input())
tree = []
for _ in range(n-1):
  num = int(input())
  tree.append(num - parameter)
  parameter = num 

gcd_v = tree[0]
for i in range(1, len(tree)):
  gcd_v = gcd(gcd_v, tree[i])
  
result = 0
for item in tree:
  result += item // gcd_v - 1
print(result)
