#input 대신 sys.stdin.readline을 사용할 수 있다.
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

import sys

# n = int(input())
# temp = []
# for i in range(n) :
#     input1, input2 = sys.stdin.readline().rstrip().split()
#     input1 = int(input1)
#     input2 = int(input2)
#     temp.append(input1+input2)

# i =0
# while i < n :
#     print(temp[i])
#     i = i +1


# #while문 대신 print(*temp,sep = "\n")로 출력
# n = int(input())
# temp = []
# for i in range(n) :
#     input1, input2 = map(int, sys.stdin.readline().split())
#     temp.append(input1+input2)

# #print("\n", join(temp)) #문자열만 가능
# print(*temp,sep = "\n")


#list로 받아서 바로 출력
n = int(input())
for i in range(n) :
    l = list(map(int, sys.stdin.readline().split()))
    print(l[0]+l[1])