while True:
  arr = []
  n = int(input())
  if n == -1:
    break
  for i in range(n):
    if n % (i+1) == 0:
      arr.append(i+1)
  arr.pop()
  if sum(arr) == n:
    print(f'{n} = {arr[0]}', end='')
    for i in range(1, len(arr)):
      print(f' + {arr[i]}', end='')
  else:
    print(f'{n} is NOT perfect.', end='')
  print('')
  
  