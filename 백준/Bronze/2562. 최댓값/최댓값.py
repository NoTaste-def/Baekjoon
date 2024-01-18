arr = []
while True:
  try:
    arr.append(int(input()))
  except:
    break

print(max(arr))
print(arr.index(max(arr))+1)


