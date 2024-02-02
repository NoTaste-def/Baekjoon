T = int(input())

result = []
a = [25, 10, 5, 1]

# def remain(money, coin, i=0):
#   if len(result) == 4:
#     return print(*result)
#   quotient, remainder = divmod(money,coin[i])
#   result.append(quotient)
#   i += 1
#   return  remain(remainder, a[i], i)

# for _ in range(T):
#   c = int(input())
#   remain(c, a)

for i in range(T):
  c = int(input())
  quotientQ, remainderQ = divmod(c,25)
  result.append(quotientQ)
  quotientD, remainderD = divmod(remainderQ,10)
  result.append(quotientD)
  quotientN, remainderN = divmod(remainderD,5)
  result.append(quotientN)
  result.append(remainderN)
  print(*result)
  result=[]
  
  
