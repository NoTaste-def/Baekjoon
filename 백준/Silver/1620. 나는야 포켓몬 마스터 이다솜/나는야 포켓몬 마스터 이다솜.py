import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}
for i in range(n):
  name = str(input().rstrip())
  dic[name] = i+1

converted_dic = {v:k for k,v in dic.items()}

for j in range(m):
  Q = input().rstrip()
  if Q.isdigit() == True:
    print(converted_dic.get(int(Q)))
  else:
    print(dic.get(Q))
