import sys
N, M = map(int,input().split())
stringsInSet = [sys.stdin.readline() for _ in range(N)]
stringsNeedToCheck = [sys.stdin.readline() for _ in range(M)]
checkResults = [x for x in stringsNeedToCheck if x in stringsInSet]
print(len(checkResults))