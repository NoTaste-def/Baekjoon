import sys

n = int(input())
상근이가가진거 = list(map(int, sys.stdin.readline().split()))
m = int(input())
상근이가찾는거 = list(map(int, sys.stdin.readline().split()))

상근이가가진거.sort()

def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start+end)//2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

for i in range(m):
  if binary_search(상근이가가진거, 상근이가찾는거[i], 0, n-1) is not None:
    print(1, end=' ')
  else:
    print(0, end=' ')
