burger = []
drink = []
for i in range(3):
  burger.append(int(input()))
for i in range(2):
  drink.append(int(input()))

result = min(burger) + min(drink) - 50
print(result)