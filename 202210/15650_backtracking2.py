from itertools import combinations
N,M = map(int,input().split())
li = [x for x in range(1,N+1)]
depth = M
results = list(combinations(li,M))
print(*results, sep='\n')