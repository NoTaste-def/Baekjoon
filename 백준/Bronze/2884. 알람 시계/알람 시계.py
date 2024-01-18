a, b = map(int, input().split())

if b < 45 and a > 0:
  a -= 1
  b += 60
  b -= 45
elif a == 0 and b < 45:
  a = 23
  b += 60
  b -= 45
else:
  b -= 45
  
print(f'{a} {b}')