# 이항계수
import math
print(math.comb(*map(int,input().split())))

# import sys
# N, K = map(int, sys.stdin.readline().split())

# def factorial(num) :
#     oriNum = num
#     result = oriNum
#     while oriNum-1 > 1 :
#         result *= (oriNum-1)
#         oriNum -= 1
#     return result

# # N개 중에서 K개를 뽑는다
# def getBinomicalCoefficient(totalNum, pickNum) :
#     result = 1 # K=0일때
#     temp1 = factorial(totalNum)
#     temp2 = factorial(pickNum)
#     temp3 = factorial(totalNum-pickNum)
#     if temp2 > 0 and temp3 > 0 :
#         result = temp1//(temp2*temp3)
#     return result

# result = getBinomicalCoefficient(N,K)
# print(result)