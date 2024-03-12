from sys import stdin
input = stdin.readline
log = {}
cnt = 0
for i in range(int(input())):
  chat = input().rstrip()
  if chat == "ENTER": # ENTER가 들어오면 딕셔너리 초기화
    log = {}
    continue
  if chat not in log: # 딕셔너리에 사용자가 없으면
    log[chat] = True # True로 바꾸고 cnt에  +1
    cnt += 1
print(cnt)