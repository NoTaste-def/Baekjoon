x, y, w, h = map(int, input().split())

ax = w-x
ay = h-y

arr = [x,ax,y,ay]

arr.sort()
print(arr[0])
  