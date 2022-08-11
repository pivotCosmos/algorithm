import sys
N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
M = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
results = []
for number in numbers :
    if number in cards :
        results.append(1)
    else :
        results.append(0)
print(*results)