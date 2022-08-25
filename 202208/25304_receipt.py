import sys
X = int(input())
N = int(input())
prices = []
for i in range(N) :
    p, n = map(int, sys.stdin.readline().split())
    prices.append(p*n)
if sum(prices) == X :
    print("Yes")
else :
    print("No")