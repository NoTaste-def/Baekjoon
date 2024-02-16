import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = list(map(int, input().split()))

tmp = set(arr)
tmp = list(tmp)
tmp.sort()

dic = {tmp[i]:i for i in range(len(tmp))} 
# list.index는 O(N) 이므로 시간초과의 원인이 된다.
# 딕셔너리의 경우, 키나 값에 기반한 검색의 경우 O(1)의 시간복잡도이므로 훨씬 빠르다.

for item in arr:
  print(dic[item], end=' ')