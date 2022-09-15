import sys

N = int(input())
submultiple_list = list(map(int, sys.stdin.readline().split()))

if N == 1 :
    result = submultiple_list[0]**2
    print(result)
else :
    result = min(submultiple_list)*max(submultiple_list)
    print(result)