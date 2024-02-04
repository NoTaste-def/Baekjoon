import sys
import math

input = sys.stdin.readline

a, b, v = map(int,input().split())

# day 1   2   3   4
#     -2  -2  -2  -2
#     +1  +1  +1  +1
#     5   4   3   2
#     3   2   1   0
    
#     1   2   3   4   5   6
#     -5  -5
#     +1  +1
#     6   2
#     1   -4
    
#     day*a - (day-1) * b >= v
#     (a-b)day + b >= v
#     day >= (v-b) / (a-b)

day = (v-b) / (a-b)
day = math.ceil(day)
print(day)