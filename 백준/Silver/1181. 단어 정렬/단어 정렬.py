import sys
input = sys.stdin.readline
n = int(input())
arr = [ input().rstrip() for _ in range(n)]
for item in sorted(set(arr), key = lambda x : (len(x), x)):
  print(item)

