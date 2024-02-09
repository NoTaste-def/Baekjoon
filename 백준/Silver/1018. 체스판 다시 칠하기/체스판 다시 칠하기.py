n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
result = []
for i in range(n-7): # i,j 위치부터 8x8 검사. index를 벗어나지 않기 위해 n,m에 각각 -7
  for j in range(m-7):
    cnt1 = 0 # 첫번째 칸이 W일지 B일지의 경우 모두를 구한뒤, 더 작은 카운트 값을 가지는 것을 답으로.
    cnt2 = 0
    for a in range(i,i+8):
      for b in range(j,j+8):
        if ((a+b) % 2 == 0): # TestCase 1. a = 1, b = 1 / a=1, b=3 / ... / 일 때 B 만 걸러짐.
          if arr[a][b] != 'B':
            cnt1 += 1
          if arr[a][b] != 'W':
            cnt2 += 1
        else:             # TestCase 1. 에 적용하면 W만 걸러짐.
          if arr[a][b] != 'W':
            cnt1 += 1
          if arr[a][b] != 'B':
            cnt2 += 1
    result.append(cnt1)
    result.append(cnt2)

print(min(result))