from sys import stdin
from collections import Counter
import math
input = stdin.readline
n = int(input())
arr = []
for _ in range(n):
  arr.append(int(input()))
arr.sort()
# 산술평균
print(round(sum(arr) / len(arr)))
# 중앙값
print(arr[len(arr)//2])
# 최빈값
tmp = Counter(arr)
cnt = tmp.most_common(2)
if len(cnt) > 1:
  if cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
  else:
    print(cnt[0][0])
else:
  print(cnt[0][0])
# 범위
print(max(arr)-min(arr))