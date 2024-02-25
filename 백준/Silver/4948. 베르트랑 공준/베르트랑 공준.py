import math
from sys import stdin
input = stdin.readline

MAX = 123456*2 + 1 # 최대 범위
arr=[1]*MAX # 최대범위 만큼 1로 초기화된 배열을 미리 생성

for i in range(1, MAX): # 배열 인덱싱을 위해 1부터 MAX까지 순회.
  if i == 1: # 1인 경우 스킵.
    continue
  for j in range(2, int(math.sqrt(i))+1): # for문을 순회하며 인덱스 값이 소수인지 판정.
    if i%j == 0: # 소수가 아니면
      arr[i] = 0 # 0으로 값 할당 
      break
    
while True:
  num = int(input())
  if num == 0:
    break
  cnt = 0
  for i in range(num+1, 2*num+1):
    cnt += arr[i] # 인덱스 i가 소수가 아니면 0, 소수면 1이므로 cnt에 덧셈
  print(cnt)