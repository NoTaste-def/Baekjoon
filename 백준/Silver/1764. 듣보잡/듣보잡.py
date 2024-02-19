n, m = map(int,input().split())
dic = {str(input()):False for _ in range(n)}
for _ in range(m):
  tmp = str(input())
  if tmp in dic :
    dic[tmp] = True
result = []
for k, v in dic.items():
  if v == True:
    result.append(k)

result.sort()

print(len(result))
for item in result:
  print(item)