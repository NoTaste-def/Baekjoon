from sys import stdin
input = stdin.readline
n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dicA = {key:0 for key in A}
dicB = {key:0 for key in B}

for k,v in dicA.items():
  if dicB.get(k) == 0:
    dicB[k] = True
    dicA[k] = True

result = []
for k,v in dicA.items():
  if v == 0:
    result.append(k)
for k,v in dicB.items():
  if v == 0:
    result.append(k)
print(len(result))