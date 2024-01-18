T = int(input())
RS = []

for i in range(T):
  RS.append(input().split())

for r, s in RS: # 언패킹
  for i in range(len(s)):
    print(s[i]*int(r), end='')
  print()