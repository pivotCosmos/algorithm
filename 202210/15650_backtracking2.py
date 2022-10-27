from itertools import combinations
N,M = map(int,input().split())
li = [x for x in range(1,N+1)]
depth = M
results = [x for x in combinations(li,M)]
for tpl in results :
    print(*list(tpl))