import sys
N = int(input())
li = list(map(int,sys.stdin.readline().split()))
V = int(input())
count = 0
for i in range(len(li)) :
    if li[i] == V :
        count += 1
print(count)