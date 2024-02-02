array = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, b = input().split()
result = 0

n = ''.join(reversed(n))

b = int(b)

for i in range(len(n)-1, -1, -1):
  result += ( array.find(n[i]) * (b**i) )
  
print(result)