from sys import stdin
input = stdin.readline
n = int(input())
# 1회 : 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 
# 2회 : 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 (1배수)
# 3회 : 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 (2배수)
# 4회 : 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 (3배수)
# 5회 : 1 0 0 1 1 1 1 1 0 0 1 0 1 0 0 1 (4배수)
# 6회 : 1 0 0 1 0 1 1 1 0 1 1 0 1 0 1 1 (5배수)
# 7회 : 1 0 0 1 0 0 1 1 0 1 1 1 1 0 1 1 (6배수)
# 8회 : 1 0 0 1 0 0 0 1 0 1 1 1 1 1 1 1 (7배수)
# 9회 : 1 0 0 1 0 0 0 0 0 1 1 1 1 1 1 0 (8배수)
# 10회: 1 0 0 1 0 0 0 0 1 1 1 1 1 1 1 0 (9배수)
# 11회: 1 0 0 1 0 0 0 0 1 0 1 1 1 1 1 0 (10배수)
# 12회: 1 0 0 1 0 0 0 0 1 0 0 1 1 1 1 0 (11배수)
# 13회: 1 0 0 1 0 0 0 0 1 0 0 0 1 1 1 0 (12배수)
# 14회: 1 0 0 1 0 0 0 0 1 0 0 0 0 1 1 0 (13배수)
# 15회: 1 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 (14배수)
# 16회: 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 (15배수)
# 17회: 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 (16배수)

# 홀수 0
# 짝수 1
# 12의 약수 = 2 3 4 6 12
# 2의 배수 = 2 4 6 12 
# 2(1) 4(2의배수, 4의배수) 6(2의배수, 3의배수, 6의배수), 12(12의 배수)
# 0 1 0 0

# 1 4 9 16... 번째 마다 하나씩 열림.
# 3 5 7 9 11 이런식으로 cnt 하나씩 증가.

# 1 4 9 16 25

# def eratos(n):
#   if n==0 or n==1:
#     return False
#   for i in range(2, int(n**0.5)+1):
#     if n%i == 0:
#       return False
#   return True

cnt = 1
p = 3
num = 1

while True:
  if p+num >= n:
    break
  cnt += 1
  num += p
  p += 2
print(cnt)