N = int(input())

start = 1
end = 1
i = 0
cnt = 1

while True:
  if start <= N and N <= end:
    print(cnt)
    break
  end += (i+1)*6
  start += i*6
  i += 1
  cnt += 1
  