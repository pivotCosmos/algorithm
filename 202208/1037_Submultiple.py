import sys

N = int(input())
submultiple_list = list(map(int, sys.stdin.readline().split()))
if N == 1 :
    unique_submultiple = submultiple_list[0]
    result = unique_submultiple**2
    print(result)
else :
    min_num = min(submultiple_list)
    max_num = max(submultiple_list)
    result = min_num*max_num
    print(result)