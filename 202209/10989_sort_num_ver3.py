import sys
N = int(sys.stdin.readline())
# numbers = [int(sys.stdin.readline()) for _ in range(N)] # 최대 10,000,000개라서 저장하면 메모리 초과
counts = [0]*10001
for _ in range(N) :
    v = int(sys.stdin.readline())
    counts[v] += 1

for index in range(len(counts)) :
    for v in range(counts[index]) :
        print(index)