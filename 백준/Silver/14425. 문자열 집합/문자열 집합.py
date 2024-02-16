import sys
input = sys.stdin.readline
dic = {}
cnt = 0
n, m = map(int, input().split())
for _ in range(n):
  item = input().rstrip()
  dic[item] = True
for _ in range(m):
  item = input().rstrip()
  if item in dic: # 키만 리턴, dic.items() 사용시 키, 값 모두 리턴
    cnt += 1
print(cnt)