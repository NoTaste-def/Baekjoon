import copy 

cnt = 0
res = -1

def sort(arr, start, end):
  if (start < end):
    mid = (start+end)//2
    sort(arr, start, mid) # 전반
    sort(arr, mid+1, end) # 후반
    return merge(arr, start, mid, end) # merge

def merge(arr, start, mid, end):
  global cnt, res
  
  tmp = []
  i = start
  j = mid + 1
  
  while i <= mid and j <= end:
    
    if arr[i] < arr[j]:
      tmp.append(arr[i])
      i += 1
      
    else:
      tmp.append(arr[j])
      j += 1
    
  while i <= mid:
    tmp.append(arr[i])
    i += 1
    

  while j <= end:
    tmp.append(arr[j])
    j += 1
    
  i = start
  t = 0
  
  while i <= end:
    arr[i] = tmp[t]
    cnt += 1
    if cnt == k:
      res = arr[i]
      break
    
    i += 1
    t += 1
  
  return arr

n, k = map(int, input().split())
arr = list(map(int, input().split()))

sort(arr, 0, n-1)
print(res)