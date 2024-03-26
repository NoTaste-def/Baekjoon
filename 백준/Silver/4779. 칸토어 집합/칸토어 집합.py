from sys import stdin
input = stdin.readline

def cantoa(dash):
  if dash == 1:
    return "-"
  len = dash//3
  return cantoa(len)+" "*len + cantoa(len)

while True:
  try:
    n = int(input())
    len = 3**n
    print(cantoa(len))
  except:
    break

