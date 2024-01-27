import sys

cro_alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
voca = sys.stdin.readline().strip()

for alph in cro_alph:
  voca = voca.replace(alph, "a")

print(len(voca))
    