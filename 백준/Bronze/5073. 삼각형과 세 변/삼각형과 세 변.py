while True:
  a, b, c = map(int, input().split())
  if a == 0 and b == 0 and c == 0:
    break

  arr=[a,b,c]
  arr.sort()
  
  if arr[0]+arr[1] <= arr[2]:
    print('Invalid')
  elif arr[0] == arr[1] == arr[2]:
    print('Equilateral')
  elif arr[0]==arr[1] or arr[0]==arr[2] or arr[1]==arr[2]:
    print('Isosceles')
  elif arr[0]!=arr[1] or arr[0]!=arr[2] or arr[1]!=arr[2]:
    print('Scalene')