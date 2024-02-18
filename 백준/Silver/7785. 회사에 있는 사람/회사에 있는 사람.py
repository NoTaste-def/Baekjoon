import sys
input = sys.stdin.readline
n = int(input())
dic = {}
result = []
for _ in range(n):
  name, state = map(str, input().split())
  if state == 'enter':
    dic[name] = True
  elif state == 'leave':
    dic[name] = False

for i in dic.keys():
  if dic[i] == True:
    result.append(i)
result.sort(reverse=True)
print(*result, sep='\n')