t = int(input())
a = list(map(int,input().split()))
a.sort()
n = a[0] * a[-1]
print(n)