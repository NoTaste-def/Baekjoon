arr = input()

def palindrome(arr):
  if len(arr) <= 1:
    return True
  
  elif arr[0]==arr[-1]:
    return palindrome(arr[1:-1])
  else:
    return False

if palindrome(arr):
  print(1)
else:
  print(0)