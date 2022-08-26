# import sys
# N = int(input())
# numbers = list(map(int,sys.stdin.readline().split()))
# numberSet = set(numbers) # 중복제거
# sortedNumbers = sorted(list(numberSet)) # 정렬
# results = []
# for i in range(N) :
#     results.append(sortedNumbers.index(numbers[i]))
# print(*results)

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int,input().split()))
num_set = sorted(set(numbers)) # 중복제거, 정렬
num_dict = {value:index for index,value in enumerate(num_set)}

results = [num_dict[x] for x in numbers]
print(*results)