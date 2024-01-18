initialTotalPrice = int(input())
kindOfThings = int(input())
verificationTotal = 0
for i in range(0, kindOfThings):
  price, num = map(int, input().split())
  verificationTotal += price*num
if verificationTotal == initialTotalPrice:
  print('Yes')
else:
  print('No')