from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
dic = {}
for _ in range(n):
  word = input().rstrip()
  if word in dic:
    dic[word] += 1
  elif len(word) >= m:
    dic[word] = 1

result = sorted(dic.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) 
# 람다식 해설.
# lambda x : ( 여기 차례대로 설명 )
# -x[1] => 빈도수 순으로 정렬인데, - 부호를 붙여줌으로서 오름차순이 아닌 내림차순으로 정렬
# -len(x[0]) => 글자의 길이를 기준으로 내림차순 정렬
# x[0] => 알파벳의 사전순으로 오름차순 정렬
# 각 조건은 왼쪽일수록 우선도가 높음.
# 그리고 딕셔너리는 키로 값에 접근이 가능하지만
# 리스트와 같이 인덱싱으로도 접근이 가능하다. 0은 키 1 은 값.

for i in result:
  print(i[0])
