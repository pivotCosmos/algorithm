import sys
N = int(input())
members = [list(sys.stdin.readline().split()) for _ in range(N)]
for member in members :
    member[0] = int(member[0])
newMembers = sorted(members, key=lambda x: x[0])
for member in newMembers :
    print(*member)