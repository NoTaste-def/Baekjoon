from sys import stdin
input = stdin.readline
a, b = map(int, input().split())
c, d = map(int, input().split())

def gcd(b,d):
  while d>0:
    b,d = d, b%d
  return b

lcm = b*d//gcd(b,d)
hat = lcm//b * a + lcm//d * c

newGCD = gcd(lcm, hat)

print(f'{hat//newGCD} {lcm//newGCD}')

