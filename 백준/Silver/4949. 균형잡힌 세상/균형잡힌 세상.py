from sys import stdin
input = stdin.readline
while True:
  
  n = input().rstrip()
  if n == '.':
    break
  else:
    stack=[]
    for item in n:
      if item in '([':
        stack.append(item)
      elif item == ')':
        if stack and stack[-1] == '(':
          stack.pop()
        else:
          stack.append(item)
          break
      elif item == ']':
        if stack and stack[-1] == '[':
          stack.pop()
        else:
          stack.append(item)
          break
    if not stack:
      print('yes')
    else:
      print('no')