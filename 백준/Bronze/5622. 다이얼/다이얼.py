dic = {'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10, 'operator':11}

string = str(input())

getkey = list(dic.keys())

tmp = 0

for i in range(0,len(getkey)):
  for alph in string:
    if getkey[i].find(alph) >= 0:
      tmp = tmp + dic[getkey[i]]
    else:
      pass
print(tmp)