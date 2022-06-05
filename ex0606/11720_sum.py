#N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

n = int(input())
num = int(input())
numList = []
for i in range(n) :
    numList = list(map(int,str(num)))
print(sum(numList))

# 처음부터 문자열리스트로 받기
    # data = list("ABC")
    # print(data)   #['A', 'B', 'C']
    # print(*data)  # A B C
# n=int(input())
# s=input()
# sum = 0
# for i in range(n):
#     sum+=int(s[i])
# print(sum)