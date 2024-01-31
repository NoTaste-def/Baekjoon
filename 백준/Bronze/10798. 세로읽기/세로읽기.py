import sys

fisrt = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()
third = sys.stdin.readline().strip()
forth = sys.stdin.readline().strip()
fifth = sys.stdin.readline().strip()

index = [len(fisrt), len(second), len(third), len(forth), len(fifth)]
index.sort()

result = []

for i in range(index[-1]):
  if(len(fisrt) > i):
    result.append(fisrt[i])
  if(len(second) > i):
    result.append(second[i])
  if(len(third) > i):
    result.append(third[i])
  if(len(forth) > i):
    result.append(forth[i])
  if(len(fifth) > i):
    result.append(fifth[i])

print(*result, sep='')