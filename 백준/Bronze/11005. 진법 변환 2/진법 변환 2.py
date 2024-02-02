# mapper = { 
#           10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',
#           16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',25:'P',
#           26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z'
#           }

# n, b = input().split()
# n = int(n)
# b = int(b)
# quotient = n
# tmp = []
  
# while True:
#   if quotient < b:
#     if quotient > 9:
#       tmp.append(mapper[quotient])
#     else:
#       tmp.append(quotient)
      
#     break
  
#   quotient = quotient // b
#   remainder = quotient % b
#   if remainder > 9:
#     tmp.append(mapper[remainder])
#   else:
#     tmp.append(remainder)
    
# tmp = ''.join(tmp[::-1])

# print(tmp)

array = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, b = map(int, input().split())
string = ''

while n:
  string += str(array[n%b])
  n //= b
print(string[::-1])