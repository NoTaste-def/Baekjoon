while True:
  n = list(map(int, input().split()))
  if n[0] == 0 and n[1] == 0:
    break
  elif n[0] > n[1]:
    print('Yes')
  else:
    print('No')