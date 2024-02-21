from sys import stdin
input = stdin.readline
n,m = map(int,input().split())

def gcd(a,b):
  while b>0:
    a,b = b, a%b
  return a

print( n*m // gcd(n,m))