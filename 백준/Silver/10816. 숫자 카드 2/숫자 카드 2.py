from sys import stdin
input = stdin.readline
n = int(input())
상근이꺼 = input().split()
m = int(input())
checker = input().split()

def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    
    if arr[mid] > target:
      end = mid - 1
    elif arr[mid] < target:
      start = mid + 1
    else:
      return mid
  return None

dic = {key:0 for key in checker}
dummy = sorted(checker)

for item in 상근이꺼:
  if binary_search(dummy, item, 0, m-1) is not None:
    dic[item] += 1
for i in checker: # Correct
  print(dic[i], end=' ')

# for k, v in dic.items(): # Wrong. Dictionary cannot have duplicate keys
#   print(v, end=' ')
