a= int(input())
b= int(input())


# +, + = Quad 1
if a > 0 and b > 0 :
  print('1')
# -, + = Quad 2
elif a < 0 and b > 0 :
  print('2')
# -, - = Quad 3
elif a < 0 and b < 0 :
  print('3')
# +, - = Quad 4
elif a > 0 and b < 0 :
  print('4')
else:
  print('No Quadrant')