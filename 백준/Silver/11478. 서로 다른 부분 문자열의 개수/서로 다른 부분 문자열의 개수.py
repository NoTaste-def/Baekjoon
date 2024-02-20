s = str(input())
n = set(s)
for i in range(0, len(s)):
  for j in range(len(s)+1-i):
    n.add(s[j:j+i])
print(len(n))