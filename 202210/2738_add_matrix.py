import sys
N,M = map(int,input().split())
A = []
for _ in range(N) :
    line_li = list(map(int,sys.stdin.readline().split()))
    A.append(line_li)
for i in range(N) :
    line_li = list(map(int,sys.stdin.readline().split()))
    for j in range(M) :
        A[i][j] += line_li[j]
for i in range(N) :
    print(*A[i])