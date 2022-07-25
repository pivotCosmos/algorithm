import sys
n,x = map(int,input().split())
numbers = list(map(int,sys.stdin.readline().split()))
for i in range(len(numbers)) :
    if numbers[i] < x :
        print(numbers[i], end=' ')