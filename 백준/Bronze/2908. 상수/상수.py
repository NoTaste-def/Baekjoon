a, b = map(str, input().split())

## 역순으로 바꾸는 방법 1
# Are = list(a)
# Bre = list(b)
# Are.reverse() # 파이썬에서는 문자열 상태로 정렬 불가. 반드시 리스트화 해줘야 reverse 함수 가능
# Bre.reverse()

# a = ''.join(Are) # list를 문자열로 치환
# b = ''.join(Bre)

# int(a)
# int(b)

## 역순으로 바꾸는 방법 2

reversedA = a[::-1]
reversedB = b[::-1]

int(reversedA)
int(reversedB)

# 파이썬 삼항연산자라고 하네요
print(reversedA) if reversedA > reversedB else print(reversedB) 
