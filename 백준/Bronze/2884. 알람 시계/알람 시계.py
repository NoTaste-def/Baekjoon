# h, m = map(int, input().split())
# total = h * 60 + m - 45
# if total < 0:
#     total += (60 * 24) # 예외처리.
# print(total // 60, total % 60)
# # 전체를 60으로 나눈 몫은 시간.
# # 전체를 60으로 나눈 나머지는 분.

a, b = map(int, input().split())

if b < 45 and a > 0:
  a -= 1
  b += 60
  b -= 45
elif a == 0 and b < 45:
  a = 23
  b += 60
  b -= 45
else:
  b -= 45
  
print(f'{a} {b}')
