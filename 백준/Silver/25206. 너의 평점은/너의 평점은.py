# import sys
# data = sys.stdin.readlines()

# # 그냥 깡으로 받습니다. 전 라인을 리스트 형식으로요.
# # 자 그런데 규칙성이 있습니다. 평점이랑 학점 위치가 일정해요.

# # ??? : 어 앞에 뭔가 많이 와서 길이가 달라지는데 위치가 왜 일정한가요.

# # 뒤에서 보세요. 일정하잖아요?

# # [-3:-1] 과목평점
# # [-7:-4] 까지는 학점
# # 자, 이제 데이터까지 추출할 수 있습니다.

# # print(data[0][-3:-1])
# # print(data[0][-7:-4])
# # 원하면 확인 ㄱㄱ


# # 아 그럼 평점은요? 
# gpa = ['F', 'D0', 'D+', 'C0', 'C+', 'B0', 'B+', 'A0', 'A+']
#       # 0     1     2     3     4     5     6     7     8
#       # 2로 나누고 0.5 더해주면 될듯요.

# #  (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값
# # sum(학점 * 평점) / sum(학점)

# 학점 = []
# 평점 = []
# 숫자평점 = []

# for i in range(0, len(data)):
#   평점.append(data[i][-3:-1])
#   학점.append(data[i][-7:-4])

# # 여기서 잠깐. P <- 이거 지워야 하네요. 어떻게 할까요.
# for i in range(len(평점)):
#   if 평점[i] == '0 ':
#     del 평점[i]
#     del 학점[i]
# # P여도 평점이 존재하므로, 같이 지워줘야 합니다.

# # 이제 평점을 점수로 변환해야함.
# # 어캐할까요.

# for score in 평점:
#   for i in range(len(gpa)):
#     if score==gpa[i]: 
#       tmp = (i/2 + 0.5)
#       숫자평점.append(tmp)
      
# 정제된평점 = list(map(float,숫자평점))
# 정제된학점 = list(map(float,학점))


# # 리스트끼리 연산 1번
# for i in range(0, len(data)):
#   곱 = [a*b for a,b in zip(정제된학점, 정제된평점)]

# print('%.6f'%(sum(곱)/sum(정제된학점)))
#       # ^ 소수점 6자리 표현하는법


## 사실 위에처럼 안해도 됩니다.
## 그냥 저렇게 해보고 싶었음.

영어평점 = ['F', 'D0', 'D+', 'C0', 'C+', 'B0', 'B+', 'A0', 'A+']
숫자평점 = [0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
총합 = 0
결과 = 0
for _ in range(20):
  과목, 학점, 평점 = input().split()
  학점 = float(학점)
  if 평점 != 'P':
    총합 += 학점
    결과 += 학점 * 숫자평점[영어평점.index(평점)] 
    # 받은 평점이랑 같은 녀석을 영어평점 리스트에서 찾아내고 그 인덱스를 반환함.
    # 그럼 알아서 숫자 평점 값이 들어가겠죠.
print('%.6f'%(결과/총합))
