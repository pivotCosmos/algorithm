import sys
N = int(input())
members = [list(sys.stdin.readline().rstrip().split()) for _ in range(N)]
newMembers = sorted(members, key=lambda x: x[0])
for member in newMembers :
    print(*member, sep=' ')