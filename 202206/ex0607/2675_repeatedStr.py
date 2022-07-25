# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:
import sys

# n = int(input()) # 문자열 개수
# inputList = [] # 반복횟수와 문자열 저장
# tempList = [] # inputList 분리해서 저장
# result = '' # 새로 만든 문자열
# resultList = []
# for i in range (n) :
#     inputList = list(sys.stdin.readline().rstrip().split())
#     tempList = list(inputList[1])
#     result = ''
#     for j in range(len(tempList)) :
#         for r in range(int(inputList[0])) :
#             result += tempList[j]
#     resultList.append(result)
# print(resultList)

t = int(input())
for i in range(t) :
    e = ''
    r, s = map(str, input().split())
    q = int(r)
    p = len(s)
    for j in range(p) :
        x = q*s[j] #문자와 숫자 곱셈 가능
        e += x
    print(e)

