from collections import Counter
import sys

arr=[]
a = str(sys.stdin.readline().strip())
counter = Counter(a.upper())
dic = dict(counter)

[ arr.append(key) for key, value in dic.items() if max(dic.values()) == value]

if len(arr)>=2:
  print('?')
else:
  print(arr[0])