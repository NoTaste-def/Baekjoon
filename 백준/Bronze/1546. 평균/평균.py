n = int(input())

scoreLi = list(map(int, input().split()))
maxScore = max(scoreLi)

scoreLi = [(scoreLi[i] / maxScore*100 ) / n  for i in range(0,n)]

print(sum(scoreLi))