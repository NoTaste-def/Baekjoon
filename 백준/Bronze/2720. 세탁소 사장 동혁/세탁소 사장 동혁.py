T = int(input())

result = []
a = [25, 10, 5, 1]

def remain(money, coin, i):
  if len(result) == 4:
    return print(*result)
  quotient, remainder = divmod(money,coin[i])
  result.append(quotient)
  return  remain(remainder, coin, i+1)

for _ in range(T):
  c = int(input())
  remain(c, a, 0)
  result=[]

# for i in range(T):
#   c = int(input())
#   quotientQ, remainderQ = divmod(c,25)
#   result.append(quotientQ)
#   quotientD, remainderD = divmod(remainderQ,10)
#   result.append(quotientD)
#   quotientN, remainderN = divmod(remainderD,5)
#   result.append(quotientN)
#   result.append(remainderN)
#   print(*result)
#   result=[]
  
  
