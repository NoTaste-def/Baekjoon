import sys
input = sys.stdin.readline
n = list(input().rstrip())
list(map(int,n))
n.sort(reverse=True)
print(*n, sep='')
