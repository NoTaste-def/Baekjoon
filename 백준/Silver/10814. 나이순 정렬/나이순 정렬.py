import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr=[]
for i in range(n):
  age, name = input().split()
  arr.append([int(age), name])
arr.sort(key = lambda x:x[0])
for age, name in arr:
  print(age, name)
  
# Stable, Unstable 정렬 문제.