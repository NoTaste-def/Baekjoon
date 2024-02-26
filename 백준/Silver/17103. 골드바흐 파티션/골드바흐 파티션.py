from sys import stdin
input = stdin.readline

prime = [False, False] + [True]*999999

for i in range(2, 1000001):
  if prime[i]: # True값이면
    for j in range(i*2, 1000001, i): # i의 배수 제거
      prime[j] = False

t = int(input())
for _ in range(t):
  cnt = 0
  n = int(input())
  for i in range(2, n//2+1): # 이 루프는 n//2 이상일 필요가 없음.
    # 입력이 100 일때 / 예를 들어 71 까지 루프를 돈다 치자, 29가 필요함.
    # 근데 n-i, i 를 따지는 입장에서 i가 29까지만 가도 n-i이 자연스레 71이 나오게 됨.
    # 그니깐 반갈까지만 루프 돌리면 되는 것. 
    # +1은 n//2 꽉 채워서 돌리기 위함.
    if prime[i] and prime[n-i]: # n-i + i = n임. n은 짝수, 그럼 n-i랑 i가 소수겠지?
      cnt += 1
  print(cnt)