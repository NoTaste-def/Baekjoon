while True:
  name, age, weight = list(input().split())
  
  if name == '#':
    break
  
  if int(age) > 17 or int(weight) >= 80:
    print(name + ' Senior')
  else:
    print(name + ' Junior')