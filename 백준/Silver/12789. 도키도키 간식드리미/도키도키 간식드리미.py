import sys
n = int(input())
arr = list(map(int,input().split()))
rest = []
target = 1
for i in arr:
  rest.append(i)
  while rest and rest[-1] == target: # rest 에서 타깃을 찾으면,
    rest.pop() # 뽑아서 간식 멕이고
    target += 1 # 다음 순번 찾으러 ㄱㄱ
  if len(rest) > 1 and rest[-1] > rest[-2]: # 2명 이상의 대기자가 존재, 마지막 원소가 그 전 원소보다 클 경우.
    # 예를 들자면 / rest에 2, 4 가 들어가 있다면 2를 못빼냄. 4를 먼저 빼야 2를 뺄 수 있기 때문.
    print('Sad')
    sys.exit()
if rest:
  print('Sad')
else:
  print('Nice')
