# https://programmers.co.kr/learn/courses/30/lessons/43165
from itertools import *

def solution(numbers, target):
    answer = 0
    if sum(numbers) == target :
            answer = 1
    else :
        for i in range(1, len(numbers)) :
            minusTuples = list(combinations(numbers, i))
            for j in range(len(minusTuples)) :
                # print(minusTuples[j],sum(minusTuples[j]))
                if sum(numbers) - sum(minusTuples[j])*2 == target :
                    answer = answer + 1
                    # print('true')
    return answer
# print(solution([4,1,2,1],4))