# https://www.acmicpc.net/problem/11659
import sys
N,M = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))
# 시간초과
# for _ in range(M) :
#     start,end = map(int,sys.stdin.readline().split())
#     numbers_sliced = numbers[start-1:end]
#     my_sum = sum(numbers_sliced)
#     print(my_sum)

# 부분합
sum = 0
prefix_sum = [0]
for number in numbers :
    sum += number
    prefix_sum.append(sum)

for _ in range(M) :
    start, end = map(int, sys.stdin.readline().split())
    print(prefix_sum[end]-prefix_sum[start-1])