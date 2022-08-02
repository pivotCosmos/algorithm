import sys

N = int(input())
li = []
for i in range(N) :
    temp = sys.stdin.readline().rstrip().split()
    numTemp = [int(temp[0]),int(temp[1])]
    li.append(numTemp)
    
li.sort()

for i in range(N) :
    print(*li[i], sep=' ')