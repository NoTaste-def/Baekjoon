n = int(input())

cnt = 0
while n >= 0:
  if n % 5 == 0:
    cnt += (n//5)
    print(cnt)
    break
  cnt += 1
  n -= 3
else:
  print(-1)

