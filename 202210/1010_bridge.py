# 다리 놓기
import sys, math

T = int(input())
for _ in range(T) :
    L, R = map(int, sys.stdin.readline().split())
    print(math.comb(R,L))