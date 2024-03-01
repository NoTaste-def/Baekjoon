n = int(input())
for _ in range(n):
  stack=[]
  arr = input()
  for item in arr:
    if item == '(':
      stack.append(item) # ( 만 스택에 집어넣고
    elif item == ')':
      if stack: # 스택이 비어있지 않고(True),  ')' 를 만나면 '(' 를 pop.
        stack.pop()
      else:
        print('NO')
        break
  else: # for - else 문. for문이 break가 없이 수행됐다면 else문 수행.
    if not stack:
      print('YES')
    else:
      print('NO')